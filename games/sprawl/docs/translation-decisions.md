# SPRAWL — decyzje tłumaczenia

## Skąd te ustalenia

SPRAWL przetłumaczono (vertical, potem full 0.2 — 717/717 wpisów `Game.locres`) zanim
repo wprowadziło etap ustalania kierunku z użytkownikiem przed verticalem. Nie ma więc
próbki EN/PL rozstrzygniętej w rozmowie. Ten plik i `translations/bible.yaml` powstały
2026-09-26, przed niezależnym przeglądem, i **odtwarzają** decyzje z
`translations/REVIEW.md` oraz z samego tłumaczenia. Żadna z nich nie jest decyzją
użytkownika: użytkownik potwierdził w grze działanie spolszczenia (selektor, flaga,
zapis wyboru, próbka początku gry), ale nie zatwierdzał tonu ani terminów.

Źródła faktów: klucze `Dialogue_Subs` niosą mówcę (`E1M1_FATHER_…`, `REAPER_…`,
`E3M2_POLITICIAN_…`), a treść EN — płeć i relacje.

## Decyzje odtworzone z fullu 0.2

### 1. Kryptonimy zostają po angielsku

SEVEN, SIX, FIVE i numery programu (One…Six w kodeksie) zostają w oryginale,
nieodmienne. SEVEN to bohaterka — rodzaj żeński („Her name was SEVEN”, „you were just
their new toy” → „byłaś”); SIX to mężczyzna („I was always the better soldier” → „byłem”).

### 2. Nazwy miejsc i ról tłumaczone

Father → Ojciec, Reaper → Żniwiarz (kryptonim SIX i nazwa programu: „program ŻNIWIARZ”),
Spire → Iglica, Walled City → Miasto za Murem, Dark City → Ciemne Miasto,
Badlands → Pustkowia, Overseer → Nadzorca, Pythia → Pytia.

### 3. Nazwy własne producentów, frakcji i klas jednostek zostają

SPRAWL, AEON, NCO, ICARUS, GOR, IMAGO-DEI, Domand, nazwy i modele broni
(MEGATECH A8, SHOGO-KENBISHI…), klasy jednostek Ghost, Spectre, O.H.G.R, Oni, Bull,
Okami, Sendai, Suzumebachi. Opisowa część nazwy przeciwnika jest tłumaczona
(„Light Mech Class Spectre” → „Lekki mech klasy Spectre”).

### 4. Rejestry

- **Ojciec** — spokojny, wyniosły, z chłodną ironią; na „ty” do SEVEN; kwestie
  rozbite na kilka napisów łączone wielokropkiem („…i dadzą mi dostęp…”).
- **SIX** — szyderczy, wrzeszczący; „Just die!” → „Po prostu zdechnij!”, „Daddy” → „Tatuś”.
- **Raporty wojskowe** — WIELKIE LITERY jak w EN, urzędowy szyk.
- **Czaty hakerów** — małe litery, brak interpunkcji jak w EN, przekleństwa
  zachowane w mocy („fucking” → „jebany”, „cunt” → „chuju”).
- **Matka** — narratorka żeńska; urywane zdania, sklejone słowa, powtórzenia
  i wtrącenia zakłóceń są celowe i nie są wygładzane.

### 5. Elementy techniczne

Znaczniki `<red>`, `<amber>`, `<blink>`, ikony `<img id="…"/>`, encje `&lt;…&gt;`,
ciągi kodów i łacina w transmisjach zostają bez zmian. `[REDACTED]` → `[UTAJNIONO]`.

### 6. Miejsca interpretacyjne (z REVIEW.md)

- `Tutorials/E1M1_COMBAT_10_BODY`: „overkill” → „doszczętnie zniszczyć”.
- `UIStringTable/LEVEL_E1M4_NAME`: „Ghost Wetware” → „Biologiczne widmo”.
- „SEVERED STEEL” zostaje (nawiązanie do innej gry).
- Club Simulacra / Klub Null — różnica z oryginału zachowana.

## Po niezależnym przeglądzie

Wynik przeglądu z 2026-09-26: `docs/localization-review.md`. Rozstrzygnięcia
użytkownika po przeglądzie dopisujemy tutaj, z odrzuconymi wariantami.
