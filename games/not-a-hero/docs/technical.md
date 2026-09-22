# NOT A HERO — ustalenia techniczne

Stan: 2026-09-23. Instalacja GOG: `C:\Games\Not A Hero`.

## Werdykt i stan

Pełne tłumaczenie 0.2.0 zbudowane i zainstalowane do testu (2026-09-23).
Vertical potwierdzony w grze częściowo: polskie litery w dialogach działają.
**Pełne przejście czeka na użytkownika.** Dostarczenie: łatki różnicowe przez
wspólne `tools/patch.py` dla `NOT A HERO.exe` (tylko napisy), `Assets.dat`,
`Src/talk.ini`, `Src/ENDS.ini`, `Src/chat.ini`, `Src/LEVELS/SETTINGS.ini`.
Plugin odpada: natywny runtime Chowdren bez punktu ładowania kodu.
Polski zastępuje angielski; na ekranie wyboru języka flaga brytyjska (obraz 6170)
zastąpiona polską w barwach i ramce flagi francuskiej z gry.

Następny krok: przejście gry według listy w `docs/translation-decisions.md`
i poprawki po screenach. Paczka 0.2.0 leży w `site/public/pobierz/` (gra w „w trakcie”).

## Dostępne tłumaczenia i źródła

Nie znaleziono dostępnego polskiego spolszczenia ani użytecznej paczki/narzędzi
innego tłumaczenia fanowskiego (szukano: spolszczenie, fan translation, tradução,
traduzione, руссификатор; wyniki mylą grę z dodatkiem do Resident Evil 7).

- https://www.gog.com/en/game/not_a_hero — oficjalnie EN, DE, ES, FR, IT; brak PL.
- https://www.clickteam.com/clickteam-blog?p=not-a-hero-made-with-fusion — Clickteam Fusion.
- https://www.mp2.dk/ — wykonawca portu: system lokalizacji i runtime Chowdren.
- https://github.com/snickerbockers/fp-assets — opis kontenera Assets.dat Chowdrena.

## Pliki gry

- `NOT A HERO.exe`: 4 134 400 B, FileVersion `1.0.0.0` (wersja zasobu, nie wydania).
  Chowdren (Clickteam Fusion skompilowany do C++), SDL2, OpenAL. GOG ID 1429698467.
- `Assets.dat`: 32 336 434 B. Tabela 18 831 offsetów (uint32) od 0x92D2; pierwsze
  18 793 to obrazy (nagłówek `<6HI`: w, h, …, długość; RGBA w zlib), 18793 to blok
  fontów, dalej 37 shaderów D3D. `tools/assets.py` dopisuje zmienione obrazy na końcu
  i przestawia tylko ich wpisy w tabeli; reszta pliku zostaje bajt w bajt.
- `Src/talk.ini` (odprawy + pule słów), `Src/ENDS.ini` (omówienia + kopie pul),
  `Src/chat.ini` (kwestie w poziomach, podpowiedzi), `Src/LEVELS/SETTINGS.ini`
  (nazwy, opisy, wyzwania misji). Warianty `-fre/-ger/-ita/-spa` bez pul.
- `menu/<lang>/<n>.png`: 557 grafik menu na język; angielskie leżą w Assets.dat.
  Numer obrazu wynika z kodu EXE (`build.menu_map`).
- Dźwięk: OGG/WAV w `Audio/`, nietknięty.

## Tekst INI

- CP1252 na wejściu; zmienione linie zapisywane kodowaniem gry (`fonts.encode`), reszta bajt w bajt.
  `tools/ini.py` wyznacza wpisy (plik|sekcja|klucz; powtórzona sekcja chat.ini
  `[PASSIVEUP7]` dostaje `~2`, `~3`) i pilnuje silnika: znaczniki `$END$`,
  `$LEVELSELECT$`, `$RESTART$`, `@` bez zmian, liczba `#` i `^` bez zmian
  (tempo i zdarzenia liczone na wiersz: `SPAWNLINE`, `SPAWNWORD`, `BLNEWn`, `PICn`,
  `OBJn`), brak nowych wstawek. Wiersze z samych znaczników zostają nietknięte.
- Pule losowanych słów: każdy znacznik `$NAZWA$` ma w EXE własny kod podmiany,
  więc nie da się dodać nowych pul. Oficjalne FR/DE/IT/ES pule usunęły. Po polsku
  pule przymiotnikowe są przysłówkami, rzeczownikowe i czasownikowe zastąpione
  stałymi słowami (szczegóły w bible.yaml, sekcja `losowanie`).
- `OBJn=1` pokazuje obrazek przedmiotu misji przy kwestii n; `$SUBJECTOBJECT$`
  zostaje (w mianowniku), bo tekst musi pasować do obrazka. W FR `OBJNUM`
  ustala przedmiot na scenie — w trybie angielskim niesprawdzone.
- Atlas 5873 (font okna dialogowego) ma w komórce `*` głowę BunnyLorda — cenzura.

## Fonty

Atlasy 32 × 7 komórek dla bajtów 32–255 (glify Windows-1252). 21 atlasów
(`tools/fonts.py`) dostaje polskie litery złożone z pikseli liter bazowych.
Kodowanie gry (`fonts.encode`): polskie litery na pozycjach CP1250 tam, gdzie
teksty FR/DE/IT/ES ich nie używają; Ś Ł Ń Ę ż przeniesione do wolnych komórek
(0x8A, 0xA4, 0xD0, 0xCB, 0xBE), bo w CP1250 zajmowałyby Œ £ Ñ Ê ¿ — w 0.2.0
przed poprawką wybór języka pokazywał „ESPAŃOL”. ASCII i znaki innych języków
nietknięte (sprawdzone porównaniem komórek). 19 wykryto po konstruktorach w EXE, 5392 i 5873 (okno dialogowe)
po kształcie atlasu po teście nr 1. Atlas 789 ma inny układ — pominięty.
„ i ” (0x84/0x94) oraz – (0x96) są w atlasach, więc tekst używa polskich cudzysłowów.

## Grafiki menu (`build.menu_images`, `tools/menus.py`)

Położenia i kroje zmierzone na oryginałach (`tools/locate.py`, pasma pikseli):
- menu główne (0–87, 277–279, 298–301, 304–345, 480–496), dźwięk (280–297),
  pauza (497–536), tablice samouczka (537–556): font 3017/2088;
- wybór misji DAY 1–21 / SECRET 1–3 (88–276): atlas 3424, odstęp 7, wiersze co
  14 px od y=66; cyfry gra rysuje bez lewego wcięcia, więc numer z położenia;
- karty postaci (355–412): 3424, odstęp 9, opis od y=71 co 13 px, `{…}` = czerwony;
- postęp wyborów (346–354): 3424 + 3037 dla podpisu; pierwszy wiersz 2 px niżej,
  bo akcent wychodziłby poza obrazek;
- duży ekran „DAY 22” (786): 3424 ×2 i ×3, podkreślenie przerysowane;
- reset (336–345), kontroler (1892, 149), „SHOOT HER” (446–476: 3037, odstęp 11).
- Tabliczki EXIT (414–444) zostają: ramka nie mieści WYJŚCIE.
Pułapka: przy odstępie wierszy 10 px (kontroler) górne znaki diakrytyczne
wchodzą w poprzedni wiersz — tam dobrano słowa bez nich.

## Napisy w EXE (`tools/exe.py`)

143 angielskie napisy interfejsu w `.rdata` (0x303318–0x30720c). Kod kopiuje je
ze stałą długością: `push len; push str; call assign` oraz inline `movq`/`mov`
w statycznych inicjalizatorach (sprawdzone capstone), więc polski tekst ma
najwyżej tyle bajtów co angielski; krótszy jest dopełniany spacjami (wokół dla
komunikatów, na końcu dla etykiet z kolumną). Wersje DE/IT/FR/ES są osobnymi
ciągami. Pominięte: debug (ANIM, STATE, SPELL LINE, eksport danych), tytuł.
Ekran wyboru języka: jeden ciąg `ENGLISH
ESPAÑOL…` (0x30683c, 45 bajtów) —
pierwsza pozycja zamieniona na „POLSKI ”.

## Budowanie i test

Build: `.venv\Scripts\python.exe games\not-a-hero\tools\build.py --game "C:\Games\Not A Hero"`
→ `dist/build`, podglądy w `dist/preview`, ZIP w `dist/`. Build sprawdza sumy
oryginałów i odmawia pracy na plikach spolszczonych — gdy tłumaczenie jest
zainstalowane, buduj z `--game backups\not-a-hero`.
Pomocnicze: `tools/extract.py` (zrzut tekstów do `work/`), `tools/review.py`
(odtworzenie `en-pl-review.json` z `pl.json`).

Test lokalny: `tools/install.py --game …` (z `--restore` przywraca). Kopie oryginałów
w `backups/not-a-hero/` i jako `*.przed-spolszczeniem` obok plików gry.

Historia testów w grze:
- nr 1 (2026-09-22): brak polskich liter w dialogach — font okna dialogowego
  (5392/5873) był spoza listy; dodany.
- nr 2 (2026-09-22): polskie litery w dialogach działają. Brak dźwięku okazał się
  błędem gry: świeży `Bin/Profile.ini` nie ma `SFXVOL`/`SOUNDTRACKVOL`, głośność
  startuje od 0 (opisane w instrukcji dla graczy).
- 0.2.0 (2026-09-23): zainstalowane; zweryfikowane poza grą podglądy wszystkich
  grup grafik, rekonstrukcja z łatek i raport kontrolny. Test w grze: czeka.

Materiał gry pozostaje w instalacji użytkownika; repo i paczka nie niosą zasobów gry.
