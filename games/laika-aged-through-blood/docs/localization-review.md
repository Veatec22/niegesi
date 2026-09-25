# Laika: Aged Through Blood — review lokalizacji po fullu

Niezależny przegląd (osobny agent, tylko do odczytu). Zmiany w tym dokumencie mają status
**proponowane**; nic z tego nie zostało jeszcze naniesione na `pl.json` ani EN/PL.

## Zakres

- **Data:** 2026-09-24.
- **Wejścia:** `translations/pl.json` SHA-256 `de0fcdccffa417f7991c3e1389f813be0850060e1a62b89aae4f3511f9333921`,
  `translations/en-pl-review.json` SHA-256 `7b16b51b41ab1554be4cd0ed04b40656d2f60a8dd6c33aa75aadca9e56ea7338`;
  pomocniczo `bible.yaml`, `docs/translation-decisions.md`, `docs/technical.md`, `work/l10n-report.md`,
  tabele RU/ES/FR i skrypty dialogów `D_*` z plików gry.
- **Zgodność plików:** 3470 kluczy w obu plikach, polski tekst identyczny w 3470/3470;
  angielski w EN/PL identyczny z `work/source/en.json` (pozostałe 739 wpisów źródła jest pustych).
- **Przeczytane:** 3470 z 3470 wpisów, czyli DIALOGUES 2448 (716 scen, kolejność ze skryptów gry),
  UI 378 (w tym osiągnięcia), ITEMS 264, QUESTS 218, ZONES 83, CHARACTERS 79.
  Manifest partii: `work/review-coverage.md`.
- **Luki i ograniczenia:** 49 kluczy dialogowych nie ma skryptu, więc kolejność kwestii wziąłem
  z numerów w kluczu. Nie widziałem gry: długość tekstów, łamanie wierszy i glify fontów oceniam
  tylko z tekstu. Wpisy bez rozstrzygnięcia są w sekcji „Do rozmowy” z oznaczeniem *brak kontekstu*.
- **Kontrole automatyczne:** płeć w 1. osobie czasu przeszłego zgadza się z mówiącym
  (wyjątkiem są tylko 3 znane cytaty Primo), męskie formy 2. osoby padają tylko do mężczyzn,
  tokeny się zgadzają (raport kontrolny: 0). Nad limit i ponad długość EN wychodzi tylko
  `UI_TUT_CANDLES_DESC`.

Ogólna ocena: tłumaczenie jest wierne i ma dobry rytm. Głosy postaci są rozróżnione, a tiki
słowne prowadzone konsekwentnie. Pewnych błędów jest niewiele i są punktowe (odmiana,
składnia, dwa przesunięcia sensu). Rozmowy wymaga głównie skala wulgaryzmów i kilka kalk.

## Błędy

### A. Pewne (odmiana, składnia, sens, termin)

| # | Klucz | EN | Obecne PL | Proponowane PL | Przesłanka | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `I_FLUTE_REED_DESC` | …Hope it fits Gusto's handcrafted flute! | …Oby pasowała do ręcznie robionego fletu Gusta! | …Oby pasowała do ręcznie robionego fletu Gusto! | Gusto to kobieta (biblia; „Zgubiłam” w `D_A_Musicians_Flute_*`). Żeńskie imię na -o się nie odmienia, więc „Gusta” czyta się jak mężczyzna. | proponowane |
| 2 | `I_PARTITURES_DESC` | It reeks of alcohol, so it's probably Rollo's. | Cuchną alkoholem, więc pewnie są Rolla. | Cuchną alkoholem, więc pewnie należą do Rollo. | Rollo to kobieta („sprzedałam”, „Wytrzeźwiałam”), odmiana jak wyżej. W zadaniach jest już poprawnie: „nuty Rollo”. | proponowane |
| 3 | `D_B_Alfredo_BeforeKidnap2_ALFREDO_2` | EVEN MORE HORRIBLE THAN THE VILLAIN'S IN GUTSY GUS'S ADVENTURES!! | JESZCZE OKROPNIEJSZY NIŻ ZŁOCZYŃCA Z PRZYGÓD GUSA GARDZIELI!! | JESZCZE OKROPNIEJSZY NIŻ TEN ZŁOCZYŃCY Z PRZYGÓD GUSA GARDZIELI!! | W EN chodzi o kapelusz złoczyńcy (the villain's), a PL porównuje kapelusz do złoczyńcy. Rosyjska wersja ma „чем у злодея”. | proponowane |
| 4 | `Q_D_S_Flower_DESC` | …swallowed all that "funerary friend" bullshit… | …łyknęła te bzdury o „pogrzebowym przyjacielu”… | …łyknęła te bzdury o „pogrzebowej przyjaciółce”… | To termin z biblii („pogrzebowa przyjaciółka”, bo Puppy jest dziewczynką). W dialogach jest tak 5 razy, tu jedyny raz inaczej. | proponowane |
| 5 | `Q_D_S_OldCamp_DESC` (1. zdanie) | Hilda left her family braid Where We Used to Live, nowadays known as Where All Was Lost. | Hilda zostawiła rodzinny warkocz tam, Gdzie Kiedyś Żyliśmy, dziś znanym jako <color…>Tam, Gdzie Wszystko Przepadło</color>. | Hilda zostawiła rodzinny warkocz w miejscu, Gdzie Kiedyś Żyliśmy, dziś znanym jako <color=#FF492E>Tam, Gdzie Wszystko Przepadło</color>. | „znanym” nie ma się z czym uzgodnić, bo „tam” to przysłówek. Potrzebny jest rzeczownik „miejscu”. | proponowane |
| 6 | `D_B_Shaza_E3_LAIKA_3` | …if we got out of this alive and I could live a normal life. | Pytałaś, co chciałabym robić, gdybyśmy wyszły z tego żywe i mogła żyć normalnie. | Pytałaś, co chciałabym robić, gdybyśmy wyszły z tego żywe, a ja mogłabym żyć normalnie. | Podmiot zmienia się z „my” na „ja”, a „i mogła” zostaje bez osoby. Zdanie jest niegramatyczne. | proponowane |
| 7 | `D_4_FloatingCity_MainGauge_Walkie_INSIDER_3` | Then kept some soldiers to keep us Renegades from doing anything. | A tu zostawili żołnierzy, żeby my, Renegaci, nic nie zrobili. | A tu zostawili żołnierzy, żebyśmy my, Renegaci, nic nie zrobili. | Po „żeby” z podmiotem „my” potrzebna jest forma „żebyśmy”. Pluck nie mówi gwarą, więc to nie stylizacja. | proponowane |
| 8 | `I_ENTOM_INVITATION_DESC` | It bugs me to think what Mina will feed her guests with. | Aż mnie świerzbi, czym Mina nakarmi gości. | Aż mnie swędzi na myśl, czym Mina nakarmi gości. | „Świerzbi mnie” znaczy „mam ochotę”, a EN mówi o niepokoju (RU „беспокоит”, ES „no quiero pensar”). „Swędzi” zachowuje grę z tikiem Miny „Swędzi!”. | proponowane |
| 9 | `I_METAL_BAD_DESC` (2. zdanie) | The result is, well, pretty cheap, and it's all over the Wastelands. | Wyszedł, cóż, całkiem tandetny i walają się go pełne Pustkowia. | Wyszedł, cóż, całkiem tandetny i wala się po całych Pustkowiach. | Zdanie łączy dwie składnie („walać się” i „pełne Pustkowia”) i jest niegramatyczne. | proponowane |
| 10 | `D_2_Lighthouse_BeforeControls_Undone1_LAIKA_6` | I'm the radio guy. Here to check the radios. | Jestem radiowiec. Przyszłam sprawdzić radia. | Jestem radiowcem. Przyszłam sprawdzić radia. | Orzecznik rzeczownikowy stoi w narzędniku. Sama gra używa tu narzędnika: „Jestem … Technikiem” (`…Wastelands_Undone1`). | proponowane |
| 11 | `D_B_Bustender_Default1_BUSTENDER_1` | You're the biker who's been kicking bird ass! Hilarious! | Jesteś tą motocyklistką, która skopuje ptasie tyłki! Przezabawne! | Jesteś tą motocyklistką, która kopie ptasie tyłki! Przezabawne! | Forma „skopuje” jest nienormatywna. | proponowane |
| 12 | `D_S_NewSheriff_Briefing_ALFREDO_10` | NOW GO GET ME ONE! DO AS YOUR SHERIFF ORDERS! | A TERAZ IDŹ MI JEDNĄ ZDOBYĆ! WYKONUJ ROZKAZY SWOJEGO SZERYFA! | A TERAZ IDŹ I ZDOBĄDŹ MI JAKIŚ EGZEMPLARZ! WYKONUJ ROZKAZY SWOJEGO SZERYFA! | „Jedną” nie ma do czego się odnieść (wcześniej padają „literaturę” i „starocie”), a szyk jest nienaturalny. „Egzemplarz” wraca w `…Complete_ALFREDO_2` („WYJĄTKOWY EGZEMPLARZ”). | proponowane |
| 13 | `D_A_GiftsPuppy_GameBoy_Intro_LAIKA_8` | It's like... every single cell in my body screams while it's torn apart. | To jakby... każda komórka mojego ciała krzyczała, kiedy rozrywa ją na strzępy. | To jakby... każda komórka mojego ciała krzyczała, rozrywana na strzępy. | „Rozrywa” nie ma podmiotu, a czasy się nie zgadzają. | proponowane |
| 14 | `Q_D_S_Prophecy_DESC` (ostatnie zdanie) | I live many lives as myself, but they live many selves in just one life. | …ja żyję wieloma życiami jako ja, a oni w jednym życiu są wieloma sobą. | …ja żyję wieloma życiami jako ja, a oni w jednym życiu bywają wieloma różnymi osobami. | Zaimek „sobą” nie tworzy liczby mnogiej, więc fraza jest niegramatyczna. | proponowane |
| 15 | `Q_D_3_TheBigTree_Bishops` | …behind double doors… | …za dwuskrzydłymi drzwiami… | …za dwuskrzydłowymi drzwiami… | Normatywna jest forma „dwuskrzydłowe”, której używa już dialog `…FirstDoorFound_ORELLA_7`. Chodzi o spójność. | proponowane |

### B. Bardzo prawdopodobne (kalki, przesunięcia sensu, drobne terminy)

| # | Klucz | EN | Obecne PL | Proponowane PL | Przesłanka | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | `D_S_PoochiesCorpse_TalkToShaza_SHAZA_4` | Puppy needs closure. We all do. | Puppy potrzebuje zamknięcia. Wszyscy potrzebujemy. | Puppy musi się z tym pożegnać. My wszyscy też. | To kalka, a polskie zdanie da się przeczytać jako „Puppy trzeba zamknąć”. RU ma „примириться с утратой и отпустить”, ES „cerrar esa herida”. | proponowane |
| 17 | `D_4_FloatingCity_Boss_Barks7_CITADELBOSS_RIGHT_1` | My people need closure, and the Egg will bring it. | Mój lud potrzebuje zamknięcia, a Jajo mu je da. | Mój lud potrzebuje zakończenia, a da mu je Jajo. | Kalka jak wyżej. RU ma „достойный финал”, ES „cerrar el ciclo”. Kwestię wygłasza bóg-showman, więc „zakończenie” ze sceną w tle pasuje. | proponowane |
| 18 | `D_A_GiftsPuppy_BookMother_BeforeKidnapping_LAIKA_3`, `D_B_Puppy_F1_LAIKA_5`, `D_S_HideAndSeek_Child3Missing_CHILD4_5` | Language, Puppy! … / Puppy! Language! / Language! | Puppy, język! … / Puppy! Język! / Język! | Puppy, jak ty się wyrażasz! Kto ci tak powiedział? / Puppy! Nie wyrażaj się! / Nie przeklina się! | Polski nie ma upomnienia „Język!”. Inne wersje gry adaptują: RU „Не ругайтесь!”, ES „¡Esa boca!”, FR „on dit pas de gros mots”. | proponowane |
| 19 | `D_A_GiftsPuppy_Dreamcatcher_LAIKA_11` | You lost me three plotwists ago, honey. | Zgubiłaś mnie trzy zwroty akcji temu, kochanie. | Pogubiłam się trzy zwroty akcji temu, kochanie. | „Zgubiłaś mnie” to kalka z „you lost me”. | proponowane |
| 20 | `Q_D_S_NightmaresOne_DESC` (ostatnie zdanie) | I guess I'll help them or I'm never gonna hear the end of it. | Chyba im pomogę, bo inaczej nie usłyszę końca narzekań. | Chyba im pomogę, bo inaczej Carey nie da mi żyć. | Kalka idiomu. | proponowane |
| 21 | `D_S_TutorialHook_GatherItem_ANARCHIST_3` | I got a kind of messy situation here! | Mam tu taką trochę bałaganiarską sytuację! | Mam tu mały pasztet! | „Bałaganiarski” opisuje osobę, nie sytuację. | proponowane |
| 22 | `D_B_Shaza_C1_SHAZA_2` | If only I knew how to make you smile! | …jak cię rozśmieszyć! | …jak sprawić, żebyś się uśmiechnęła! | EN mówi o uśmiechu, nie o śmiechu. Uśmiech to motyw całej postaci (Hilda: „Kiedy ostatnio się uśmiechnęłaś?”, „Uśmiechnęłaś się, kiedy mi ją dawałaś”). | proponowane |
| 23 | `D_S_BoneFlour_Complete_COOK_2` | Human? That's normal. | Po ludzku? To normalne. | Jak ludzkie? To normalne. | „Wyglądać po ludzku” znaczy „wyglądać przyzwoicie”, więc riposta traci sens (kości wyglądają jak ludzkie). | proponowane |
| 24 | `UI_LOG_SACK_DESTROYED_MESSAGE` | <color>Oldest Sack</color> Lost | <color>Stary worek</color> stracony | <color=#1EC8AD>Najstarszy worek</color> stracony | Komunikat mówi, który worek przepadł, a „stary” gubi tę informację (RU „самая старая”, ES „más antiguo”). PL ma 25 znaków przy limicie orientacyjnym 20, więc trzeba sprawdzić w grze. | proponowane |
| 25 | `Q_D_A_MusiciansDrums_DESC` (2. zdanie) | …but she fell into a coma during Fogg's birth. | …ale przy porodzie Fogg zapadła w śpiączkę. | …ale rodząc Fogg, zapadła w śpiączkę. | „Fogg” się nie odmienia, więc da się przeczytać, że to Fogg zapadła w śpiączkę. | proponowane |
| 26 | `D_2_Lighthouse_Borderpoints_Undone2_LIGHTCORPORAL1_2` | …your little non-bird friends here, Roy! | …przywozić kumpli, którzy nie są ptakami, Roy! | Wiesz, że nie wolno ci tu przywozić swoich nieptasich kumpli, Roy! | Ptaki zawsze piszemy wielką literą (biblia). W tej samej sekwencji pada też „nieptasie ścierwo”, a zdanie jest krótsze. | proponowane |

Razem: **15 pewnych** (A) i **11 bardzo prawdopodobnych** (B, 13 kluczy).

## Decyzje sprzed verticala — ponowna ocena

| Decyzja | Werdykt | Uzasadnienie i przykłady |
| --- | --- | --- |
| Laika mówi w rodzaju żeńskim i do wszystkich na „ty” | **utrzymać** | Sprawdzone automatycznie na wszystkich 2448 dialogach, bez odstępstw. |
| „matko” do Mai, „kochanie” do Puppy | **utrzymać** | Działa w chłodzie i w czułości (`D_0_Walkie_3_A_LAIKA_4`, `D_F_DaughterDies_Complete_LAIKA_13` „Wdech, matko.”, `D_1_Mines_AfterBoss_2`). |
| Zwrot po imieniu w mianowniku | **utrzymać, doprecyzować w biblii** | Laika raz odchodzi od reguły: „Hildo” (`D_S_OldCamp_Briefing_LAIKA_1`, `…OldCamp_Complete_LAIKA_1`, `D_S_Seashell_Complete_LAIKA_1`), choć do Gundy, Dalii i Orelli mówi w mianowniku. Hilda konsekwentnie mówi „słodka Laiko” (9×) i to dobrze buduje jej staroświecki, ciepły głos. Wołacze u innych postaci („Avo”, „Mayo”, „bracie Jakobie”) też są w porządku. Propozycja w „Do rozmowy”. |
| Starsza w rodzaju żeńskim (EN: ey/em/eir) | **utrzymać, ale zapisać jako świadomą stratę** | Cała gra konsekwentnie używa zaimków niebinarnych (Primo, Carey, Molly, Maya, `Q_D_1_Mines_BackHome`). Starsza sama mówi w czasie przeszłym („Uzgodniłam”, „słyszałam”, „zmusiłyśmy”), więc polski wymaga rodzaju. RU i ES wybrały formę żeńską. Nie ma nowej przesłanki za zmianą, ale jest to jedyna tożsamość z oryginału, która w PL znika. Warto to powiedzieć użytkownikowi wprost. |
| Unae w rodzaju męskim | **utrzymać** | EN „Was he wearing…” (`D_S_Remnants_Molly_Done`), ES „el enterrador”. RU ma kobietę („знала”), ale pierwszeństwo ma oryginał. W PL spójnie: „znałem”, „Miałeś rację”, „bezpieczny”. |
| Roy mówi „radiowcu”, ale w rodzaju żeńskim | **utrzymać** | Spójne we wszystkich scenach Latarni („straciłaś”, „mogłaś”, „Zabiłaś”). Jedyny zgrzyt to „Jestem radiowiec” (błąd 10). |
| Kidgutter jako dziecko | **utrzymać** | `D_S_PoochiesCorpse_Kidgutter`: „Ty, mały”, „moje dziecięce życie”. |
| Płeć pozostałych postaci | **utrzymać; jedna sprzeczność do decyzji** | Antropolog (m) i sierżant (m) potwierdzone w RU. Sklepikarze na stacjach: Kally jest kobietą („miałam”, RU „собиралась”), a Dally mówi „Mam dwóch braci” (RU „два брата”), czyli sprzeczność jest w źródle. Tally, Dally i Xoot mają w PL formy bezosobowe, dobrze. Szczegóły w „Do rozmowy”. |
| Tiki słowne | **utrzymać** | Carey („cholernie pewna”, przedrzeźnianie przez „i” jest czytelne, np. „Pribiwiłiś gitiwić łidigi isti?”), Kris, Borden, Walterio, Molly, Zooey, Petey, Mina, Herman, Xoot („Pewniaczek!” tylko dla „Sure thang”, a „for sure” to „Na pewno”, i to jest poprawne), Renato „ty palancie”, Hektystka „zakuty łbie”, „w moim hektystycznym życiu”. U Molly podwójne „założę się” wydłuża dymki (`D_B_Molly_DuringKidnap` ma 114 zn.), więc trzeba sprawdzić w grze. |
| „Tam, Gdzie …” | **utrzymać** | Nazwy pięknie działają jako okoliczniki („Pojedziesz tam, Gdzie Krwawi Skała”, „Byłaś tam, Gdzie Będziemy Żyć?”). Wymuszają jednak dopiski „miejsce, Gdzie” i „stamtąd, Gdzie”, a raz doprowadziły do błędu składni (błąd 5). Przy korektach pilnować uzgodnienia z rzeczownikiem. |
| viscera → wnętrzności | **utrzymać** | Liczebniki się zgadzają, a gra słów Puppy („wnętrzności są jak… pieniądze”) działa. |
| Ptaki wielką literą | **utrzymać** | Jedno odstępstwo: błąd 26. |
| motor, kościana kapliczka, zryw, spowolnienie, krótkofalówka, machina wojenna, projekt | **utrzymać** | Spójne w UI, zadaniach i dialogach. |
| Ponura Motocyklistka, zakuty łeb, Hektystka, sercolśń, Pustkowia/Pustkowianie, Latające Miasto, Podgniazdo, Jajo, Renegaci | **utrzymać** | Dobrze się odmieniają („zakutołbim życiu”, „z sercolśnią”, „Nadzieja sercolśni”). |
| pogrzebowa przyjaciółka | **utrzymać** | Popraw jedno miejsce (błąd 4). Przy tej okazji ujednolicić „wianek/wieniec” (w „Do rozmowy”). |
| Zaawansowany Technik… (żart na długości) | **utrzymać** | Działa, zwłaszcza zniekształcona wersja w `…Wastelands_Undone2_LAIKA_3` i narzędnik „Wytrzymalszym Radiowym Jakimśtam Technikiem”. |
| Wykorzystane okazje („bujać się/fotel bujany”, „Na oparach”, „Drzewo genealogiczne”, „Piekielne wyżyny”, „Hak zakutego łba”, „Niewybuch”) | **utrzymać** | Wszystkie są trafne. Do tego dochodzą udane rozwiązania, których decyzje nie wymieniają: „zarobaczony, zarobiony” (Mina), „W moim barze” (Qwota), „prochu, pobłogosławionego prochami naszego rodu”, „Pilnuj swojego szczeniaczka”. |
| Zachód → wschód (`…OldTown_CloseGauge_OfficeUndone_INSIDER_2`) | **utrzymać** | Zadania (`Q_D_4_FloatingCity_UpperGauges`) i druga, symetryczna kwestia (`…Office_CloseGauge_OldTownUndone_INSIDER_2`, „na zachód” do Fabryki) potwierdzają układ Fabryka NW, Dzielnica Biur NE. Wewnętrzne nazwy stref (`LeftSuburb`, `LeftCity`) tego nie rozstrzygają, więc trzeba sprawdzić na mapie. |
| „czterech par” filarów | **utrzymać** | Orella wylicza 8 filarów (`…BreakFail1_ORELLA_6`). |
| „ma ikrę” / „skończy z flakami na wierzchu” | **utrzymać** | Gra słów jest oddana częściowo, bo riposta nawiązuje do flaków, nie do ikry. Lepszego wariantu, który zachowuje oba znaczenia, nie znalazłem. |
| Liczebniki przy {0} | **utrzymać** | Wszystkie `R_C_*` sprawdzone, formy zawsze się zgadzają. |

## Do rozmowy

1. **Skala wulgaryzmów, w obie strony.** EDITORIAL i PITFALLS każą trzymać siłę oryginału.
   - Osłabione:
     - „Don't fuck with me” → „Nie pogrywaj ze mną” (`D_K_Herman_Undone_LAIKA_3`, `D_4_FloatingCity_Wastelands_Walkie_LAIKA_4`). Rekomendacja dla sceny z Hermanem: „Nie pierdol. Wiem, że to ty.” Przy Shazie „Nie pogrywaj” może zostać; RU też łagodzi („Не нарывайся”).
     - „If you fuck me over…” → „wykiwasz” (`D_B_ShazaF1_LAIKA_1`). Wariant: „wydymasz”.
   - Wzmocnione:
     - „bullshitting me” → „robi mnie w chuja” (`Q_D_F_DaughterDies_DESC`). Wariant: „wciska mi kit… a to jej własna głowa wciskała kit jej”. Zysk: bliżej EN. Koszt: mniej soczyście.
     - „bastards” → „skurwysyny” (`D_4_FloatingCity_Briefing_LAIKA_8` „Wszystkie Ptaki to skurwysyny”, `…MeetingInsider_Intro_LAIKA_5`, `D_S_SacredPlace_Undone2_LAIKA_1`). Przy LAIKA_8 w EN jest też nawiązanie do ACAB. Rekomendacja: zostawić, bo pasuje do rejestru Laiki, ale to decyzja użytkownika.
   - `D_F_PuppysBirth_Labor_02_MAYA_5` „PUSH, YOU PUSSY!” → „PRZYJ, CIOTO!”. „Ciota” to homofobiczna obelga wobec mężczyzn, wykrzyczana do rodzącej. RU ma „СЛАБАЧКА”, ES „NENAZA”. Rekomendacja: „PRZYJ, CIPO!”, bo oddaje oba znaczenia „pussy” (mięczak i genitalia), w tej samej sile. Łagodniejszy wariant: „PRZYJ, MIĘCZAKU!”.
2. **Tytuł zadania „Closure” → „Zamknięcie”** (`Q_D_S_PoochiesCorpse_NAME`). Wiąże się z błędami 16–17. Rekomendacja: „Pożegnanie”. Wariant: „Domknięcie”. RU ma „Отпуская прошлое”, ES „Cierre”.
3. **Wieniec czy wianek.** Laika i Puppy w `D_S_Flower_*` mówią „wieniec (honorowy)”. Zadania (`Q_D_S_Flower_DESC`, `…GiveToPuppy`) i `D_B_Puppy_A1_PUPPY_1` mają „wianek”, czyli coś na głowę, nie na pogrzeb. Rekomendacja: wszędzie „wieniec”. W ustach Puppy „wianek” da się obronić jako dziecięce słowo, ale w zadaniach już nie.
4. **Wołacz „Hildo” u Laiki.** Rekomendacja: zmienić na „Hilda”, zgodnie z decyzją o mianowniku, i dopisać w biblii wyjątek dla wołaczy innych postaci (Hilda „Laiko”, Maya „Avo”).
5. **Sklepikarze na stacjach, W02/W04/W06** (*brak kontekstu*, sprzeczność w źródle). Kally w PL jest kobietą (`D_A_Musicians_GuitarAndGlasses_Item`, RU potwierdza), ale Dally mówi „Mam dwóch braci” (`D_B_Shopkeeper_Gas_W04_Default3`). Rekomendacja: „Mam dwoje rodzeństwa, wiesz? Ale nigdy byś ich nie poznała…”. Usuwa sprzeczność bez zgadywania. „Dwoje z nich to kretyni” u Tally już jest neutralne.
6. **Nazwa strefy napisów** `ZN_Credits_NAME` „Tam, Gdzie Mówimy, Kto” brzmi urwanie. Warianty: „Tam, Gdzie Mówimy, Kto Jest Kim” albo, za RU („Где Мы Называем Имена”), „Tam, Gdzie Wymieniamy Imiona”.
7. **Kalki i drobna idiomatyczność** (kolejność według wagi):
   - `D_S_DyingBird_Briefing_DYINGBIRD_4` „Uczciwie.” → „Należy mi się.” (ES „Me lo merezco”)
   - `D_4_FloatingCity_Tunnel_BeforeBoss_MAYA_2` „Puppy cała płonie.” → „Puppy jest cała rozpalona.” (RU „сильный жар”; w scenie z ogniem da się to przeczytać dosłownie)
   - `D_F_YoungLaika_PostFlashback_LAIKA_2` „Bawi się ze mną?” → „Pogrywa sobie ze mną?”
   - `D_B_Gunlady_BeforeKidnap2_GUNLADY_1` „Przez nią jesteś…” → „Dzięki niej jesteś…”
   - `D_S_PoochiesCorpse_TalkToShaza_SHAZA_1` „A w innych wiadomościach” → „A poza tym”
   - `D_4_FloatingCity_MainGauge_CompleteGoal_INSIDER_4` „Zgaduję tylko, że…” → „Mogę się tylko domyślać, że…”
   - `D_S_NightmaresThree_Briefing_CAREY_4` „Nie może utrzymać kiszek!” → „Nie panuje nad kiszkami!”
   - `D_A_Musicians_Complete_FLUTE_2` „nam się zejść z powrotem” → „nam się znów zejść”
   - `D_S_YoungLaika_Eat2_MAYA_1` „na pewno cię różne miejsca zawiezie” → „na pewno zawiezie cię w różne miejsca”
   - `D_A_GiftsPuppy_ToyAnimal_LAIKA_9` „I rozedrze ci to serce.” → „I to rozedrze ci serce.”
   - `D_K_Herman_Undone_2_LAIKA_7` „To ty przetrwasz.” → „W takim razie przeżyjesz.”
   - `D_A_Statues_Undone` „ślubów mojego prapradziadka” → „przysięgi mojego prapradziadka”
   - `D_S_GhostRevenge_Complete_LAIKA_5` „Na rzecz sprawy.” → „Dla sprawy.”
   - `D_A_Blackjack_2C` „Masz to coś, nieznajoma?” → „Masz to, czego trzeba, nieznajoma?”
   - `Q_D_S_TutorialDash_DESC` „Tylko to przychodzi mi do głowy jako zdroworozsądkowe.” → „To jedyna rozsądna rzecz, jaka przychodzi mi do głowy.”
   - `Q_D_S_Tombstone_DESC` „kto zajmie po mnie moje miejsce” → „kto zajmie po mnie miejsce” (oraz „Matka” małą literą)
   - `D_A_GiftsPuppy_BookMother_BeforeKidnapping_PUPPY_2` „Największa twarda suka” → „Najtwardsza suka”
   - `D_A_MayasHouse_Bike_Rest_LAIKA_1` „kiedy dostałam pierwszej krwi” → „kiedy pierwszy raz zaczęłam krwawić” (tak samo `D_F_PuppysBirth_Briefing_MAYA_2`)
8. **Spójność form UI (drobne):**
   - `UI_TUT_BOAT_NAME` „STERUJ ŁODZIĄ” to tryb rozkazujący, podczas gdy pozostałe tytuły samouczków są rzeczownikami (HAMOWANIE, BALANS). Wariant „ŁÓDŹ”, bo „STEROWANIE ŁODZIĄ” ma 17 zn. przy limicie 16.
   - `Q_D_S_SacredPlace_NAME` „Strząsnąć martwe liście” to jedyny tytuł w bezokoliczniku. Wariant: „Strząśnij martwe liście”.
9. **Gus Gardziel** (`I_ALFREDO_COMIC_NAME`, Alfredo). „Gutsy” znaczy „śmiały” (RU „Отважный Гас”), a „gardziel” to gardło, więc sens przepada, choć aliteracja G–G zostaje. Rekomendacja: zostawić, chyba że użytkownik woli „Gusa Śmiałka”.
10. **`D_B_Chief_A2_LAIKA_1`** „mogłybyśmy ich uratować” (Laika i Starsza, ale kontekstem jest cała wioska). Tuż wcześniej Starsza mówi „mogliśmy” (`D_B_Chief_A1_CHIEF_1`). Wariant: „moglibyśmy”, dla spójności.

## Do sprawdzenia w grze

1. **Nazwy miejsc na planszy wejścia i na mapie:** „Tam, Gdzie Spoczywają Przodkowie” (32 zn.) i „Tam, Gdzie Warczą Nasze Motory” (30 zn.). Czy mieszczą się w pasku, nie łamią się i nie nachodzą na grafikę?
2. **Ustawienia:** „SYNCHRONIZACJA PIONOWA” (22 zn.), „SPOWOLNIENIE ROZMÓW”, „CZUŁOŚĆ MOTORU (PAD)”, „ZASTOSUJ” (8 zn., limit 8). Trzeba też ocenić, czy „SPOWOLNIENIE ROZMÓW” sugeruje spowolnienie czasu podczas rozmów przez krótkofalówkę, czy samych rozmów.
3. **Glify spoza podstawowych polskich liter:** pauza „—” (`D_S_Prophecy_Complete_LAIKA_3`, `D_4_FloatingCity_Boss_Barks10`, opisy zadań `Q_D_F_PuppysBirth_DESC`, `Q_D_S_Seashell_DESC`, `Q_D_S_Tombstone_DESC`), „º” w „360º/120º/170º”, „Í” w BEÍCOLI, symbole ♊♋… Antropologa, wielokropek „…”. Vertical sprawdził „ ” i ąęłśżźćńó, tych nie.
4. **Długie dymki krótkofalówki podczas jazdy:** `D_B_Gunlady_BeforeKidnap4` (119 zn.), `D_B_Molly_DuringKidnap` (114), `D_B_Molly_AfterKidnap2` (90), `D_S_TutorialHook_Briefing_Undone1_ANARCHIST_2` (78). Czy da się je przeczytać przy domyślnym „SPOWOLNIENIU ROZMÓW”?
5. **Samouczki z ikonami:** `UI_TUT_CANDLES_DESC` (114 zn. przy limicie 50, jedyny PL dłuższy od EN), `UI_TUT_HOOK_COLUMN_DESC_*`, `UI_TUT_DASH_DESC_*`, `UI_TUT_WHEELIE_DESC_*`. Czy tekst mieści się w ramce razem z ikonami przycisków?
6. **Komunikat o worku** (`UI_LOG_SACK_DESTROYED_MESSAGE`) po ewentualnej zmianie na „Najstarszy worek stracony”: czy mieści się w logu (limit 20).
7. **Latające Miasto:** czy z Fabryki do Dzielnicy Biur rzeczywiście jedzie się na wschód (uzasadnienie odstępstwa przy `…OfficeUndone_INSIDER_2`).
8. **Rozmowy z Carey:** czy przedrzeźnianie („Pribiwiłiś gitiwić łidigi isti?”) jest czytelne jako przedrzeźnianie, a nie jako błąd fontu lub tekstu.
9. **Osiągnięcia w rodzaju żeńskim** (Hazardzistka, Zabójczyni, Psychopatka, Graczka, Kucharka): jak wyglądają w grze, o ile gra je pokazuje. Nakładka GOG/Steam bierze teksty od wydawcy, więc tam i tak zostanie angielski.

## Stan po integracji (agent prowadzący, 2026-09-24)

- **Wprowadzone:** wszystkie 15 błędów z tabeli A (w nr 3 zamiast proponowanego
  „TEN ZŁOCZYŃCY” — „NIŻ KAPELUSZ ZŁOCZYŃCY”) i wszystkie 11 z tabeli B (13 kluczy).
- **Wprowadzone z „Do rozmowy” jako poprawki językowe bez zmiany tonu:** pkt 3 (wszędzie
  „wieniec”), pkt 4 („Hilda” w ustach Laiki; wyjątek wołaczy zapisany w biblii), pkt 5
  („dwoje rodzeństwa”), pkt 7 (wszystkie wymienione kalki), pkt 8 („ŁÓDŹ”,
  „Strząśnij martwe liście”), pkt 10 („moglibyśmy”).
- **Czeka na użytkownika (tekst bez zmian):** pkt 1 (skala wulgaryzmów, w tym
  „PRZYJ, CIOTO!”), pkt 2 (tytuł „Zamknięcie”), pkt 6 (nazwa strefy napisów),
  pkt 9 (Gus Gardziel), rodzaj Starszej jako świadoma strata.
- **Ponowna kontrola:** build 0.2.0 przechodzi (klucze, znaczniki), `en-pl-review.json`
  odtworzony z `pl.json`, raport kontrolny: brak=0, tokeny=0, płeć=0.
- **Rozstrzygnięcia użytkownika (2026-09-24):** pkt 1 — „PRZYJ, CIPO!” oraz wzmocnienie tylko
  osłabionych wulgaryzmów (Herman, Shaza ×2); pkt 2 — „Pożegnanie”; pkt 6 — „Tam, Gdzie
  Mówimy, Kto Jest Kim”. Pkt 9 i rodzaj Starszej bez zmian (rekomendacja: zostawić).
