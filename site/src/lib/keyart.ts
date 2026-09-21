import { existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { withBase } from './url';

const keyartDir = fileURLToPath(new URL('../../public/keyart/', import.meta.url));

/**
 * Keyart bierze się z tools/keyart.py. Dopóki pliku nie ma, kafelek zostaje
 * przy placeholderze z DESIGN.md — płaska plama, etykieta i inicjał tytułu.
 */
export function keyartFor(slug: string) {
  const webp = existsSync(`${keyartDir}${slug}.webp`);
  const jpg = existsSync(`${keyartDir}${slug}.jpg`);

  if (!webp && !jpg) return null;

  return {
    webp: webp ? withBase(`keyart/${slug}.webp`) : null,
    jpg: jpg ? withBase(`keyart/${slug}.jpg`) : null,
    src: (jpg ? withBase(`keyart/${slug}.jpg`) : withBase(`keyart/${slug}.webp`)) as string,
  };
}
