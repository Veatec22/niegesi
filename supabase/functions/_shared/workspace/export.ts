import { refId } from './ids.ts';
import type { Entry, WorkRow } from './types.ts';

export const EXPORT_FORMAT = 1;

export interface CorrectionsExport {
  format: typeof EXPORT_FORMAT;
  game: string;
  main_sha: string;
  exported_at: string;
  comment: string;
  corrections: { namespace: string; key: string; english: string; before: string; after: string }[];
  conflicts: {
    namespace: string;
    key: string;
    english: string;
    before: string | null;
    after: string;
    main_english: string;
    main_polish: string;
  }[];
}

/**
 * Eksport jednej gry (0009, 0020): korekty do wdrożenia oraz osobna lista konfliktów,
 * których agent nie nanosi. Bez akceptacji, szkiców i wyników pracy bez wpisu na main
 * (0017). Nie zmienia żadnych danych.
 */
export function buildExport(input: {
  game: string;
  mainSha: string;
  exportedAt: string;
  comment: string;
  rows: WorkRow[];
  entries: Entry[];
}): CorrectionsExport {
  const main = new Map(input.entries.map((entry) => [refId(entry), entry]));
  const present = input.rows.filter((row) => !row.missing && main.has(refId(row)));
  return {
    format: EXPORT_FORMAT,
    game: input.game,
    main_sha: input.mainSha,
    exported_at: input.exportedAt,
    comment: input.comment,
    corrections: present
      .filter((row) => row.action === 'correct' && row.state === 'pending')
      .map((row) => ({ namespace: row.namespace, key: row.key, english: row.english, before: row.before!, after: row.after })),
    conflicts: present
      .filter((row) => row.state === 'conflict')
      .map((row) => {
        const entry = main.get(refId(row))!;
        return {
          namespace: row.namespace,
          key: row.key,
          english: row.english,
          before: row.before,
          after: row.after,
          main_english: entry.english,
          main_polish: entry.polish,
        };
      }),
  };
}
