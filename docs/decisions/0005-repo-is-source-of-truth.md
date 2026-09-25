# Repo przechowuje wydania, Supabase pracę redakcyjną

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Tekst, który trafia do paczki, zawsze pochodzi z repo. Supabase przechowuje tylko
wersję bazową z importu i korekty względem niej. Korekty wracają do repo przez agenta,
który je nanosi i przebudowuje paczkę. Dzięki temu build, paczki i praca agenta
nie zależą od bazy, a jej utrata oznacza najwyżej utratę nienaniesionych korekt.

## Rozważone warianty

- **Supabase jako główne źródło tekstów, repo dostaje z niego pełne pliki**:
  odrzucone. Każdy build i każda zmiana agenta wymagałyby synchronizacji z bazą.
  Dwie kopie mogłyby się też rozjechać bez żadnej kontroli konfliktów.
