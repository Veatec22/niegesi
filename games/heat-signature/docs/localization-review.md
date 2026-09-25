# Heat Signature — niezależny przegląd lokalizacji PL

Reviewer w świeżym kontekście, tylko do odczytu. Data: 2026-09-25.
Status wszystkich poprawek poniżej: **proponowane** (nic nie zostało naniesione przez reviewera).

## Zakres

- `translations/pl.json` — SHA-256 `a1cdf851e2acff55f9f8ad740a9de80ee5b11b93e13193cce009644a849448bc`, 2650 kluczy.
- `translations/items.json` — SHA-256 `3949ba4ce2256221923663fcbb8c36eb5cfa908cac2b4d8f5876b236ddb16ed6`
  (24 rzeczowniki, 25 przymiotników, 5 określeń).
- `translations/en-pl-review.json` — 2704 wiersze; wartości PL 1:1 zgodne z `pl.json` (brak braków,
  rozjazdów i nadmiarowych kluczy). `parts/*.json` zgodne z `pl.json`; 117 kluczy pl.json (vertical) jest poza parts.
- Kontekst: oryginalne `Dialog/*.txt` (13 plików, czytane scenami), `work/strings-by-function.txt`,
  `work/preview-out.txt`, `work/l10n-report.md`, `plugin/Translate.h` (logika składania).
- Złożone napisy sprawdzano Pythonowym portem silnika z `Translate.h` na aktualnym `dist/notgeese/pl.tsv`.
  Uwaga: `work/preview-out.txt` jest starszy od `pl.json` — pokazuje m.in. „Zabij oficera Sovereign w, który…”
  i „Guard, patroluje”; aktualny TSV daje poprawnie „Zabij oficera Sovereign, który…” i „Strażnik, patroluje”.
  Warto odświeżyć podgląd przed oddaniem.
- Pokrycie partii: `work/review-coverage.md`. Przeczytano **2704/2704** wiersze: 522 wiersze dialogów scenami
  (13 plików: 4 barmanów, Fiasco ×4, TutorialEnd, 4 terminale), 1578 literałów EXE, 550 szablonów, 54 wiersze słownika
  nazw przedmiotów (plus ~40 złożonych nazw i napisów sprawdzonych symulacją). Luki: brak obrazu gry (długość, ucinanie,
  kontekst części etykiet) — wymienione w „Do sprawdzenia w grze”.
- Wynik: 28 punktów pewnych błędów (część grupuje kilka kluczy; 4 dotyczą techniki składania lub wymagają potwierdzenia
  w grze — zaznaczone jako „pewność średnia”), 12 drobnych propozycji redakcyjnych, 7 tematów do rozmowy.
  Najważniejsze: wycieki formy męskiej dla postaci gracza w UI (pkt 15, 20–22) i błąd szablonów `{0}{9}` (pkt 27).

## Błędy (pewne) — proponowane poprawki

Format: klucz EN → obecne PL → proponowane PL. Przesłanka pod spodem.

### Dialogi

1. **`It was, but it also bricked their long range drive, so they were stuck. Sovereign sent no help, so they set up shop.`**
   (BartenderDialogueFoundry.txt:105)
   - obecne: `Okazał się, ale przy okazji uwalił im napęd dalekiego zasięgu, więc utknęli. Sovereign nie przysłało pomocy, więc się tu urządzili.`
   - proponowane: `Okazał się dobry, ale przy tym uwalił im napęd dalekiego zasięgu, więc utknęli. Sovereign nie przysłało pomocy, więc się tu urządzili.`
   - przesłanka: język — „Okazał się,” bez orzecznika jest niegramatyczną elipsą (EN „It was” odsyła do „if the acid was good”); dodatkowo powtórzenie „okazał/okazji”.

2. **`What if you have the wrong person?`** (BartenderDialogueOffworld.txt:255, odpowiedź gracza o torturach)
   - obecne: `A jeśli trafi na niewłaściwą osobę?`
   - proponowane: `A jeśli to niewłaściwa osoba?`
   - przesłanka: składnia — „trafi” nie ma podmiotu (tortury/wy?); odpowiedź Genevy „All force is wrong when you're wrong” dotyczy pomyłki co do osoby.

3. **`Nothing. They're all dead by thirty-six.`** (FiascoEndGame.txt:109)
   - obecne: `Nic. Wszyscy nie żyją przed trzydziestką szóstką.`
   - proponowane: `Nic. Wszyscy giną, zanim skończą trzydzieści sześć lat.`
   - przesłanka: język — „Wszyscy nie żyją przed…” to niepoprawne połączenie kwantyfikatora z przeczeniem i stanem; „trzydziestką szóstką” niejasne (wiek).

4. **`No shortage of parties who'll pay you to screw with Sovereign, so keep screwing with Sovereign.`** (BartenderDialogueSovereign.txt:156)
   - obecne: `Nie brakuje chętnych, żeby ci zapłacić za mieszanie Sovereign szyków, więc mieszaj dalej.`
   - proponowane: `Nie brakuje chętnych, którzy zapłacą ci za mieszanie szyków Sovereign, więc mieszaj dalej.`
   - przesłanka: język — rozbity frazeologizm („mieszać komuś szyki”) i szyk; „chętnych, żeby ci zapłacić” to kalka.

### Narracja otwierająca (EXE: oTutorial_Step_0)

5. **`First three times, no-one who lived there could fight it.`**
   - obecne: `Za pierwszymi trzema razami nikt z mieszkańców nie mógł się przeciwstawić.`
   - proponowane: `Za pierwszymi trzema razami żadna z mieszkających tu osób nie mogła się przeciwstawić.`
   - przesłanka: zgoda rodzaju w ciągu zdań — następne kwestie (`This time one of them can.` → „Tym razem jedna może.”, `This time one of them has…` → „Tym razem jedna ma…”) odsyłają żeńskim „jedna” do „mieszkańców” (r. męski). „Osoba” daje poprawne „jedna” bez zmieniania kolejnych dwóch wpisów i zachowuje fakt, że Fiasco jest kobietą.

### UI i menu

6. **`If you turn off permadeath, anything that would normally permanently kill your character will instead return you to when you last left a station.\r\n#We don't recommend doing this unless permadeath is really spoiling the game for you - it leads to less interesting stories and less variety.`**
   - obecne: `Gdy wyłączysz trwałą śmierć, wszystko, co normalnie zabiłoby twoją postać na zawsze, cofnie cię do chwili, gdy ostatnio opuszczasz stację.\r\n#Odradzamy to, …` (reszta bez zmian)
   - proponowane: `Gdy wyłączysz trwałą śmierć, wszystko, co normalnie zabiłoby twoją postać na zawsze, cofnie cię do chwili ostatniego opuszczenia stacji.\r\n#Odradzamy to, chyba że trwała śmierć naprawdę psuje ci zabawę — historie są wtedy mniej ciekawe i mniej różnorodne.`
   - przesłanka: język — czas teraźniejszy „opuszczasz” w odniesieniu do przeszłości; forma rzeczownikowa jest neutralna płciowo.

7. **`We'd like to get your thoughts when you feel you're done. This button will try to take you to our feedback form, but if it doesn't, you can copy it to you clipboard instead.`**
   - obecne: `Kiedy uznasz, że masz dość, chętnie poznamy twoje zdanie. …`
   - proponowane: `Gdy skończysz grać, chętnie poznamy twoje zdanie. Ten przycisk spróbuje otworzyć nasz formularz opinii (po angielsku). Jeśli się nie uda, możesz skopiować link do schowka.`
   - przesłanka: sens — „when you feel you're done” = gdy skończysz z grą; „masz dość” znaczy „jesteś zmęczony/zniechęcony”.

8. **`If you've encountered a mission whose difficulty level or pay seemed wrong, tell us about it here! This button will try to take you to the form, but if it doesn't, you can copy it to you clipboard instead.`**
   - obecne: `Jeśli trafisz na misję, której poziom trudności albo zapłata wydają się nie takie, daj nam znać! …`
   - proponowane: `Jeśli trafisz na misję, której poziom trudności albo zapłata wydają się nieodpowiednie, daj nam znać! Ten przycisk spróbuje otworzyć formularz (po angielsku). Jeśli się nie uda, możesz skopiować link do schowka.`
   - przesłanka: język — „wydają się nie takie” jest urwane/potoczne w instrukcji.

### Przedmioty i cechy

9. **` not recharged due to Technophobe`** i szablon **`{0} not recharged due to Technophobe`**
   - obecne: ` — nienaładowano (Technofobia)` / `{0} — nienaładowano (Technofobia)`
   - proponowane: ` — nie naładowano (Technofobia)` / `{0} — nie naładowano (Technofobia)`
   - przesłanka: ortografia — „nie” z bezosobową formą na -no/-to piszemy osobno.

10. **` unlocked.#It can now be found in this and all future galaxies.`** i szablon **`{0} unlocked.#It can now be found in this and all future galaxies.`**
    - obecne: ` — odblokowano.#Można go teraz znaleźć…` / `Odblokowano: {0}.#Można go teraz znaleźć w tej i wszystkich przyszłych galaktykach.`
    - proponowane: ` — odblokowano.#Ten przedmiot można teraz znaleźć w tej i wszystkich przyszłych galaktykach.` / `Odblokowano: {0}.#Ten przedmiot można teraz znaleźć w tej i wszystkich przyszłych galaktykach.`
    - przesłanka: rodzaj — „go” nie pasuje do przedmiotów unikatowych żeńskich (np. „Multikula”, `The Multiball`).

11. **`Effective against armoured guards.`** / **`Effective against shielded guards.`**
    - obecne: `Skuteczny na opancerzonych strażników.` / `Skuteczny na strażników z tarczami.`
    - proponowane: `Skuteczny przeciw opancerzonym strażnikom.` / `Skuteczny przeciw strażnikom z tarczami.`
    - przesłanka: język — „skuteczny na kogoś” to potoczna kalka; norma: „skuteczny przeciw/wobec”.

12. **`{0} [Damaged]`** i fragment **` [Damaged]`** (DrawInventoryList, obok `Pod Destroyed`)
    - obecne: `{0} [uszkodzony]` / ` [uszkodzony]`
    - proponowane: `{0} [uszkodzona]` / ` [uszkodzona]`
    - przesłanka: rodzaj — w liście ekwipunku oznacza kapsułę („Kapsuła Breacher”, stan `Damaged` jest już przetłumaczony jako „Uszkodzona”). Pewność średnia: potwierdzić na ekranie ekwipunku z uszkodzoną kapsułą (patrz „Do sprawdzenia”).

### Misje — ekran końca misji

13. **`Times Seen:`**, **`Times Seen: `**, **`Times Seen: {0}`**
    - obecne: `Razy zauważono:` / `Razy zauważono: ` / `Razy zauważono: {0}`
    - proponowane: `Liczba wykryć:` / `Liczba wykryć: ` / `Liczba wykryć: {0}`
    - przesłanka: język — „Razy zauważono” jest niegramatyczne; obok są „Alarmy:”, „Zabójstwa:”.

14. **`Non-target crew killed:`** / **`Non-target crew harmed:`**
    - obecne: `Zabici spoza celu:` / `Ranni spoza celu:`
    - proponowane: `Zabici (poza celami):` / `Ranni (poza celami):`
    - przesłanka: język — „spoza celu” jest niejasne (sugeruje miejsce); chodzi o załogę niebędącą celem misji.

15. **`Remain unseen`** (GetReminderForSpecialMissionType — przypomnienie klauzuli ducha)
    - obecne: `Pozostań niewidoczny`
    - proponowane: `Nie daj się zobaczyć`
    - przesłanka: **rodzaj gracza** — forma męska w komunikacie do losowej postaci; to jedyny taki wyciek znaleziony w przypomnieniach klauzul.

16. **`Times seen: `** (DrawMissionRatingsText) — jak pkt 13: `Razy zauważono: ` → `Liczba wykryć: `.

17. **`The most lethal contractors in the galaxy. Step into their pulsing sensor range …`** (InitialiseEnums, opis Predatora)
    - obecne: `Najzabójczy najemnicy w galaktyce. …`
    - proponowane: `Najbardziej zabójczy najemnicy w galaktyce. Wejdź w pulsujący zasięg ich czujnika, a natychmiast cię wykryją, teleportują się do ciebie i zabiją jednym ruchem. Tarcze nie pomogą — ostrze już w tobie tkwi, gdy kończą glitch. Powodzenia.\r\n\r\nZawieszenie Drapieżnika wyłącza jego czujnik i teleporter. Przeprogramowanie robi coś innego.`
    - przesłanka: język — „najzabójczy” nie jest poprawną formą stopnia najwyższego (l.mn. męskoosobowa).

18. **`{0} was detected by {1}'s heat sensor.`** (oSensorModule_Step_0)
    - obecne: `{0} — wykrył czujnik ciepła: {1}.`
    - proponowane: `Czujnik ciepła ({1}) wykrywa: {0}.`
    - przesłanka: sens/składnia — obecny szyk czyta się „{0} wykrył czujnik ciepła”, czyli odwrotnie; propozycja trzyma imię w mianowniku po dwukropku jak inne wpisy dziennika („Gio Vanderstar zabija: Strażnik”). Fragmenty zapasowe ` was detected by ` → ` — wykrył cię ` i `'s heat sensor.` → ` (czujnik ciepła).` dają przy braku szablonu „X — wykrył cię Y (czujnik ciepła).”, co jest poprawne, ale tylko dla gracza.

19. **`Doesn't tick up while paused, obviously.`** w kluczu **` for every ten seconds you spend on or near the ship. Doesn't tick up while paused, obviously.`**
    - obecne: ` za każde dziesięć sekund na statku lub w jego pobliżu. Podczas pauzy oczywiście nie liczy.`
    - proponowane: ` za każde dziesięć sekund na statku lub w jego pobliżu. Podczas pauzy licznik oczywiście stoi.`
    - przesłanka: składnia — „nie liczy” bez podmiotu.

### HUD, stan postaci, dziennik

20. **Etykiety stanu wspólne dla strażników i postaci gracza** — formy męskie trafiają do postaci
    (w tym kobiet) na ekranie wyboru postaci i w HUD gracza. Konteksty z EXE:
    `Unconscious` (ArrivedAtPlayersBody, HealPlayerIfBleeding…), `UNCONSCIOUS` (PlayerStateUnconscious),
    `Dead` / `Captured` / `Lost` / `Available` / `Active` (CharacterSelect, LoadCharacters, CharacterIsChooseable…).
    | klucz | obecne | proponowane |
    | --- | --- | --- |
    | `Unconscious` | Nieprzytomny | Bez przytomności |
    | `UNCONSCIOUS` | NIEPRZYTOMNY | BEZ PRZYTOMNOŚCI |
    | `Dead` | Martwy | Nie żyje |
    | `Captured` | Pojmany | W niewoli |
    | `Lost` | Zaginiony | Zaginięcie |
    | `Available` | Dostępny | Do wyboru |
    | `Active` | Aktywny | W akcji |
    - przesłanka: **rodzaj gracza/postaci** — postacie są losowane (Female/Male); te same klucze opisują też strażników, więc forma musi być neutralna. Etykiety w szyku z przecinkiem (`, Dead` → „, martwy”, `, Unconscious` → „, nieprzytomny”) dotyczą tylko opisu strażnika i mogą zostać.

21. **`Killed in mysterious - some might say glitchy - circumstances`** (PlayerCreate — przyczyna śmierci postaci)
    - obecne: `Zginął w tajemniczych — niektórzy powiedzą: glitchowych — okolicznościach`
    - proponowane: `Śmierć w tajemniczych — niektórzy powiedzą: glitchowych — okolicznościach`
    - przesłanka: **rodzaj postaci** — pozostałe przyczyny są rzeczownikami („Wykrwawienie w kosmosie”, „Uduszenie w kosmosie”, „Anihilacja w: …”); napis pojawia się w „Dziś pijemy za: X.##…”.

22. **`Crumbled to dust`** (PlayerHandleDamageSignal)
    - obecne: `Rozsypał się w pył`
    - proponowane: `Obrócenie w pył`
    - przesłanka: jak wyżej — forma męska dla postaci gracza.

23. **`Your ship won't dock without you inside - it's possible you left yourself behind somewhere`**
    - obecne: `Statek nie zadokuje bez ciebie w środku — możliwe, że zostawiono cię gdzieś po drodze`
    - proponowane: `Statek nie zadokuje bez ciebie w środku — możliwe, że twoja postać została gdzieś po drodze`
    - przesłanka: sens — „zostawiono cię” wskazuje na kogoś trzeciego; w EN to gracz sam się „zostawił” (np. zdalne sterowanie kapsułą). Propozycja jest neutralna płciowo.

### Postacie, rankingi, statystyki

24. **`Glorious Peers`** (GloryLeaderboardMenu)
    - obecne: `Chwalebni rówieśnicy`
    - proponowane: `Chwalebni rywale`
    - przesłanka: sens — „peers” to gracze o podobnym wyniku, nie „rówieśnicy” (ten sam wiek).

25. **`You start with an embarrassing amount of money.`** (cecha `Rich`)
    - obecne: `Zaczynasz z żenująco dużą ilością pieniędzy.`
    - proponowane: `Zaczynasz z żenująco dużą sumą pieniędzy.`
    - przesłanka: język — „ilość” przy pieniądzach jest błędem normatywnym.

26. **`#Defended: only their {0} can be crashed or hacked`**
    - obecne: `#Chroniony: zawiesić albo zhakować można tylko jego {0}`
    - proponowane: `#Chroniony: zawiesić albo zhakować można tylko jego sprzęt: {0}`
    - przesłanka: składnia — luka stoi w pozycji biernika, a gra wstawia mianownik („tylko jego Tarcza”, „tylko jego Czujnik ciepła”); przy nazwach żeńskich wychodzi błąd. Dwukropek trzyma nazwę w mianowniku.

### Technika składania (pewne, potwierdzone symulacją silnika)

27. **Szablony z sąsiadującymi lukami `{0}{9}`** — 28 wierszy w `pl.tsv`, np.
    `Rescue my mum from {0}{9}`, `Rescue my idiot kid, who got captured by {0}{9}`.
    `Translate.h` dopasowuje najkrótszą niepustą lukę, więc `{0}` dostaje jeden znak, a reszta wpada do `{9}`.
    Symulacja: `Rescue my mum from the Glitchers, as fast as possible` → **„Uratuj moją mamę z rąk the Glitchers, jak najszybciej”**
    (bez przyrostka: „…z rąk Glitchers” — poprawnie; z `Offworld Security` błąd niewidoczny, bo nie ma „the”).
    - proponowane: zmienić te szablony na `…{0}, {9}` (EN i PL, z przecinkiem jako literałem) i dodać wiersze bez przecinka:
      `as fast as possible` → `jak najszybciej`, `avoiding alarms as much as possible` → `unikając alarmów, jak się da`,
      `killing as few people as possible` → `zabijając jak najmniej osób`, `killing as few other people as possible` → `zabijając jak najmniej innych osób`,
      `harming as few other people as possible` → `krzywdząc jak najmniej innych osób`, `being seen as little as possible` → `pokazując się jak najmniej`.
      Alternatywa: poprawka w silniku (pusta litera między lukami = dopasuj najdłuższą wartość ze słownika). Wybór należy do agenta prowadzącego.
    - przesłanka: technika — angielska resztka w celu misji osobistej.

28. **Brak szablonu `{0} Stronghold`** (PlaceStrongholds dokleja ` Stronghold` do nazwy frakcji)
    - obecnie: `Foundry Stronghold` → „Foundry — twierdza” (fragment); jest tylko `The {0} Stronghold` → „Twierdza {0}”.
    - proponowane: dodać szablon `{0} Stronghold` → `Twierdza {0}`.
    - przesłanka: spójność nazw twierdz na mapie i w komunikatach. Pewność średnia co do dokładnej postaci napisu — potwierdzić na mapie.

## Drobne propozycje redakcyjne (niski koszt, do przyjęcia hurtem)

| klucz EN | obecne | proponowane | uzasadnienie |
| --- | --- | --- | --- |
| `I don't have the bandwidth to process that.` | Nie mam mocy przerobowych, żeby to przetworzyć. | Nie mam mocy przerobowych, żeby to ogarnąć. | „przerobowych… przetworzyć” — tautologia |
| `We've got no interest in the acid, but as the nearest planet this is legally our space, and we won't stand for killing in our space.` | …ale jako najbliższa planeta mamy tu prawnie swoją przestrzeń, a w naszej przestrzeni nie będzie zabijania. | Kwas nas nie interesuje, ale jesteśmy najbliższą planetą, więc prawnie to nasza przestrzeń, a w naszej przestrzeni nie będzie zabijania. | „mamy tu prawnie swoją przestrzeń” — sztywne |
| `We agree. Ours is killing.` | Zgoda. Nasza to zabijanie. | Zgoda. Nasza granica to zabijanie. | gracz mówił „granice” (l.mn.); „nasza” bez rzeczownika wisi |
| `You guys took it from there. And I only got shot once.` | Dalej poszło już z wami. A ja dostałam kulkę tylko raz. | Dalej to już była wasza robota. A ja dostałam kulkę tylko raz. | „poszło z wami” — kalka |
| `They're extremely engineers. Leave a thousand drillers, shipbuilders and technicians…` | …wiertaczy, szkutników i techników… | …wiertaczy, stoczniowców i techników… | szkutnik buduje łodzie |
| `Loot` (lista sterowania) | Łup | Zabierz łup | etykieta czynności, jak „Rzuć”, „Użyj” |
| `Pause a lot! You have as long as you like to:` | Często włączaj pauzę! Masz wtedy dowolnie dużo czasu na: | Często włączaj pauzę! W pauzie możesz bez pośpiechu: | po dwukropku stoją „Przybliżenie”, „(Przytrzymaj) Przesuwaj kamerę”, „Celuj” — „czasu na: Celuj” się nie składa (w pełni zgrane nie będzie, bo etykiety są wspólne) |
| `Your Character Inspires {0}% Of Normal Liberation Progress` (+ fragment `Your Character Inspires `) | Twoja postać wzbudza {0}% zwykłego postępu wyzwalania | Twoja postać daje {0}% zwykłego postępu wyzwalania | „wzbudzać postęp” — zła kolokacja |
| `#Vulnerable when we liberate {0} more {1} stations` | #Będzie podatna, gdy wyzwolimy jeszcze tyle stacji {1}: {0} | #Będzie podatna po wyzwoleniu kolejnych stacji {1} (jeszcze: {0}) | czytelniejsze, dalej bez odmiany liczby |
| `You've had a good run. You'll go down in history…` (2 warianty) | To był dobry okres. … | To była udana kariera. … | „good run” to udana passa/kariera |
| ` killed.` / ` escaped.` (fragmenty zapasowe) | — zabity. / — uciekł. | — nie żyje. / — ucieczka. | szablony `{0} killed.`/`{0} escaped.` są już neutralne; fragmenty dają formę męską, gdy szablon nie zadziała |
| `Ex-Glitcher`, `Ex-Sovereign`, `Ex-Foundry`, `Ex-Offworld`, `Ex-Foundry: `, `Ex-Foundry: {0} used {1} without consuming a charge.` | Ex-… | Eks-Glitcher, Eks-Sovereign, Eks-Foundry, Eks-Offworld (i w szablonie) | polski przedrostek, z łącznikiem przed nazwą własną |

## Decyzje sprzed verticala

| Decyzja | Werdykt | Uzasadnienie / zakres |
| --- | --- | --- |
| Terminal treningowy mówi poprawnie, wersalikami, z entuzjazmem (**ustalenie użytkownika**) | **utrzymać** | Wszystkie 4 pliki PracticeTerminal* spójne („TRENING ROZPOCZĘTY”, „ŚWIETNA WALKA!”, „POMIŃ EMOCJONUJĄCĄ WALKĘ”). Nie proponuję powrotu do błędów. |
| Suchy humor, przekleństwa tej samej siły | **utrzymać** | Potwierdzone w całości (Geneva „do cholery”, Mirfak „gówno”, Asli „spieprzyli”). Jeden wyjątek siły: „O kurwa, żyjesz.” — patrz „Do rozmowy”. |
| Fiasco — kobieta; Asli Sixty — kobieta | **utrzymać** | Formy żeńskie spójne w narracji, TutorialEnd (gracz = Fiasco), FiascoEndGame, FiascoPersonalMission*, dialogu Glitchers. Brak wycieków męskich. Wyjątek składniowy w narracji: pkt 5 (zgoda „jedna” z „mieszkańców”). |
| Breaker, Geneva, Mirfak, gracz — neutralnie | **utrzymać** | Przeczytane wszystkie odpowiedzi `#` i kwestie barmanów: brak form rodzajowych (np. „Dało się to przewidzieć”, „A, ucieczka.”, „Wstąpienie było twoim wyborem…”, „Kieruję ochroną”). Koszt: kilka sztywniejszych zdań (np. „stacja ukradziona”). **Wycieki znalezione poza dialogami** — w UI: pkt 15, 20–22 (etykiety stanu postaci, przyczyny śmierci, „Pozostań niewidoczny”). |
| Nazwy przedmiotów: rzeczownik + przymiotniki odwrotnie + określenia na końcu | **utrzymać, z proponowaną zmianą jednego przymiotnika** | Składanie działa i jest zgodne w rodzaju. Problem: `Shiplocked` → „przypisany do statku” + określenie końcowe daje dwuznaczność: „Zamieniacz przypisany do statku dalekiego zasięgu”, „Tarcza awaryjna przypisana do statku o dużej pojemności” (czyta się jak „statek dalekiego zasięgu”). Propozycja w „Do rozmowy”. |
| Terminy gadżetów (Zamieniacz, Wizytator, Omijacz, Poślizg, Zawieszacz, Przeprogramator, Kopiarka kart), crash → zawiesić, glitch jako zapożyczenie | **utrzymać** | Konsekwentne w opisach, cechach, podpowiedziach, opisach wrogów („Zawieszenie Drapieżnika…”). |
| Etykiety cech broni jako rzeczowniki/frazy (Tłumik, Cichy strzał, Zapalnik czasowy…) | **utrzymać** | Spójne; drobne odstępstwa przymiotnikowe (`Lethal` → „Śmiercionośny”, `Restockable` → „Uzupełnialny”, jakości `Standard/Rare` → „Standardowy/Rzadki”) nie przeszkadzają. |
| Cechy postaci jako rzeczowniki bez rodzaju | **utrzymać; jeden wyjątek** | Słabość, Technofobia, Duma, Kruchość… — dobrze. Wyjątek: `Liberator` → „Wyzwoliciel” (i `Liberator available` → „Wyzwoliciel dostępny”) — patrz „Do rozmowy”, temat 2. |
| Liczby bez odmiany („Liczba użyć: 3.”, „Zabójstwa: 12”) | **utrzymać** | Sprawdzone szablony statystyk, amunicji, granatników, dni/godzin, „Zabij 3 oficerów…”. Wyjątek językowy „Razy zauważono” (pkt 13). |
| Misje osobiste: osobne szablony na relację | **utrzymać; poprawka techniczna** | Treść wszystkich 13 relacji × warianty poprawna (rodzaj, przypadki, „drugą połówkę”). Błąd techniczny `{0}{9}` (pkt 27). |
| `Better.` → „Bywało lepiej.” (żart Breaker) | **utrzymać** | Riposta „Bywało lepiej, bo teraz jest źle, czy…” i odpowiedzi „To pierwsze/To drugie” działają. |
| Sovereign/Foundry/Offworld jako rodzaj nijaki, Glitchers l.mn. | **utrzymać** | Spójne; w dialogach naturalnie przeplata się z „oni” tam, gdzie EN mówi „they” o ludziach frakcji. |
| Dryf, Matka Pustki, Gębołamacz, Breacher/Coldfire itd. bez tłumaczenia | **utrzymać** | Zgodne w całej grze. |
| Stacja z narracji jako zmienna nazwa („<nazwa> — ta stacja…”) | **utrzymać** | Ale patrz pkt 5 (kolejne zdania narracji). |
| Odpowiedzi w nawiasach kwadratowych (`[Continue]`) zostają w pliku | **brak kontekstu** | Nie da się ocenić bez gry — patrz „Do sprawdzenia”. |

## Do rozmowy

1. **„No.” w znaczeniu „tak”** — `Yep.` (FiascoEndGame, odpowiedź gracza) → „No.”; `Oh. Yep.` → „Aha. No.”;
   `Yep. Oh boy do they kill a lot. Ask me why I left.` → „No. O rany…”; `Yep. That's the slogan, right?…` → „No. Tak brzmi hasło…”;
   też w opisie Multikuli (`…Yeah.` → „No.”). Na liście odpowiedzi gracza „No.” obok „Co koniec? Czego koniec? Co?” łatwo przeczytać jako przeczenie (także przez angielskie „No”).
   **Rekomendacja:** „No tak.” / „Aha. No tak.” w odpowiedziach gracza; u Mirfaka „No jasne.”; w opisie przedmiotu można zostawić.
2. **Tytuły i etykiety męskoosobowe opisujące postać gracza** — `PACIFIST` (ocena misji, obok „DUCH”, „CISZA”, „BEZ DRASNIĘCIA”) → „PACYFISTA”;
   `Liberator` → „Wyzwoliciel”, `Liberator available` → „Wyzwoliciel dostępny”; `Daily Challenger` → „Uczestnik wyzwania dnia”; `Defector` → „Dezerter”;
   slogan Sovereign „Jeśli jesteś dobry… najlepszy” (ekran frakcji i dialog Mirfaka).
   **Rekomendacja:** zmienić tylko to, co wygląda jak opis konkretnej postaci: „PACYFIZM” (paralela do „CISZA”), `Liberator` → „Wyzwolenie” (jak inne cechy-rzeczowniki), `Liberator available` → „Wyzwolenie dostępne”. Role („Dezerter”, „Uczestnik”) i slogan zostawić jako rodzaj ogólny. Zysk: brak zgrzytu przy postaciach kobiecych; koszt: 3 wpisy.
3. **`Shiplocked` w nazwach przedmiotów** — obecnie „przypisany/-a/-e do statku”, co przed określeniem końcowym daje „…przypisany do statku dalekiego zasięgu”.
   **Rekomendacja:** przymiotnik „pokładowy / pokładowa / pokładowe” w `items.json` („Zamieniacz pokładowy dalekiego zasięgu”, „Karabin wytłumiony pokładowy”); etykietę cechy `Shiplocked` → „Sprzęt pokładowy” (opis „Podłączony do sieci zasilania tego statku…” bez zmian). Alternatywa: zostawić i przesunąć ten przymiotnik za określenia (wymaga zmiany w silniku).
4. **`Holy shit you're alive.` → „O kurwa, żyjesz.”** (TutorialEnd, pierwsza kwestia Breaker po samouczku) — mocniejsze niż oryginał; biblia każe trzymać tę samą siłę.
   **Rekomendacja:** „Jasna cholera, żyjesz.” (albo „O w mordę, żyjesz.”). Zostawić, jeśli to świadomy wybór tonu Breaker.
5. **`Yeah, you stole a station! How do you steal a station?` → „No właśnie, stacja ukradziona! Jak się kradnie stację?”** — neutralizacja płci Breaker usztywnia zdanie.
   **Rekomendacja:** „No właśnie, ukradliście stację! Jak się kradnie stację?” (l.mn. = ekipa Breaker i Fiasco; nadal neutralne).
6. **Tablica misji / zleceń** — EN ma „missions board”, „jobs board”, „Job Listings”, „Mission Listings”; PL: „tablica misji”, „tablica zleceń”, „Oferty zleceń”, „Oferty misji”, „ekran ofert”.
   **Rekomendacja:** ujednolicić na „tablica misji” i „Oferty misji” w UI (`Job Listings`, `. This opportunity is blown… check the jobs board.` i szablon), w dialogu Fiasco można zostawić „tablicę zleceń”. Niski koszt, lepsza orientacja gracza.
7. **Drobne propozycje redakcyjne** — tabela wyżej; rekomenduję przyjąć hurtem.

## Do sprawdzenia w grze

1. **Misja osobista z frakcją „the Glitchers” i klauzulą** (np. „Rescue my mum from the Glitchers, as fast as possible”) — po poprawce pkt 27 nie może się pojawić „z rąk the Glitchers”.
2. **Nazwy stacji z dopełniaczem angielskim** (`X's Y`, np. stacje przemianowane po wyzwoleniu — `Renamed to {0} in honour of {1}'s help.`) — szablon `{0}'s {1}` → „{1} — {0}” (przeznaczony do nazw pamiątek) łapie też takie nazwy w lukach. Symulacja: `Liberate Castor's Rest` → „Wyzwól stację **Rest — Castor**”. Sprawdzić, czy gra generuje nazwy stacji z „'s”; jeśli tak — ograniczyć szablon (np. dodać wiersze exact dla nazw stacji albo warunek w silniku).
3. **Opis celu misji z klauzulą „else”** (SetDescriptionTargetNameAndClausesForMission: `, kill no-one` + ` else` → „, nikogo nie zabijaj” + „ więcej”) — w symulacji `Assassinate, kill no-one else` → „Assassinate, nikogo nie zabijaj więcej”. Nie znam faktycznej postaci napisu; sprawdzić ekran ofert misji z klauzulą bezkrwawą/pacyfistyczną: czy nie zostaje angielski czasownik i czy „więcej” nie czyta się jak „już nigdy” (lepsze: „poza celem nikogo nie zabijaj”).
4. **Ekwipunek z uszkodzoną kapsułą** — pkt 12: czy dopisek dotyczy kapsuły („Kapsuła Breacher [uszkodzona]”).
5. **Opis strażnika z Obrońcą** (`#Defended: only their {0}…`) — jaka nazwa trafia do luki (pkt 26).
6. **Mapa twierdz** — „Twierdza Foundry” vs „Foundry — twierdza” (pkt 28).
7. **Długie nazwy przedmiotów** w liście ekwipunku i sklepie, np. „Pistolet przeciwpancerny ogłuszający szybkostrzelny cichy”, „Tarcza awaryjna przypisana do statku o dużej pojemności” — ucinanie „...” i czytelność.
8. **Odpowiedzi `[Continue]`, `[Something else]`** w TutorialEnd i FiascoEndGame — czy wyświetlają się po polsku („[Dalej]”, „[Coś innego]”) i czy przejścia działają.
9. **Samouczek, ekran „Pause a lot!”** — nagłówek z dwukropkiem i trzy etykiety pod nim.
10. **Ekran wyboru postaci i HUD gracza po ogłuszeniu** — etykiety stanu po poprawce pkt 20 („Bez przytomności”, „W niewoli”, „Do wyboru”).
11. **`work/preview-out.txt` do odświeżenia** — obecny plik pochodzi sprzed ostatniej zmiany `pl.json` i pokazuje nieaktualne błędy.

## Integracja przez agenta prowadzącego — 2026-09-25

**Wprowadzone** (partie `translations/parts/90-review.json`, `91-review-runtime.json`,
`tools/gen_personal.py`): punkty 1–28 w całości, z tym że punkt 27 rozwiązano
inaczej niż w propozycji — zamiast luk `{0}{9}` każda klauzula ma własny szablon
`{0}, <klauzula>`, a cel misji trafia do luki i tłumaczy się rekurencyjnie
(„Uratuj moją mamę z rąk Glitchers, jak najszybciej”). Szablon `{0}'s {1}`
usunięto (rozbijał „Castor's Rest”). Dodano szablony `{0}, kill no-one else`
i `{0}, harm no-one else` („poza celem nikogo nie zabijaj”). Przyjęto całą tabelę
drobnych propozycji redakcyjnych, w tym Eks-Glitcher/Eks-Sovereign/Eks-Foundry/Eks-Offworld.

Przy integracji wyszło, że `assemble.py` tylko dopisywał do `pl.json`: fragmenty
świadomie usunięte z partii (` from `, ` hit `, ` killed.`) i 112 szablonów `{9}`
zostawały w pliku. Teraz `pl.json` = klucze verticala + partie; 2536 wpisów.

**Ponowna kontrola:** podgląd 194 napisów (`work/preview-out.txt`, odświeżony),
661/662 linii dialogów, wszystkie 2800 wierszy `pl.tsv` przyjęte, test silnika
i fontów, raport kontrolny (tokeny 0, płeć 0). Paczka przebudowana i zainstalowana.

**Rozstrzygnięte przez użytkownika** („Do rozmowy” 1–6, partia `parts/95-user.json`; przyjęte wszystkie, tablica ujednolicona na „zlecenia” zamiast „misji”): „No.” jako „tak”,
PACYFISTA/Wyzwoliciel, Shiplocked → „pokładowy”, siła „O kurwa”, „stacja
ukradziona”, tablica misji/zleceń. Naniesione, przebudowane i zainstalowane.
