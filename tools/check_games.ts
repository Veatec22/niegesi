// Stan wszystkich gier wobec pracowni korekty, tymi samymi regułami co Edge Functions.
//
//   npx -y deno run --allow-read tools/check_games.ts
//
// Sprawdza plik tłumaczenia (0013), strukturę i biblię, a przy grach przed migracją 0021
// zgodność pl.json z review. Drukuje tabelę stanu gier i procesu. Kod wyjścia 1, gdy
// gra spoza list wyjątków poniżej ma błąd — albo gdy gra z listy wyjątków już go nie ma
// (wtedy trzeba ją z listy usunąć, żeby lista mówiła prawdę).
import { parse as parseYaml } from 'jsr:@std/yaml@1';
import {
  FormatError,
  parseReview,
  resolveLayout,
  speakersFromBible,
} from '../supabase/functions/_shared/workspace/mod.ts';

/** Gry, których review panel dziś odrzuca; do naprawy w repo (0013). */
const REVIEW_PENDING: Record<string, string> = {
  'boomerang-x': 'zdublowany wpis difficulty_select_prompt',
  'dread-templar': 'słownik zamiast listy wpisów',
  otxo: '104 wpisy bez pola polish',
};

/** Gry, które jeszcze mają pl.json (migracja 0021). Po migracji gra wypada z listy. */
const PL_JSON_PENDING = new Set([
  'anger-foot', 'boomerang-x', 'bpm', 'broforce', 'cyber-hook', 'deadbolt', 'dread-templar',
  'heat-signature', 'holy-shoot', 'hyper-light-drifter', 'i-am-your-beast', 'katana-zero',
  'labyrinth-of-the-demon-king', 'laika-aged-through-blood', 'my-friend-pedro', 'neon-abyss',
  'not-a-hero', 'otxo', 'rain-world', 'skate-story', 'somber-echoes', 'sprawl', 'turbo-overkill',
  'void-bastards', 'wild-bastards',
]);

const root = new URL('../games/', import.meta.url);
const exists = (path: URL) => {
  try {
    Deno.statSync(path);
    return true;
  } catch {
    return false;
  }
};
const read = (path: URL) => (exists(path) ? Deno.readTextFileSync(path) : null);
const issue = (error: unknown) =>
  error instanceof FormatError ? `${error.file}: ${error.issues[0]}` : (error as Error).message;

type Row = { game: string; entries: string; layout: string; plJson: string; bible: string; decisions: string; review: string };
const rows: Row[] = [];
const failures: string[] = [];

const games = [...Deno.readDirSync(root)]
  .filter((d) => d.isDirectory && exists(new URL(`${d.name}/game.yaml`, root)))
  .map((d) => d.name)
  .sort();

for (const game of games) {
  const dir = new URL(`${game}/`, root);
  const t = (name: string) => new URL(`translations/${name}`, dir);
  const row: Row = { game, entries: '', layout: '—', plJson: '—', bible: '—', decisions: '—', review: '—' };
  let entries: ReturnType<typeof parseReview> | null = null;

  const reviewText = read(t('en-pl-review.json'));
  try {
    if (reviewText === null) throw new Error('brak translations/en-pl-review.json');
    entries = parseReview(JSON.parse(reviewText));
    row.entries = String(entries.length);
    if (game in REVIEW_PENDING) failures.push(`${game}: review już przechodzi — usuń grę z REVIEW_PENDING`);
  } catch (error) {
    row.entries = `błąd: ${issue(error)}`;
    if (!(game in REVIEW_PENDING)) failures.push(`${game}: ${issue(error)}`);
  }

  let speakers: Set<string> | null = null;
  const bibleText = read(t('bible.yaml'));
  if (bibleText !== null) {
    try {
      const found = speakersFromBible(parseYaml(bibleText));
      speakers = found ? new Set(found.keys()) : null;
      row.bible = speakers ? `${speakers.size} postaci` : 'tak';
    } catch (error) {
      row.bible = `błąd: ${issue(error)}`;
      failures.push(`${game}: bible.yaml: ${issue(error)}`);
    }
  }

  const structureText = read(t('structure.yaml'));
  if (structureText !== null && entries) {
    try {
      const layout = resolveLayout(parseYaml(structureText), entries, speakers);
      row.layout = `${layout.groups.length} grup, ${layout.sequences.length} rozmów`;
    } catch (error) {
      row.layout = `błąd: ${issue(error)}`;
      failures.push(`${game}: structure.yaml: ${issue(error)}`);
    }
  }

  const plText = read(t('pl.json'));
  if (plText !== null) {
    row.plJson = PL_JSON_PENDING.has(game) ? 'do migracji' : 'jest';
    if (!PL_JSON_PENDING.has(game)) failures.push(`${game}: pl.json wrócił po migracji (0021)`);
  } else if (PL_JSON_PENDING.has(game)) {
    failures.push(`${game}: pl.json usunięty — usuń grę z PL_JSON_PENDING`);
  }

  if (exists(new URL('docs/translation-decisions.md', dir))) row.decisions = 'tak';
  if (exists(new URL('docs/localization-review.md', dir))) row.review = 'tak';
  rows.push(row);
}

const header = ['Gra', 'Wpisy', 'Struktura', 'pl.json', 'Biblia', 'Decyzje', 'Review'];
console.log(`| ${header.join(' | ')} |\n| ${header.map(() => '---').join(' | ')} |`);
for (const r of rows) {
  console.log(`| ${[r.game, r.entries, r.layout, r.plJson, r.bible, r.decisions, r.review].join(' | ')} |`);
}
const ready = rows.filter((r) => /^\d+$/.test(r.entries)).length;
console.log(`\nOtwiera się w pracowni: ${ready}/${rows.length}. Jeden plik tłumaczenia: ${rows.filter((r) => r.plJson === '—').length}/${rows.length}.`);

if (failures.length) {
  console.error(`\nBłędy (${failures.length}):\n- ${failures.join('\n- ')}`);
  Deno.exit(1);
}
