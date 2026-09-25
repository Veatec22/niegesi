// Połączenie z Supabase: logowanie linkiem z e-maila (0014), funkcje pracowni i odczyty
// przez RLS. W przeglądarce jest wyłącznie klucz publishable; żadnego klucza uprzywilejowanego.
import { createClient, type Session, type SupabaseClient } from '@supabase/supabase-js';
import type { GameView, JournalItem, WorkspaceErrorBody } from '../../../supabase/functions/_shared/workspace/mod.ts';

/**
 * Klucz publishable projektu Not Geese. Jest publiczny z założenia (jak adres projektu),
 * więc stoi w repo i trafia do buildu na GitHub Actions. Pusty = panel pokazuje brak
 * konfiguracji. Pobranie: `npx supabase projects api-keys --project-ref kulwhymoxgaiqpipwbav`
 * (klucz `sb_publishable_…`, nigdy `sb_secret_…`).
 */
const PROJECT_PUBLISHABLE_KEY = '';

export const SUPABASE_URL: string = import.meta.env.PUBLIC_SUPABASE_URL ?? 'https://kulwhymoxgaiqpipwbav.supabase.co';
export const SUPABASE_PUBLISHABLE_KEY: string = import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY || PROJECT_PUBLISHABLE_KEY;

if (SUPABASE_PUBLISHABLE_KEY.startsWith('sb_secret_')) throw new Error('Pracownia: w przeglądarce wolno użyć tylko klucza publishable.');

export class ApiError extends Error {
  constructor(readonly status: number, readonly body: WorkspaceErrorBody) {
    super(body.message);
  }
}

/** Brak odpowiedzi serwera — zapis mógł przejść albo nie; szkice zostają. */
export class NetworkError extends Error {}

export interface JournalRow extends JournalItem {
  at: string;
}

export class Api {
  readonly client: SupabaseClient;

  constructor() {
    this.client = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {
      auth: { flowType: 'pkce', persistSession: true, detectSessionInUrl: true, autoRefreshToken: true },
    });
  }

  async session(): Promise<Session | null> {
    const { data } = await this.client.auth.getSession();
    return data.session;
  }

  async sendLink(email: string): Promise<void> {
    const { error } = await this.client.auth.signInWithOtp({
      email,
      // Rejestracja wyłączona: link dostaje tylko istniejące konto.
      options: { shouldCreateUser: false, emailRedirectTo: new URL('/admin/', location.origin).href },
    });
    if (error) throw error;
  }

  async signOut(): Promise<void> {
    await this.client.auth.signOut();
  }

  async isAdmin(): Promise<boolean> {
    const { data, error } = await this.client.rpc('workspace_is_admin');
    if (error) throw error;
    return data === true;
  }

  /** Ostatnie otwarcie gier, które użytkownik już otwierał (0011: bez postępu pozostałych). */
  async openedGames(): Promise<Map<string, string>> {
    const { data, error } = await this.client.from('workspace_games').select('game, refreshed_at');
    if (error) throw error;
    return new Map((data ?? []).map((row) => [row.game as string, row.refreshed_at as string]));
  }

  async journal(game: string): Promise<JournalRow[]> {
    const { data, error } = await this.client
      .from('workspace_journal')
      .select('at, kind, namespace, key, detail')
      .eq('game', game)
      .order('id', { ascending: false })
      .limit(300);
    if (error) throw error;
    return (data ?? []) as JournalRow[];
  }

  open(game: string): Promise<GameView> {
    return this.call('workspace-open', { game });
  }

  save(body: { game: string; expected_revision: number; request_id: string; actions: unknown[] }): Promise<GameView> {
    return this.call('workspace-save', body);
  }

  private async call(name: string, body: unknown): Promise<GameView> {
    const session = await this.session();
    if (!session) throw new ApiError(401, { error: 'forbidden', message: 'Sesja wygasła. Zaloguj się ponownie.' });
    let response: Response;
    try {
      response = await fetch(`${SUPABASE_URL}/functions/v1/${name}`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${session.access_token}`,
          apikey: SUPABASE_PUBLISHABLE_KEY,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      });
    } catch {
      throw new NetworkError('Brak połączenia z serwerem. Szkice zostały w przeglądarce.');
    }
    let payload: unknown = null;
    try {
      payload = await response.json();
    } catch {
      // niżej
    }
    if (response.ok && payload && typeof payload === 'object') return payload as GameView;
    const error = payload && typeof payload === 'object' && 'message' in payload
      ? payload as WorkspaceErrorBody
      : { error: 'internal', message: `Serwer odpowiedział błędem ${response.status}.` } as WorkspaceErrorBody;
    throw new ApiError(response.status, error);
  }
}
