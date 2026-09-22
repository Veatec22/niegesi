# NOT A HERO — decyzje tłumaczenia (0.2.0)

## Losowane słowa BunnyLorda
- **Pule przymiotników jako przysłówki.** Odprawy i omówienia losują słowa
  z pul (`$AWESOME$`, `$TERRIBLE$`, `$FUCKING$`…). Oficjalne FR/DE/IT/ES pule
  usunęły i mają stałe zdania (pliki gry). Nowych pul dodać się nie da — każdy
  znacznik ma w EXE własny kod. Po polsku pule przymiotnikowe są przysłówkami
  (NIESAMOWICIE, OKROPNIE, TOTALNIE…), bo przysłówek się nie odmienia: „JEST
  $AWESOME$”, „$TERRIBLE$ PODLI PACHOŁKOWIE”, „BĘDZIE $FUCKING$ $TERRIBLE$”.
  Losowość zostaje w ok. 90% miejsc; zdania pisane tak, żeby każda wartość pasowała.
- **Pule rzeczowników i czasowników zastąpione stałymi słowami** (LOCATION,
  MAFIA, NOUN, VERB, PARTS…): wymagałyby przypadków. Stałe wybory są z samej puli
  i trzymają ton (WOMBAT, GALARETOWA MAFIA, KOLOSEUM PIZZY).
- **Przedmiot misji `$SUBJECTOBJECT$` zostaje**, bo gra pokazuje jego obrazek.
  Stoi w mianowniku, w cudzysłowie albo po dwukropku („TOWAR: „TORT””).
- **DISSAPOINTED** jako „JEST MI SMUTNO/PRZYKRO…”, **QUANTITIES** jako
  nieodmienne okoliczniki czasu, **INSULTS** tylko po „CO ZA”.

## Postacie
- **BunnyLord: on; do drużyny „wy”, do agenta „ty”.** Agent to postać wybrana
  przez gracza, także Samantha i Kimmy (pliki gry), więc zwroty do agenta są
  neutralne płciowo („poszło ci”, „twoja rozprawa”, nigdy „zrobiłeś”).
  Dotyczy omówień, rozmów wstępnych i kwestii w poziomach.
- **DOOD → MORDO** — potoczne i neutralne płciowo.
- **Telefony w poziomach są do Steve'a** („MR STEVENSON”, „GOOD BOY”) — formy męskie.

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| THE SHOOTORIAL | STRZELOUCZEK | strzelanie + samouczek | decyzja |
| GLOBAL MEGALORD | MEGALORD ŚWIATA | grafika postępu ma 127 px, GLOBALNY się nie mieści | decyzja |
| BUNNYLORD FUN CLUB | FUN KLUB BUNNYLORDA | zachowuje grę fan/fun | decyzja |
| BUNNYWAGON / BUNNYCOPTER | KRÓLIKOWÓZ / KRÓLIKOPTER | nazwy mówiące | decyzja |
| milkshake | koktajl | krótki, odmienny | decyzja |
| TWEETSIES | ĆWIERKACZ | dziecinne zdrobnienie jak w oryginale | decyzja |
| GET TO THE CHOPPA | DO HELIKOPTERA | utarty cytat z „Predatora” | decyzja |
| TRIAD YAKUZA | TRIADA YAKUZA | pomieszanie gangów to żart oryginału | decyzja |

## Okazje wykorzystane
- Cenzura gwiazdką (K*REWSKO, ZAJ*BIŚCIE) — font dialogów rysuje w miejscu `*`
  głowę BunnyLorda, jak w oryginale.
- Tytuły misji: „SKOK WSZECHMOGĄCY” (Bruce Wszechmogący), „CZARNY PIAR”,
  „POSZŁO Z DYMEM”, „PODANA NA ZIMNO”, „JIPI-KAJ-EJ”; Jesus: „HEJ, ZEUS”.
- Polskie cudzysłowy „” i półpauza — glify są w fontach gry.

## Świadome odstępstwa od oryginału
- **Napisy HUD w EXE mają limit bajtów** angielskiego ciągu; stąd skróty:
  dni tygodnia PON./WT./…, „VODKAVILLE. DZ. 1”, „MENU GŁ.”, „ŚLIZG = BTN”, liczniki
  „ OFIAR”, „ ŻYWI.”, „ ZGON.”, „ ZOST.”.
- **Wyzwania z liczbą** jako „ETYKIETA: @” („EGZEKUCJE: 3”), żeby liczebnik zawsze pasował.
- **Tabliczki EXIT w poziomach zostają** — ramka nie mieści WYJŚCIE, a napis jest powszechny.
- **Polski zajmuje miejsce angielskiego**: na ekranie wyboru języka polska flaga
  i napis POLSKI zamiast brytyjskiej flagi i ENGLISH. Pozostałe języki działają
  bez zmian — polskie litery nie zajmują znaków francuskich ani hiszpańskich. Osobnego szóstego języka gra nie przewiduje (lista języków jest
  w kodzie), a tylko tryb angielski ma losowane słowa. Angielski wraca po przywróceniu.
- **Komunikat o padzie**: „DLA KLAWIATURY / ODŁĄCZ PADA / LUB KLAWISZ K” — wiersze
  co 10 px nie mieszczą górnych znaków diakrytycznych, dobrano słowa bez nich.
- Poziom 3: „BILLBOARD Z KRÓLIKIEM” — nazwa jest też w EXE, limit 24 bajtów.

## Mniej pewne (sprawdź w grze)
1. **Pierwsze odprawy i omówienia z losowaniem** — czy zdania z przysłówkami
   brzmią naturalnie przy różnych wylosowanych słowach (odpraw kilka razy).
2. **Odprawy z przedmiotem misji** (dzień 4, 6, 11, 16): czy „$SUBJECTOBJECT$”
   pokazuje polską nazwę i czy pasuje do obrazka.
3. **HUD w trakcie gry**: KRYTYCZNE!, ŁADUJ!, EGZEKUCJA!, cele („ZABIJ DILERÓW!”),
   licznik „10 S ZOSTAŁO!” — długość i wyśrodkowanie po dopełnieniu spacjami.
4. **Ekran wyników / statystyk** (WYNIKI): wyrównanie kolumn etykiet z EXE.
5. **Wybór misji i karty postaci** — DZIEŃ 1…21, opisy pod imionami.
6. **Wstęp gry** (rozmowa z BunnyLordem przed treningiem) i ekran końcowy
   „DZIEŃ WYBORÓW”, jeśli dostępny.

## Raport kontrolny
`work/l10n-report.md`: brak, tokeny, płeć, terminy, spójność, liczebniki — 0.
Długość: 6 dłuższych kwestii dialogowych (okno samo łamie wiersze) i jedna karta
postaci mieszcząca się w szerokości. Typografia: 3 zamierzone spacje dopełnienia
w EXE. Wielkie litery: 2 fałszywe alarmy (polecenia z klawiszem). Wyjątki
opisane w `translations/bible.yaml` (`ignoruj`).
