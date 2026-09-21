import { getCollection, type CollectionEntry } from 'astro:content';
import { withBase } from './url';

export type Status = 'ukonczone' | 'w-trakcie' | 'wstrzymane';
export type Tone = 'navy' | 'red' | 'ink';

export type Game = CollectionEntry<'games'>['data'] & {
  id: string;
  status: Status;
  percent: number;
  testLabel: string;
  tone: Tone;
  lead: string;
  href: string;
};

const TEST_LABEL: Record<CollectionEntry<'games'>['data']['tested'], string> = {
  potwierdzony: 'test w grze: potwierdzony',
  czesciowy: 'test w grze: częściowy',
  strukturalnie: 'test w grze: czeka',
};

const TONES: Tone[] = ['navy', 'red', 'ink'];

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

export async function getGames(): Promise<Game[]> {
  const [entries, docs] = await Promise.all([getCollection('games'), getCollection('gameDocs')]);
  const leads = new Map(docs.map((doc) => [doc.id, leadFromReadme(doc.body)]));

  return entries
    .map((entry) => {
      const { done, total } = entry.data.entries;
      // Podłoga, nie zaokrąglenie: 1774 z 1776 nie ma prawa pokazać 100%.
      const percent = total > 0 ? Math.floor((done / total) * 100) : 0;

      return {
        ...entry.data,
        id: entry.id,
        status: (done >= total ? 'ukonczone' : 'w-trakcie') as Status,
        percent,
        testLabel: TEST_LABEL[entry.data.tested],
        lead: leads.get(entry.id) ?? '',
        // Gra nie ma własnej strony — link otwiera panel i daje się udostępnić.
        href: withBase(`/?gra=${entry.data.slug}`),
        tone: 'navy' as Tone,
      };
    })
    .sort((a, b) => b.percent - a.percent || b.entries.done - a.entries.done)
    .map((game, index) => ({ ...game, tone: TONES[index % TONES.length]! }));
}

export function stats(games: Game[]) {
  const translated = games.reduce((sum, game) => sum + game.entries.done, 0);

  return [
    { value: String(games.length), label: 'gier' },
    { value: translated.toLocaleString('pl-PL'), label: 'przetłumaczonych wpisów' },
    { value: String(games.filter((game) => game.status === 'ukonczone').length), label: 'z kompletem tekstu' },
    { value: String(games.filter((game) => game.tested !== 'strukturalnie').length), label: 'sprawdzonych w grze' },
  ];
}

/** „485 wpisów" albo „153 z 2305 wpisów" — bez powtarzania liczby, gdy komplet. */
export function entriesLabel(game: Game): string {
  const { done, total } = game.entries;
  return done >= total ? `${done} wpisów` : `${done} z ${total} wpisów`;
}
