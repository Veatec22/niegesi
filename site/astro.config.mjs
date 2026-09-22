// @ts-check
import { defineConfig } from 'astro/config';

import sitemap from '@astrojs/sitemap';

// GitHub Pages z własną domeną https://notgeese.cc/ (DNS w Cloudflare), więc strona
// stoi pod / — tak samo lokalnie i na produkcji. Ścieżki w obrębie strony składamy
// przez withBase() z src/lib/url.ts, gdyby kiedyś wróciła pod podkatalog.
export default defineConfig({
  site: 'https://notgeese.cc',
  base: '/',
  devToolbar: { enabled: false },
  build: { format: 'directory' },
  integrations: [sitemap()],
});