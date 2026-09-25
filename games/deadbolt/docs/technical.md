# DEADBOLT — rozpoznanie techniczne

## Stan: pełne 0.2.0 (2026-09-25)

619 wpisów: cała gra (STRG, 8 plików `dia_*.json`, 34 operacje etykiet na grafikach —
menu główne, samouczek, „Wstecz”, teczka misji). Po niezależnym przeglądzie
(`docs/localization-review.md`) i przepisaniu wierszy płomieni na pełny rym
(`work/verses.py`, decyzja w `docs/translation-decisions.md`). `review.py`: 0 problemów,
test pluginu bez gry: OK (460 napisów STRG, wszystkie dialogi przetłumaczone, 253 ms).
Zainstalowane lokalnie z manifestem `backups/deadbolt/plugin/manifest.json`; paczka
w `site/public/pobierz/`. **Pełne przejście w grze czeka na użytkownika** — lista
w `docs/localization-review.md`, „Do sprawdzenia w grze”.

### Historia verticala

170 wpisów próbki (menu pauzy i ustawienia, nowa/wczytana gra, ostrzeżenie,
podpowiedzi w mieszkaniu i przy drzwiach, cele pierwszych misji, podsumowanie,
porady po śmierci, dia_fp misje 0–2). Plugin zbudowany, **sprawdzony testem bez gry**
i zainstalowany lokalnie z manifestem `backups/deadbolt/plugin/manifest.json`.
Menu główne (`sMain`, jedna grafika
960×540) i samouczek (`sTutorial`, „HOLD… THEN…”) to grafiki — w verticalu po angielsku, w 0.2.0 z polskimi etykietami.

Test bez gry (`tools/test_plugin.py`): `tools/harness.cpp` robi to co runner — cały
data.win w buforze ze sterty, potem `Direct3DCreate9` z naszego d3d9.dll — i zrzuca, co
zobaczy gra. Wynik 0.1.0: bufor odnaleziony (jedno trafienie, bajt w bajt), 154 wiersze
STRG + 1 zawężony do kodu, 18 liter w każdym z 3 fontów, strony tekstur przekodowane,
dia_fp.json przekierowany i poprawny, całość 245 ms. Render liter ze zrzuconych struktur:
`work/harness/render.png`. To nie jest dowód renderowania w grze.

**Test 0.1.0 w grze (2026-09-25): nic nie przetłumaczone.** Log: plugin załadowany,
`data.win buffer: 0 exact matches`. Wyszukiwanie sprawdzało tylko pierwsze 64 KB regionu
i wymagało całego pliku bajt w bajt. W grze bufor najpewniej leży głębiej w regionie
menedżera pamięci runnera albo runner zmienia coś przed `Direct3DCreate9`. 0.1.1 przeszukuje
całe zapisywalne regiony, wymaga równości tylko GEN8/STRG/FONT/TXTR/TPAG i loguje każdego
kandydata z listą chunków różniących się od pliku.

**Test 0.1.1 w grze (2026-09-25): działa** — potwierdzone przez użytkownika. Log: jeden
kandydat w regionie prywatnym (bufor 0x30 bajtów za początkiem regionu), różni się od pliku
tylko w **CODE (70 616 bajtów)** — runner przerabia kod jeszcze przed `Direct3DCreate9`
(przebieg wstępny albo `0x52d7a0`). STRG/FONT/TXTR/TPAG nietknięte. 154 + 1 wierszy, 54 litery,
89 napisów dia_fp, 234 ms. Od tej poprawki plugin czyta kod (sloty, operandy `push.s`)
z kopii pliku na dysku i zmienia operand w buforze tylko wtedy, gdy nadal wskazuje ten sam napis.

Budowanie i instalacja:

```powershell
.venv\Scripts\python.exe games\deadbolt\tools\review.py --game "C:\SteamLibrary\steamapps\common\DEADBOLT"
.venv\Scripts\python.exe games\deadbolt\tools\build_plugin.py
.venv\Scripts\python.exe games\deadbolt\tools\test_plugin.py --game "C:\SteamLibrary\steamapps\common\DEADBOLT"
.venv\Scripts\python.exe games\deadbolt\tools\install.py --game "C:\SteamLibrary\steamapps\common\DEADBOLT"
.venv\Scripts\python.exe games\deadbolt\tools\install.py --game "C:\SteamLibrary\steamapps\common\DEADBOLT" --restore
```

Pliki: `plugin/Plugin.cpp` (plugin), `tools/fonts.py` (projekt liter → `notgeese/fonts.txt`,
podgląd `work/font-preview.png`), `tools/strings_usage.py` (gdzie kod używa każdego napisu,
klasyfikacja wyświetlanie/logika, `--dump` jednego wpisu CODE), `tools/review.py`
(en-pl-review.json + kontrola znaczników), `translations/pl.json` (źródło tłumaczeń).

Klucze `pl.json`: `s<indeks>` (napis STRG wszędzie), `s<indeks>@<wpis CODE>` (tylko w tym
wpisie — plugin przestawia operand `push.s` na wolny slot od końca listy STRG), `j:<plik>/<ścieżka>`
(dialog; plugin tłumaczy wartości JSON po tekście, więc powtórzenia dostają to samo).

Ustalenia z verticala:
- Napisy „logiczne” (klucze ini, `asset_get_index`, porównania): 177 tylko-logika,
  52 mieszane; wśród tekstów dla gracza mieszany jest tylko „Controls” (sekcja Prefs.ini
  i pozycja menu pauzy) — dlatego `s222@gml_Object_oPause_Create_0`.
- `global.quest == "Stage cleared"` (oChangeRoom) porównuje z osobnym napisem, którego gra
  nie wyświetla — nie tłumaczyć.
- Interpreter liczy napis przy każdym `push.s` (`0x51a767`): baza + wpis + 4 (pole długości).
- Fonty nie mają „ ” ani półpauzy: cudzysłowy i myślniki proste.
- Doklejane imiona/liczby: forma z dwukropkiem („Zabij: &r&” + imię, „Liczba zgonów: ” + n).
- `fontMedium` ma „Ó”/„É” bez kresek (rasteryzacja) — plugin zastępuje „Ó”.
- fontSmall ma pod glifami tylko 28 wolnych wierszy: komórki co 1 px, do krawędzi prostokąta.

Stan: 2026-09-25. **Werdykt: warto, trudność średnia. Decyzja użytkownika: plugin**
(bez aplikatora `.exe`; do łatki wracamy tylko, jeśli plugin trafi na ścianę).
To analiza plików i disassembly runnera, nie działające spolszczenie. Gry nie
uruchamiano i niczego w niej nie zmieniano.

## Spolszczenia w sieci

- Steam: tylko angielski (API sklepu, appid 394970, `supported_languages`).
- Nie znaleziono dostępnego polskiego spolszczenia. Na forum GrajPoPolsku wyszukiwarka
  zwraca 0 wyników dla „deadbolt”.
  [spolszczeniepl.com](https://spolszczeniepl.com/games/25936-deadbolt.html) to strona
  repacka gry, nie paczka tłumaczenia (nie otwiera się, błąd certyfikatu). Programosy.pl
  podaje samą grę.
- Rosyjski: [ZoG Forum Team 1.2 z 30.03.2019](https://www.playground.ru/deadbolt/file/deadbolt_rusifikator_teksta_1_2_ot_30_03_2019_zog_forum_team-1219830)
  (Rigel — tekst i zasoby, Укушевич — tekstury). Podmienia pliki gry; interfejs
  i dialogi, z teksturami. Potwierdza, że część napisów jest w grafice. Jest też
  starszy przekład DiSTiNCT. Opisów narzędzi nie znaleziono.

## Lokalna instalacja

- Steam: `C:\SteamLibrary\steamapps\common\DEADBOLT`, buildid 22449372.
- `deadbolt_game.exe` 3 832 320 B, FileVersion 1.0.0.87 — standardowy runner GMS 1.4.
  Importuje `d3d9.dll`, `dsound.dll`, `xinput1_3.dll`; `D3DX9_43.dll` leży w katalogu gry.
- `data.win` 4 130 572 B: GEN8 `deadbolt_game` 1.0.0.1749, **bytecode 15, kod VM**
  (CODE 1543 wpisy, VARI/FUNC niepuste) — nie YYC. Kod da się zdekompilować
  (np. UndertaleModTool obsługuje GMS 1.4).
- `deadbolt_map_editor.exe` (64 MB) — osobny edytor map, poza zakresem.

Odtworzenie analizy (tylko odczyt, wyniki w `work/`):

```powershell
.venv\Scripts\python.exe games\deadbolt\tools\inspect_game.py --game "C:\SteamLibrary\steamapps\common\DEADBOLT"
```

## Teksty

1. **`dia_*.json` obok exe** (8 plików, ~26 KB): notatki i rozmowy przy teczkach,
   ognisku (`dia_fp.json` — misje od „płomieni”, wiersze) i sejfach. 262 pola
   `Dialogue`/`Name`/`Description`, ~2400 słów. Gra czyta je `json_decode`.
2. **STRG w `data.win`**: 6329 napisów, z czego heurystycznie ~595 tekstów dla gracza
   (~3800 słów): menu, ustawienia, sterowanie, podpowiedzi „E: OTWÓRZ DRZWI”, cele,
   nazwy i opisy misji, przydomki wrogów, okrzyki, podpowiedzi po śmierci, broń,
   długie opowiadania z kaset, napisy końcowe. **Liczba jest szacunkiem**, nie zakresem.
3. **Etapy `Stages/*.nc`**: w nagłówku nazwa poziomu („Noisy Neighbors”), ta sama
   co w STRG, ale z inną pisownią („Noisy Neighbours”). Która jest wyświetlana — do
   sprawdzenia w kodzie; zapewne `.nc` tylko dla map własnych.
4. **Tekst w grafice**: teczka misji (`sMissionFolder`: „Name:”, „Case #:”), możliwe
   inne. Szyldy w poziomach wyglądają na dekorację. Pełny przegląd atlasów do zrobienia.

Znaczniki: `#` = nowa linia (GMS 1.x), `&y&`, `&r&`, `&b&`, `&w&`, `&dk&` kolor,
`&!&` powrót. Wiele napisów jest sklejanych w kodzie (`"&y&'" + klawisz + "'&!&: OPEN DOOR"`,
`"You have died " + n + " times..."`, `"Kill the &r&backup (" ...`) — szyk polskiego
zdania musi się zmieścić w tych kawałkach; ewentualnie zmiana w bytecode.

Razem **~850 wpisów, ~6000 słów** — mała gra, pełne tłumaczenie to niewielka robota.

## Polskie znaki

Trzy fonty, wszystkie rasteryzowane do atlasu:

| font | krój | rozmiar | zakres | polskie |
|---|---|---|---|---|
| fontTiny | NBP Informa FiveSix | 12 | 32–127 | brak |
| fontSmall | Windows Command Prompt | 12 | 32–127 | brak |
| fontMedium | Windows Command Prompt | 24 | 32–220 | tylko Ó |

Trzeba dorysować 18 (fontMedium 16) liter w trzech fontach pikselowych — jak w Hyper
Light Drifter i Katana ZERO, składając kreski, kropki i ogonki z istniejących glifów
(ó ze „Ó”/akcentów fontMedium). Runner GMS 1.4 rysuje UTF-8, więc wystarczy glif w FONT.

## Metoda: plugin `d3d9.dll`, zmiana bufora `data.win` w pamięci

Pliki gry na dysku zostają nietknięte. Plugin to proxy `d3d9.dll` jak w Heat Signature
(MinHook, build MSVC x86); różnica: tu nie przechwytujemy rysowania, tylko poprawiamy
dane gry w pamięci, zanim runner je rozbierze.

### Co mówi disassembly runnera (`deadbolt_game.exe` 1.0.0.87, bez ASLR)

Adresy poniżej są dowodem z tej wersji, **nie wchodzą do pluginu**.

- Ścieżka `data.win` (UTF-16 w `.rdata`) trafia do zmiennej globalnej; start gry
  (`0x5594c0`) robi kolejno:
  1. `0x559502` — wczytanie całego pliku do bufora na stercie: `_wfopen(L"rb")`,
     `fseek`/`fgetpos`, `malloc`, `fread` (`LoadSave.cpp`, `0x43f450`);
  2. `0x559538` — przebieg wstępny (`0x45a4b0`): wymaga `FORM.len == rozmiar − 8`,
     zapamiętuje bazę bufora, GEN8, CODE i **wskaźnik listy STRG z ostatniego chunku
     STRG**; nieznane chunki pomija;
  3. `0x559587` — inicjalizacja grafiki (`0x45b680` → `0x425e30` → `Direct3DCreate9`).
     `d3d9.dll` jest w imporcie **opóźnionym**, więc proxy ładuje się dopiero tutaj;
  4. `0x5597f4` — główny parser chunków (`0x45a950`): FONT, TXTR, CODE, SPRT…
     Nieznany chunk jest tu logowany i psuje wynik ładowania, STRG/VARI/DAFL pomija.
- **Luka między 2 a 4 to punkt wejścia pluginu:** bufor jest w pamięci, nic poza
  przebiegiem wstępnym go jeszcze nie czytało.
- Wszystkie wskaźniki w pliku (STRG, FONT, glify, TXTR, PNG) runner zamienia na adresy
  jako `baza + przesunięcie` w 32 bitach. Nowe dane mogą więc leżeć w naszej pamięci:
  przesunięcie = `adres − baza` (mod 2³²). Nie trzeba powiększać bufora ani przesuwać chunków.
- TXTR (`0x45a800`): PNG spod wskaźnika, długości nie podaje (dekoder czyta do IEND).
- FONT (`0x41d070`): lista wskaźników do glifów, bez tabeli zakresu. Glif szukany
  **wyszukiwaniem binarnym** po kodzie znaku (`0x41b030`), brak = U+25AF. Pola
  „pierwszy/ostatni znak” nie ograniczają wyszukiwania. Lista musi być posortowana.
- FONT kończy się 512-bajtowym ogonem (tablica 256 × u16) — nie ruszamy.

### Plan pluginu

1. Przy `Direct3DCreate9` (poza DllMain) odnaleźć bufor: przeszukać zatwierdzone
   prywatne regiony pamięci pod kątem `FORM` + `GEN8` z nazwą `deadbolt_game`
   i `FORM.len` równym długości `data.win` na dysku. Zero lub więcej niż jedno
   trafienie → wyłączenie z wpisem w logu.
2. **Napisy:** dla każdego wpisu listy STRG, którego tekst jest w `pl.tsv`
   (dopasowanie po angielskim tekście), zapisać nasz napis (`u32 długość` + UTF-8 + 0)
   i przestawić przesunięcie w liście. Nieznane zostają po angielsku; w logu liczba
   dopasowanych i brakujących.
3. **Fonty:** dla `fontTiny`, `fontSmall`, `fontMedium` (po nazwie) nowa kopia struktury
   fontu z listą glifów uzupełnioną o polskie litery (posortowaną), wskaźnik w liście
   FONT na kopię. Piksele liter dorysowane w wolnym miejscu **wewnątrz prostokąta
   atlasu tego fontu** (wolne wiersze pod glifami: 46 / 28 / 96 px), więc TPAG bez
   zmian. Strona tekstury (0 dla Tiny, 1 dla Small i Medium) dekodowana z bufora przez
   WIC, dorysowane litery, zakodowana ponownie; wskaźnik PNG w TXTR na nową. W paczce
   są tylko nasze glify (kształty liter), nie piksele gry.
4. **Dialogi JSON:** hak MinHook na `kernel32!CreateFileW` (runner i `GMFile.dll`
   z MSVCR100 czytają przez niego) przekierowuje `dia_*.json` na wersję polską
   wygenerowaną z oryginału + `pl.tsv` w `notgeese/cache/`.
5. Log: wersja pluginu, PE i GEN8 gry, liczby dopasowań, wynik każdego kroku.
   Każdy błąd wyłącza całość i zostawia grę po angielsku.

Zabezpieczenie przed częściowym stanem: fonty najpierw, napisy dopiero po udanych
fontach. Jeśli runner kiedyś zmieni kolejność (grafika po parserze), zmiany w buforze
nie zadziałają, ale nic się nie zepsuje.

Niesprawdzone do czasu testu: czy CODE rozwiązuje napisy przez listę STRG z przebiegu
wstępnego (tak wynika z kodu, dowód w grze), czy WIC poradzi sobie z PNG 2048×2048
w rozsądnym czasie, i jak zachowuje się tryb `-game`/Steam overlay.

### Odrzucone

- Łatka `data.win` z aplikatorem `.exe` — użytkownik nie chce dawać graczom exe;
  zostaje jako wyjście awaryjne.
- Przekierowanie `data.win` na przebudowany plik — wymaga proxy ładowanego przy starcie
  procesu (winmm/dbghelp), a `d3d9.dll` przychodzi za późno.
- Podmiana tekstu przy rysowaniu (jak Heat Signature) — gra skleja napisy z kolorami
  `&y&…&!&` i fragmentów, więc na etapie rysowania kawałki nie pasowałyby do słownika.

## Niepewne

- Które napisy STRG są naprawdę wyświetlane (dekompilacja kodu rozstrzygnie) i jak
  długie pola mają menu i podpowiedzi (fontTiny jest bardzo mały).
- Nazwy poziomów w `.nc` vs STRG.
- Pełna lista grafik z tekstem.
- **Napisy używane w logice.** Tłumaczenie w STRG zmienia napis wszędzie, gdzie kod
  go używa — także w porównaniach czy kluczach map. Przed verticalem trzeba
  zdekompilować kod (UndertaleModTool obsługuje bytecode 15) i do `pl.tsv` brać tylko
  wpisy wyświetlane. Zapis gry (`save1.sav`, `Prefs.ini`) trzyma liczby, nie nazwy.

## Następny krok

Test pełnego 0.2.0 w grze przez użytkownika (lista „Do sprawdzenia w grze” w
`docs/localization-review.md`, zwłaszcza wiersze płomieni w teczce, ekran Charona
i podpowiedzi fontTiny). Otwarte warianty: „grim and dim” w finale, rodzaj Świecy
w dia_lv3_7, skróty przycisków pada.
