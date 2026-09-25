# Rain World — przegląd lokalizacji (review po fullu 0.2.0)

## Zakres

- **Data:** 2026-09-24. Przegląd zrobił osobny agent w świeżym kontekście, tylko do odczytu.
  Przerwał go raz limit API, po wznowieniu doczytał całość.
- **Wejście:** `translations/en-pl-review.json` (SHA-256 `e010aec7…acbac94`) i `translations/pl.json`
  (SHA-256 `580257ba…1d06b2a`) — po 4914 wpisów, zgodne klucze i treść. Różnica wobec 4913
  w `game.yaml` to dopisany wpis `str:POLISH`.
- **Przeczytane:** 4914/4914, w 25 partiach po 200 wpisów w kolejności pliku: 2474 `str:`
  (UI, Remix, Wyprawy, Jolly, opisy, krótkie kwestie iteratorów) i 2440 `dlg:` (perły, rozmowy,
  echa, czatlogi, transmisje, komentarz twórców, Watcher 200–242).
- **Przebiegi:** wierność (sens, negacje, liczby, rodzaj, znaczniki), redakcja (sceny czytane po polsku),
  ocena decyzji. Wątpliwe miejsca porównane z `work/ref-rus.json`, `work/ldstr.tsv`, IL gry
  (`Conversation.LoadEventsFromFile`, `OracleBehavior.AlreadyDiscussedItemString`,
  `CreatureJokeDialog`) i `world/*/displayname.txt`.
- **Znaczniki:** nic nie zginęło; różnice to tylko ręcznie dodane `<LINE>`.
- **Luki:** gra nie była uruchamiana (szerokości pól, czas wyświetlania do testu); rosyjski porównany
  tylko w miejscach wątpliwych; mówiący w części kwestii Watchera 214–221 nieustalony.

## Błędy pewne — wszystkie wprowadzone

| Klucz | Problem | Poprawka |
| --- | --- | --- |
| `dlg:138.txt#11`, `#15`, `dlg:139.txt#7`, `#11` | brak dopisku ` : -30`; gra pomija takie linie w EN, a bez dopisku pokazałaby polską | dopisek przywrócony |
| `str:PREVIOUS` | „WSTECZ” obok „WSTECZ” (BACK) w trzech menu | POPRZEDNIA |
| `dlg:uw_d01-saint.txt#3`, `dlg:ms_x02-white.txt#5` | CL przetłumaczone jako „Samotne Wieże” | Milcząca Konstrukcja |
| `str:How did you fit them inside here anyhow?` | „ich” o jednym stworzeniu | „go” |
| `str:Clear a total of ## challenges to unlock.` | „2 wyzwań” | „ukończ łącznie wyzwania: ##” |
| `str:Hang on Mom` | niegramatyczne „Uwieszony mamy” | Trzymaj się mamy |
| `str:Ascended`, `str:Ascension` | „Wniebowstąpienie” wbrew biblii | Wzniesienie |
| `dlg:14.txt#7`, `dlg:15.txt#13`, `dlg:240.txt#9`, `dlg:132-artificer.txt#15` | składnia i aspekt | poprawione |
| `dlg:47.txt#5` | nadzorcy w formie niemęskoosobowej | „byli bardzo uparci” |
| `dlg:100.txt#3`, `dlg:140.txt#5` | sens odwrócony („zbyt zdesperowany, by się wyrwać”) | „w desperackiej chęci wyrwania się… nie zachowasz umiaru” |
| `dlg:105.txt#7` | „lotne” (kalka volatile) | niestabilne |
| `dlg:lp_6.txt#5` | pytanie HR nie domyka pytania PG | „Kiedy odkryjemy…? Czy kiedy…” |
| `dlg:7-artificer.txt#1` | „przyjaciółki” bez oparcia; to SCS | bliskiego przyjaciela |
| `dlg:42.txt#9`, `dlg:42-artificer.txt#5` | formy męskie w liście starożytnego | bez rodzaju |
| czatlogi i transmisje: `21.txt#5`, `22.txt#13`, `22-spear.txt#13`, `43.txt#9`, `chatlog_sb0.txt#7`, `132.txt#15`, `lp_6.txt#9`, 12 linii `chatlog_cc0/hi0/gw1/si3/si4/si5` | rodzaj iteratorów, których płci nie podaje ani EN, ani rosyjski; NN raz męska, raz żeńska | bez rodzaju |
| `dlg:dm_i10-white.txt#19`, `#21`, `dlg:hi_a19-white.txt#11` | Topicular i Ender („they”) z formami męskimi | bez rodzaju |

## Propozycje redakcyjne

**Wprowadzone** (lepsze i zgodne z przyjętymi zasadami, bez zmiany decyzji):

- **Twórcy bez zaimka w EN** (Andrew, Slugitar, RatRat, Tollycastle, Joar) w 7 liniach przepisani bez rodzaju,
  zgodnie z regułą biblii. `lf_j01-white.txt#13` inaczej niż w propozycji: „którymi zajmuje się aktualizacja 1.5
  autorstwa Joara”, bo proponowane „rozwiązywał” też ma rodzaj.
- **UI:** „Widoczne nazwy/miniatury poziomów” (było „Pokazuję…”), „Limit wybuchów Pirotechnika”,
  „Postęp przepraw bez Ocalałego”, „Kamera (nie) przełącza graczy”, „Zabij/Wznieś wszystkie: ##”, opis Wyprawy,
  oba opisy Łowcy.
- **Iteratory:** „Lepiej stąd uciekaj”, „Pozwól, że będę mówić dalej…”, „dawno odeszłych stwórców” (odeszli, nie umarli),
  „Przyprowadziłeś”, „Może skosztujesz próbki?”, „Dawno spełniliśmy swoje zadanie” (było „przeżyliśmy swój cel”),
  „Słońca… on mi ufał”, „sąsiadki i zwierzchniczki”, „Nic mi to nie mówi”, „z wgranej mi wiedzy”, „świecidełek”.
- **Echa:** `4.txt#3`, `1.txt#7`, `1-saint.txt#3`, `6-saint.txt#7` — płynniej, dalej bez rodzaju.
- **Komentarz:** `hi_a17#17`, `hr_a14#1`, `hi_c14#1`, `gw_c05-inv#5/#7`, `uw_f01-rivulet#3`, `dm_u07#5`, `si_a17-saint#1`,
  `ss_d02#5`; „mądry Polak po szkodzie” w ustach Willa → „łatwo być mądrym po fakcie”;
  `lm_legentrancearty#7` — tam EN ma „they”, więc zwykły „Pirotechnik… trafił”.
- **Watcher 216:** „A... SELF.” → „Jakaś... JAŹŃ.” (było „JA... SAM.”, co dodawało rodzaj i zmieniało sens),
  „an OTHER.” → „ktoś INNY.”.

**Rozstrzygnięte bez zmiany:**

- **Perły 237/238** (list i zwój starożytnych, formy męskie): w 238 autor pisze o sobie „Nine-Leaf, when he comes”
  — to parodia skargi na Ea-nasira. Formy męskie zostają, wyjątek zapisany w biblii (`starozytni-dokumenty`).
- **„Templariusz zbieraczy” / „Uczeń zbieraczy”** zostają: krótkie nazwy stworzeń w arenie, sens czytelny.
- **Twórcy zwracają się do gracza w formach męskich** („Skoczyłeś sam…”) — konsekwencja decyzji o graczu, zostaje.
- **„starożytni” / „Starożytni”** — mieszana pisownia zostaje: wielka litera tam, gdzie twórcy piszą „Ancients”
  jak nazwę własną.

## Decyzje

| Decyzja | Werdykt |
| --- | --- |
| Luna żeńska, Kamyk męski, Bąk męski | utrzymać |
| Echa i starożytni bez rodzaju | utrzymać; list 42 dociągnięty, 238 wyjątkiem z tekstu |
| Gracz męski za „ślimakotem” | utrzymać |
| Twórcy bez rodzaju w 1. osobie | utrzymać; 3. osoba dociągnięta do reguły |
| Nieustaleni iteratorzy bez rodzaju | **nowa decyzja**, wprowadzona (jak w rosyjskim) |
| Pirotechnik | utrzymać (użytkownik zaakceptował) |
| iterator, nie Przeliczacz | utrzymać (użytkownik: „idziemy w iterator”); dodatkowy argument: gra słów w perle 20 |
| Ocalały, przeprawa, zbieracz, fala, przeniesienie, Drzazga Słomy | utrzymać |
| Wzniesienie | utrzymać; poprawione 2 odstępstwa |
| Kody mówiących w czatlogach tłumaczone | utrzymać |

## Stan po poprawkach

98 wpisów zmienionych, build i `en-pl-review.json` odświeżone, paczka przebudowana i zainstalowana.
Raport kontrolny: 0 braków, 0 tokenów, 0 zgłoszeń rodzaju mówiącego; typografia 1 (nagłówek czatlogu
w formacie gry). Dopisek ` : -30` sprawdzony w zbudowanym `138.txt`.

## Do sprawdzenia w grze

1. **Włócznik, rozmowa z Luną (138/139):** linie „Jest...” i „Jeśli on...” nie powinny się pojawić, tak jak w EN.
2. **Opcje → tła, kopie zapasowe, arena:** przyciski „WSTECZ” i „POPRZEDNIA” obok siebie, szerokość „POPRZEDNIA”.
3. **Jolly Co-op:** „Kamera (nie) przełącza graczy” — czy się mieści.
4. **Czatlogi i transmisje:** kolory mówiących, także nieprzetłumaczonych kodów (EOC, NGI, HR, HF, UU).
5. **Luna, wołacze:** „mały archeologu” na początku zdania, „Nie! Mały stworku... zjadłeś... mnie!”.
6. **„Trzymaj się mamy”** — gdzie gra wyświetla tę nazwę.
7. **Odblokowanie wyzwań w arenie:** „Aby odblokować, ukończ łącznie wyzwania: ##”.
