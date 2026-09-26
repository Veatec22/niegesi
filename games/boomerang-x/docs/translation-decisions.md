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

Status: **uzgodnione z użytkownikiem 2026-09-26 — wariant A** (szczegóły niżej,
„Po niezależnym review”). Źródło: notatki twórców mówią
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

Status: **decyzja tłumacza**; jedna zmiana użytkownika po review. THE GRUDGE PIT →
DÓŁ PORACHUNKÓW (było: DÓŁ URAZY), YORANWOOD → YORAŃSKI BÓR,
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

## Po niezależnym review (2026-09-26)

Wynik: `docs/localization-review.md`. Rozstrzygnięcia użytkownika dopisujemy tutaj
i do biblii jako `zrodlo: uzytkownik`, razem z odrzuconymi wariantami.

- **Decyzja 1 otwarta ponownie — nowa przesłanka.** Notatka twórców przy
  `millipede_statue_room_default_1`: Tepan i Kenak nie mają płci, „if needed, Tepan
  should be gendered female, and Kenak male”.
- Pewne poprawki reviewera wprowadzone (10 wpisów), m.in. przecieki rodzaju „wziąłeś”
  (gracz) i „towarzysz towarzyszowi” (Tepan i gracz).

### Rozstrzygnięcia użytkownika (2026-09-26)

Użytkownik przyjął wszystkie osiem rekomendacji („Wszystkie punkty 1-8 tak”):

1. **Tepan zostaje bez rodzaju (wariant A)**, najsztywniejsze konstrukcje wygładzone:
   `millipede_sewers_lore_3` „mignęło mi, jak przechodzisz”, `_statue_room_default_6`
   „Tylko parę razy mi to mignęło”, `_sauna_lore_6` „Nie trzeba było w ogóle tak długo
   tam zostawać”, `_sauna_lore_7` „w nogi — wszystkie sto — i precz stamtąd!”,
   `_chasm_default_4` „na moich oczach nigdy nie zadziałała”, `_sauna_lore_3` „im dłużej
   to trwało” (zamiast propozycji reviewera „z każdym dniem”, która nie łączy się
   z „tym bardziej”). Odrzucony wariant B: rodzaj żeński zgodny z notatką twórców.
2. „… Kill” → **„Zabójstwo …”** w pięciu powiadomieniach kombo; odrzucone „Trafienie …”.
3. THE GRUDGE PIT → **„DÓŁ PORACHUNKÓW”**; odrzucone „DÓŁ URAZY”.
4. HUD Scale → **„Wielkość HUD-u”**; odrzucone „Wielkość interfejsu”.
5. **„Sterowanie klawiaturą i myszą”** i dla symetrii **„Sterowanie padem”**;
   odrzucone „Zmień klawiaturę i mysz”, „Zmień sterowanie padem”.
6. „friend” → **„bratnia duszo”**; odrzucone „przyjacielu” (męskie wobec gracza).
7. „solemn” → **„otoczone szczególną powagą”**; odrzucone „wyjątkowo uroczyste”.
8. Etykiety przełączników: **„Przerywnik na początku gry”**, **„Odrodzenie od ostatniej
   fali”**; odrzucone formy rozkazujące.

Pozostałe propozycje z `docs/localization-review.md` (tematy 7, 9-bis, 10 i tabela
„Pozostałe”) nie były przedmiotem tej decyzji i zostają otwarte.
