import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';

const slugFromPath = ({ entry }: { entry: string }) => entry.split('/')[0];

/**
 * Metadane gry z game.yaml — tylko pola, których używa strona. Plik ma też pola dla
 * narzędzi (steam_appid, year, keyart_shot z tools/keyart.py, phase, test_notes);
 * schemat je pomija.
 */
const games = defineCollection({
  loader: glob({ pattern: '*/game.yaml', base: '../games', generateId: slugFromPath }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    version: z.string(),
    entries: z.object({ done: z.number(), total: z.number() }),
    tested: z.enum(['potwierdzony', 'czesciowy', 'strukturalnie']),
    engine: z.string(),
    approach: z.string(),
    scope: z.string(),
    // Na czym spolszczenie sprawdzono: sklep (klucz jak w `stores`) i wersja gry z jej menu
    // albo z PlayerSettings.bundleVersion. Informacja dla gracza, nigdy warunek działania.
    tested_on: z.array(z.object({ store: z.string(), version: z.string() })).default([]),
    stores: z.record(z.string()).default({}),
    quote: z
      .object({ text: z.string().nullable().default(null), source: z.string().nullable().default(null) })
      .default({ text: null, source: null }),
    download: z.object({
      kind: z.enum(['zip', 'patch', 'none']),
      file: z.string().nullable().default(null),
      bytes: z.number().nullable().default(null),
    }),
  }),
});

/** README gry — instrukcja instalacji dla gracza, renderowana w panelu gry. */
const gameDocs = defineCollection({
  loader: glob({ pattern: '*/README.md', base: '../games', generateId: slugFromPath }),
});

/** Katalog: statusy spolszczeń, a pod każdym gry z datą dodania. Kolejność statusów w pliku = kolejność w filtrze. */
const statuses = defineCollection({
  loader: file('../games/catalog.yaml'),
  schema: z.object({
    label: z.string(),
    description: z.string(),
    tone: z.enum(['ink', 'outline', 'accent']),
    games: z.record(z.coerce.date()).default({}),
  }),
});

export const collections = { games, gameDocs, statuses };
