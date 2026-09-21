// @ts-check
import { defineConfig } from 'astro/config';

// GitHub Pages projektu: https://veatec22.github.io/niegesi/ — tam strona żyje pod /niegesi/,
// więc workflow publikacji podaje SITE_BASE=/niegesi/. Lokalnie strona stoi pod /.
// Każdą ścieżkę w obrębie strony składamy przez withBase() z src/lib/url.ts.
export default defineConfig({
  site: 'https://veatec22.github.io',
  base: process.env.SITE_BASE ?? '/',
  devToolbar: { enabled: false },
  build: { format: 'directory' },
});
