# Boomerang X — decyzje tłumaczenia

## Stan

Data: 2026-09-26. Pełny przekład 359/359 wpisów (wersja paczki 1.1, 2026-09-21).
Vertical 0.1 (38 wierszy: menu, pauza, opcje, pierwsze tablice samouczka, pierwsza
kwestia Tepana) użytkownik widział w grze. Pełnego tłumaczenia nikt jeszcze nie ograł.

Etap ustalania kierunku (`localization-direction`) nie istniał, gdy powstawał przekład.
Poniższe decyzje podjął tłumacz przy fullu 1.0. **Żadna nie ma potwierdzenia
użytkownika** — ten dokument i `translations/bible.yaml` zostały spisane wstecznie
2026-09-26 z tekstów, notatek twórców i `docs/technical.md`, przed niezależnym review.

## Decyzje z przekładu 1.0

### 1. Tepan bez rodzaju gramatycznego

Status: **decyzja tłumacza, do potwierdzenia**. Źródło: notatki twórców mówią
o Tepanie wyłącznie „they/themselves” (np. `millipede_statue_room_default_2`:
„Tepan introduces themselves”). Polszczyzna wymusza rodzaj w czasie przeszłym, więc
kwestie są przebudowane tak, żeby go nie ujawniać:

- `millipede_sewers_lore_3`: „I saw you pass through…” → „Udało mi się zobaczyć, jak przechodzisz…”
- `millipede_sewers_lore_4`: „I remember falling through one.” → „zdarzyło mi się przez takie wpaść.”
- `millipede_sauna_lore_7`: „I got me and my hundred legs right out of there!” → „wyniosło mnie stamtąd razem ze stoma nogami!”

Koszt: konstrukcje bezosobowe („udało mi się”, „zdarzyło mi się”, „nie było mi dane”)
powtarzają się i miejscami brzmią sztywniej niż swobodne EN. Alternatywy nierozważane
z użytkownikiem: rodzaj męski („Tepan” odmienia się jak imię męskie), rodzaj żeński.

### 2. Postać gracza bez rodzaju

Status: **decyzja tłumacza**. Gracz nie mówi, płeć nie pada. Tepan zwraca się na „ty”,
formy rodzajowe wobec gracza są omijane („Udało ci się!”, „nic ci nie jest”).

### 3. Kaspidae żeńska, Pustelnik męski

Status: **decyzja tłumacza**. W EN obie postacie mają „they”. Kaspidae dostaje rodzaj
żeński za rzeczownikiem „modliszka” (`millipede_statue_room_lore_2`, `_lore_4`),
Pustelnik — męski za rzeczownikiem „Pustelnik” (`millipede_sauna_default_4`–`_6`).

### 4. Nazwy mocy

Status: **decyzja tłumacza** (`docs/technical.md`, wersja 1.0). Flux → Strumień,
Slingshot → Zryw, Scattershot → Odłamki, Needle → Igła, Blaze → Żar,
Oblivion Comet → Kometa Zapomnienia, Comet Mode → tryb komety. Krótkie, jednowyrazowe
tam, gdzie EN jest jednowyrazowe; limit 20 znaków przy nazwach mocy.

### 5. Nazwy miejsc tłumaczone, imiona i ludy zostają

Status: **decyzja tłumacza**. THE GRUDGE PIT → DÓŁ URAZY, YORANWOOD → YORAŃSKI BÓR,
THE DEEPEST FOLLY → NAJGŁĘBSZE SZALEŃSTWO, HALL OF THE ERSATZ FEAST → SALA POZORNEJ UCZTY
itd. Tepan, Kaspidae, Kenak, Atsil, Vashkatar, Entacca, Yoran bez zmian.

### 6. Tryb bez końca

Status: **decyzja tłumacza**. Endless Run → Bieg bez końca, leaderboard → ranking,
nazwy kategorii-smaków przetłumaczone (Marakuja, Melon, Śliwka), Hardcore → Hardkor.

### 7. Ograniczenia techniczne wpływające na tekst

- `difficulty_select_prompt` występuje w tabeli gry dwa razy z różnym EN; oba wiersze
  dostają to samo PL („Wybierz poziom trudności:”).
- Znaczniki `|pause|`, `|short_pause|`, `|long_pause|` sterują tempem wyświetlania
  dialogu; `[[..._icon]]` to ikony przycisków; `{0}`, `{1}` liczby; `<size=80>` rozmiar.
- Tytuły ekranów sterowania mieszczą około 15 znaków w wierszu (notatka twórców).
- Fonty przycisków (Dead Stock) mają własne `ó ł`, pozostałe polskie litery biorą
  z fallbacku `beer money` — widoczne różnice rozmiaru opisuje `docs/technical.md`.

## Po niezależnym review

Wynik: `docs/localization-review.md`. Rozstrzygnięcia użytkownika dopisujemy tutaj
i do biblii jako `zrodlo: uzytkownik`, razem z odrzuconymi wariantami.
