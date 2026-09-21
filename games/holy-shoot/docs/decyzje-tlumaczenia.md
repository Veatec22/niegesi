# Holy Shoot — decyzje tłumaczenia (0.2.0)

Fakty i źródła: `translations/biblia.yaml`. Raport kontrolny: `work/l10n-report.md`.
Gra ma tylko angielski, więc płeć i sens ustalano z samego tekstu.

## Postacie

- **Gracz to Samuel albo Toshiko**, więc wszystko, co mówią do gracza wróżka, anioły,
  bossowie i opisy, jest bezrodzajowe („Udało się!”, „Ale ci to nie wychodzi”,
  „Już się rumienisz!”). Kwestie Samuela są w formie męskiej, Toshiko w żeńskiej.
- **Toshiko mówi żargonem IT** („Zdebugowane i usunięte!”, „404: nie znaleziono
  demona!”, „Uruchamiam niszczyciel_demonów.exe!”).
- **Wróżka-towarzyszka jest rodzaju żeńskiego** (w oryginale „it”): „Ta-dam! Przybyła
  twoja bohaterka”. Pyskata jak w oryginale.
- **Bossowie z przydomkami:** Baron Przypalacz (Burnsalot, piekielny bobas z mleczakiem
  i smoczkiem), Lady Miłogeddon (Lovemageddon), Komornik (The Debtkeeper, Mamona —
  żargon finansowy: „Jesteś pod kreską!”, „Towar nie podlega zwrotowi”).
- **Duchy z grami słów:** Needapu („need a poo”) → Kupulkan (Kukulkan + kupa), więc
  kwestia „nawet nie myśl o żartach z mojego imienia” dalej działa; Milcah Kow
  („milk a cow”) → Milka Krasula. Spearatrix zostaje (spartanka, „byłam numerem 301”).

## Terminy

| EN | PL | Dlaczego |
| --- | --- | --- |
| run | wyprawa | z verticalu; jedno podejście w roguelite |
| perk | atut | utarte w polskich wydaniach (Fallout, CoD) |
| dash | zryw | krótko, łatwo się odmienia |
| companion | towarzyszka | towarzyszem jest wróżka |
| Divine Offerings | Boskie Datki | datek na tacę; waluta ulepszeń |
| Glimmering Dust | Migotliwy Pył | |
| Healing Basin / Level-Up Altar | Uzdrawiająca Misa / Ołtarz Awansu | |
| Mayhem (Mode) | Pogrom (tryb Pogromu) | |
| The Challenger | „Wyzywacz” | NPC ustawiający trudność wyzwań |
| Angel Manager / Angelic Merchant | Anielski Kierownik / Anielski Kupiec | |
| Order of the Sanctum | Zakon Sanktuarium | |
| Heaven's Light / Thunder Lance / Frozen Grip / Wail of Fear | Światło Niebios / Włócznia Gromu / Lodowy Uścisk / Lament Trwogi | efekty żywiołów |
| Greed / Lust / Sloth / Wrath | Chciwość / Rozpusta / Lenistwo / Gniew | królestwa piekła |

Nazwy broni przetłumaczone, gdy coś znaczą: Wykałaczka, Łamiszczęk, Kwakostrzał,
Zszywacz, Pyskacz (minigun), Brennekator (strzelba na brenneki), Ulubieniec Tłumów.

## Okazje wykorzystane

- „Demonetized” → „Zdemonetyzowany” (atut na demony), „Zapocalypse” → „Porażalipsa”,
  „Crit Happens” → „Krytyk się zdarza”, „Well, Well, Well” → „No proszę, proszę”
  (atut do Uzdrawiającej Misy), „pyramid scheme” → „piramidy finansowe” (majański duch).

## Świadome odstępstwa

- Liczby w opisach po dwukropku albo przed „s” („Zabij wrogów: {Arg0}.”), bez
  odmiany liczebników.
- Kilka opisów w oryginale ma literówki lub błędy (Toshiko „his path”, „Defat Baron”) —
  po polsku poprawnie.
- Teksty diagnostyczne twórców (`Steam Stat Saved`, `MapOrigin…`) przepisane dosłownie.

## Mniej pewne (sprawdź w grze)

- **Drzewko ulepszeń i ekran atutów** — najdłuższe nazwy („Niewidzialność: nienaruszona
  zasłona”, „Elektryzująca niespodzianka”) mogą się nie mieścić.
- **Przyciski wyboru ducha i ekran „Wyprawa do piekieł”** — przypisywanie miejsc
  („Przypisz lub zdejmij:” + klawisz).
- **Napisy kwestii bossów i wróżki** — czy tempo i długość pasują.
- **Ustawienia grafiki** — „Synchronizacja pionowa” jest dłuższa od „V-Sync”.

## Raport kontrolny

`work/l10n-report.md`: braki 0, tokeny 0, angielskie resztki 0 (poza listą nazw),
spójność 0. Zostają liczebniki przy placeholderach (fałszywe alarmy — liczba stoi
przed „s” albo po dwukropku), kilka długości do obejrzenia i nazwy własne
wielką literą.
