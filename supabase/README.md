# Supabase — pracownia korekty

Backend prywatnej pracowni ([specyfikacja](../docs/specs/editorial-workspace.md),
decyzje 0004–0020 w [docs/decisions](../docs/decisions/)). Projekt: Not Geese
(`kulwhymoxgaiqpipwbav`). Supabase trzyma wyłącznie wynik pracy: akceptacje, korekty,
dziennik. Teksty gier funkcje pobierają z `main` przy każdym otwarciu i zapisie.

| Ścieżka | Do czego |
| --- | --- |
| `migrations/` | Tabele `workspace_*`, RLS tylko dla administratora, RPC `workspace_apply` i `workspace_is_admin`. |
| `functions/_shared/workspace/` | Czyste reguły wspólne z przeglądarką: review, struktura, rozliczanie, zapis, eksport. |
| `functions/_shared/github.ts` | Odczyt `Veatec22/notgeese@main` (SHA, potem pliki z tego SHA). Tylko serwer. |
| `functions/workspace-open/` | `POST { game }` — otwarcie lub odświeżenie gry z rozliczeniem. |
| `functions/workspace-save/` | `POST { game, expected_revision, request_id, actions }` — zapis szkiców jednej gry. |
| `tests/` | Testy SQL na lokalnym PostgreSQL. |

Zapis idzie wyłącznie przez `workspace_apply`: jedna transakcja, blokada wiersza gry,
kontrola rewizji (druga karta) i identyfikatora żądania (ponowienie). Tabele są dla konta
administratora tylko do odczytu. Funkcje działają z JWT użytkownika w granicach RLS;
klucz `service_role` nie jest nigdzie używany.

Eksport (0020) składa przeglądarka funkcją `buildExport` z danych zwróconych przez
`workspace-open` — nie zmienia bazy, więc nie potrzebuje osobnej funkcji.

## Testy

```sh
npx -y deno test --allow-read --allow-env=NOTGEESE_GITHUB_TOKEN supabase/functions/tests/
supabase/tests/run-local.sh     # jako zwykły użytkownik; initdb odmawia pracy jako root
```

Pierwsze sprawdzają reguły i orkiestrację funkcji (atrapa bazy, podstawiony GitHub z plikami
SCM). Drugie uruchamiają migrację na tymczasowym PostgreSQL z namiastką `auth.uid()`
i sprawdzają dostęp administratora, obcego konta i anon, rewizję, ponowienia i atomowość.
Nie zastępują testu na prawdziwym projekcie po wdrożeniu.

## Wdrożenie

Wymaga zalogowanego CLI (`npx supabase login`) albo tokena w `SUPABASE_ACCESS_TOKEN`.

```sh
npx -y supabase@2.118.0 link --project-ref kulwhymoxgaiqpipwbav
npx -y supabase@2.118.0 db push
npx -y supabase@2.118.0 functions deploy workspace-open workspace-save
```

W panelu projektu, Authentication:

1. Wyłącz rejestrację (Sign In / Providers → „Allow new users to sign up”).
2. URL Configuration: Site URL `https://notgeese.cc`, redirect `https://notgeese.cc/admin/`
   i do testów `http://localhost:4321/admin/`.
3. Users → Add user: e-mail administratora. Następnie w SQL Editor:

   ```sql
   insert into public.workspace_admins (user_id)
   select id from auth.users where email = '<adres administratora>';
   ```

Opcjonalnie (0016): token fine-grained tylko do odczytu Contents tego repo, żeby nie
dzielić limitu 60 zapytań/h bez uwierzytelnienia:
`npx supabase secrets set NOTGEESE_GITHUB_TOKEN=<token>`.

Po wdrożeniu sprawdź: otwarcie SCM zwraca 485 wpisów, obce konto dostaje 403, zapis
z nieaktualną rewizją 409. Stan wdrożenia wpisuj w [0003](../docs/decisions/0003-editorial-workspace.md).
