# Hyper Light Drifter — technika i stan prac

Stan: 2026-09-23. Instalacja GOG: `C:\Games\Hyper Light Drifter`
(build GOG 52291896322577314; wersja wydania do odczytania w GOG Galaxy).

## Stan

Pełne tłumaczenie 0.1.0: wszystkie 126 wpisów (110 w `MenuText.txt`, 16 w `Phrases.txt`).
Zbudowane, zweryfikowane z plików, zainstalowane do testu z kopią oryginałów
w `backups/hyper-light-drifter/`. Paczka łatki: 83 KB (łatka exe 747 B).
**Test w grze czeka** — to pierwszy test tej metody (litery w nowej sekcji exe).
Niezależny przegląd tekstów (2026-09-25): `docs/localization-review.md`; dwie drobne
poprawki w `en-pl-review.json`, jeszcze nie w paczce 0.1.0.

Następny krok: test według listy w `docs/translation-decisions.md`, potem okładka
(`tools/keyart.py --game hyper-light-drifter`) i numer wersji z GOG Galaxy do `game.yaml`.

## Spolszczenia w sieci

- Steam: 6 języków (EN, FR, IT, DE, ES, JA), bez polskiego —
  <https://store.steampowered.com/app/257850/Hyper_Light_Drifter/>. Pliki gry mają
  jeszcze rosyjski, którego sklep nie wymienia.
- Wyszukiwarka zwraca listę „Polish” przy grze, ale to lista języków interfejsu Steama,
  nie gry.
- spolszczeniepl.com: strona z „RePackiem” gry (`ENG/Polski` w tytule) — nie paczka
  spolszczenia; strona nie otwiera się poprawnie (błąd certyfikatu).
- Nie znaleziono dostępnego polskiego spolszczenia ani fanowskich narzędzi do tej gry.
  Poradniki Steam o „języku” gry dotyczą wymyślonego alfabetu glifów, nie lokalizacji.

## Silnik i pliki

GameMaker Studio 1.4, bytecode 16, kod **YYC** (natywny x86, 32 bity, ASLR).
`HyperLightDrifter.exe` (628 812 800 B) zawiera cały `data.win` jako blok FORM
w sekcji `.data` (plik 0x1017620, RVA 0x1019a20), a runner czyta go wprost z obrazu
exe w pamięci: kod wpisuje adres 0x1419a20 do struktury {wskaźnik, rozmiar}
(`0x1043176`), którą potem dostaje dispatcher chunków (`0x106cf60`).

Teksty są w dwóch zwykłych plikach obok exe:

- `MenuText.txt` (UTF-8 z BOM, CRLF): 110 wpisów `=|KLUCZ|nr`, po nich linie
  `ENG|`, `FRN|`, `SPA|`, `JAP|`, `GER|`, `ITA|`, `RUS|`. Linie bez `|` to komentarze
  autorów o limitach („15 Chars max”); inne języki przekraczają je o kilka znaków.
- `Phrases.txt` (UTF-8 bez BOM, CRLF): 16 podpowiedzi `PHR|KLUCZ|nr` ze znacznikami
  `[BUTTON_*]` i `[spr_*]` (ikony przycisków i sprite'y).

Kody języków i nazwy w wyborze języka są wkompilowane w exe
(`ENG FRN SPA ITA JAP GER RUS` przy 0xfdcc19; `ENGLISH FRANÇAIS ESPAÑOL ITALIANO
JAPANESE DEUTSCH РУССКИЙ` przy 0xff1611). Ósmego języka nie ma gdzie dopisać bez
przepisywania kodu, więc **polski zajmuje miejsce włoskiego**: łaciński slot z tym samym
fontem co angielski. Rosyjski odpada, bo `f_cyr` w zakresie Latin-1 rysuje cyrylicę
(„ó” wychodzi jako „у”).

Reszta exe to napisy debugowe, lista klawiszy i nazwy kontrolerów; widoczny tekst gry
jest w całości w dwóch plikach .txt. `Credits.txt` i `BackerNames.txt` (napisy końcowe,
nazwiska) zostają bez zmian.

## Fonty

Chunk FONT ma 8 fontów. Łacina idzie przez `f_uni` („Visitor TT2 BRK”, 9 pt, 1072 glify,
atlas 512×256 na stronie tekstur 10 w (2, 1030)). Font to piksele 5×7 z rzędami 0–1 na
akcent; małe litery to wersaliki, choć nie zawsze te same (`n` ≠ `N`).

Wszystkie 18 polskich liter ma wpisy glifów (5×7, przesunięcie 6), ale ich pola w atlasie
są puste — GameMaker wyrenderował zakres znaków, których krój nie miał. „Ó/ó” są
prawdziwe (Latin-1). To samo w `f_cyr` i `f_jp` (tam pola 0×0); `f_arial` polskich
wpisów nie ma w ogóle.

`tools/fonts.py` składa 16 liter z liter samej gry: kreska = „Ó” − „O” (sprawdzane),
kropka = jeden piksel w rzędzie 1, ogonek = dwa piksele w rzędach 7–8 jak cedylla „Ç”
(też wysokość 9), Ł = pień przesunięty do kolumny 1 i skos przez pień.
Podgląd: `dist/font-preview.png`.

## Metoda

Pluginu nie da się zrobić: YYC to natywny kod bez runtime'u do wpięcia (jak Katana ZERO).
Dostarczamy **łatki różnicowe** trzech plików (`tools/patch.py`).

Teksty: linie `ITA|` niosą polski (albo angielski, gdy brak tłumaczenia); reszta pliku
bajt w bajt bez zmian.

Exe (`tools/build.py`):

1. „ITALIANO” → „POLSKI” w miejscu (dopełnione zerami).
2. 16 glifów `f_uni` dostaje nowe pola w pustym pasie strony tekstur 10 (od rzędu 1424;
   zawartość strony kończy się na 1418, wszystkie TPAG tej strony kończą się na 1418).
   Zmieniane w miejscu: x, y (względem prostokąta fontu — wskazują poza niego, na tę samą
   stronę) i wysokość (9 dla liter z ogonkiem).
3. Nowy PNG strony 10 (`tools/pngsplice.py`): oryginalny strumień deflate skopiowany
   bit w bit do ostatniego symbolu przed rzędem 1424, kod końca bloku z tabeli
   oryginalnego bloku, wyzerowany bit „ostatni blok” w jego nagłówku, dalej nowe bloki
   z naszymi rzędami (filtr 0) i nowa suma Adler-32. IDAT pocięte jak w oryginale.
4. Ten PNG leży w nowej sekcji `.ngpl` na końcu exe (dane tylko do odczytu), a wskaźnik
   strony 10 w TXTR wskazuje ją jako przesunięcie od FORM w pamięci. Stary PNG zostaje
   nietknięty. Nagłówek PE: liczba sekcji, SizeOfImage i suma kontrolna (liczona jak
   CheckSumMappedFile; na oryginale daje zapisane 0x257afcc5).

Dlaczego nie w miejscu: blok FORM leży w `.data` przed zmiennymi globalnymi gry, więc nie
może urosnąć, a nowy PNG jest o 136 B dłuższy od miejsca (oryginał koduje 624 puste
rzędy w 2483 B gotową tabelą; nowy blok potrzebuje własnej). Przekodowanie całej strony
mieści się, ale wtedy łatka niesie 113 KB grafiki gry (fonty i sprite'y interfejsu) —
wbrew zasadzie paczek. Obecnie łatka exe to 747 B, nowych bajtów 492.

Handler TXTR (`0x106d2e0`) bierze wskaźnik PNG z wpisu i woła tworzenie tekstury
(`0x1112360`) z jednym argumentem rozmiaru wspólnym dla wszystkich stron — nie liczy
długości PNG z różnicy wskaźników, więc PNG poza FORM nie psuje sąsiednich stron.

Weryfikacja w buildzie: poza zadeklarowanymi miejscami exe bajt w bajt jak oryginał;
chunki FORM bez zmian; wszystkie pozostałe strony wskazują te same PNG; nowy PNG dekoduje
się do zamierzonego obrazu; na stronie zmieniły się tylko piksele polskich liter; glify
inne niż polskie bez zmian; teksty — tylko linie `ITA|`, każda równa PL z `en-pl-review.json`; każdy
znak tłumaczenia ma w `f_uni` niepuste piksele.

**Niepewne, do potwierdzenia w grze:** czy runner nie przycina współrzędnych glifów do
prostokąta fontu i czy loader PNG przyjmuje nasz strumień (standardowy deflate, zlib go
dekoduje). Objaw porażki pierwszego: puste miejsca w miejscu polskich liter;
drugiego: zepsuta strona tekstur 10 (fonty menu).

## Budowanie

```powershell
.venv\Scripts\python.exe games\hyper-light-drifter\tools\review.py --game backups\hyper-light-drifter
.venv\Scripts\python.exe games\hyper-light-drifter\tools\build.py --game backups\hyper-light-drifter
.venv\Scripts\python.exe games\hyper-light-drifter\tools\install.py --game "C:\Games\Hyper Light Drifter"
.venv\Scripts\python.exe games\hyper-light-drifter\tools\install.py --game "C:\Games\Hyper Light Drifter" --restore
.venv\Scripts\python.exe tools\patch.py release --original backups\hyper-light-drifter\HyperLightDrifter.exe --built games\hyper-light-drifter\dist\build\HyperLightDrifter.exe --relative HyperLightDrifter.exe --original backups\hyper-light-drifter\MenuText.txt --built games\hyper-light-drifter\dist\build\MenuText.txt --relative MenuText.txt --original backups\hyper-light-drifter\Phrases.txt --built games\hyper-light-drifter\dist\build\Phrases.txt --relative Phrases.txt --readme games\hyper-light-drifter\docs\INSTALL-patch.txt --out-dir games\hyper-light-drifter\dist --game-name hyper-light-drifter --package-name Hyper-Light-Drifter --version 0.1.0
```

Build przyjmuje tylko oryginały (sumy SHA-256 w `tools/hld.py`).

## Stan testów

- Pliki: build i weryfikacja jak wyżej; łatka odtwarza build bajt w bajt (sprawdza
  `patch.py release`).
- W grze: **jeszcze nie testowane.**

## Pracownia korekty

`translations/structure.yaml` dzieli 126 wpisów na 4 grupy (menu, tryby gry, ustawienia, podpowiedzi) po kluczach.

## Materiał gry

Paczka nie niesie zawartości gry: łatki tekstów to nasze linie, łatka exe to nasze rzędy
PNG (16 liter złożonych z pikseli liter gry i przezroczystość), zmienione pola glifów,
nazwa języka, nagłówki sekcji i sumy kontrolne. Reszta nowego PNG jest kopiowana
z pliku gracza.
