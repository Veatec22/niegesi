import { getCollection, type CollectionEntry } from 'astro:content';
import { withBase } from './url';

export type Tone = 'ink' | 'red' | 'graphite';

/** Status z games/statusy.yaml, razem z pozycją w pliku — ta wyznacza kolejność na stronie. */
export type Status = Omit<CollectionEntry<'statuses'>['data'], 'games'> & { id: string; order: number };

export type Game = CollectionEntry<'games'>['data'] & {
  id: string;
  status: Status;
  tone: Tone;
  lead: string;
  href: string;
};

const TONES: Tone[] = ['ink', 'red', 'graphite'];

/** Pierwszy akapit README gry, bez nagłówka i bez noty „Część Nie gęsi". */
function leadFromReadme(body: string | undefined): string {
  if (!body) return '';
  const paragraph = body
    .replace(/\r\n/g, '\n') // część README w repo ma końce linii CRLF
    .split(/\n{2,}/)
    .map((block) => block.trim())
    .find(
      (block) =>
        block.length > 0 &&
        !block.startsWith('#') &&
        !block.startsWith('>') &&
        !block.startsWith('|') &&
        !/^\*(Part of|Część)/.test(block),
    );

  if (!paragraph) return '';

  return paragraph
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // linki → sam tekst
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/[*`]/g, '')
    .replace(/\s*\n\s*/g, ' ')
    .trim();
}

export async function getStatuses(): Promise<Status[]> {
  const entries = await getCollection('statuses');
  return entries.map(({ id, data: { games: _, ...rest } }, order) => ({ ...rest, id, order }));
}

/**
 * Gra → status według games/statusy.yaml. Build ma się wywrócić, gdy gra nie ma statusu,
 * ma dwa albo plik wymienia slug, którego nie ma w games/ — cicha pomyłka byłaby gorsza.
 */
async function statusBySlug(slugs: string[]): Promise<Map<string, Status>> {
  const [entries, statuses] = await Promise.all([getCollection('statuses'), getStatuses()]);
  const assigned = new Map<string, Status>();

  entries.forEach((entry, index) => {
    for (const slug of entry.data.games) {
      const previous = assigned.get(slug);
      if (previous) throw new Error(`games/statusy.yaml: „${slug}" stoi i w „${previous.id}", i w „${entry.id}".`);
      if (!slugs.includes(slug)) throw new Error(`games/statusy.yaml: „${slug}" nie ma w games/.`);
      assigned.set(slug, statuses[index]!);
    }
  });

  const missing = slugs.filter((slug) => !assigned.has(slug));
  if (missing.length > 0) throw new Error(`games/statusy.yaml: brak statusu dla ${missing.join(', ')}.`);

  return assigned;
}

export async function getGames(): Promise<Game[]> {
  const [entries, docs] = await Promise.all([getCollection('games'), getCollection('gameDocs')]);
  const leads = new Map(docs.map((doc) => [doc.id, leadFromReadme(doc.body)]));
  const statuses = await statusBySlug(entries.map((entry) => entry.data.slug));

  return entries
    .map((entry) => {
      return {
        ...entry.data,
        id: entry.id,
        status: statuses.get(entry.data.slug)!,
        lead: leads.get(entry.id) ?? '',
        // Gra nie ma własnej strony — link otwiera panel i daje się udostępnić.
        href: withBase(`/?gra=${entry.data.slug}`),
        tone: 'ink' as Tone,
      };
    })
    .sort((a, b) => a.status.order - b.status.order || b.entries.done - a.entries.done)
    .map((game, index) => ({ ...game, tone: TONES[index % TONES.length]! }));
}

export function stats(games: Game[]) {
  const translated = games.reduce((sum, game) => sum + game.entries.done, 0);

  return [
    { value: String(games.length), label: 'gier' },
    { value: translated.toLocaleString('pl-PL'), label: 'przetłumaczonych wpisów' },
    { value: String(games.filter((game) => game.status.id === 'gotowe').length), label: 'gotowe' },
    { value: String(games.filter((game) => game.tested !== 'strukturalnie').length), label: 'sprawdzonych w grze' },
  ];
}

/** „485 wpisów" albo „153 z 2305 wpisów" — bez powtarzania liczby, gdy komplet. */
export function entriesLabel(game: Game): string {
  const { done, total } = game.entries;
  return done >= total ? `${done} wpisów` : `${done} z ${total} wpisów`;
}
