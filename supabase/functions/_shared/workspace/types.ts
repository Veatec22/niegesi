// Kontrakty pracowni korekty. Czysty TypeScript bez Deno, Node, DOM i sekretów —
// ten sam moduł importuje Edge Function i strona (decyzja 0016).

/** Wpis z en-pl-review.json po walidacji (0013). Tekst nigdy nie jest przycinany. */
export interface Entry {
  namespace: string;
  key: string;
  english: string;
  polish: string;
  context?: string;
  note?: string;
  max_length?: number;
}

export interface EntryRef {
  namespace: string;
  key: string;
}

/** Zapisany wynik pracy jednego wpisu (0009, 0011). */
export type WorkAction = 'accept' | 'correct';

/**
 * Stan po rozliczeniu z main. „review” to akceptacja, której tekst zmienił się na main
 * — wpis wraca do przejrzenia, a zapis zostaje, żeby pokazać różnicę.
 */
export type WorkState = 'accepted' | 'review' | 'pending' | 'conflict';

export interface WorkRow extends EntryRef {
  action: WorkAction;
  english: string;
  /** PL przed korektą; przy akceptacji null. */
  before: string | null;
  /** Zaakceptowany PL albo PL po korekcie. */
  after: string;
  state: WorkState;
  /** Wpisu nie ma na main (0017). Stan zostaje z ostatniego rozliczenia. */
  missing: boolean;
}

export interface Group {
  id: string;
  name: string;
  entries: EntryRef[];
}

export type Certainty = 'pewna' | 'odtworzona';

export interface Sequence {
  id: string;
  name: string;
  group: string;
  order: { certainty: Certainty; source: string };
  speakers: { certainty: Certainty; source: string };
  lines: (EntryRef & { speaker?: string })[];
}

export interface Layout {
  groups: Group[];
  sequences: Sequence[];
}

export const UNSORTED_GROUP = { id: '_unsorted', name: 'Do uporządkowania' } as const;
export const SINGLE_GROUP = { id: '_all', name: 'Wszystkie wpisy' } as const;

/** Wpis dziennika gry. `detail` niesie teksty potrzebne do odtworzenia zmiany. */
export interface JournalItem extends Partial<EntryRef> {
  kind:
    | 'accept' | 'correct' | 'unset' | 'forget'
    | 'settle' | 'missing' | 'returned';
  detail: Record<string, unknown>;
}

/** Akcja ze szkicu wysyłana przy zapisie gry. `base` to EN/PL z main przy powstaniu szkicu. */
export type DraftAction =
  | (EntryRef & { kind: 'accept'; base: { english: string; polish: string } })
  | (EntryRef & { kind: 'correct'; base: { english: string; polish: string }; after: string })
  | (EntryRef & { kind: 'unset'; base: { english: string; polish: string } })
  | (EntryRef & { kind: 'forget' });

/** Odpowiedź workspace-open i workspace-save: gra z main plus rozliczony wynik pracy. */
export interface GameView {
  game: string;
  main_sha: string;
  revision: number;
  entries: Entry[];
  layout: Layout;
  /** Identyfikator postaci z bible.yaml → nazwa do wyświetlenia. */
  speakers: Record<string, string>;
  /** Wyniki pracy wpisów obecnych na main. */
  work: WorkRow[];
  /** Wyniki pracy bez wpisu na main (0017). */
  missing: WorkRow[];
  /** Zmiany stanów z tego rozliczenia. */
  changes: JournalItem[];
  /** Ponowienie zapisu, który już przeszedł. */
  duplicate?: boolean;
}

/** Treść odpowiedzi z błędem obu funkcji. */
export interface WorkspaceErrorBody {
  error: 'bad_request' | 'method' | 'not_found' | 'forbidden' | 'format' | 'github' | 'revision' | 'stale' | 'busy' | 'internal';
  message: string;
  file?: string;
  issues?: string[];
  retry_at?: string | null;
  revision?: number;
  stale?: (EntryRef & { main: { english: string; polish: string } | null })[];
  invalid?: string[];
}

export class FormatError extends Error {
  constructor(public readonly file: string, public readonly issues: string[]) {
    super(`${file}: ${issues.slice(0, 5).join('; ')}${issues.length > 5 ? ` (i ${issues.length - 5} więcej)` : ''}`);
    this.name = 'FormatError';
  }
}
