// @ts-check
import { defineConfig } from 'astro/config';

// GitHub Pages projektu: https://veatec22.github.io/niegesi/
// Każdą ścieżkę w obrębie strony składamy przez withBase() z src/lib/url.ts.
export default defineConfig({
  site: 'https://veatec22.github.io',
  base: '/niegesi/',
  devToolbar: { enabled: false },
  build: { format: 'directory' },
});
