# Rain World — decyzje tłumaczenia (0.2.0)

Pełny tekst podstawki, Downpour i The Watcher: 4913 wpisów. Szczegóły i źródła każdego
terminu są w `translations/bible.yaml`; tu to, co można zakwestionować jednym zdaniem.

## Postacie

- **Patrząca na Księżyc — kobieta, przezwisko „Luna”.** Rosyjski „Смотрящая-на-Луну”, „я устала”;
  angielskie „she” w perłach i czatlogach. Rzeczownik żeński pasuje do postaci lepiej niż „Księżyc”.
  Do gracza: „mały stworku”, „przyjacielu”, „mały archeologu” (wołacze z `NameForPlayer`).
- **Pięć Kamyków — mężczyzna, przezwisko „Kamyk”.** Rosyjski „я занят”, angielskie „he/him”.
  W Downpour ta sama klasa mówi też za Lunę sprzed upadku (kampania Włócznika) — płeć ustalana
  linia po linii z rosyjskiego.
- **Bąk (Spinning Top, The Watcher) — rodzaj męski.** Rosyjski w dialogu 209 „Я провёл”.
- **Echa i starożytni — bez form rodzajowych** („przysiadało się”, „nie udało mi się”), a w przymiotnikach
  rodzaj nijaki za „echem” („przykute do wspomnień”). Angielski nie mówi, kim byli.
- **Gracz — rodzaj męski za rzeczownikiem „ślimakot”** („wróciłeś”, „jesteś głodny”); iteratory mówiące
  o nim jak o zwierzęciu — nijaki za „stworzeniem”.
- **Iteratory o nieustalonej płci — bez form rodzajowych** (GW, HR, UU, WO, EOC, PG, SI, PI, Niezrównana
  Niewinność): „doszły mnie”, „nie wypada mi”. Rosyjski robi tak samo. Męscy według rosyjskiego: SCS, BZN, NGI.
  Dodane po review.
- **Listy starożytnych bez rodzaju**, z wyjątkiem perły 238: autor pisze o sobie „Nine-Leaf, when he comes”
  (parodia skargi na Ea-nasira), więc tam formy męskie.
- **Twórcy w komentarzu Downpour — bez form rodzajowych w pierwszej osobie.** To prawdziwe osoby
  (Andrew, Will, Dakras, Norgad, Screams, Cappin, Slugitar…); płci nie zgadujemy z pseudonimów.
  Stąd „udało mi się”, „moim zamiarem było”, strona bierna. O innych osobach tylko tak, jak mówi
  oryginał („he” o Cappinie, Willu, Screamsie; „they” albo brak zaimka — Minkimaro, Ender, Topicular,
  Andrew, Slugitar, RatRat, Tollycastle, Joar — bez rodzaju).

## Ślimakoty

| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| Survivor | Ocalały | wiki podaje i „Przetrwaniec”, i „Ocalały”; rosyjski „Выживший”. W próbce 0.1.0 był „Przetrwaniec” — zmienione na naturalniejsze | wiki-pl, ru |
| Monk / Hunter | Mnich / Łowca | utarte na polskiej wiki | wiki-pl |
| Gourmand | Smakosz | „indulger of the simpler pleasures” | decyzja |
| Artificer | Pirotechnik | „master of pyrotechnics and explosives”; wiki „Artyficer” to kalka; „Pirotechniczka” odrzucona | użytkownik |
| Rivulet / Spearmaster / Saint | Strumyk / Włócznik / Święty | wiki i rosyjski | wiki-pl, ru |
| Watcher | Obserwator | nazwa dodatku „The Watcher” zostaje po angielsku | wiki-pl |
| slugpup | ślimakocię (w Jolly Co-op „maluch”) | zdrobnienie jak „kocię” | decyzja |

## Terminy

| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| iterator | iterator | wiki ma „Przeliczacz”, ale niekonsekwentnie; rosyjski zostawia „итератор”; perła 20 gra słowami „iterujemy… Iteratory” | ru, użytkownik |
| Sliver of Straw | Drzazga Słomy | postać żeńska („She's quite legendary”); sliverists → drzazgiści | decyzja |
| Seven Red Suns / No Significant Harassment | Siedem Czerwonych Słońc (SCS) / Brak Znaczącego Nękania (BZN) | kody w czatlogach tłumaczone razem z imionami, bo gra koloruje linie po przetłumaczonym kodzie | ru, kod gry |
| Big Sis Moon | Starsza Siostra Luna (SSL) | jak wyżej | ru |
| passage | przeprawa | „przejście” myliłoby się z przejściami między pokojami | decyzja |
| Expedition / perk / burden | Wyprawa / atut / brzemię | — | decyzja |
| Scavenger | zbieracz | zbierają i handlują; wiki „Grabiarze” | decyzja |
| Void Sea / Void Fluid | Morze Pustki / Płyn Pustki | — | ru |
| ripple / warp (Watcher) | fala / przeniesienie | rosyjski „рябь” | decyzja |
| Lizard / Vulture | jaszczur / sęp | „jaszczurka” byłaby za mała | ru |
| Five Pebbsi | Pięć Kamyksi | gra słów z Pepsi; grafika reklamy w grze zostaje po angielsku | decyzja |
| Joke Rifle | żartostrzelba | primaaprilisowy żart twórców | decyzja |

Nazwy regionów, podregionów i stworzeń: pełna lista w biblii i `en-pl-review.json`
(np. Obrzeża, Korony Kominów, Szeregi Farm, Zewnętrzne Rubieże, Rurowisko; skolopendra,
muchoperz, kluskomucha, spadoskorek, Tatko Długonogi).

## Okazje wykorzystane

- „Five Pebbsi” → „Pięć Kamyksi” — polska gra słów z Pepsi.
- Batfly/batnip → muchoperz/muchomiętka (catnip → kocimiętka).
- Chatlogowe nazwy grup: [DRZAZGAOCEANU], [AZYLNATRZECHKLEJNOTACH], [KLATKAOMENU] — sklejone jak w oryginale.

## Świadome odstępstwa od oryginału

- **Andrew o Pirotechniku mówi „she” i „her children”.** Imię zostaje „Pirotechnik”, bo tak nazywa
  postać cała gra (rosyjski też ma męskie „Техник”), a w tych kilku liniach komentarza zaimki idą
  przez „ta postać”/„jej”, a „matczyna miłość” zostaje.
- **Rozwinięcia skrótów regionów** (komentarz przy Lunie: „(OE) Outer Expanse…”) zostają po angielsku,
  bo tłumaczą angielskie skróty z plików gry.
- **Dwukropki** w statystykach („Czas:”, „Śmierci:”) bez spacji przed znakiem, wbrew angielskiemu „Time :”.
- **Wielkie litery w nazwach własnych** (imiona ech, nazwy komnat Kamyka: „Magistrala Systemów Ogólnych”)
  zostają jak w oryginale — działają jak imiona i tytuły, nie opisy.
- **Dopisek ` : -30` w czterech kwestiach Luny (138/139)** zostaje w polskim tekście: to instrukcja, przez którą
  gra tych linii nie wyświetla — tak samo w angielskim.
- **Klucze z końcówką `-ru2`** (odmiana „rund” dla liczb 2–4 w arenie) przetłumaczone, choć gra
  najpewniej używa ich tylko po rosyjsku; podstawowy wpis ma dopełniacz („RUND NA SESJĘ”).
- **„Luna” to też nazwa miasta w komentarzu.** Gdzie oba znaczenia stoją obok siebie, dopowiadamy
  „miasto Luna”. Rosyjski ma tę samą kolizję.

## Mniej pewne (sprawdź w grze)

1. **Czatlogi i transmisje (Downpour).** Tu plugin przepuszcza otwarty tekst przez deszyfrowanie gry.
   Jeśli zamiast polskiego tekstu zobaczysz krzaczki albo pustą perłę — to ten mechanizm.
   Najprościej: w kampanii Włócznika antena nadawcza albo perła z czatlogiem przyniesiona Lunie.
2. **Komentarz twórców** (jeśli masz odblokowany): czy linie się mieszczą. Polskie zdania są
   o 20–40% dłuższe, więc dziesięć najdłuższych kwestii bez łamania w oryginale dostało ręczne
   `<LINE>`; najdłuższy wiersz ma teraz ok. 150 znaków, tyle co angielski. Imiona twórców przed
   dwukropkiem powinny zostać.
3. **Rozmowa z Luną i odczyt perły** w dowolnej kampanii z postępem — kolory mówiących, łamanie
   wierszy, polskie litery w dymkach.
4. **Długie etykiety w Remiksie i Wyprawach**, np. „Ochrona przedmiotów przed rybami odrzutowymi”,
   „Ukryj odliczanie deszczu w bezpiecznych miejscach”, „Naciśnij POTWIERDŹ, aby wejść w interakcję”.
5. **Arena i piaskownica** — nazwy stworzeń w liczbie mnogiej i pojedynczej, „RUND NA SESJĘ”.
6. **Włócznik, rozmowa z Luną (perły 138/139):** linie „Jest...” i „Jeśli on...” nie powinny się pojawić, jak w EN.
7. **Opcje → tła, kopie zapasowe:** „WSTECZ” i „POPRZEDNIA” obok siebie — czy „POPRZEDNIA” się mieści.

## Review po fullu

Niezależny przegląd całości (4914/4914 wpisów): `docs/localization-review.md`. Wprowadzono 98 poprawek:
cztery kwestie Luny, które bez dopisku ` : -30` pokazałyby się graczowi, dwa „WSTECZ” obok siebie w menu,
pomyloną Milczącą Konstrukcję, kilka zdań o odwróconym sensie, rodzaj iteratorów i twórców bez zaimka
w oryginale oraz redakcję głosów Luny, ech i komentarza. Przegląd językowy nie zastępuje testu w grze.

## Rozstrzygnięte z użytkownikiem

- **Pirotechnik** zostaje (2026-09-24, „wszystko git”).
- **iterator** zostaje, „Przeliczacz” odrzucony (2026-09-24, „idziemy w iterator”).

## Raport kontrolny

`work/l10n-report.md` po poprawkach: 0 braków, 0 tokenów, 0 płci i adresata według biblii.
Terminy: 85 → 9 (biblia zaktualizowana; zostały fałszywe trafienia jak „rot” = gnić,
„Basilisk Lizard” = Bazyliszek, „challenge” jako „poziom trudności”). Spójność 31 — zamierzone pary liczby pojedynczej i mnogiej nazw stworzeń
i odmiany `-ru2`. Angielskie resztki 44 — emotikony twórców, „Hmmm…”, skróty, nazwy własne.
Długość 34 — do obejrzenia w grze (punkt 4). Typografia 1 — nagłówek czatlogu w formacie gry „[ZAPIS TRANSMISJI : …]”;
w statystykach dwukropki poprawione, dopisek „ : -30” wyciszony w biblii.
