/** Ścieżka w obrębie strony z uwzględnieniem `base` — dziś strona stoi pod / wszędzie. */
export function withBase(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${path.replace(/^\//, '')}`;
}
