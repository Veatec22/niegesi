# Pracownia — rozstrzygnięcia techniczne przed prototypem

Data: 2026-09-25. Fakty sprawdzone; szczegóły wykonawcze opisuje specyfikacja.

## Repo i dostęp do GitHuba

GitHub API dla `Veatec22/notgeese` zwróciło `private: false`, `visibility: public`,
`default_branch: main`. Nie zmieniano widoczności repo. Poprawiono nieaktualny opis
w AGENTS.md. Panel nadal jest prywatny, mimo publicznych tekstów źródłowych.

[GitHub](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
potwierdza 60 żądań REST/h na IP bez uwierzytelnienia i zwykle 5000/h z tokenem.
Nie potwierdzono konkretnego współdzielenia IP tego projektu Supabase; nie zakładać go
jako faktu. To nie jest gwarancja przepustowości endpointów raw.

Przyjęte 0008 nadal obowiązuje: publiczne repo działa bez tokena. Adapter GitHuba może
przyjąć opcjonalny token tylko do odczytu z sekretu funkcji (nigdy z przeglądarki).
Rekomendacja wdrożeniowa: token fine-grained ograniczony do odczytu Contents tego repo.
Nie kopiować istniejącego szerokiego tokena `gh`. Brak tokena nie blokuje prototypu.
Przy limicie pokazać czas ponowienia, nie wykonywać automatycznej pętli żądań.
Jedno ustalenie SHA na otwarcie/odświeżenie, następnie wszystkie pliki z tego SHA.

## Wspólny TypeScript

Tak: moduł bez `Deno`, Node, DOM i sekretów może działać w obu środowiskach.
[Astro](https://docs.astro.build/en/guides/imports/) importuje TS, a
[Deno](https://docs.deno.com/runtime/fundamentals/typescript/) obsługuje TS bezpośrednio.
[Supabase](https://supabase.com/docs/guides/functions/development-tips) zaleca
`supabase/functions/_shared/` na kod współdzielony funkcji.

Tam trzymamy czyste kontrakty i reguły. Reguły rozliczenia wykonuje tylko serwer;
przeglądarka nie rozlicza samodzielnie bazy. Współdzielenie nie zmienia 0012.
Importy względne `.ts`, sprawdzenie konfiguracji TS/Vite w implementacji.
Potwierdzenie na poziomie dokumentacji; próba tego samego modułu w Deno i bundlerze
Astro jest kryterium pierwszego etapu implementacji, nie wykonanym testem.

## Układ i wdrażanie

`supabase/config.toml`, `supabase/migrations/`, `supabase/functions/<funkcja>/`,
`supabase/functions/_shared/`; frontend w istniejącym `site/`.
Agent wdraża kod zapisany w repo przez CLI. MCP służy też do odczytów i weryfikacji,
a w razie potrzeby może wdrożyć dokładnie ten sam plik, bez osobnej wersji kodu w panelu.
[Migracje Supabase](https://supabase.com/docs/guides/deployment/database-migrations).

Lokalnie CLI 2.72.8; sprawdzono help `migration new`, `db push`, `functions deploy`.
Przed implementacją przypiąć aktualną zweryfikowaną wersję narzędzia; dostępne MCP
pozwala kontrolować wdrożenie. Deno nie znaleziono w PATH. W tej sesji nie tworzono
migracji ani funkcji i nie zmieniano konfiguracji projektu.

## Szkice

[localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
jest rozdzielone według origin, czyli schematu, hosta i portu. Porty localhost też
mają osobne szkice. W panelu krótka informacja „Szkice tylko w tej przeglądarce”;
w lokalnym podglądzie dopisek o oddzieleniu od notgeese.cc. Zapis do bazy jest
granicą dostępności na innych urządzeniach. Nie obiecujemy trwałości po usunięciu
danych przeglądarki. Brak możliwości lokalnego zapisu musi być widoczny.

## Testowanie i pytania produktowe

Użytkownik potwierdził trzy główne obszary: API otwarcia/odświeżenia/zapisu z dostępem
administratora; przepływ w przeglądarce; eksport i naniesienie do repo.
Ekran czytania rozstrzyga prototyp. Graf dialogów pozostaje poza pierwszą wersją.

Do specyfikacji trafiają jawnie kwestie nieobjęte grillem: usunięcie klucza z main,
rozliczanie sprzecznych przeniesień grup i atomowość „Zapisz wszystkie”. Prototyp
nie ustanawia dla nich nowych reguł produkcyjnych.
