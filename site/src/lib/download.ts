import { existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import type { Game } from './games';
import { withBase } from './url';

const publicDir = fileURLToPath(new URL('../../public/pobierz/', import.meta.url));

function humanSize(bytes: number | null): string | null {
  if (!bytes) return null;
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(bytes < 10 * 1024 * 1024 ? 1 : 0)} MB`;
}

const published = (file: string | null): file is string => !!file && existsSync(publicDir + file);

/**
 * Paczka pojawia się na stronie tylko wtedy, gdy plik naprawdę leży w public/pobierz.
 * Dzięki temu strona nigdy nie obiecuje pliku, którego nie ma.
 */
export function downloadFor(game: Game) {
  const { kind, file, bytes, patch } = game.download;
  const size = humanSize(bytes);

  if ((kind === 'zip' || kind === 'patch') && published(file)) {
    // Guzik „zainstaluj" bierze zip (gry pluginowe) albo samą łatkę (gry deltowe).
    const payload = kind === 'zip' ? file : patch;
    const install =
      game.install && published(payload)
        ? { kind, url: withBase(`pobierz/${payload}`), marker: game.install.marker }
        : null;

    return {
      available: true as const,
      href: withBase(`pobierz/${file}`),
      label: 'Pobierz spolszczenie',
      note:
        kind === 'zip'
          ? [size, 'ZIP · rozpakuj do katalogu gry'].filter(Boolean).join(' · ')
          : [size, 'ZIP · rozpakuj do katalogu gry i uruchom NieGesiPatch.exe'].filter(Boolean).join(' · '),
      install,
    };
  }

  if (kind === 'none') {
    return {
      available: false as const,
      href: null,
      label: 'Jeszcze nie ma paczki',
      note: 'Tłumaczenie w toku — paczka powstanie po ukończeniu.',
      install: null,
    };
  }

  return {
    available: false as const,
    href: null,
    label: 'Paczka w przygotowaniu',
    note: size
      ? `Gotowa paczka waży ${size} i czeka na sposób publikacji.`
      : 'Paczka gotowa lokalnie, czeka na sposób publikacji.',
    install: null,
  };
}
