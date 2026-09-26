# Void Bastards — niezależny przegląd lokalizacji PL

Data: 2026-09-26. Trzech reviewerów w świeżym kontekście (subagenci bez historii
tłumaczenia), tylko do odczytu, każdy na swojej partii, z dostępem do całego pliku
do sprawdzania spójności. Poprawki nanosił i weryfikował agent prowadzący.
Przegląd językowy **nie zastępuje testu w grze** — pełne przejście 0.2.x nadal czeka.

## Zakres

- Wejście: `translations/en-pl-review.json`, SHA-256
  `8226f2be871429140a26fc6dc0864f2ea0ab1742676133eb062537ae51448cd7` (przed poprawkami),
  2480 wpisów, 2479 z tekstem. Po poprawkach: `7dae46cbd8f47d11aea346adba04fd3faad70438627326b2cdf9fe0d1bc5da27`.
- Kontekst: `translations/bible.yaml`, `docs/translation-decisions.md`, `docs/technical.md`,
  `work/l10n-report.md`, pole `context` (notatki twórców z I2).
- Partie (wszystkie przeczytane w całości, **2480/2480**):
  - **A — narracja, 591 wpisów:** Dialog 174, CS 103, Star Map Event 92, MapPopup 75, Hint 66,
    Mission 22, Debrief 11, Campaign Flow 9, Loading 8, DemoDialog 7, desc_* 7, tydy_desc_* 7,
    DLC 3, RichPresence 3, StartMenu 2, Cutscene 1, Void Bastards 1.
  - **B — przedmioty i mechanika, 912 wpisów:** Part, Upgrade, UpgradeDescription(+AtLevel),
    ProgressUpgradeDetail, Junk, Item, Workbench, Component, Module Name, Interact, Hacked,
    Legend, NPC, Action, Log, Stat, Loadout, FOOD/FUEL/OBJECTIVE/objective, costsXMerits.
  - **C — interfejs i systemy, 977 wpisów:** Key, Options, PauseMenu, Difficulty, Profile, Offense,
    Character Trait(+Tooltip), Ship, Ship Trait(+Tooltip), Achievement, Challenges, Star Map, Map,
    HUD, UI, Title, Language, PRESS ANY…, seach_key_*.
- Luki: w repo nie ma kodu gry ani tabel innych języków (`work/ref-*.json` poza gitem), więc
  nie da się ustalić, co gra dokleja do części etykiet — zebrane w „Nierozstrzygnięte”.

## Błędy — wprowadzone (31 wpisów)

| Klucz | EN | Było | Jest | Przesłanka |
| --- | --- | --- | --- | --- |
| `UpgradeDescription(+AtLevel)/PistolAmmo_L1` | …in hab modules | w modułach mieszkalnych | w kwaterach | „hab” = moduł „Kwatery” / KWAT na mapie; „modułu mieszkalnego” gracz nie zobaczy |
| `UpgradeDescription(+AtLevel)/RadDartGunAmmo_L1` | …in pac nuc bays | w wyrzutniach atomowych Pac | w modułach min atomowych Pac | „nuc bay” = „Miny atomowe” / ATOM; „wyrzutnie” (WYRZ) to moduł torped — tekst wysyłał w złe miejsce |
| `UpgradeDescription(+AtLevel)/HackDoor_L1`, `_L2` | lock or unlock doors | zamykania i otwierania / zamykanie i otwieranie | blokowania i odblokowywania / blokowanie i odblokowywanie | zmieniało mechanikę; terminal: „zablokuj/odblokuj”, „Zablokowano” |
| `Hint/Lock` | Lock doors… (they can't unlock them) | Zamykaj drzwi… nie umieją ich otworzyć | Blokuj drzwi… nie umieją ich odblokować | spójnie z HackDoor |
| `Hint/Robots` | Secbots can unlock doors… | Secboty otwierają drzwi… | Secboty odblokowują drzwi… | jw. |
| `UpgradeDescription/BombThrower_L1`, `DartGun_L1`, `Laser_L1`, `Zapper_L1`; `UpgradeDescriptionAtLevel/DartGun_L1–L3`, `Laser_L1–L2`, `Zapper_L1–L2`; `Star Map Event/HazardDescription` | …. don't / doesn't / passes… | mała litera po kropce | wielka litera | ortografia — przepisana niechlujność EN (12 wpisów) |
| `Challenges/mystery monsters description` | Prepare yourself for anything! | Bądź gotowy na wszystko! | Przygotuj się na wszystko! | forma męska do gracza (biblia: bezrodzajowo) |
| `Challenges/DifficultySelectSettingsValue`, `…SettingsAdditionalValue`, `…SuggestHarder`, `…SuggestHarderAlt` | These settings are worth␣ | …ustawienia: | …ustawienia:␣ | liczba doklejana w kodzie — bez spacji „ustawienia:12”; build zachowuje spacje końcowe |
| `Star Map/VoidArk` | …where you were recently rehydrated | …niedawno przywrócono ci płyny | …niedawno cię nawodniono | „rehydrate” = „nawodnić” w całej grze (Stat, Achievement, Dialog/Respawn*) |
| `Star Map Event/TwisterDescription` | …and not just in the way that you did after… Ion Bru | i nie tak jak po… | i to nie tylko tak jak po… | odwrócony sens, ginął żart |
| `MapPopup/Janitorial` | dirt and grime | brudu i smaru | kurzu i brudu | „grime” to brud; „smar” to w tej samej legendzie zagrożenie (HazardOil) |
| `Star Map Event/MineFlotsamDescription` | You find an inert buzz bomb drone. The buzzer has run out… | nieaktywny dron-bombę. Brzęczkowi skończyła się… | nieaktywnego drona-bombę. Skończyła mu się… | błąd biernika; „Brzęczek” to w grze nazwa części (Buzz Box) |

Odrzucone jako pewne: `Legend/HeartstarterTerminal` („Igniter␣”) — spacja w EN najpewniej
przypadkowa; `Dialog/InitialObjectives_2_BACS` (małe litery) — w EN ten wydruk jest
konsekwentnie małymi literami.

## Decyzje sprzed verticala — werdykty

| Decyzja | Werdykt | Przykłady / uwagi |
| --- | --- | --- |
| B.A.C.S. — mężczyzna, korpo-nowomowa | **utrzymać** | „Wiedziałem, że wybrałem…”, „musiałem odnotować”; żargon („interesariusze”, „Aneks:”) działa. Słabsze tylko miejsca, gdzie obejście rodzaju zmienia go w komunikat bezosobowy (Do rozmowy 1) |
| Gracz bezrodzajowo | **utrzymać** | 1 wyciek naprawiony (mystery monsters). Dobre obejścia: „bystrą osobę”, „zastanawiało cię”. `StartMenu/UnlockFoon` „prawdziwy z ciebie twardy drań” — cytat nazwy poziomu, akceptowalne |
| Cechy postaci jako rzeczowniki | **utrzymać** | spójne we wszystkich 69 cechach; najmocniejsza część tłumaczenia |
| Opisy osiągnięć `_past` bezosobowo | **utrzymać**, szyk do rozmowy | Do rozmowy 2 |
| Piraci — szkocki → polski slang | **utrzymać** | „Gnojek zwiał. Kurde.”, „My nie mordercy! My piraci!”; do rozmowy tylko „kapuś” i „osobiście” |
| Li Hua bezrodzajowo | **utrzymać** | |
| Liczby jako etykiety, `COUNT dni / COUNT dzień`, `_PLURAL` w mianowniku | **utrzymać** | 4 brakujące spacje dodane |
| Nazwy klawiszy | **utrzymać** | ewentualnie LPM/PPM/ŚPM po teście |
| klient, zasługa, punkty lizusa, autoryzacja, karta obywatela, złom, identyfikator, drukarka wierszowa, BHP, Mgławica Sargassowa | **utrzymać** | spójne w całym pliku |
| action items → zadania do realizacji | **utrzymać z korektą biblii** | w praktyce cała gra mówi „zadanie/zadania”; biblia dopasowana do praktyki |
| Nazwy wrogów (Muszka, Podglądacz, Klawisz, Gówniarz, Woźny, Skryba, Upiór, Turysta, Zek) | **utrzymać** | do rozmowy tylko stopnie „Veteran” (Do rozmowy 5) |
| Void Ark, S.T.E.V., P.A.L., FTL, WCG, CNT bez tłumaczenia | **utrzymać** | Void Ark nieodmienny, rodzaj męski — spójnie |
| Okazje: Klient wygasł, Twardy Drań, Bułka z masłem, Lizus, Śledzik na śniadanie, O ja cię kręcę!, Trumna poczeka, krawężnik | **utrzymać** | |
| „Złodzieje sklepowi wszystkich krajów, łączcie się!” | **utrzymać** | w grze sprawdzić, czy napis zdąży się wyświetlić |
| Zszywacz, Walkurzacz, Klasterflak, Chirurgia dla bystrzaków, Teatr operacyjny, Kazamaty | **utrzymać** | odwołania w opisach amunicji zgodne |
| Log akcji ~20 znaków | **utrzymać** | wszystkie wpisy Log mieszczą się (najdłuższy 18) |
| VSync na liście „bez tłumaczenia”, a w opcjach „Synchronizacja pionowa” | **brak kontekstu** | rozstrzygnie test szerokości; lista tylko wycisza raport, nie wymusza |
| Długie nazwy w warsztacie i na mapie gwiezdnej | **brak kontekstu** | test w grze; skróty zapasowe niżej |

## Do rozmowy

Stan po rozmowie z użytkownikiem (2026-09-26): **punkty 1–7 przyjęte i wprowadzone**
(31 wpisów), z tymi wyborami: w 6 „przerób / złom do przeróbki / Przerobiono” (plus
`MapPopup/fixTerminal` „Przerabia złom”), w 7 „Zarządzanie pieczarkowe”. Z punktów 5 i 7
przyjęto tylko pozycje przedstawione w rozmowie — „Pirat bosman”, „Figura autorytetu”,
„stacja… papiernicza” i „Do realizacji!” pozostają otwarte, tak jak punkty 8–10.

1. **Sztywne obejścia rodzaju w samouczku B.A.C.S.-a** (pierwsze minuty gry):
   - `Dialog/BuzzController_1_BACS` „Czy zauważono na tym statku brzęczek?” → „Czy wiesz, że na tym statku jest brzęczek?”
   - `Dialog/Helm_1_BACS` „Zgubiony kierunek? …” → „Nie wiesz, dokąd iść? …”
   - `Dialog/Leave_1_BACS` „…zanim dojdzie do zabicia albo uduszenia.” → „…zanim ktoś cię zabije albo się udusisz.”
   - `Dialog/ReturnWorkbench_2_BACS` „Skoro można by w warsztacie zbudować lokalizator części.” → „Zamiast budować w warsztacie lokalizator części.”
   - Zysk: naturalny głos B.A.C.S.-a, dalej bezrodzajowo. Koszt: 4 wpisy.
2. **Osiągnięcia `_past` z „… udana” na końcu** (`ach_campaign_complete`, `hard_complete`,
   `impossible_complete`, `no_deaths`, `no_deaths_impossible`, `no_ugprades`, `no_weapons`,
   `only_primary/secondary/tool` `_desc_past`): „Ucieczka z mgławicy na poziomie NORMALNY … udana.”
   → „Udana ucieczka z mgławicy na poziomie NORMALNY …”. Przy okazji `depth_two` → „Doprowadzono
   S.T.E.V. na drugą głębokość mgławicy.”, `survive_pirate` → „Przeżyto spotkanie z piratami.” ~12 wpisów.
3. **Piraci:** `Dialog/PirateDisabled_1_Pirate` „Jakiś kapuś puścił…” → „Jakiś frajer puścił…”
   („dobber” po szkocku to idiota, twórcy: „somebody”); `PirateEscape_2_LiHua` „mam to niby zrobić
   osobiście??” → „Matoły — mam tam wyleźć i zrobić to za was??”; `PirateScanB_2_Pirate` „Luli gadał”
   → „Luli ciągle gada…” (płeć Luli nieznana).
4. **Nazwy akcji na ekranie klawiszy** (`Action/Attack`, `Jump`, `Run`): „Strzał/Skok/Bieg” obok
   „Celuj/Kucnij/Przeładuj” → „Strzelaj/Skacz/Biegnij”.
5. **Stopnie wrogów** (`NPC/Alien L2` „Stary woźny”, `Sniper L2` „Starszy skryba”, `Sniper L3` „Stary skryba”)
   — hierarchia czyta się odwrotnie → „Woźny weteran”, „Skryba weteran”. Też `NPC/Pirate L2`
   „Pirat mat” → „Pirat bosman” (niski priorytet).
6. **„upscale” = „ulepsz”** (`Interact/Convert`, `ToConvert`, `Log/Converted`) koliduje z ulepszeniami
   z warsztatu → „uszlachetnij / Uszlachetniono” albo „przerób / Przerobiono”.
7. **Kalambury i puenty:** `Dialog/LinePrinter_2_BACS` „Proszę się nadal doczekiwać, szukając
   identyfikatora.” → „Proszę czekać dalej — i przy okazji szukać identyfikatora.”;
   `Challenges/hush` „Zarządzanie grzybkowe” → „Zarządzanie pieczarkowe” / „Metoda pieczarki”;
   `ach_no_upgrades_name` „Sknerstwo” → „Sknera”; `Challenges/hacker` „Autorytet” (= cecha
   AUTHORITATIVE) → „Figura autorytetu”; `Dialog/InitialObjectives_3_Player` → „Super. Gdzie tu
   najbliższa stacja… papiernicza?”; `Workbench/ProgressUpgradeTitle` „Zadanie!” (= `…Alt2`) → „Do realizacji!”.
8. **Drobne luki wierności:** `UpgradeDescription(+AtLevel)/ToxicResist_L1` (EN mówi o czasie mdłości),
   `PlasmaLauncher_L2` (czas przeładowania o połowę), `MonsterScan_L1` (brak „do budowy”),
   `ProgressUpgradeDetail/DepthProgress_L4` („mandated” → „nakazane”), `Offense/UNOBSERVANT`
   → „Niezgłoszenie choroby przedstawicielom Xonnox.”, `Character Trait Tooltip/LOOKS_THE_PART`,
   `SUSPICIOUS` „…to wykrywają” → „…wykrywają tę postać”, `Star Map Event/BombDescription`
   „żeby się wyłączyli” → „wyłączyły” (urządzenia).
9. **Wygładzenia komiksu i B.A.C.S.-a:** `CS_Prog5_PG1_PAN4_Text1` → „A teraz cię wysuszymy przed
   podróżą FTL.”; `CS_Prog5_PG2_PAN2_Text5` → „Areszt bezterminowy.”; `Dialog/FTL_2_BACS` —
   bezokolicznik jak w pozostałych zadaniach; `UseLocate_1_BACS` „Bystre myślenie!” → „Sprytnie!”;
   `ProgressPickupC_1_BACS` anakolut → „Nawet w postaci woreczka proszku…”; `RespawnH_1_BACS`
   „przerwy na wypróżnienie płynne i stałe”; `CS_Intro_PG1_PAN1_Text2` „cholera… cholernego”;
   `Hint/MineSafe`, `MapPopup/Powerplant` („płyn płynie”), `Star Map Event/HealthDescription`,
   `desc_short`, `desc_long_f`, `Stat/FoodEaten`, `Interact/PAL`, `Ship Trait/NO_MINIMAP`,
   `Title/CameraCuteName`, `Options/ToggleRunLabel`, `Star Map/ShipTerminal` („Requisitions” = „Zaopatrzenie”).
10. **Długość (raport 18 zgłoszeń):** `Star Map Event/PirateFollowingTitle` → „Piraci namierzają!”,
    `Dialog/Sentinels_2_BACS` → „Nikt nie będzie ci miał za złe, że ich zamordujesz.”,
    `Offense/FLEET_FOOT` → „Przechodzenie poza pasami.” — reszta tylko jeśli test pokaże ucięcie
    (skróty zapasowe: LPM/PPM/ŚPM, „VP ds. muszek”, „Świadectwo rej.”, „Ładunek łańcuchowy”, ŁAD/MOST).

## Nierozstrzygnięte (przeczytane, brak kontekstu)

- `Challenges/DifficultySelect*` — który wariant (zwykły czy Alt z `#`) gra wybiera i co dokleja po liczbie.
- `Interact/UsesAvailable`, `Remaining`, `SecondsAvailable`, `Discovered`, `To`, `StockRemaining`,
  `Workbench/UseProgressPart` — zależą od doklejanej liczby/nazwy.
- `NPC/Boss`, `NPC/Allied` — możliwe zbitki „Szef Stary woźny”.
- `Star Map/Builds`, `All`, `Gain/Lose/Eat/Burn`; `Star Map Event/*Effect` „Zyskano/Utracono”; `Star Map Event/All`.
- `Title/*CuteName` z Pan/Pani; `PauseMenu/Seconds`, `DemoDialog/Seconds` „s”; `Profile/StatusTitle`;
  `Challenges/ModeScore` „Zdobyte w tym:”; `Stat/PiratesEscaped` „Zbiegli piraci” (ucieczki gracza?).
- Piraci o nieznanym kliencie w rodzaju męskim („Rozwalić go!”, „palanta… go dorwijcie”) — rodzaj
  ogólny przy wyzwiskach, nie zwrot do gracza; akceptowalne.

## Do sprawdzenia w grze

- **Wyzwania → ekran trudności:** spacja przed liczbą punktów lizusa i co stoi po liczbie.
- **Ustawienia sterowania:** długie „Lewy/Prawy/Środkowy przycisk myszy”, także w podpowiedziach z `KEY`.
- **Warsztat i szafka na części:** najdłuższe nazwy („Chirurgia dla bystrzaków” 24, „Świadectwo
  rejestracji” 22, „Wiceprezes ds. muszek” 21, „Zagrożenia środowiskowe” 23).
- **Mapa statku:** skróty ŁADOWNIA, MOSTEK obok KWAT, SPRZ — czy etykiety nie nachodzą.
- **Mapa gwiezdna:** tytuły zdarzeń („Namierzenie przez piratów!”, „Tunel czasoprzestrzenny”), nazwy statków,
  etykiety „Zyskano/Utracono” przy zasobach.
- **Profil postaci:** wykroczenia (FLEET_FOOT), opisy amunicji.
- **Napisy dialogów:** czy `BuzzController_3_Player` i `Sentinels_2_BACS` zdążą się przeczytać.
- **Opcje:** „Synchronizacja pionowa”.

## Ponowna kontrola po poprawkach

- 31 zmienionych wpisów sprawdzonych ponownie z EN; zmieniane było tylko pole `polish`,
  klucze, EN i kolejność bez zmian (plik zapisany w tym samym formacie).
- `l10n_report.py`: 0 zgłoszeń poza 18 długości (bez zmian). 15 zgłoszeń typografii (spacja
  końcowa w EN bez doklejanej treści) opisane w biblii jako wyjątek; 4 prawdziwe braki spacji naprawione.
- `tools/check_games.ts`: przechodzi.
- Po decyzjach użytkownika: kolejne 31 wpisów; raport kontrolny bez nowych zgłoszeń
  (długość nadal 18), `check_games.ts` przechodzi. Terminy „przerób” i „weteran” dopisane do biblii.
- Paczka nie była przebudowywana — poprawki wejdą do następnego wydania.
