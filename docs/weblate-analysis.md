# Weblate jako wzór pracowni korekty

Rozpoznanie z 2026-09-25 na kodzie [WeblateOrg/weblate](https://github.com/WeblateOrg/weblate)
(commit `86928160a7c6`) i limitach Supabase. Materiał wejściowy do grillowania
pracowni ([0003](decisions/0003-editorial-workspace.md)), nie specyfikacja.
Decyzje zapadają w `docs/decisions/`, słownik pojęć w [glossary.md](glossary.md).

## Czym Weblate jest

Django + Celery + Postgres + Redis, na licencji **GPL-3.0-or-later**. Całość kręci się
wokół repozytorium VCS: każdy plik tłumaczeń to komponent, Weblate czyta go przez
translate-toolkit, a zmiany buforuje i commituje z powrotem. Jest wielojęzyczny,
wieloużytkownikowy, z uprawnieniami, rozliczeniami i dodatkami.

Wniosek: **przenosimy pojęcia, nie kod.** Nasze repo jest na MIT, więc przepisanie
modułów Weblate na TypeScript byłoby utworem zależnym na GPL. Czytamy kod, żeby
zrozumieć projekt; implementujemy od zera. Kod Pythona i tak nie działa w Deno.

## Model danych Weblate → nasz odpowiednik

| Weblate | Co to jest | U nas |
|---|---|---|
| Project → Category → Component → Translation | projekt, grupy komponentów, plik, plik w danym języku | **Gra**. Jeden język docelowy, więc Translation znika. Komponent ≈ źródło tekstów gry (tabela I2, STRG, dialogi JSON) — dziś spłaszczone do jednego `en-pl-review.json`. |
| `Unit` (`trans/models/unit.py`) | jedna kwestia: `context` (klucz), `source`, `target`, `state`, `note`, `explanation`, `flags`, `position`, `priority`, `previous_source`, `labels`, `variant` | **Wpis**. Klucz, EN, PL, kontekst. `position` daje kolejność w pliku — u nas za mało, bo potrzebujemy kolejności w rozmowie. |
| `StringState` (`utils/state.py`) | pusty 0, wymaga edycji 10/11/12, przetłumaczony 20, zatwierdzony 30, tylko do odczytu 100; przy włączonym review „przetłumaczony” = „czeka na przegląd” | Wzór stanów korekty. U nas prawie wszystko jest przetłumaczone przez agenta, więc oś to raczej: do korekty → poprawione → zatwierdzone, plus „pytanie”. |
| `previous_source` | EN sprzed zmiany; zmiana źródła zrzuca wpis do „wymaga edycji” i pokazuje różnicę | **Bardzo przydatne**: aktualizacja gry zmienia EN, ponowny import ma pokazać, co się zmieniło. |
| `explanation`, `note` | objaśnienie dla tłumacza (edytowalne) i komentarz z pliku | Kontekst z ekstrakcji + notatka z biblii. |
| `flags` (`checks/flags.py`) | `max-length`, `placeholders:`, `forbidden`, `read-only`, `ignore-*`… | Limity długości (Boomerang X ma `max_char_limit`), wyłączanie sprawdzeń na wpisie. |
| `Label` | kolorowe etykiety w projekcie | **Grupy** (menu, ustawienia, dialogi…). Weblate ma etykiety płaskie, bez kolejności i bez hierarchii. |
| `Variant` | łączy wpisy będące wariantami tego samego tekstu (regex na kluczu) | Warianty kwestii (np. różne odmiany tej samej linii). |
| `Suggestion` + `Vote` | propozycja bez nadpisania tekstu, głosowanie | Dla jednego użytkownika zbędne. Ewentualnie: propozycje agenta/reviewera do przyjęcia jednym klikiem. |
| `Comment` (`resolved`) | wątek przy wpisie, do źródła albo tłumaczenia | **Uwagi** — „mam pytanie”, zgłoszenia do agenta, z rozwiązaniem. |
| `Change` (`trans/models/change.py`) | dziennik wszystkiego: `action`, `old`, `target`, `user`, `details` | **Historia** wpisu i cofanie. |
| `PendingUnitChange` (`trans/models/pending.py`) | zmiana czekająca na commit do repo | **Najbliższy odpowiednik naszego eksportu.** Weblate commituje sam; u nas bufor opuszcza bazę jako eksport dla agenta. |
| `Check` (`dismissed`) + `checks/*` | wynik sprawdzenia per wpis, do odrzucenia | Sprawdzenia przy zapisie. Patrz niżej. |
| Glosariusz (`glossary/`) | osobny komponent z terminami, flagi `terminology`, `forbidden`, `read-only`; dopasowanie Aho-Corasick; sprawdzenie „nie trzyma się glosariusza” | **Terminy z `bible.yaml`**, podświetlone w EN, z ostrzeżeniem, gdy PL ich nie używa. |
| `Memory` (`memory/`) | pamięć tłumaczeń: `source`, `target`, `origin`, wyszukiwanie przez `pg_trgm` | Podobne kwestie z tej i innych gier. `pg_trgm` jest dostępne w Supabase, więc to działa w samej bazie. |
| `Screenshot` | obraz przypięty do wielu wpisów | Screeny z testów w grze (Storage), później. |
| `WorkflowSetting` | review włączone/wyłączone, sugestie, blokada edycji | Jeden stały przepływ, bez konfiguracji. |
| Machinery, AI check | tłumaczenie maszynowe, sprawdzenie przez LLM | Tłumaczy agent w repo, nie panel. Poza zakresem. |
| VCS, addons, alerts, billing, agreements, workspaces | integracja z repo i organizacją | Poza zakresem. Supabase nie dotyka GitHuba. |

## Sprawdzenia warte przeniesienia

Z kilkudziesięciu sprawdzeń Weblate dla gier EN→PL liczy się kilkanaście, wszystkie
to proste porównania EN/PL, łatwe do napisania od nowa w TypeScript:

- znaczniki i placeholdery (`placeholders`, `xml-tags`, BBCode, własne formaty gier:
  `{0}`, `%s`, `<color>`, `\n` — lista per gra),
- spacje i nowe linie na początku/końcu, podwójna spacja,
- zgodność końcowej interpunkcji (`.`, `?`, `!`, `…`, `:`) — jako podpowiedź, nie błąd,
- tekst niezmieniony względem EN (`same`), z listą wyjątków (nazwy własne),
- niespójność: ten sam EN przetłumaczony różnie (`inconsistent`),
- powtórzone słowo (`duplicate`),
- glosariusz (`check_glossary`) i słowa zakazane,
- maksymalna długość (`max-length`), a docelowo szerokość w pikselach fontu gry (`max-size`).

Weblate przelicza sprawdzenia przy każdym zapisie i trzyma wyniki w tabeli. Mamy już
podobną logikę w `.claude/skills/localization/scripts/l10n_report.py` — to naturalny
drugi wzorzec, nasz własny.

## Czego Weblate nie rozwiązuje

Weblate nie wie, kto mówi i w jakiej kolejności. `position` to kolejność w pliku,
etykiety są płaskie, warianty łączą tylko teksty. To dokładnie problem krótkofalówek
w Laice. Scena, rozmowa, mówca i kolejność muszą być naszym własnym modelem, zasilanym
z ekstrakcji gry (wzorem jest articy:draft, patrz
[localization-tools-research.md](localization-tools-research.md)).

## Ograniczenia Supabase Edge Functions

Deno/TypeScript, 256 MB pamięci, **2 s czasu CPU na żądanie**, 150 s zegara
(plan darmowy). Największa gra ma ~4,9 tys. wpisów (Rain World), wszystkie razem
~45 tys. Import jednej gry mieści się, jeśli ciężka praca (upsert, porównanie z bazą)
dzieje się w Postgresie przez RPC, a funkcja tylko waliduje i przekazuje. Pamięć
tłumaczeń i wyszukiwanie — w bazie (`pg_trgm`), nie w funkcji.

## Stan plików w repo, który import musi przyjąć

`en-pl-review.json` jest wymagany dla każdej gry, ale kształt się różni:
`key/english/polish` wszędzie, do tego zależnie od gry `context`, `note(s)`, `status`,
`namespace`, `id`, `table/entry_id/term`, `max_char_limit`; Dread Templar ma słownik
zamiast listy. `pl.json` też nie jest wszędzie płaską mapą klucz → tekst
(np. Heat Signature ma `parts/`). Import musi to znormalizować, a naniesienie poprawek
wrócić do właściwego pliku każdej gry.
