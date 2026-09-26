# Somber Echoes — niezależny przegląd lokalizacji

## Zakres

- Data: 2026-09-25. Przegląd według `.claude/skills/localization-review/SKILL.md`,
  przeprowadzony przez osobnego subagenta w świeżym kontekście, tylko do odczytu.
  Poprawki naniósł i zweryfikował agent prowadzący.
- Wejście: `translations/en-pl-review.json`, 1507 wpisów, SHA-256
  `535a17f23dede2ba6095b7c4a14ed07db3a45eca13a0d3029eecf27dd438c806` (przed poprawkami);
  `translations/bible.yaml` (`8ce6f7f1…`), `docs/translation-decisions.md` (`d2bfd265…`),
  `docs/technical.md`, raport `l10n_report.py`.
- Przeczytano 1507/1507 wpisów w pięciu partiach, bez luk:

  | Partia | Wpisy |
  | --- | ---: |
  | Dialog (czytany scenami po posortowaniu kluczy) | 326 |
  | Journal | 101 |
  | StringTables, część 1 | 400 |
  | StringTables, część 2 | 398 |
  | Challenges + Updated1–4 | 282 |

- Kontrole maszynowe: liczba nowych linii EN/PL zgodna we wszystkich wpisach, placeholdery
  i tokeny `[ICON:…]` nienaruszone, brak spacji przed `?!:;`, dywizów zamiast pauz
  i prostych cudzysłowów.
- Ograniczenie: lista 111 wpisów próbki 0.1 zaakceptowanej przez użytkownika nie jest zapisana
  w repo, więc nie da się wskazać, czy poprawka dotknęła wpisu z próbki. Najbardziej
  prawdopodobny jest `CirceAutoSecurity1.2` (początek gry); poprawka wynika z decyzji
  w biblii, nie ze zmiany kierunku.
- Przeczytane, ale nierozstrzygnięte (brak kontekstu, tekst bez zmian):
  - `STRING_Menu/Log` „Dziennik” — ta sama etykieta co Journal; czy to dwie zakładki?
  - `STRING_Journal/TITLE_Survivor` i pokrewne „Ocalały” — czy etykieta pojawia się przy kobietach.
  - `STRING_MapRooms/EngineRoom-ManagementOffices` „Assembly Hall” → „Hala montażowa”
    (klucz sugeruje biura, możliwa „sala zgromadzeń”).
  - `Dialog/SurvivorSDB1.2` „feebleness of Nocturne” → „słabość Nokturnu” — w EN prawdopodobnie
    literówka (fickleness?); tłumaczenie idzie za literą.
  - `STRING_Tutorials/TUT_ElevatorGoToGreatherThanGod` „świątyni Ponad Bogiem” — nie wiadomo,
    któremu pomieszczeniu na mapie odpowiada.
  - `STRING_Tutorials/TUT_EvadeEnemy` „the following enemy” → „następnego wroga” (a nie „ścigającego”).

## Błędy

Status: **wprowadzone** — naniesione w `en-pl-review.json` (pole `polish`) po sprawdzeniu z EN.

| Klucz | EN | Było | Jest | Przesłanka |
| --- | --- | --- | --- | --- |
| `Dialog/Dialog/SurvivorGRA1.2` | Last seen alive, she was making her way, to power up the shuttle. | Ostatnio widziano ją, gdy zmierzała uruchomić zasilanie promu. | Ostatni raz widziano ją żywą, gdy szła uruchomić zasilanie promu. | „zmierzać” nie łączy się z bezokolicznikiem; „ostatnio” = „niedawno”, a EN mówi „last seen alive” |
| `Dialog/Dialog/CirceAutoSecurity1.2` | …power up the district C.I.R.C.E chamber… | …miejscowej komory C.I.R.C.E. | …miejscowej komory Kirke. | biblia: komora to Kirke; to samo zadanie w dzienniku, zadaniach i na mapie to „komora Kirke” |
| `Dialog/Dialog/PathOfTheOracle1.3` | …to the rank of Pythia she steadily ascended. | …stopniowo zmierzała do godności Pytii. | …stopniowo doszła do godności Pytii. | EN: osiągnęła; potwierdzają to inne sceny („została Pytią”) |
| `Dialog/Dialog/SecondMemory1.2` | With an empty gaze, the oracle decreed… | Wyrocznia pustym wzrokiem wpatrywała się w dal: … | Wyrocznia z pustym wzrokiem orzekła: … | pominięte „decreed”, dopisane „w dal”; TheOldOracle1.2 mówi „Tak orzekła wyrocznia” |
| `Journal//E9F647A642EB028BF63C3692061FF22C` | She’s lost again in her illusions of grandeur | Znów zaginęła we własnych urojeniach wielkości. | Znów zagubiła się we własnych urojeniach wielkości. | „zaginąć” = przepaść bez wieści |
| `Journal//A833B708409F2090F3880CA0A9BF0E0A` | …experiments that bear my and Harmonia’s face | …eksperymentów o twarzach mojej i Harmonii. | …eksperymentów o moich rysach i rysach Harmonii. | niezgodność liczby („mojej” / „twarzach”); „rysy” jak w HarmoniaTheHorrible1.3 |
| `StringTables/STRING_MapElements/Transition_Disabled` | Exit | Wyjdź | Wyjście | element legendy mapy; pozostałe to rzeczowniki (Drzwi, Winda, Prom) |
| `StringTables/STRING_MapElements/Transition_Enabled` | Exit | Wyjdź | Wyjście | jw. |

## Decyzje sprzed verticala

| Decyzja | Werdykt | Uzasadnienie |
| --- | --- | --- |
| Eter / Nyks | utrzymać | bóstwo „Etera”, energia „Eteru” konsekwentnie; nieodmienne „Nyks” działa przy postaci i substancji |
| Para Eter i Nyks w formie męskoosobowej | utrzymać | wszystkie wystąpienia poprawne (DivineWrath, EnterAether, pokonanie bossa) |
| Rozłam | utrzymać | wydarzenie zawsze wielką literą; przenośne „fracture” słusznie inaczej („rozbicie naszyjnika”, „coś pękło”) |
| Blask / Nokturn | utrzymać | rodzina „nocny” spójna; „blask” w zwykłym znaczeniu nie myli się z terminem |
| Popielisko / Ściekowisko / Gaj | utrzymać | przyimki spójne w dialogach, mapie, promach i wyzwaniach |
| Sturęcy | utrzymać | „Sturękich” poprawnie odmieniane |
| Kirke vs C.I.R.C.E. | utrzymać, do rozmowy | podział zachowany, jedyny rozjazd poprawiony; otwarte, czy dać graczowi mostek (niżej) |
| Pytia | utrzymać | Pierwsza Pytia, 260. Pytia |
| Panna | utrzymać | pasuje do Udręki Demeter i Porwania; w dzienniku „dziewczyna w uścisku” jest opisem sceny, nie tytułem — może zostać |
| Via Regia, Via Pelagus, Opera Publica | utrzymać | łacina jak w oryginale |
| Gladius, Arbiter | utrzymać tekst, zmienić zapis w biblii | gladius w nazwach ulepszeń jest pospolity (małą literą); biblia doprecyzowana |
| Rzeczowniki odczasownikowe w wyzwaniach | utrzymać | Oślepienie Cyklopa, Uciszenie Harmonii; osiągnięcia z rozkaźnikiem idą za EN |
| Formy żeńskie Adrestii | utrzymać | dziennik w całości w rodzaju żeńskim; „trybun Adrestia” jako tytuł akceptowalny |
| Narrator bez inwersji | utrzymać | podniosłość niesie słownictwo; nie znaleziono kalkowanego szyku |
| „Pod każdym kamieniem” | utrzymać | wariant „Zajrzyj pod każdy kamień” możliwy, niekonieczny |
| Strefy (Sektor przemysłowy, Dział naukowy, Dolne/Górne kwatery) | utrzymać | spójne |

Dopisane do biblii (bez zmiany tekstu): Spopieleni, Feniks, Legion Helikonu, Mojry, boska dwójca.

## Do rozmowy

Tekst w tych miejscach pozostaje bez zmian do decyzji użytkownika.

Najważniejsze:

1. **Mostek Kirke ↔ C.I.R.C.E.** (`CirceAFOnAI1.1` i pozostałe „Interfejs C.I.R.C.E. — … — aktywny”).
   W EN komora i interfejs to oczywiście ten sam system; po polsku gracz widzi „komorę Kirke”,
   a zaraz „Interfejs C.I.R.C.E.”. Rekomendacja: zostawić (skrót wygląda jak system, imię jak miejsce).
   Wariant: „Interfejs komory Kirke (C.I.R.C.E.)” — czytelniej, ale dłużej.
2. **Dwie „Udręki”** — `Memory_Maiden-Complete` „Demeter's Torment” → „Udręka Demeter” oraz
   `Memory_Seafarer-Complete` „Poseidon's Blight” → „Udręka Posejdona”. Rekomendacja: „Niedola Posejdona”
   (lub „Klątwa Posejdona”), żeby wspomnienia były rozróżnialne; „jego udręka” w PoseidonTrapped1.2 może zostać.
3. **`Hephaestus3_TITLE`** „Own worst enemy” → „Własny największy wróg” (kalka). Rekomendacja: „Sam sobie wrogiem”.
4. **`ACHIEVEMENT_WellOnYourWay_TITLE`** „Well on your way” → „Dobra droga”. Rekomendacja: „Na dobrej drodze”.
5. **`AntenorCovetous1.1`** „My mind's eye is growing more potent” → „Wzrok mego umysłu rośnie w siłę” (kalka).
   Rekomendacja: „Moje wewnętrzne oko nabiera mocy.” Wariant: „Oczy mej duszy widzą coraz więcej.”
6. **„Czysta Nyks” jako materia** — `NecklaceProduction1.1` „naszyjnika z czystej Nyks”, `NyxInfusedFibre_DESC`
   „nasycone Nyks”. Czyta się jak imię bogini. Rekomendacja: „z czystego Nokturnu” (NyxPotency1.1: Nokturn nazwano
   na cześć Nyks). Koszt: odejście od litery EN; trzeba by przejrzeć wszystkie „Nyx” jako substancję.
7. **`TUT_GatherAether`** „to restore Adrestia” → „aby odnowić Adrestię”. Rekomendacja: „aby Adrestia odzyskała siły”.
8. **„Bow & Spear aim”** (`Lantern_TITLE-Level3` i pokrewne) → „Celowanie łukiem i włócznią”. Broń w grze to „Nocny rozbłysk”.
   Rekomendacja: zostawić (EN też mówi „bow”); wariant „Celowanie rozbłyskiem i włócznią”.

Niski priorytet:

- `SurvivorCPC1.1` „lecz wciąż trwający” → „lecz wciąż się trzymający”.
- `SacredOak_DESC` „przed dziewiczym rejsem” → „w czasie dziewiczego rejsu” (EN: on its maiden voyage).
- `DivineWrath1.1` „ryknęli jednym głosem, będąc gniewem wcielonym” → „Eter i Nyks, gniew wcielony, ryknęli jednym głosem.”
- `PoseidonFleeing1.1` „z każdą chwilą będąc coraz bliżej” → „coraz bardziej się zbliżając”.
- „niewrażliwość” (`Lantern_DESC-Level1` i pokrewne) → „nietykalność”, częstsze w grach.
- `ACHIEVEMENT_NecklaceReforged_DESC` „Doprowadź do ukończenia naszyjnika przez Hefajstosa” → „Pozwól Hefajstosowi ukończyć naszyjnik”.
- `ACHIEVEMENT_Completionist_TITLE` „Kompletna kolekcja” → ewentualnie „Kolekcjonerka” (żeńskie tytuły Adrestii).
- `Header_Collectables` „Znajdźki” → „Kolekcja” (rejestr gry).
- `Bosses_FactoryArm-*` „ramię fabryczne” → „Ramię fabryczne” wielką literą, jak inni bossowie.
- `DefacedStatue1.2` „dumny i wyniosły” → „dumny i wyprostowany” (EN: proud and tall).
- `HephaestusTraitorFull1.5` „Własna zdrada była solą na jego rany” — niejasne, czyja zdrada.
- `Rise of Man` → „Kolebka ludzkości” — adaptacja, zostawić.
- `TUT_Pause_ICON`, `TUT_UI-Back` „— Wyjdź” obok „Wyjście” w `TUT_ExitAetherLamp_ICON` — dwie konwencje podpowiedzi.

## Decyzje użytkownika (2026-09-26)

Przyjęte i **wprowadzone** w `en-pl-review.json`:

| Klucz | EN | Było | Jest |
| --- | --- | --- | --- |
| `STRING_InventoryItems/Memory_Seafarer-Complete` | Poseidon's Blight | Udręka Posejdona | Niedola Posejdona |
| `STRING_Quests/Hephaestus3_TITLE` | Own worst enemy | Własny największy wróg | Sam sobie wrogiem |
| `STRING_Updated4/ACHIEVEMENT_WellOnYourWay_TITLE` | Well on your way | Dobra droga | Na dobrej drodze |
| `Dialog/Dialog/AntenorCovetous1.1` | My mind's eye is growing more potent | Wzrok mego umysłu rośnie w siłę. | Moje wewnętrzne oko nabiera mocy. |

„Udręka Demeter” i „jego udręka” w PoseidonTrapped1.2 zostają. Pozostałe tematy z listy „Do rozmowy”
(Kirke ↔ C.I.R.C.E., „czysta Nyks”, „odnowić Adrestię”, „Celowanie łukiem i włócznią” i niski priorytet)
bez odpowiedzi — **otwarte**, tekst bez zmian.

## Do sprawdzenia w grze

- Selektor języka: czy jest „Polski”, czy przełącza od razu i zostaje po restarcie.
- Legenda mapy: gdzie widać „Wyjście” (Transition_*); długie nazwy „System podtrzymywania życia (1)”,
  „Sklepy z egzotycznymi roślinami”, „Przeprawa przez nieczystości”.
- Pierwsza komora Kirke w Dolnych kwaterach: ciąg komunikatów zabezpieczeń i „Interfejs C.I.R.C.E.”
  — czy gracz łączy obie nazwy.
- Rozmowy z ocalałymi: czy „Ocalały” pojawia się przy kobietach.
- Menu: czy „Log” i „Journal” to dwie zakładki (obie „Dziennik”).
- Długie napisy: AntenorHubris1.1 (wiersz 126 znaków), NyxOverflow, SpecimentGrowth, StrandedInTheVoid,
  ArtemisMissing, LoveLetter — łamanie wierszy i czas wyświetlania.
- Wyzwania i ranking: ucięcie „Strącenie Ptaka stymfalijskiego”, „Gracz w rankingu światowym”.
- Wersaliki w nagłówkach: czy renderuje się Ą (Maitree-Cinzel Medium go nie ma).

## Stan po poprawkach

- Zmienione tylko pola `polish` ośmiu wpisów; `key`, `english` i struktura bez zmian (diff 8/8 linii).
- Plik po poprawkach: SHA-256 `d01d17d91ddea21e4535128083e6f6cbb5b104e1b4d923accbf2f7d84b4bedab`.
- `l10n_report.py` po poprawkach: brak=0, tokeny=0, płeć=0, adresat=0, liczebniki=0; terminy=9, długość=9,
  wielkie litery=6, typografia=27 i angielski=22 bez zmian wobec stanu sprzed review (fałszywe alarmy opisane
  w `translation-decisions.md`). Spójność=3 to nowe, zamierzone: „Exit” jako przycisk („Wyjdź”, `STRING_Buttons/Exit`)
  i jako element mapy („Wyjście”, `Transition_*`).
- `npx -y deno run --allow-read tools/check_games.ts` przechodzi (Review: tak).
- Paczka nie była przebudowywana; poprawki trafią do najbliższego wydania (0.2.0 w `dist/` ich nie zawiera).
- Synteza reviewera: terminy spójne z biblią (jedyny rozjazd — Kirke — poprawiony), narrator podniosły
  i czytelny, dziennik Adrestii naturalny w 1. osobie żeńskiej, instrukcje mechanik wierne. Ogólna ocena: bardzo dobre.
