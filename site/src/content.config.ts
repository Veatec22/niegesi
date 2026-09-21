import { defineCollection, z } from 'astro:content';
import { file, glob } from 'astro/loaders';

const slugFromPath = ({ entry }: { entry: string }) => entry.split('/')[0];

/** Metadane maszynowe: liczby, statusy, linki. Jedyne źródło dla tabeli w README i dla strony. */
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
    source: z.string().nullable().default(null), // stary zapis, zastępuje go tested_on
    // Na czym spolszczenie sprawdzono: sklep (klucz jak w `stores`) i wersja gry z jej menu
    // albo z PlayerSettings.bundleVersion. Informacja dla gracza, nigdy warunek działania.
    tested_on: z.array(z.object({ store: z.string(), version: z.string() })).default([]),
    year: z.number().nullable().default(null),
    steam_appid: z.number().nullable().default(null),
    keyart_shot: z.number().nullable().default(null), // numer zrzutu ze Steama, patrz tools/keyart.py
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

/** Proza: README gry — krótki opis i instalacja. Renderowane na podstronie, lead trafia do panelu. */
const gameDocs = defineCollection({
  loader: glob({ pattern: '*/README.md', base: '../games', generateId: slugFromPath }),
});

/** Statusy spolszczeń i przypisane do nich gry. Kolejność w pliku = kolejność na stronie. */
const statuses = defineCollection({
  loader: file('../games/statusy.yaml'),
  schema: z.object({
    label: z.string(),
    description: z.string(),
    tone: z.enum(['ink', 'outline', 'accent']),
    games: z.array(z.string()).default([]),
  }),
});

export const collections = { games, gameDocs, statuses };
