/** Ścieżka w obrębie strony z uwzględnieniem `base` — na Pages strona żyje pod /niegesi/. */
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}
