import { existsSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { withBase } from './url';

const keyartDir = fileURLToPath(new URL('../../public/keyart/', import.meta.url));

/** Proporcje kapsuły ze Steama (616×353) i zrzutów w galerii (16:9). */
export const COVER_SIZE = { width: 616, height: 353 };
export const SHOT_SIZE = { width: 1600, height: 900 };

export interface Art {
  /** `srcset` w wariancie AVIF i WebP, np. „…/cover-616.avif 616w, …/cover-1232.avif 1232w". */
  avif: string;
  webp: string;
  /** Największy WebP jako `src` dla przeglądarek bez `srcset`. */
  src: string;
}

/**
 * Okładka i galeria z tools/keyart.py, w katalogu `public/keyart/<slug>/`.
 * Dopóki okładki nie ma, kafelek zostaje przy placeholderze z DESIGN.md —
 * płaska plama, etykieta i inicjał tytułu.
 */
export function keyartFor(slug: string, gallery: number[]) {
  const dir = `${keyartDir}${slug}/`;
  if (!existsSync(dir)) return null;

  const files: string[] = readdirSync(dir);
  const url = (file: string) => withBase(`keyart/${slug}/${file}`);
  const art = (stems: [string, number][]): Art | null => {
    const present = stems.filter(([stem]) => files.includes(`${stem}.avif`) && files.includes(`${stem}.webp`));
    if (present.length === 0) return null;
    const srcset = (ext: string) => present.map(([stem, width]) => `${url(`${stem}.${ext}`)} ${width}w`).join(', ');
    return { avif: srcset('avif'), webp: srcset('webp'), src: url(`${present.at(-1)![0]}.webp`) };
  };

  const covers = files
    .map((file: string) => /^cover-(\d+)\.avif$/.exec(file))
    .filter((match): match is RegExpExecArray => match !== null)
    .map((match): [string, number] => [`cover-${match[1]}`, Number(match[1])])
    .sort((a: [string, number], b: [string, number]) => a[1] - b[1]);

  const cover = art(covers);
  const shots = gallery
    .map((number) => art([[`shot-${number}-${SHOT_SIZE.width}`, SHOT_SIZE.width]]))
    .filter((shot) => shot !== null);

  if (!cover && shots.length === 0) return null;
  return { cover, shots };
}
