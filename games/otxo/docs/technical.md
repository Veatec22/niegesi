# OTXO — technika i stan prac

## Wersja 0.2 — przegląd skillem lokalizacji (2026-09-22)

Tłumaczenie przeszło standard `.claude/skills/localization`: biblia
(`translations/bible.yaml`), raport (`work/l10n-report.md`), lektura wszystkich
1364 wpisów i spis decyzji w `docs/translation-decisions.md`. Zmieniono 15 wpisów.

Pozostałe języki gry leżą obok jako zwykłe INI. `work/ref-extract.py` zrzuca je
do `work/ref-all.json` (poza gitem) — rosyjski posłużył do sprawdzenia płci
i do potwierdzenia, które teksty gra skleja z nazwami (`В: `, `СРАЖАЕТСЯ С: `):

```powershell
.venv\Scripts\python.exe games\otxo\work\ref-extract.py "C:\Games\OTXO"
```

Test w grze 0.2: nie robiony, zmiany są wyłącznie tekstowe.

## Wersja 0.1

1364 wpisy, czyli wszystko, co gra ma do powiedzenia: menu, ustawienia, samouczek,
102 trunki, dialogi wszystkich postaci z plaży, lore Pisma Bekatuy, cały dziennik
bohatera, nazwy broni i statystyki przebiegu. Pozostałe 104 klucze są w oryginale
puste albo symboliczne i zostają nietknięte.

## Format

Teksty OTXO leżą w zwykłych plikach INI obok pliku wykonywalnego — jeden na język,
UTF-8, CRLF, jedna sekcja i linie `<numer>="<tekst>"`:

```
script_english.ini                    [english]             1468 wartości
OTXO_script_english_fre-FR.ini        [french]
OTXO_script_english_ger-DE.ini        [german]
OTXO_script_english_por-BR.ini        [portuguese]
OTXO_script_english_rus.ini           [russian]
OTXO_script_english_spa-ES.ini        [spanish]
OTXO_script_english_zho-CN.ini        [chinese-simplified]
```

Sama podmiana tekstu jest więc trywialna. Problemem jest **ósmy slot, którego nie ma**.
OTXO to GameMaker skompilowany do kodu natywnego: w `data.win` nie ma chunków
z bytecode'em, a nazwy tych sześciu plików i siedem nazw sekcji to literały wewnątrz
`OTXO_Release.exe`. Nie ma czego rozszerzyć bez łatania kodu maszynowego, a dopisanie
`script_polish.ini` niczego nie uruchomi, bo nikt go nie szuka.

Polski **przejmuje więc slot chiński** — tą samą drogą poszedł fanowski mod japoński.
To nie jest dołożenie ósmego języka, tylko podmiana lokalizacji chińskiej: po instalacji
gra nie ma już chińskiego, pod chińską flagą jest polski. Oryginał wraca przez
przywrócenie kopii zapasowej.

## Dlaczego akurat chiński: czcionki

Wybór slotu zdecydowały czcionki i potwierdził go test w grze. OTXO trzyma 29 wypalonych
czcionek w `data.win` i większość z nich nie umie napisać po polsku:

| czcionka | krój | glifów | polskie znaki |
| --- | --- | --- | --- |
| `font1`, `font2`, `font6` — menu | ITC Avant Garde Gothic | 190 | tylko `ó` |
| `font1_rus` — wariant rosyjski | Noto Sans Mono | 273 | tylko `ó` |
| `font4`, `font5`, `dialoguefont1` — dialogi | Courier New Baltic | 437 | **komplet** |

Czcionki menu mają ASCII i Latin-1, więc `ó` się narysuje, a `ę`, `ź`, `ł` już nie.
Courier New Baltic ma komplet, ale obsługuje dialogi, nie menu, i nie da się jej tam
podstawić bez ruszania kodu natywnego.

Ratunkiem jest obiekt `obj_font_loader`, który **dogrywa czcionki z plików TTF leżących
obok pliku wykonywalnego**: `notosans.ttf` i `yahei.ttf`. Oba mają wszystkie osiemnaście
polskich liter. Chiński jest jedynym slotem, który rysuje interfejs czcionką z dysku
zamiast wypaloną — stąd wybór.

Slot wybiera się parametrem: `build.py --slot ger-DE` zbuduje to samo dla niemieckiego.

## Budowanie i weryfikacja

```powershell
.venv\Scripts\python.exe games\otxo\tools\extract.py --game "C:\Games\OTXO"
.venv\Scripts\python.exe games\otxo\tools\build.py --game "C:\Games\OTXO"
```

Plik nie powstaje od zera. Build bierze plik angielski jako szablon, podmienia nagłówek
sekcji i wstawia tłumaczenia w istniejące linie. Dzięki temu wpisy nieprzetłumaczone
zostają po angielsku zamiast zniknąć, a każda dziwność oryginału przeżywa bez zmian —
a jest ich sporo: osiem kluczy nie ma wartości w cudzysłowie, jedna linia niesie znak
za zamykającym cudzysłowem, część plików ma inne zestawy kluczy niż angielski,
a francuski powtarza cztery klucze.

Build sprawdza się względem oryginału i bez tego nie zapisze pliku:

- przepisanie angielskiego pliku bez żadnego tłumaczenia daje go **bajt w bajt**;
- zbudowany plik ma dokładnie ten sam zestaw kluczy co angielski i tyle samo linii;
- każda wartość odczytana z powrotem jest albo tłumaczeniem, albo nietkniętym oryginałem;
- nagłówek sekcji to `[chinese-simplified]`, czyli ten, którego szuka gra;
- żaden tekst nie zawiera cudzysłowu ani znaku nowej linii, które rozwaliłyby linię;
- archiwum jest otwierane ponownie i porównywane bajtowo z plikiem wynikowym.

Źródłowy `script_english.ini` jest przypięty sumą SHA-256; inna wersja gry zostaje
odrzucona i nic się nie zapisuje. Wynik: `dist/OTXO_script_english_zho-CN.ini` (72 KB)
oraz `dist/OTXO-PL-0.2.zip` (30 KB) z tym plikiem i `READ-ME.txt`.

Paczka zawiera **wyłącznie nasz tekst** — żadnego bajtu z gry, żadnej biblioteki
obcego autorstwa. To najczystszy przypadek w całym repo.

Instalacja do testów przez [`tools/install.py`](../../../tools/install.py) z katalogu
głównego — odkłada oryginał do `backups/otxo/`.

## Status testów

**Slot francuski (1.106): przejęcie slotu działa, czcionka nie.** Menu wyświetliło się
po polsku, co dowiodło, że gra czyta podmieniony plik. Ale `ę`, `ź` i `Ź` nie narysowały
się wcale: „Język" wyszło jako „J zyk". Zgadza się co do znaku z tablicą glifów
`font1`/`font2`/`font6` odczytaną z `data.win`. Francuski przywrócono do oryginału.

**Slot chiński (1.106): działa, z pełnymi ogonkami.** Menu wyświetliło *Nowy przebieg*,
*Opcje*, *Język*, *Wyjdź do pulpitu* i *ZATWIERDŹ* — wszystkie znaki poprawnie.

Po tym teście przetłumaczono całą resztę. **Pełna wersja jest zbudowana i zainstalowana,
ale w grze niesprawdzona.** Do obejrzenia zostaje: łamanie dłuższych zdań w opisach
trunków i w dzienniku (najdłuższy wpis ma 157 znaków), ekran statystyk po przebiegu
oraz czy wybór języka utrzymuje się między uruchomieniami.

## Flaga: dlaczego zostaje chińska

Próba przemalowania flagi dojechała do konkretnej ściany i warto zapisać, do której.

Co ustalone na pewno:

- flagi to jeden sprite `sprFlags`, **siedem klatek po 100×50 px**, wszystkie na stronie
  tekstur 1, pod znanymi współrzędnymi;
- wpis w chunku TXTR to siedem liczb: `scaled, mips, długość bloba, szerokość, wysokość,
  ?, wskaźnik`. **Trzecia to długość skompresowanych danych**, więc podmiana mniejszym
  blobem i poprawienie tej liczby niczego w pliku nie przesuwa;
- strona z flagami ma 8192×8192, czyli 67 mln pikseli — koszt jednorazowy, nie przeszkoda.

Ścianą jest kodek. **GameMaker nie używa publicznej specyfikacji QOI.** Dekoder napisany
od zera rozjeżdża się na wszystkich trzech stronach, a przejście wariantów formatu nie
daje ani jednej kombinacji zgodnej z liczbą pikseli z nagłówka:

| strona | deklarowane piksele | najlepsze trafienie |
| --- | --- | --- |
| 0 | 4 096 | 4 912 (1,20×) |
| 1 | 67 108 864 | 65 789 785 (0,98×) |
| 2 | 33 554 432 | 40 018 942 (1,19×) |

Gdyby chodziło o jeden parametr, wszystkie trzy myliłyby się tak samo. Mylą się różnie,
więc to inna konstrukcja formatu, do odczytania z implementacji, nie z danych.

Zrobienie tego przez UndertaleModTool dałoby zmodyfikowany `data.win` — 15,8 MB
zawierającego całą zawartość gry. Dołączenie go do paczki to redystrybucja cudzych
zasobów zamiast samego tłumaczenia, czyli dokładnie to, czego zasady w `AGENTS.md`
zabraniają. Łatka binarna nic by nie dała, bo przekodowanie strony zmienia cały
ośmiomegabajtowy strumień, a `data.win` przestaje pasować po każdej aktualizacji gry.

Dla porządku: **żadne istniejące tłumaczenie OTXO tego nie rozwiązało.** Japoński mod
WitheredPoppiMk-4 podmienia dokładnie te same dwa pliki co my, a jego instrukcja każe
sprawdzić, „czy flaga zmieniła się na chińską" — chińska flaga jest u nich wskaźnikiem
powodzenia. Turecki zestaw również sprowadza się do podmiany plików w katalogu gry.

## Materiały do korekty

- [EN/PL JSON](../translations/en-pl-review.json) — każdy wpis z kluczem, angielskim
  oryginałem i tłumaczeniem; klucze są te same, których używa gra.
- [Polskie teksty](../translations/pl.json) — źródło dla builda.

`extract.py` odświeża plik korektorski po zmianach w `pl.json`.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „OTXO po polsku”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Pełne spolszczenie OTXO: 1364 wpisy, czyli wszystko, co gra ma do powiedzenia — menu,
ustawienia, samouczek, 102 trunki, dialogi wszystkich postaci z plaży, lore Pisma
Bekatuy, cały dziennik bohatera, nazwy broni i statystyki przebiegu.

Paczka to **jeden plik tekstowy, 72 KB, w całości nasz** — nie ma w niej ani bajta
z gry. Podmieniasz jeden plik i tyle.

### Zanim zainstalujesz

Polski **przejmuje slot chiński**. To nie jest dołożenie ósmego języka: po instalacji
gra nie ma już chińskiego, a pod chińską flagą jest polski. W menu języka flaga
pozostaje chińska — to kosmetyka, nie błąd.

Innego wyjścia nie ma. OTXO to GameMaker skompilowany do kodu natywnego, siedem slotów
językowych to literały w pliku wykonywalnym, a chiński jest jedynym, który dogrywa
czcionkę z dysku — czyli jedynym, który w ogóle umie narysować polskie znaki.
Szczegóły w [technice](../docs/technical.md).

### Instalacja

1. Zamknij grę.
2. Zrób kopię pliku `OTXO_script_english_zho-CN.ini` z katalogu gry, gdzieś poza nim.
3. Wypakuj [paczkę ZIP](../dist/OTXO-PL-0.1.zip) do katalogu gry i potwierdź zastąpienie.
4. Uruchom grę i w opcjach wybierz język pod **chińską flagą**.

Pełna [instrukcja instalacji i przywrócenia](../docs/INSTALL.txt).

### Przywrócenie

Wgraj z powrotem swoją kopię `OTXO_script_english_zho-CN.ini`. Można też zweryfikować
pliki gry w GOG Galaxy albo w Steamie.

### Stan

Sprawdzone w grze: menu, wybór języka i polskie znaki na slocie chińskim.
Pełny przebieg czeka na przejście — do obejrzenia zostaje łamanie dłuższych opisów
trunków i wpisów dziennika oraz ekran statystyk.

Wersja źródłowa: GOG, 1.106.

[Szczegóły techniczne, budowanie i materiały do korekty](../docs/technical.md) ·
[Metadane](../game.yaml)
