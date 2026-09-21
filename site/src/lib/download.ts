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
  const { kind, file, bytes } = game.download;
  const size = humanSize(bytes);

  if ((kind === 'zip' || kind === 'patch') && published(file)) {
    return {
      available: true as const,
      href: withBase(`pobierz/${file}`),
      label: 'Pobierz spolszczenie',
      // Rozmiar i format stoją w przycisku; jak zainstalować, mówi README gry.
      meta: [size, 'ZIP'].filter(Boolean).join(' · '),
    };
  }

  if (kind === 'none') {
    return {
      available: false as const,
      href: null,
      label: 'Jeszcze nie ma paczki',
    };
  }

  return {
    available: false as const,
    href: null,
    label: 'Paczka w przygotowaniu',
  };
}
