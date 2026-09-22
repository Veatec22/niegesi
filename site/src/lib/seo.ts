/**
 * Tytuły i opisy stron pod wyszukiwarkę. Każda gra ma własny adres /<slug>/, a jej tytuł
 * zaczyna się od fraz, które ludzie wpisują: „<gra> spolszczenie". Ten sam tytuł ustawia
 * skrypt panelu, gdy panel otwiera się bez przeładowania.
 */
export const HOME_TITLE = 'Not Geese — spolszczenia do gier';
export const HOME_DESCRIPTION =
  'Nieoficjalne polskie tłumaczenia gier indie. Teksty, narzędzia i instrukcje instalacji dla każdego tytułu osobno.';

export function gameTitle(title: string): string {
  return `${title} spolszczenie — polska wersja do pobrania | Not Geese`;
}

/** Opis pod tytułem w wynikach: Google ucina w okolicy 155–160 znaków, więc zakres skracamy. */
export function gameDescription(game: { title: string; version: string; scope: string }): string {
  const lead = `Spolszczenie ${game.title} (wersja ${game.version}) do pobrania za darmo, z instrukcją instalacji.`;
  const room = 158 - lead.length - 1;
  const scope = game.scope.length > room ? `${game.scope.slice(0, room - 1).replace(/[\s,;—-]+\S*$/, '')}…` : game.scope;
  return `${lead} ${scope}`;
}
