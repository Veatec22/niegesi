# Skate Story — niezależny review lokalizacji PL (ustalenia robocze)

Plik: games/skate-story/translations/en-pl-review.json, 2305 wpisów, SHA-256 fe12c3b00fbfc95241ea6a11a30e225234b7eeda9e8ab8ef45c6e1fd71f9b1f3.
Data: 2026-09-26. Indeksy [n] = pozycja w liście JSON (0-based).
Kategorie: PEWNY BŁĄD / WARIANT / BRAK KONTEKSTU.

## b01 — UI, poziomy, rozdziały, mówcy, samouczek (tut/05, 07, 10), modyfikatory trików

UI bardzo porządne: tryb rozkazujący w przyciskach, sentence case, terminy Steam/Microsoft („Synchronizacja pionowa”, „Okluzja otoczenia”, „Filtrowanie anizotropowe”). Nazwy poziomów dobre („Okousta”, „Głośnia Wiecznej Stonogi”, „Pod podziemiem”). Nie znalazłem pewnych błędów.

- [484] UI/Gameplay/ShowCutsceneUI oraz [576] UI/Settings-Gameplay-btn-Show Cutscene UI — **WARIANT**
  - EN: Show Cutscene UI
  - PL: Interfejs scen
  - Proponowane PL: Pokaż interfejs w scenach
  - Przesłanka: sąsiednie przełączniki to „Pokaż prędkościomierz”, „Pokaż samouczki”; samo „Interfejs scen” nie mówi, że to włącznik widoczności. Limit 50 znaków — mieści się.

- [620] UI/Soul-Expiry-Timer i [621] UI/Soul-Expiry-Timer-top — **BRAK KONTEKSTU** (do testu)
  - EN: SOUL\n\n\nEXPIRY
  - PL: DUSZA\n\n\nWAŻNOŚĆ
  - Proponowane PL (jeśli licznik stoi między słowami): DUSZA\n\n\nWYGASA
  - Przesłanka: EN czyta się „soul expiry” = „wygaśnięcie duszy”; „DUSZA … WAŻNOŚĆ” nie składa się w frazę. Z licznikiem pośrodku „DUSZA [0:30] WYGASA” czyta się jak zdanie. Zależy od układu na ekranie — sprawdzić w grze. Zachować trzy \n.

- [496] UI/Generic/Ender — **BRAK KONTEKSTU**
  - EN: ENDER / PL: ZAKOŃCZENIE
  - W slangu deskorolkowym „ender” to ostatni, kończący trik (partu, kombinacji). Jeśli etykieta stoi przy triku kończącym kombo, lepsze byłoby „FINISZ” albo „TRIK KOŃCOWY”; jeśli przy napisach/wyniku — „ZAKOŃCZENIE” jest w porządku. Rozstrzygnąć w grze.

- [388]–[404] Trick/modifier-* — **BRAK KONTEKSTU** (do testu)
  - Modyfikatory są mieszanką przysłówków („Szybko”, „W dół”), przymiotników („Potężny”) i rzeczowników („Przeskok”, „Kolec”, „Wyjście”). Nie wiadomo, jak gra je skleja z nazwą triku (np. „Fast Kickflip Over Gap”?). Jeśli skleja w jeden ciąg, polska kolejność/forma może dać „Potężny Szybko Kickflip Ponad Przeskok”. Sprawdzić wynik na ekranie kombo; jeśli wyświetla się jako osobne etykiety — zostawić.

- [339] Levels/ch8-02-path-bolgia-name i [342] Levels/ch8-09-bosspath-skatersoul-name — **WARIANT** (niski priorytet)
  - EN: Ten Bolgias / PL: Dziesięć Jarów
  - Proponowane PL: Dziesięć Rowów
  - Przesłanka: „bolgia” to rów/dół Malebolge z VIII kręgu Piekła Dantego; polskie przekłady mówią o rowach/dołach. „Jary” brzmią dobrze, ale gubią aluzję. Gust — do decyzji.

Uwagi bez zmiany: [406] ostrzeżenie zdrowotne to istniejący tekst twórców (spacja na początku, „oświetlone, oraz” — przecinek przed „oraz” jest błędem, ale to tekst wydawcy, biblia go wyłącza). [2288] końcowe \n zachowane. [2286] „II. GRIND” — termin, zgodnie z biblią.

## b02 — ch1 (Liceum, Filozof, Philoso, Szczęśliwy Sześcian, sklep, boss)

Rozdział bardzo dobry: narracja zwięzła, głos Filozofa („W istocie”, „zadumiewające”, „podumam”) przekonujący, żart „ogród pełen głów” (heady garden) oddany. Echo otwarcia „Ten demon…” zgodne z decyzją.

- [772] ch1/09-lyceum/2rabbit2lookthinkpiece-1-seq-02 — **PEWNY BŁĄD** (znaczenie)
  - EN: Anyway, my role is done here, I believe.\nLook through your arm, the *blu*Moon Vision*blu* will guide your way.\nI'm starving from all this scampering around...\nSee you tomorrow, Skater.
  - PL: Tak czy inaczej, chyba zrobiłem już swoje.\nSpójrz przez swoje ramię — *blu*Księżycowy Wzrok*blu* wskaże ci drogę.\nUmieram z głodu od tego biegania...\nDo jutra, Skejterze.
  - Proponowane PL: Tak czy inaczej, chyba zrobiłem już swoje.\nSpójrz przez swoją szklaną rękę — *blu*Księżycowy Wzrok*blu* wskaże ci drogę.\nUmieram z głodu od tego biegania...\nDo jutra, Skejterze.
  - Przesłanka: „patrzeć/spojrzeć przez ramię” to po polsku utarte „obejrzeć się za siebie” — gracz zrozumie „odwróć się”, a chodzi o patrzenie przez przezroczyste (szklane) ramię/rękę, w której tkwi Księżycowy Wzrok ([767]: „Przez twoje szklane ciało widzę Księżycowy Wzrok”). Jeśli „szklaną” to dopisek za daleko, minimum: „Spójrz przez swoją rękę”.

- [729] / [733] / [786] termin „stale” — **WARIANT** (spójność mechaniki)
  - EN [729]: …makes a trick go <color=red>stale</color>. → PL: …robi się <color=red>oklepany</color>.
  - EN [733]: The legendary kickflip deals more damage, but gets stale quickly. → PL: Legendarny kickflip zadaje większe obrażenia, ale szybko się nudzi.
  - EN [786]: However, it gets stale more quickly and has a slower timing. → PL: Jednak szybciej traci skuteczność przy powtarzaniu i wymaga wolniejszego rytmu.
  - Proponowane PL [733]: Legendarny kickflip zadaje większe obrażenia, ale szybko staje się oklepany.
  - Proponowane PL [786]: Jednak szybciej staje się oklepany i wymaga wolniejszego rytmu.
  - Przesłanka: [729] wprowadza kolorem mechanikę „stale” jako „oklepany”; dalsze samouczki tej samej mechaniki mówią o niej trzema różnymi sformułowaniami, co zaciera, że to ten sam stan.

- [744] ch1/08-captureskater/1kneeldemon-1-seq-03 — **WARIANT**
  - EN: "It has come to my attention that you have been skateboarding."
  - PL: „Doszło mnie, że jeździsz na deskorolce”.
  - Proponowane PL: „Doszło do mojej wiadomości, że jeździsz na deskorolce”.
  - Przesłanka: EN to urzędowa formuła; „doszło mnie, że…” jest rzadkie i brzmi niezręcznie (poprawne jest „doszły mnie słuchy”/„doszła mnie wieść”). Polska formuła urzędowa oddaje ton Filozofa-sędziego.

- [795] ch1/09-lyceum/philoso3teaturnin-1-seq-01 — **WARIANT** (rym Philoso)
  - EN: A tea, a bile, for me?\nI don't chug, I sip the tea.\n99 cents isn't entirely free.\nFor this quest a **Thinkpiece** for thee.
  - PL: Herbata i żółć — to wszystko dla mnie?\nNie duszkiem, a łyczkiem popijam ją ładnie.\nDziewięćdziesiąt dziewięć centów to nie całkiem darmo.\nZa trud twój **Myślokształt** niech będzie zapłatą.
  - Proponowane PL: Herbata i żółć — to wszystko dla mnie?\nNie duszkiem, a łyczkiem popijam ją ładnie.\nDziewięćdziesiąt dziewięć centów to nie całkiem darmo.\nMasz więc **Myślokształt** — nie trudziłeś się marno.
  - Przesłanka: biblia: dla Philoso rym ważniejszy niż dosłowność; para „darmo / zapłatą” nie rymuje się, reszta czterowiersza tak. „darmo / marno” domyka rym, zachowuje nagrodę za zadanie. Znaczniki ** zachowane.

- [798] ch1/09-lyceum/platofires1talk-1-seq-01 — **WARIANT**
  - EN (ostatni wers): Say, *red*fling yourself across my view*red*... and I shall ponder you.
  - PL (ostatni wers): Otóż *red*przeleć mi przed oczami*red*... a podumam o tobie.
  - Proponowane PL (cały wpis): Śpię na tym łożu płomieni, obserwując Wieczną Stonogę.\nTo zadumiewające. Pełne... zadumy.\nOch, nad czym podumam dzisiejszej nocy?\nCzy dalej rozważać, jak śpi Stonoga?\nGdy sunie po niebie, czy zastanowię się, czy śni?\nCzy też podumam o tobie, nowym mieszkańcu mego ogrodu pełnego głów?\nNo więc *red*przeleć mi przed oczami*red*... a podumam o tobie.
  - Przesłanka: „Otóż” wprowadza wyjaśnienie, nie prośbę; tu „Say,” = zachęta. „No więc”/„Proszę więc” brzmi naturalnie.

- [788] ch1/09-lyceum/happycube0meet-1-seq-02 — **WARIANT**
  - EN: Look!\nAll it did was create all these *blu*gassy manholes*blu* around me!\nIt's so nasty!
  - PL: Patrz!\nPojawiły się tylko wokół mnie te wszystkie *blu*gazowe studzienki*blu*!\nTo takie paskudne!
  - Proponowane PL: Patrz!\nJedyne, co z tego wyszło, to te wszystkie *blu*gazowe studzienki*blu* wokół mnie!\nTo takie paskudne!
  - Przesłanka: szyk „Pojawiły się tylko wokół mnie” sugeruje „tylko wokół mnie (a nie gdzie indziej)”; EN mówi „jedynym skutkiem było…”.

- [906] ch1/12-boss/stomp2amb0-1-seq-01 — **WARIANT** (niski priorytet)
  - EN: "HM." the Philosopher was shook.
  - PL: „HM” — Filozof zadrżał.
  - Proponowane PL: „HM” — Filozofem wstrząsnęło.
  - Przesłanka: [911] „Hmm...” — Filozof zadrżał (trembled) daje dosłownie ten sam opis; „was shook” to potoczne „wstrząśnięty”, stopniowanie reakcji bossa.

- [755] (i całe ch1) Lyceum → Liceum — **BRAK KONTEKSTU / do rozmowy**
  - „Liceum” po polsku kojarzy się najpierw ze szkołą średnią; arystotelesowskie Lyceum to po polsku zwykle „Likejon”. Oryginał gra na szkole filozoficznej. „Liceum” jest czytelne i ma pewien komiczny efekt „szkoły”, więc zostawienie jest obronne — patrz „Do rozmowy”.

- [893] ch1/12-boss/33phase3goal-1-seq-01 — **BRAK KONTEKSTU** (długość celu, do testu)
  - EN: Stomp tricks to deal damage. / PL: Kończ triki tupnięciem, by zadawać obrażenia. (45 zn.)
  - Jeśli pole celu ucina: „Kończ kombo tupnięciem, by ranić” (32 zn.) — [903] potwierdza, że chodzi o kombo zakończone tupnięciem.

Uwagi bez zmiany: [826] „Witaj, mój obywatelu” (constituent) — dopuszczalne; „mój wyborco” byłoby zabawniejsze politycznie, ale to gust. [787] „Święte piekło” — kalka „Holy hell”, ale w piekle ma sens; zostawić. [734] „się wyczerpała” vs [1085] „wygasła” (soul expired) — patrz synteza.

## b03 — ch2 (Sen Skejtera, Le Bageland, Krwawe Wzgórza, metro, telefon od Lichy, Krwawy Księżyc)

Rozdział mocny: „świeciło pustkami”, „Ostatnio opróżniano go nigdy”, „Nieźle się wzięli za gapowiczów”, telefon Lichy per „pan” spójny. Pewnych błędów brak.

- [1061] ch2/10-boss-chase/amb6-1-seq-01 — **WARIANT**
  - EN: "Yet another faceless demon to chase me," the Moon flickered.
  - PL: „Kolejny bezimienny demon mnie ściga” — zamigotał Księżyc.
  - Proponowane PL: „Kolejny demon bez twarzy mnie ściga” — zamigotał Księżyc.
  - Przesłanka: „faceless” to „bez twarzy”/anonimowy; „bezimienny” przesuwa akcent na imię. Gra stale operuje obrazami twarzy (Księżyc ma twarz: [982], [1059]), a Skejter jest bezimiennym szklanym demonem — dosłowne „bez twarzy” zachowuje kontrast twarz/brak twarzy.

- [1089] ch2/13-moonbleed/moonbleed-1-seq-04 — **WARIANT**
  - EN: Sleep drained out as the Moon deflated.
  - PL: Sen wypływał, a Księżyc opadał z sił.
  - Proponowane PL: Sen wypływał, a Księżyc flaczał.
  - Przesłanka: „deflated” — obraz fizyczny (uchodzi powietrze), domyka [1062] „Zaczęło puchnąć”. „Opadał z sił” jest metaforą zmęczenia i gubi obraz. „Kurczył się” też byłoby dobre.

- [1026] ch2/07-worldmap/103amb-1-seq-01 — **WARIANT** (język)
  - EN: The subway wouldn't go backwards further.
  - PL: Metro nie chciało już dalej cofać.
  - Proponowane PL: Metro nie chciało się już dalej cofać.
  - Przesłanka: „cofać” bez „się” w znaczeniu „jechać do tyłu” jest potoczne (o kierowcy); o pojeździe w narracji naturalniejsze „cofać się”.

- [990] ch2/04-bloodheights/larryquestget-1-seq-01 — **WARIANT** (rym Larry'ego)
  - EN: MMMMMM, MMM, MM.\nVIBES ARE WHAT I FEAST.\nRIDE FOR ME YOU BEAST.\nRIDE FOR MY *blu*SOULPIECE*blu*.
  - PL: MMMMMM, MMM, MM.\nKARMIĄ MNIE WIBRACJE.\nJEDŹ DLA MNIE, BESTIO.\nJEDŹ PO MÓJ *blu*FRAGMENT DUSZY*blu*.
  - Proponowane PL: MMMMMM, MMM, MM.\nWIBRACJE — MOJA STRAWA.\nJEDŹ DLA MNIE, BESTIO KRWAWA.\nJEDŹ PO MÓJ *blu*FRAGMENT DUSZY*blu*.
  - Przesłanka: Larry mówi rymowanymi wersalikami (FEAST/BEAST/SOULPIECE); PL zgubił rym całkowicie. „Krwawa” pasuje do Krwawych Wzgórz. Niski priorytet.

- [1034] ch2/08-telephone/2telephone-1-seq-04 — **BRAK KONTEKSTU / do rozmowy** (gra słów pain/pane)
  - EN: "I'm looking for a... skater? Made of... glass and pane?"
  - PL: „Szukam... skejtera? Ze... szkła i... bólu?”
  - Wariant: „Szukam... skejtera? Ze... szkła i... szyby?”
  - Przesłanka: w EN urzędniczka przekręca tagline („Glass & Pain” → „glass and pane” = szkło i szyba). Obecne PL oddaje tylko zawahanie; żart znika. „Szkła i szyby” odtwarza przekręcenie (tautologia zamiast bólu) i gracz zna oryginał taglinu z [2240] „Ze szkła i bólu”. Koszt: słabsze, jeśli gracz nie skojarzy taglinu. Decyzja literacka — patrz „Do rozmowy”.

- [956] ch2/01-title/2rabbietalk-1-seq-01 — **WARIANT** (niski priorytet)
  - EN (ostatni wers): Well, I'm your lucky sign.
  - PL (ostatni wers): Cóż, dobrze trafiłeś.
  - Proponowane PL (cały wpis): Nie możesz spać, co?\nKsiężyc strasznie świeci.\nMusisz jakoś zasnąć.\n...\nCóż, jestem twoim szczęśliwym znakiem.
  - Przesłanka: Królik jako „szczęśliwy znak” (aluzja do króliczej łapki na szczęście); „dobrze trafiłeś” zachowuje funkcję, gubi autoprezentację. Obecne PL jest naturalniejsze — decyzja gustu.

Uwagi bez zmiany: [994] „Trzeba było…” — dobrze uniknięto płci nieznanego poety. [993]/[996] poeci w rodzaju męskim — brak danych, przyjęte. [1085] „wygasła” — patrz synteza (soul expired).

## b04 — ch3 (Pranie Diabła, Pralnia, Plac Udręki, kwiaciarnia Beei, Larry, Fabryka Znaczeń, boss)

Świetne miejsca: „Wytrzęsło mną prawie do sucha”, „Powodzenia, miłego potępienia!”, rymy Larry'ego w [1177]/[1180] („ZĘBAMI ZGRZYTAM. / JEDZENIA NIE TYKAM.”), żart ze Spodniami [1147]/[1148]. Beea konsekwentnie żeńska.

- [1106] ch3/01-bedhail/01wakeupintro-1-seq-04 — **PEWNY BŁĄD** (znaczenie)
  - EN: The Rabbit read dimly from a letter burned bedside.
  - PL: Królik czytał sennie z listu spalonego przy łóżku.
  - Proponowane PL: Królik czytał w półmroku list, który wypalił się przy łóżku.
  - Przesłanka: w tym świecie listy „wypalają się” na miejscu doręczenia ([1038] „It burned up onto my desk” → „Wypaliła się na moim biurku”). „List spalony” po polsku = zniszczony ogniem, więc czytanie go jest sprzecznością. „Dimly” to „niewyraźnie/w półmroku”, nie „sennie” — a zdanie wcześniej [1105] Królik siedzi „bezsenny”, więc „sennie” zgrzyta.

- [1170] ch3/06-flowershop/10talkbea-1-seq-01 — **PEWNY BŁĄD** (termin z biblii, drobny)
  - EN (ostatni wers): And just my luck, the Moonflower festival is coming up...
  - PL (ostatni wers): Jak na złość zbliża się święto księżycowych kwiatów...
  - Proponowane PL (cały wpis): Witaj w mojej kwiaciarni!\nTo znaczy, byłaby nią, gdybym miała kwiaty.\nPrzyszedł łysy demon, porwał moje jedyne *blue*nożyce*blue* i *red*ściął*red* ostatni kwiat!\nPotem uciekł z *blu*nożycami*blu* do *b*Fabryki Znaczeń*b*.\nTeraz nie mam ani kwiatów, ani *blu*nożyc*blu*.\nOch, to okropne.\nJak na złość zbliża się święto Księżycowych Kwiatów...
  - Przesłanka: biblia: Moonflower = „Księżycowy Kwiat” wielką literą; to ten sam kwiat, o który Beea prosi w [1173] i który opisuje w [1174]. Z małej litery gracz nie połączy święta z przedmiotem.

- [1153] ch3/05-languishinsq/13pants11interact-1-seq-01 — **WARIANT**
  - EN (ostatni wers): Pin up the Tail and the Robe and we'll *blu*pin down the Moons*blu* for you.
  - PL (ostatni wers): Przypnij Ogon i Szatę, a my *blu*przykujemy Księżyce*blu* dla ciebie.
  - Proponowane PL (cały wpis): Dobra, dobra, masz mnie! Ale była jazda.\nTego mi było trzeba. Wytrzęsło mną prawie do sucha.\nWysusz pozostałe dwie rzeczy, a bardzo ci pomożemy.\n*red*Ogon*red* wbija się w przypadkowy tyłek,\na *blu*Szata*blu* po prostu fruwa.\nPrzypnij Ogon i Szatę, a my *blu*przyszpilimy dla ciebie Księżyce*blu*.
  - Przesłanka: EN gra słowami pin up/pin down; „przypnij / przyszpilimy” zachowuje echo, a „przyszpilić” to też „unieruchomić”. „Przykujemy” zapowiada łańcuchy z [1193], więc obecne też ma sens — gust.

- [1105] ch3/01-bedhail/01wakeupintro-1-seq-03 — **WARIANT** (niski priorytet)
  - EN: Twin Moons shone weeping as the Rabbit sat without sleeping.
  - PL: Bliźniacze Księżyce świeciły, płacząc, a Królik siedział bezsenny.
  - Proponowane PL: Bliźniacze Księżyce świeciły łkając, a Królik siedział, snu nie zaznając.
  - Przesłanka: EN ma wewnętrzny rym weeping/sleeping, typowy dla lirycznych wstawek narratora; PL może go odtworzyć bez utraty sensu.

- [1189] ch3/06-meaningslobby/11talkfrotuerepeat-1-seq-01 — **WARIANT**
  - EN: It's important to have a Meaning, at least in this economy.\nJust enter that door there!
  - PL: Ważne, by mieć Znaczenie, przynajmniej w tej gospodarce.\nPo prostu wejdź w tamte drzwi!
  - Proponowane PL: Ważne, by mieć Znaczenie, zwłaszcza przy obecnej gospodarce.\nPo prostu wejdź w tamte drzwi!
  - Przesłanka: „in this economy” to utarty (memiczny) zwrot „w tych czasach/przy takiej gospodarce”; „w tej gospodarce” brzmi jak kalka, choć w polskim internecie ta kalka też krąży jako mem. Ten sam zwrot wraca w [1309] („kawa!? w tej gospodarce!”) — obecnie spójnie; jeśli zmieniać, to oba (dla [1309]: „kawa!? przy tej gospodarce!”). Niski priorytet.

Uwagi bez zmiany: [1101] „wyprać Pranie Diabła” — Pranie jest nazwą bytu, tautologia akceptowalna. [1154]/[1155] Szata mówi bezosobowo („będzie sucho”) — zgodne z biblią (k). [1183] „z żabą za ladą” małą literą w opisie — w porządku.

## b05 — ch4 (Coney, sąd, Departament, Resolute Coffee i Gołąb, Plac Żalu, Poczekalnia, Krwawy Wieszcz)

Rozdział bardzo udany: Coney ze swoimi wersalikami, gołąb-pisarz małymi literami („jestem zajęty byciem W KROPCE”, „pomysły się parzą!”), „Mamy was!”, „Nie ma rabatu hurtowego?”. Rozwiązanie CHEESE/SER według decyzji. Żadnych pewnych błędów.

- [1388] ch4/09-boss-marketofarrivals/05bloodeyeintro-1-seq-01 — **WARIANT**
  - EN: It watches as every new underworld soul is listed.
  - PL: Patrzy, jak spisują każdą nową duszę podziemia.
  - Proponowane PL: Patrzy, jak na giełdę trafia każda nowa dusza podziemia.
  - Przesłanka: cała lokacja to parodia rynku — Targ Przybyszów, pierścień ekranu „za szybko, za drobno, by przeczytać” (tablica notowań, [1385]–[1386]), dusze czekają „na zwrot z inwestycji” ([1377]), „portfel inwestycyjny”, „salda żalu”. „Listed” = wprowadzona do notowań. „Spisują” gubi ten żart. Ostrożniejszy wariant: „Patrzy, jak notuje się każdą nową duszę podziemia.”

- [1402] ch4/09-boss-marketofarrivals/20presentboss-1-seq-08 — **WARIANT**
  - EN: The document wrapped in on itself, its header eating its tail.
  - PL: Dokument owijał się wokół siebie, nagłówek pożerał jego koniec.
  - Proponowane PL: Dokument owijał się wokół siebie, a nagłówek pożerał własny ogon.
  - Przesłanka: obraz uroborosa (wąż zjadający ogon) — „pożerać własny ogon” jest po polsku czytelny i daje zapowiedź „pętli czytania” z [1403]. „Pożerał jego koniec” jest płaskie i ma niejasne „jego”.

- [1236] ch4/03-courtroom/1judgetalk-1-seq-02 — **WARIANT**
  - EN: We're just sleeping through here.
  - PL: My tylko prześpimy tędy.
  - Proponowane PL: My tu tylko przesypiamy przejazdem.
  - Przesłanka: EN gra na „passing through”; „prześpimy tędy” jest niegramatyczne w odczuciu (brak dopełnienia), a „przejazdem” oddaje żart i brzmi jak wymówka Królika.

Uwagi bez zmiany: [1223] cale → „90–120 centymetrów” — dobra adaptacja jednostek. [1383] „KROCZĄCEGO ZGIEŁKU” zgodne z nazwą bossa [659] „Kroczący Zgiełk”. [1431] „Powoli Księżyc opadał z sił” (tired) — poprawne; dlatego w [1089] (deflated) warto inne słowo. [1368] szkielet w rodzaju męskim — zgodnie z decyzją.

## b06 — ch5 (Hellsea: Ulica Wylinki, Pingwin/Penin, Shon i pachołki, Szlamowy Trakt, Święty Karat, Fioletowy Księżyc)

Głos Pingwina (skarbie, mój drogi gryzoniu, „Jestem bogatym przemysłowcem”) i odmiana Shawnie/Seanie/Shaunie dobre. Brak pewnych błędów.

- [1491] ch5/05-moultst/291myfriendscallfuss-1-seq-01 — **WARIANT** (język)
  - EN: How could you?!\nThose were my *red*ex-best-friends*red*!\nOfficers! A tip, I've located the Moon-Eater! A demon that has toppled my ex-best-friends!
  - PL: Jak mogłeś?!\nTo byli moi *red*byli najlepsi przyjaciele*red*!\nFunkcjonariusze! Donoszę: znalazłem Pożeracza Księżyców! Demona, który przewrócił moich byłych najlepszych kumpli!
  - Proponowane PL: Jak mogłeś?!\nTo moi *red*byli najlepsi przyjaciele*red*!\nFunkcjonariusze! Donoszę: znalazłem Pożeracza Księżyców! Demona, który przewrócił moich byłych najlepszych kumpli!
  - Przesłanka: „To byli moi byli…” — niezamierzone powtórzenie czasownika i przymiotnika brzmi jak potknięcie. Po usunięciu pierwszego „byli” sens bez zmian.

- [1476] ch5/05-moultst/15npcofleave-1-seq-01 — **WARIANT** (interpretacja)
  - EN: I took her necklace away... and crushed it.\nI threw it off the grey cliffs, into the putrid sludge!\nIt was her last chained item.\nI had to do it. I had to!
  - PL: Zabrałem jej naszyjnik... i zmiażdżyłem.\nRzuciłem go z szarych klifów w cuchnący szlam!\nTo była jej ostatnia rzecz na łańcuszku.\nMusiałem to zrobić. Musiałem!
  - Proponowane PL: Zabrałem jej naszyjnik... i zmiażdżyłem.\nRzuciłem go z szarych klifów w cuchnący szlam!\nTo była ostatnia rzecz, do której była przykuta.\nMusiałem to zrobić. Musiałem!
  - Przesłanka: gra buduje motyw „każda dusza jest spętana/przykuta do swojej chciwości” ([1212]–[1213]). „Last chained item” = ostatni przedmiot, który ją wiązał; „rzecz na łańcuszku” czyta się jak opis biżuterii. Jeśli jednak autor miał na myśli dosłownie łańcuszek — obecne PL jest poprawne; stąd wariant, nie błąd.

- [1572] ch5/11-violetmoon/01startfight-1-seq-01 — **WARIANT**
  - EN: The Violet Moon screamed, ownerless.
  - PL: Fioletowy Księżyc krzyczał bez właściciela.
  - Proponowane PL: Fioletowy Księżyc krzyczał, pozbawiony właściciela.
  - Przesłanka: „krzyczał bez właściciela” czyta się jak okolicznik sposobu krzyku; EN to dopowiedzenie stanu (akt własności właśnie podarto).

- [1478] ch5/05-moultst/15npcoflove-1-seq-01 — **BRAK KONTEKSTU**
  - EN: They took my thinkpiece and tore it apart... / PL: Wzięli mój Myślokształt i rozdarli go...
  - W EN małą literą — to raczej „tekst publicystyczny”, który „rozszarpano” krytyką (dalej „I thought I made some good points!”, „diatribe”). Użycie przedmiotu „Myślokształt” jest obronne (w grze to ta sama gra słów), ale traci drugi sens. Bez zmiany, chyba że tłumacz chce: „Wzięli mój Myślokształt i nie zostawili na nim suchej nitki...”.

- [1574] ch5/11-violetmoon/90intro-1-seq-03 — **BRAK KONTEKSTU** (drobne)
  - EN: …See you later, skater. / PL: …Do zobaczenia, skejterze.
  - W EN rym „later, skater” (echo „see you later, alligator”); PL go nie oddaje, co jest do przyjęcia. Małe „skejterze” świadomie za EN — OK.

Uwagi bez zmiany: [1443] „Czas dostać po dupie!” — siła wulgaryzmu jak w EN; w slangu deskorolkowym „eat shit” to też „zaliczyć glebę”, ale obecne jest dobre. [1566] i [1584] według decyzji 0.3. [1474]/[1475] gra soul/soles nieoddana — trudna, akceptowalne.

## b07 — ch6 (Godhook: telefon Filozofa, list Diabła, Świetlista Wyspa, miraże, Fałszywe Słońce, Coney i grobowiec, TV)

Bez pewnych błędów i bez istotnych wariantów. Dobre: „Może ze skarbówki?” (IRS), „Gdzie twój klapouchy szczur?”, „Zawsze działa, zazwyczaj!”, „szlamopijca”, „WSTA. WAJ.”. Fałszywe Słońce w narracji konsekwentnie nijakie („zaśmiało się”, „zapiszczało”), w 1. osobie mówi o sobie jak o Księżycu („Nie jestem gotów”, „Jestem prawdziwym siódmym Księżycem”) — zgodnie z biblią. [1663] „*gold*Fałszywy księżyc*gold*” małą literą, bo EN „false moon” małą — poprawnie.

- [1711] ch6/13-end/02EATEN-1-seq-02 — **BRAK KONTEKSTU** (drobne)
  - EN: Among false stars is along false sun...\nand the truth shoots through you.
  - PL: Wśród fałszywych gwiazd — fałszywe słońce...\na prawda przeszywa cię na wskroś.
  - EN „along” to zapewne literówka z „a lone” (samotne) albo „a long”. Jeśli „a lone”: „Wśród fałszywych gwiazd — samotne fałszywe słońce...\na prawda przeszywa cię na wskroś.” Obecne PL jest bezpieczne; bez zmiany.

## b08 — ch7 (Kolacja: Bankiet, goście, Królik → Szczur, spalona umowa, dno, Cień Księżyca, Stonoga)

Najmocniejszy emocjonalnie rozdział i dobrze oddany: monolog Szczura [1752]–[1756], seria „NIENAWIDZĘ…”, „Widzę, więc… więc krwawię” (echo Kartezjusza), „Kolego, jesteś UGOTOWANY” (a chwilę później „Jesteś daniem głównym” — żart kulinarny działa), Penin „Chybu… Sam się dokolebałem tam, gdzie jestem”. Brak pewnych błędów.

- [1846] ch7/waitstage/89end-1-seq-03 — **WARIANT**
  - EN: A distant screech was imminent.
  - PL: Daleki skrzek był nieunikniony.
  - Proponowane PL: Zaraz miał się rozlec daleki zgrzyt.
  - Przesłanka: „imminent” = bliski, nadciągający, nie „nieunikniony”. „Screech” w samouczku grindu [2281] oddano jako „zgrzyt” — tu też chodzi o dźwięk (zapowiedź Stonogi), „skrzek” kojarzy się z ptakiem/żabą.

- [1811] ch7/08-centipede-shadow/01yearn-1-seq-01 — **WARIANT** (długość, niski priorytet)
  - EN: Do you ever yearn? / PL: Czy odczuwasz czasem tęsknotę? (30 zn., raport: ryzyko długości)
  - Proponowane PL: Tęsknisz czasem?
  - Przesłanka: krótsze, bliższe rytmowi EN (znany mem „Do you ever yearn?”), a następna kwestia [1812] „Tęsknotę? Czy tęsknię?” dalej działa jako echo — można ją wtedy uprościć do „Tęsknię? Czy ja tęsknię?”. Zmiana tylko, jeśli w grze tekst się nie mieści albo dla rytmu.

- [1754] ch7/02-rabbit-rat/03rat-1-seq-03 — uwaga do syntezy (bez zmiany tego wpisu): „We'll pass through the ditches of the eighth” → „Przepłyniemy przez rowy ósmej...” — to właśnie Bolgie VIII Głębi. Nazwa poziomu [339]/[342] to „Dziesięć Jarów”; „Dziesięć Rowów” połączyłoby obie wzmianki (patrz b01).

Uwagi bez zmiany: [1728] „Proszę iść prosto” obok „Masz stolik” — formuła kelnerska, dopuszczalna. [1753] „a shred of hope” — gra „shred” (jeździć ostro) nieoddana; trudna, „okruch nadziei” wystarcza. [1820] „To znaczy, że po nas!” — ironia przy „Czyż to nie wspaniałe?” działa.

## b09 — ch8 (Zapomnienie, Biblioteka Grzechów, uczeni, Ghosto, zjedzenie własnej duszy, Najczarniejszy Ogień)

Sekwencja umierania/powstawania [1847]–[1866] („wszystkość”), monolog „Przejechałem przez piekło…” [1915]–[1918] i echo „Ten Demon był głodny i zmęczony” [1919] — bardzo dobre. Typografia „1400 °C” zgodna z decyzją. Brak pewnych błędów.

- [1879] ch8/04-area-sinslabs/11hornscholarquest01start-1-seq-02 — **WARIANT**
  - EN: The *red*Horn of Sin*red* will honk at any *red*accumulated sin above 10,000 points.*red* Don't you dare ring it.
  - PL: *red*Róg Grzechu*red* zatrąbi przy każdym *red*grzechu wartym ponad 10 000 punktów.*red* Nie waż się go obudzić.
  - Proponowane PL: *red*Róg Grzechu*red* zatrąbi przy każdym *red*nagromadzonym grzechu powyżej 10 000 punktów.*red* Nie waż się sprawić, żeby zatrąbił.
  - Przesłanka: (1) „obudzić” róg to niepotrzebne przesunięcie metafory — EN „ring it” = „uruchomić/sprawić, że zabrzmi”; (2) „accumulated” wskazuje graczowi, że liczy się punktacja kombo (nagromadzony wynik), a nie pojedynczy „grzech” — to instrukcja zadania. Znaczniki *red* w tych samych miejscach.

- [1966] ch8/oblivion-4/03skaterssoulescapes-1-seq-04 — **WARIANT** (niski priorytet)
  - EN: It vanished without a puff. / PL: Zniknęła bez śladu.
  - Proponowane PL: Zniknęła bez jednego obłoczka.
  - Przesłanka: echo [773] „The Rabbit was a vanishing puff” → „Królik zniknął jak obłoczek”. Gust; „bez śladu” jest naturalne.

Uwagi bez zmiany: [1847] „w zapomnieniu” małą literą, bo EN „in oblivion” — potem „Zapomnienie” jako byt, zgodnie z biblią. [1890]/[1891] „Syropu Księżycowego”/„syropu księżycowego” — wielkość liter jak w EN (Moon Syrup / Moon syrup), nie ma takiego przedmiotu w tabeli, akceptowalne. [1872] „Odprężone (demoniczne) szkło” — poprawny termin techniczny.

## b10 — ch9 (Wieczna Stonoga: metro, Okousta, lodowe jezioro, piosenki Mitski/Brand New, wykład Szczura o Księżycach, boss rush, rozcięcie Stonogi, Sen Skejtera)

Wykład Szczura [2103]–[2119] czysty i poruszający; cytaty piosenek [2048]–[2055] dobrze (małe litery zachowane, kamień młyński męski zgodnie z decyzją). Echo „drżał z boską częstotliwością” [2122] ↔ [692] zachowane. Coney („CENTO”, „ZGIEŁKOWYM PIERWSZEJ RANGI!”) spójny. Brak pewnych błędów.

- [2207] ch9/13-preboss-flare/03skaterstuck-1-seq-03 — **WARIANT**
  - EN: NO! IT'S GOT US!
  - PL: NIE! MA NAS!
  - Proponowane PL: NIE! ZŁAPAŁO NAS!
  - Przesłanka: wersalikami „NIE! MA NAS!” łatwo czyta się jako „NIE MA NAS!” (przestaliśmy istnieć) — a temat nieistnienia wisi nad całą sceną ([2183] „Przestaniemy istnieć”). Formę bezosobową wybieram, bo nie wiadomo, czy „it” to język (m), czy Stonoga (ż); „DORWAŁA NAS!” też dobre, jeśli podmiotem ma być Stonoga.

- [2065] ch9/06-setitonfire-area/89win-1-seq-03 — **WARIANT** (niski priorytet)
  - EN: The Moons thawed from the ice. / PL: Księżyce odmarzły z lodu.
  - Proponowane PL: Księżyce wytopiły się z lodu.
  - Przesłanka: „odmarznąć z czegoś” jest nienaturalne; „wytopić się z lodu” oddaje uwolnienie. Analogicznie [2077] „Drobiny dusz odmarzały ze śliny.” → „Drobiny dusz wytapiały się ze śliny.”

Uwagi bez zmiany: [2168] „Nie tak jak stonoga” małą literą — EN „centipede” małą; OK. [2185] rym long/song nieoddany — akceptowalne w narracji. [2188]/[2189] „Wymiotuj!” — tryb rozkazujący jak w [1796] „ZWYMIOTUJ KSIĘŻYC”, spójne. [2221] Leśna Twarz mówi o sobie w rodzaju męskim („Chciałbym”), co pasuje do „Nie jestem dziewczyną. Jestem POSĄGIEM”.

## b11 — ch10 (epilog), __DARKPLACE (Sen Skejtera), bossowie, cele Księżycowego Wzroku, wiersze rozdziałów

Epilog ciepły i spójny („ślimaczym tempem” — gra sluggishly oddana), Hamlet w [652] zgodnie z decyzją, nazwy bossów zgodne z poziomami. Wiersze zachowują obrazy i podział wersów; „Demon odrodził się, odprężony” ([2249], annealed) — świetna podwójność.

- [2244] poems/ch03-poem-body — **PEWNY BŁĄD** (znaczenie; ta sama przesłanka co [1106])
  - EN (wers 3): the Rabbit read dimly from a letter burned bedside.
  - PL (wers 3): czytał Królik sennie z listu spalonego przy łóżku.
  - Proponowane PL (cały wpis): Bliźniacze Księżyce świeciły, płacząc, Królik leżał we śnie.\n„Zaproszenie od Diabła na dzisiejszą Kolację”,\nczytał Królik sennie list, co wypalił się przy łóżku.\n\nPrzebite dwukrotnie, połknięte bez oglądania.\nDwa Księżyce w żołądku dały już Trzy.\n\nW małym mieszkaniu Królik rzekł do Skejtera:\n„Bankiet będzie modny, w czystych ubraniach Diabła.\nŚpij już na tym łożu świeżego śniegu”.\n\nOdpływał, opadał coraz głębiej.\nPęknięcia szkła stawały się znużone i ciemniejsze.\n\nOpadała dusza niczym kamień.
  - Przesłanka: list „spalony” nie da się przeczytać; w tym świecie listy „wypalają się” na miejscu ([1038]). W wierszu Królik „leżał we śnie”, więc „sennie” może zostać (inaczej niż w [1106]).

- [2245] poems/ch04-poem-body i [2251] poems/ch10-poem-body — **WARIANT** (motyw drutu)
  - EN [2245] (wers 2–3): wiry officers of Fuss crept their shadows from / stone cabinets to file sacred paperwork.
  - PL [2245]: żylaste sługi Zgiełku wysuwały cienie / z kamiennych szaf, by składać święte dokumenty.
  - Proponowane PL [2245] (cały wpis): W Departamencie Śmierci\ndruciani funkcjonariusze Zgiełku wysuwali cienie\nz kamiennych szaf, by składać święte dokumenty.\n\nDrobny Zgiełk zbudził Skejtera ze snu.\nSnu, który był tu zakazany. Zatem do sądu.\nKtóż szydził ze Skejtera, jeśli nie Krwawy Wieszcz.\n\n„BADANIE TWOJEJ DUSZY\nNIE WYKAZUJE WAŻNEJ UMOWY\nNA POŻERANIE TYCH KSIĘŻYCÓW”.\n\nSkejter odwołał się więc rozwlekłą poezją,\nutkaną z liter w powietrzu, spisaną przez udręczonego gołębia.\nOdwołanie owinęło się wokół siebie w diabelską wstęgę Möbiusa.\n\nPapierowy trik wyciągnął Wieszcza ze strumienia dusz.\nNagłym szarpnięciem Skejter odcisnął się na jego siatkówce,\nłkając flipami i napiętymi grindami.\n\nWbrew poprawnym dokumentom, wewnątrz Wieszcza\nSkejter, już zbieg, pożarł surowo\nKsiężyc kwaśny jak jabłko.\n
  - EN [2251] (wers 1): The Devil's wiry fur still dark / PL: Szorstka sierść Diabła wciąż ciemna,
  - Proponowane PL [2251] (wers 1): Druciana sierść Diabła wciąż ciemna, (reszta bez zmian)
  - Przesłanka: „wiry” = zarówno „żylasty/szorstki”, jak i „z drutu”; gra konsekwentnie buduje świat z drutów: Zgiełk ma „ciemne druty” ([1507]), Skejter „druciany żołądek” ([1793]), „druciane gardło” ([1938]), gołąb jest „druciany” ([1306]). „Officers of Fuss” to w całej grze „funkcjonariusze Zgiełku” ([1294]), nie „sługi”. Uwaga: w [2245] PL kończy się pojedynczym \n jak EN — zachować.

- [2250] poems/ch09-poem-body — **WARIANT**
  - EN (ostatnie wersy): The Skater vomitted a soul out\nanew.
  - PL (ostatnie wersy): Skejter wypluł duszę\nna nowo.
  - Proponowane PL (cały wpis): Całe Podziemie stanęło, by patrzeć, jak nocne niebo\nkruszy się, gdy ten nieskończenie długi Robak pęka na dwoje.\n\nChoć ogon wciąż był wiecznie długi,\nczerwone oko zapiszczało skończoną liczbą altówek.\n\nSkejter rozorał metalowy pancerz od środka,\nwyrywając Księżyce z trawiennej pustki.\n\nWymiotuj! Wymiotuj!\nKsiężyce wyszły na zewnątrz.\n\nWymiotuj!\nKażda dusza ujrzała —\nZnienawidzone barwy zastąpione,\nbezsens odzyskany.\n\nSkejter zwymiotował duszę\nna nowo.
  - Przesłanka: wiersz trzy razy powtarza „Wymiotuj!”, a puenta „vomitted” domyka ten motyw (także [1796] „ZWYMIOTUJ KSIĘŻYC”); „wypluł” go przerywa. Przy okazji „Całe Podziemie” wielką literą jak w identycznym zdaniu przerywnika [2184] (EN w obu „Underworld” wielką).

- [2246] poems/ch05-poem-body — **WARIANT** (niski priorytet)
  - EN: The Moon disintegrated and coated grey cliffs with sickly purple clouds.
  - PL: Księżyc rozproszył się, pokrywając szare skały chorobliwie fioletowymi chmurami.
  - Proponowane PL (tylko ten wers): Księżyc rozproszył się, pokrywając szare klify chorobliwie fioletowymi chmurami.
  - Przesłanka: w ch5 „grey cliffs” to zawsze „szare klify” ([1476], [1581]).

- [2256] quests/moonvision-goal-GiftBox — **BRAK KONTEKSTU** (długość, do testu)
  - EN: Gift Box / PL: Pudełko z upominkiem (20 zn., raport: ryzyko). Jeśli etykieta celu się nie mieści: „Prezent”.

Uwagi bez zmiany: [2243] „Zapominalska Żaba” w rodzaju żeńskim zgodnie z decyzją. [2247] brak otwierającego cudzysłowu — tak samo w EN, zachowane. [2248] wielkie „Zaledwie” po złamaniu wersu — jak „Mere” w EN.

## b12 — przedmioty (blaty, napoje, przedmioty fabularne, naklejki, trucki, kółka) i osiągnięcia

Nazwy gier partnerskich zostawione zgodnie z biblią (w [77] poprawnie „Death's Door” zamiast literówki EN „Deaths Door”; w [29] EN „50.000” → PL „50 000”). Dobre: „Kształtomyśliciel” (Piecethinker, odwrócony Myślokształt), „Co za śśśliczne lato na sssmutek”, „Z krwi i kości” (Fleshmade), „Zależność” (Dependence ~ Independent), echo taglinów w osiągnięciach 17–19 i 25. Brak pewnych błędów.

- [66] Item/deck-biletea-name — **WARIANT**
  - EN: Let's Chug Bile Tea
  - PL: Chluśnij Żółciową Herbatą
  - Proponowane PL: Obalmy Żółciową Herbatę
  - Przesłanka: „chug” = wypić duszkiem; „chlusnąć czymś” to po polsku przede wszystkim „oblać, chlapnąć płynem”, więc „Chluśnij Żółciową Herbatą” czyta się jak „oblej (kogoś) herbatą”. „Obalmy…” zachowuje „Let's” i potoczne „obalić butelkę”. Alternatywa bliższa oryginałowi: „Chlapnijmy Żółciowej Herbaty”.

- [115] Item/deck-oneway-stop-name — **BRAK KONTEKSTU** (skłaniam się do zmiany; do sprawdzenia grafiki blatu)
  - EN: Oneway Stop / PL: Przystanek jednokierunkowy (26 zn., raport: długość)
  - Proponowane PL: Jednokierunkowy stop
  - Przesłanka: opis [114] „A different way to "skate street."” wskazuje na znaki drogowe (ONE WAY + STOP), a nie przystanek autobusowy. „Przystanek” to najpewniej błędne odczytanie „stop”. Jeśli grafika pokazuje przystanek — zostawić.

- [186] Item/sticker-TRY_HARD-name — **WARIANT** (niski priorytet)
  - EN: Try Hard / PL: Daj z siebie wszystko (21 zn., raport: długość)
  - Proponowane PL: Spinacz
  - Przesłanka: „tryhard” w slangu to ktoś, kto za bardzo się stara (pejoratywnie); polski slang: „spinać się”, „spinacz”. Jeśli naklejka to po prostu zachęta — „Staraj się” (krócej niż obecne). Gust.

- [33]/[35]/[37] Achievement/ach-17/18/19-2desc — **WARIANT** (długość, niski priorytet)
  - EN: Shatter 25 times at speed. / PL: Roztrzaskaj się przy dużej prędkości 25 razy.
  - Proponowane PL: Roztrzaskaj się 25 razy w pełnym pędzie. (analogicznie 100 i 500)
  - Przesłanka: raport wskazał ryzyko długości (45–46 zn.); na Steamie opisy osiągnięć są długie bez problemu, więc zmieniać tylko, jeśli ekran osiągnięć w grze ucina.

Uwagi bez zmiany: [182] „6.66” z kropką — nazwa naklejki (cena/liczba jako grafika), zostawić. [212] „Daj się uszczęśliwić” (Get Lucked) — łagodniejsze niż ukryty wulgaryzm EN, ale zabawne; gust. [241] „Szczur / Królik” — gra Rab/bit nieoddana, czytelne. [50] „Nieświadomość” (Oblivious) — akceptowalne.

---

## Synteza dla całej gry

### Dodatkowe ustalenia z przeglądu przekrojowego

- [706], [707], [709] ch1/05-L0/1ollieobelisk-1-seq-02/03/05 — **WARIANT** (spójność)
  - EN: …where the Skater jumps up with their board. / …where the Skater pops the board… / …brings the Skater and their board into the air.
  - PL: …w którym skejter wyskakuje wraz z deskorolką. / …podczas skoku skejter wybija deskę tylną stopą. / …unosi w powietrze skejtera i jego deskorolkę.
  - Proponowane PL [706]: Ollie to podstawowy trik, w którym Skejter wyskakuje wraz z deskorolką.
  - Proponowane PL [707]: Ollie wymaga wyczucia i precyzji: podczas skoku Skejter wybija deskę tylną stopą.
  - Proponowane PL [709]: Wykonany płynnie ollie unosi w powietrze Skejtera i jego deskorolkę.
  - Przesłanka: identyczne „encyklopedyczne” opisy trików w Liceum ([776]–[784]: „Skejter skacze do przodu”, „Skejter podkręca deskę piętą”) mają wielką literę, jak EN „the Skater” w obu miejscach. Obelisk to pierwszy tekst samouczka, więc różnica rzuca się w oczy. Alternatywnie: małe litery w obu grupach — ważne, żeby jednolicie.

- [734] ch1/06-mooncore/ranout-1-seq-01 — **WARIANT** (spójność mechaniki „soul expired”)
  - EN: The Skater's soul expired, so this eternity started over.
  - PL: Dusza Skejtera się wyczerpała, więc ta wieczność zaczęła się od nowa.
  - Proponowane PL: Dusza Skejtera wygasła, więc ta wieczność zaczęła się od nowa.
  - Przesłanka: ten sam komunikat porażki w [1085] brzmi „Dusza Skejtera wygasła”, a licznik w HUD to „SOUL EXPIRY” ([620]). Jedno słowo dla jednej mechaniki; „wygasła” pasuje do licznika i do „Kombo… wygasło” ([883], [436]).

- [1522] i [1734] (Penin) — **WARIANT** (odróżnienie głosów; do rozmowy, bo biblia zapisuje „skarbie” dla obu postaci)
  - EN [1522] (wers 2): You are sparkling, darling. / PL: Ależ lśnisz, skarbie.
  - Proponowane PL [1522] (cały wpis): OCH! Rany.\nAleż lśnisz, złotko.\nMuszę mieć cię w kolekcji.\nIle za ciebie?
  - Przesłanka: w EN Penin mówi „darling”, Beea „honey/dear”; w PL obie postacie mówią „skarbie”, a na Bankiecie ich kwestie stoją obok siebie ([1734] Penin, [1736] Beea „Przykro mi, skarbie”). „Złotko” to jubilerski, protekcjonalny zwrot, pasujący do snoba-jubilera; Beea zostaje przy „kochanie/skarbie”. [1734] „mój drogi szklaczku” bez zmiany.

### Spójność terminów (policzone w całym JSON, 2305 wpisów)

| EN | PL (biblia) | wystąpienia EN | zgodne | uwagi |
| --- | --- | ---: | ---: | --- |
| Skater | Skejter | 331 | 321 | 10 pozostałych to zaimki/podmiot domyślny („Był zmęczony…”) — poprawne; małe „skejter” w [706]/[707]/[709] (wyżej) |
| underworld | podziemie | 48 | 48 | wielkość liter idzie za EN („Podziemie” gdy „Underworld”), wyjątek [2250] (b11) |
| Centipede | (Wieczna) Stonoga | 79 | 79 | |
| Moon Vision | Księżycowy Wzrok | 4 | 4 | |
| combo | kombo | 27 | 27 | „kombem” w [1639] |
| stomp | tupnięcie/tupnąć | 18 | 18 | |
| Thinkpiece | Myślokształt | 18 | 18 | + „Kształtomyśliciel” [238] |
| Soulflower | duszokwiat | 3 | 3 | |
| Moonflower | Księżycowy Kwiat | 8 | 7 | [1170] małą literą (PEWNY BŁĄD, b04) |
| Fuss | Zgiełk | 16 | 16 | w wierszu [2245] „sługi Zgiełku” zamiast „funkcjonariusze” (b11) |
| Sloucher | Garbus | 7 | 7 | |
| Oblivion | Zapomnienie | 10 | 10 | |
| Depth | Głębia | 17 | 17 | wielkość liter za EN |
| contract | umowa (ch1: kontrakt) | 27 | 26 | 1 zaimek [1038] — poprawnie |
| deck | blat | 9 | 9 | |
| Crest | pieczęć | 2 | 2 | |
| Moonlit Spot | Księżycowa Plama | 5 | 5 | |
| Evaluation | OCENA | 11 | 11 | |
| Lyceum | Liceum | 11 | 11 | patrz „Do rozmowy” |
| stale (mechanika) | oklepany | 3 | 1 | [733], [786] (b02) |
| soul expired | wygasła | 2 | 1 | [734] (wyżej) |

Typografia: w całym pliku brak „ - ” zamiast myślnika, spacji przed ?!:; i prostych cudzysłowów; liczby z twardą spacją tysięcy (10 000, 40 000), „1400 °C”. Znaczniki (*red*, *blu*, *blue*, *gold*, *b*, **, <color>, <br>, <i>, (S), (C), *ec*, *stomp*, *combo*) w ustaleniach i propozycjach zachowane; w przeczytanych wpisach nie znalazłem uszkodzonego tokenu ani różnicy w liczbie \n.

### Głosy postaci

- **Narrator:** krótkie zdania, powtórzenia i liryczne wstawki zachowane (seria umierania w ch8, „Skejter poczuł wszystkość”). Czasem gubi wewnętrzny rym EN ([1105]) — drobne.
- **Królik/Rabbie → Szczur:** kumpelski, zmęczony, ucieka („Wybacz” ×3, „Ja biorę nogi za pas”); monolog w ch7 i wykład w ch9 w tym samym głosie, ale poważniejszym — dobrze. Rodzaj męski konsekwentny przed i po ujawnieniu.
- **Filozof:** „W istocie”, „Rozważmy”, „zadumiewające”, „podumam”, „Widzę, więc… więc krwawię”, w epilogu „ślimaczym tempem” — głos wyrazisty i spójny w ch1, ch5, ch6, ch7, ch10. Jedna urzędowa formuła do poprawy ([744]).
- **Philoso:** 4 rymowane wypowiedzi; trzy rymują się dobrze, [795] ma jedną parę bez rymu (b02).
- **Larry:** rymowane wersaliki; w ch3 świetne, w ch2 [990] rym zgubiony, w ch7 [1735] luźny — do ewentualnego podciągnięcia [990].
- **Beea:** ciepła, „kochanie/skarbie”, rodzaj żeński w ch3 i ch7 — zgodnie z decyzją.
- **Coney:** „kolego”, wersaliki przy przepisach, „UGOTOWANY”, „ZGIEŁKOWYM PIERWSZEJ RANGI”, „CENTO” — najbardziej konsekwentny głos w grze.
- **Frotue (Żaba):** uprzejmy sprzedawca, „miłego potępienia!”, męski o sobie, żeński w narracji — spójne w ch2, ch3, ch4, ch7, ch9, ch10 i wierszu ch2.
- **Penin (Pingwin):** snob, „mój drogi gryzoniu”, „Chybu… dokolebałem się” — dobry; pokrywa się z Beeą w „skarbie” (wyżej).
- **Licha:** urzędniczka, per „pan”, rodzaj żeński — spójna w jedynej scenie.
- **Fałszywe Słońce:** narracja nijaka, w 1. osobie jak Księżyc — spójne w ch6 i ch9.
- **Gołąb-pisarz:** małe litery i wybuchy wersalików zachowane — bardzo dobrze.

### Ponowna ocena decyzji z biblii i translation-decisions.md

| Decyzja | Werdykt | Przykłady / uzasadnienie |
| --- | --- | --- |
| Skejter w rodzaju męskim | **utrzymać** | cała gra spójna, także ch8 („Demon… wszedł”) i epilog („Ale mnie zaskoczyłeś!” do ślimaka). Brak kontrprzesłanek. |
| Pisownia „Skejter” | **utrzymać** | 321/331 wystąpień, reszta to zaimki. Jedyna niespójność: wielkość liter w [706]/[707]/[709]. |
| Beea w rodzaju żeńskim | **utrzymać** | [1170] „miała”, [1173] „sprzedałam”, [1736] „Przywykłam”. |
| Szkielet z Placu Żalu męski | **utrzymać** | [1368]; brak nowych danych. |
| Kamień młyński (ch9) męski | **utrzymać** | [2052]–[2055] spójne; tekst to parafraza piosenki („Millstone”), rodzaj gramatyczny rzeczownika rozstrzyga. |
| Frotue męski, „Żaba” w narracji żeńska | **utrzymać** | [978], [1346], [1722], [1827], [2243]; konsekwentne w 6 rozdziałach. |
| Licha żeńska, per „pan” | **utrzymać** | [1033]–[1044]; jedyna scena, brak nowych danych. |
| Fałszywe Słońce nijakie | **utrzymać** | [1695]–[1709], [2157]–[2159]. |
| Echo „Ten demon…” (ch1 ↔ ch8) | **utrzymać** | [683]/[684] ↔ [1919]/[1920]. |
| Wielkie litery nazw bytów świata | **utrzymać** | tłumaczenie idzie za EN także w wyjątkach (małe, gdy EN małe: [1663], [2168]). |
| podziemie / Głębia / Zapomnienie / Zgiełk / Wieczna Stonoga / Krwawy Wieszcz | **utrzymać** | 100% spójności; „Zgiełk” dobrze znosi odmiany („funkcjonariusze Zgiełku”, „Kroczący Zgiełk”, „ZGIEŁKOWYM”). |
| Myślokształt (Thinkpiece) | **utrzymać** | działa jako przedmiot i jako temat żartów; „Kształtomyśliciel” [238] potwierdza. Drobna strata drugiego sensu w [1478] (brak kontekstu). |
| Garbus (Sloucher) | **utrzymać / brak kontekstu wizualnego** | opis [63] („Slouchers chained to their desks”) pasuje do zgarbionych urzędników; notka w [384] prosi o sprawdzenie wyglądu — do testu w grze. |
| umowa / kontrakt tylko w ch1 | **utrzymać** | 25× umowa, 1× kontrakt w [687]. |
| deck = blat | **utrzymać** | UI, przedmioty, narracja [2045], [2085] spójne. |
| Księżycowy Kwiat | **utrzymać** z 1 poprawką | [1170] małą literą. |
| „Stale” jako „oklepany” (niezapisane w biblii) | **proponowana zmiana** | ujednolicić [733], [786]; dopisać do biblii. |
| „Soul expired” (niezapisane) | **proponowana zmiana** | „wygasła” w [734]; do rozważenia HUD [620]. |
| Lyceum = Liceum (niezapisane) | **brak kontekstu / do rozmowy** | patrz niżej. |
| Rymy Philoso zostawione z 0.2 | **utrzymać** z poprawką [795] | |
| Hamlet [652] | **utrzymać** | „powtarzać może” — trafne. |
| „jestem zajęty byciem W KROPCE”, „Demon Dom Ser” | **utrzymać** | działa w scenie [1315], [1363]. |
| HOUSE/CHEESE: angielskie słowo + polskie znaczenie | **utrzymać** (warunkowo) | [155], [157], [1336], [1378]; rozstrzyga test, czy modele liter w świecie są czytelne z dialogiem. |
| pain/pane oddane zawahaniem | **proponowana zmiana (wariant)** | patrz „Do rozmowy”. |
| „Ten Bolgias” = „Dziesięć Jarów” | **proponowana zmiana (wariant)** | [1754] w samym tekście gry nazywa je „rowami” — patrz „Do rozmowy”. |
| Penin „skarbie” | **proponowana zmiana (wariant)** | pokrywa się z Beeą; „złotko”. |

## Zestawienie

- Przeczytane: 2305/2305 wpisów w 12 partiach, bez luk (coverage.md).
- **PEWNY BŁĄD: 4** — [772] „Spójrz przez swoje ramię”, [1106] i [2244] „list spalony”, [1170] „księżycowych kwiatów” małą literą.
- **WARIANT: 37** (w tym grupy: stale ×2 wpisy, [2245]/[2251], [2065]/[2077], [33]/[35]/[37], [484]/[576], [339]/[342], [706]/[707]/[709]).
- **BRAK KONTEKSTU: 11** — [620]/[621], [496], [388]–[404], [755], [893], [1034], [1478], [1574], [1711], [2256], [115].

## Do sprawdzenia w grze

1. **Ustawienia → Rozgrywka / Grafika / Dostępność:** czy mieszczą się obok przełączników: „Automatyczne centrowanie kamery” [477]/[573], „Wyłącz spowolnienie przy tupnięciu” [487], „Odpychanie przełącznikiem” [603], „Obracanie kamery przy upadku” [611], „Synchronizacja pionowa” [599], „Automatycznie kontynuuj dialogi” [572]. Przy okazji oceń, czy „Interfejs scen” [576] jest zrozumiały jako przełącznik.
2. **HUD licznika duszy (ch1, pierwszy zjazd po Księżycowym posłaniu):** jak ułożone są słowa „DUSZA … WAŻNOŚĆ” [620]/[621] wokół licznika — rozstrzyga, czy zmienić na „DUSZA … WYGASA”.
3. **Ekran kombo (ch1, boss Filozofa):** jak wyświetlają się modyfikatory trików [388]–[404] razem z nazwą triku (czy nie powstaje „Potężny Szybko Kickflip…”), gdzie pojawia się „ZAKOŃCZENIE” [496], czy cel fazy 3 „Kończ triki tupnięciem, by zadawać obrażenia.” [893] mieści się w polu celu.
4. **Liceum, pierwsza rozmowa z Królikiem po wejściu [772]:** jaki gest/przycisk oznacza Księżycowy Wzrok (czy Skejter podnosi rękę i patrzy przez nią) — potwierdzi poprawkę „Spójrz przez swoją szklaną rękę”.
5. **ch4, Plac Żalu i Poczekalnia:** czy zbierane litery (modele HOUSE/CHEESE) są czytelne razem z dialogiem [1378] „Układa się w… CHEESE. Czyli SER.” i opisami słów [155]/[157].
6. **ch2, telefon na stacji Ulica Wrząca [1034]:** odbiór żartu „szkła i… bólu?” (i ewentualnego „szyby?”).
7. **ch8, karta poziomu „Ulica Minus Sześćset Sześćdziesiąta Szósta” [344]:** 42 znaki.
8. **Menu Księżycowego Wzroku (cele):** „Pudełko z upominkiem” [2256] — długość etykiety.
9. **Ekwipunek → Blaty:** grafika blatu „Oneway Stop” [115] (znak drogowy czy przystanek?) i długość nazwy; naklejka „Try Hard” [186].
10. **ch7, scena „Do you ever yearn?” [1811]:** czy dłuższy tekst mieści się w dymku.
11. **ch4, sąd i Departament:** wygląd Garbusów (Sloucher) — czy „Garbus” pasuje do sylwetki (notka w [384]).
12. **Osiągnięcia (ekran w grze):** opisy 17–19 (45–46 znaków).

## Do rozmowy z użytkownikiem (najważniejsze tematy)

1. **Gra słów pain/pane w telefonie Lichy [1034].**
   - EN: "I'm looking for a... skater? Made of... glass and pane?"
   - Obecne PL: „Szukam... skejtera? Ze... szkła i... bólu?”
   - Rekomendacja: „Szukam... skejtera? Ze... szkła i... szyby?”
   - Zysk: wraca żart (urzędniczka przekręca znany z taglinu „ze szkła i bólu” na tautologię „szkła i szyby”). Koszt: działa tylko, jeśli gracz pamięta tagline; obecne PL jest bezpieczne, ale płaskie.
2. **Lyceum → „Liceum” (cały ch1, 11 wpisów).**
   - Obecne: „Liceum”. Wariant: „Likejon” (polska nazwa szkoły Arystotelesa).
   - Rekomendacja: **zostawić „Liceum”** — czytelne, komiczne skojarzenie ze szkołą pasuje do „OCENY” i „egzaminu”; „Likejon” jest precyzyjne, ale mało kto je zna. Zapisać wybór w biblii.
3. **„Ten Bolgias” → „Dziesięć Jarów” [339]/[342].**
   - Rekomendacja: „Dziesięć Rowów”. Zysk: aluzja do Malebolge u Dantego i zgodność z [1754] („Przepłyniemy przez rowy ósmej…”), gdzie gra sama opisuje te miejsca. Koszt: „Jary” brzmią ładniej, „Rowy” prozaiczniej.
4. **Mechanika „stale” — jedno słowo („oklepany”) [729]/[733]/[786].**
   - Rekomendacja: ujednolicić do „oklepany” (propozycje w b02). Zysk: gracz rozpoznaje tę samą mechanikę w trzech samouczkach. Koszt: brak.
5. **Rymy: Philoso [795] i Larry [990].**
   - [795] ostatni wers: obecne „Za trud twój **Myślokształt** niech będzie zapłatą.” → rekomendacja „Masz więc **Myślokształt** — nie trudziłeś się marno.” (rym darmo/marno).
   - [990]: obecne „KARMIĄ MNIE WIBRACJE. / JEDŹ DLA MNIE, BESTIO.” → rekomendacja „WIBRACJE — MOJA STRAWA. / JEDŹ DLA MNIE, BESTIO KRWAWA.”
   - Zysk: głosy rymujących postaci bez dziur. Koszt: drobne odejście od dosłowności (zgodne z biblią dla Philoso).
6. **Motyw drutu w wierszach [2245]/[2251] („wiry”).**
   - Obecne: „żylaste sługi Zgiełku”, „Szorstka sierść Diabła”. Rekomendacja: „druciani funkcjonariusze Zgiełku”, „Druciana sierść Diabła”.
   - Zysk: spójność z drucianym światem (druty Zgiełku [1507], druciany żołądek i gardło Skejtera) i z terminem „funkcjonariusze Zgiełku”. Koszt: „żylasty” też jest poprawnym znaczeniem „wiry”.
7. **Targ Przybyszów jako giełda [1388].**
   - Obecne: „Patrzy, jak spisują każdą nową duszę podziemia.” Rekomendacja: „Patrzy, jak na giełdę trafia każda nowa dusza podziemia.” (ostrożniej: „…jak notuje się każdą nową duszę…”).
   - Zysk: domyka satyrę rynkową rozdziału (portfel, zwrot z inwestycji, salda żalu). Koszt: lekkie dopowiedzenie.
8. **Penin „skarbie” → „złotko” [1522].**
   - Zysk: jubilerski, protekcjonalny zwrot; odróżnia go od Beei, która mówi „skarbie” zaraz obok na Bankiecie. Koszt: zmienia zapis w biblii (rejestr Penina).
9. **Nazwa blatu „Let's Chug Bile Tea” [66].**
   - Obecne: „Chluśnij Żółciową Herbatą” (czyta się jak „oblej herbatą”). Rekomendacja: „Obalmy Żółciową Herbatę”; wariant „Chlapnijmy Żółciowej Herbaty”.
10. **HUD „SOUL EXPIRY” [620]/[621] i komunikat [734].**
    - Rekomendacja: po teście układu — „DUSZA … WYGASA” w HUD i „Dusza Skejtera wygasła…” w [734]. Zysk: jedno słowo dla mechaniki. Koszt: zależy od ułożenia na ekranie.

Pewne błędy ([772], [1106], [2244], [1170]) agent prowadzący może nanieść bez rozmowy; [772] warto pokazać użytkownikowi razem z testem 4, bo zależy od tego, jak w grze wygląda Księżycowy Wzrok.
