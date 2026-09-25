# Katana ZERO — technika i stan prac

## Stan: pełne tłumaczenie 0.2.0 (22 września 2026)

Przetłumaczone wszystkie 2851 wpisy (menu, UI, teczki, wszystkie dialogi, wiadomości,
napisy końcowe). Zbudowane, zweryfikowane odczytem z obu plików i zainstalowane na GOG 1.0.5;
paczka 78 KB leży w `site/public/pobierz/`. **Pełne przejście w grze czeka.** Decyzje
tłumaczenia: `docs/translation-decisions.md`, biblia: `translations/bible.yaml`.

Zmiany względem verticala: fonty nie mają „” ani półpauzy, więc teksty używają `"` i `-`;
xirod dostał też „ó/Ó” (90 liter zamiast 88).

Vertical potwierdzony w grze na 0.1.2 (polskie litery, menu, pierwsze dialogi); 0.1.3 dołożył licznik dni i „WYSUŃ KASETĘ”
(skrócone na prośbę użytkownika — pole jest małe).

### Historia verticala

**Test 0.1 w grze:** gra startuje, wybór „Polski” działa na miejscu rosyjskiego, polskie
teksty widać w menu, opcjach, ostrzeżeniu i pierwszym dialogu. **Polskich liter nie było
widać nigdzie** — w ich miejscu odstęp szerokości litery (czasem śmieciowy piksel). Font
znał więc glify (mapa i klatki zadziałały), tylko strona tekstury z pikselami nie trafiła
do pamięci: nie należała do żadnej grupy tekstur (TGIN), a gra wczytuje strony grupami.

0.1.1: osobna strona liter dla każdej grupy, w której siedzi font (`Default` — vcr, vhs,
xirod, big; `Non-combat in-game` — textbox), dopisana do listy stron tej grupy; obrazki
stron leżą na końcu danych TXTR, w kolejności listy. **W grze bez zmian** — liter dalej nie było.

**Właściwa przyczyna, z kodu runnera** (handler TXTR, `0x18ea6e0`): po utworzeniu tekstur
runner przechodzi po liście chunku TPAG i w każdej pozycji zamienia numer strony z pliku
(pole `+0x14`) na identyfikator tekstury w karcie (`g_TexIDs[tp]`). Identyfikatory daje
alokator pierwszego wolnego miejsca (`0x19bcea0`), więc nie są równe numerom stron.
Pozycje spoza listy zostają z surowym numerem i wskazują cudzą teksturę. Handler samego
TPAG (`0x18e974c`) tylko zapamiętuje położenie listy.

0.1.2: drugi chunk `TPAG` wstawiony tuż przed TXTR, z pełną listą — stare pozycje w tej
samej kolejności plus nasze 88. Runner zapamiętuje ten późniejszy chunk, więc przelicza
numery także naszym pozycjom; pierwszy chunk zostaje nietknięty. Grupy TGIN z 0.1.1
zostają (strona i tak musi się wczytać). **Potwierdzone w grze.**


## Spolszczenia w sieci

- [GrajPoPolsku, temat Katana ZERO](https://grajpopolsku.pl/forum/viewtopic.php?t=3723) —
  projekt ogłoszony w listopadzie 2021 pod GOG 1.0.5, bez daty i bez paczki. Ostatni wpis
  (czerwiec 2024) to pytanie o postęp, bez odpowiedzi autora. Brak dostępnej paczki.
- Wersja na Netflix (mobilna) ma podobno polski, ale nie dotyczy PC.
- Steam: 10 języków, bez polskiego (API sklepu, `supported_languages`).
- [ZenHAX](https://zenhax.com/viewtopic.php@t=11326.html): tłumacze na inne języki używali
  `exestringz` i HxD, bo teksty są w exe; zmiana długości napisu wywracała grę.

## Silnik i teksty

GameMaker Studio 2, bytecode 17, **kod skompilowany YYC** do natywnego x86 (32 bity, ASLR).
Nie ma plików z tekstami ani loadera modów; `data.win` trzyma grafikę, dźwięk i fonty,
a cały tekst jest wkompilowany w `Katana ZERO.exe` jako stałe w sekcji `.data`.

Języki (w tej kolejności): EN, JA, KO, DE, FR, ES, PT, RU, ZH-Hans, ZH-Hant. Teksty idą
dwiema drogami (szczegóły w docstringu `tools/exe.py`):

1. **Tablice `text[język * 32000 + nr]`** w `init_lines` (dialogi, 2492 wpisy) i
   `init_misc_text` (UI, 267). Kluczem jest `funkcja:linia` — numer linii GML, który YYC
   zapisuje przy każdym przypisaniu, więc to identyfikator z pliku, nie nasz.
2. **Menu i ustawienia** w `init_option_translations` (92): dziesięć napisów tworzonych
   kolejno plus `"end"`, potem skrypt wybiera wersję. Kluczem jest `funkcja:EN`
   (`#2` przy powtórzeniu).

Nazwa języka w selektorze to wpis `init_misc_text:1790` w każdym języku („English”,
„Deutsch”, „Русский”…), więc „Polski” wpisuje się jak każdy inny tekst.

Znaczniki w dialogach: kolory `[r] [o] [y] [a] [p] [l]`, zamknięcie `[/]`, efekty
(`[*]`, `[!]`, `[^<>]`, łączone, np. `[r!^<*>]`), `[@]`, `[./]`. Gwiazdka poza nawiasem
to pauza w wypowiedzi. `tools/review.py` pilnuje, żeby znaczniki i łamania linii były
identyczne; liczbę pauz tylko zgłasza.

## Metoda

Pluginu nie da się zrobić: YYC to natywny kod bez runtime'u, do którego można się
wpiąć, a proxy-DLL wymagałby własnego natywnego loadera (w repo nie ma kompilatora C)
i podmiany `data.win` w pamięci. Zostaje **łatka różnicowa** obu plików (`tools/patch.py`).

**Polski zajmuje slot rosyjski.** Tablica ma sztywne 10 języków; jedenasty wymagałby
przepisania kodu. Rosyjski ma najlepszą ścieżkę rysowania: wszystkie fonty dla języków
niełacińskich i łacińskich to fonty ze sprite'ów tworzone jednym `font_add_sprite_ext`,
a rosyjski dodatkowo zamiast TTF `font_xirod` (Latin-1) używa `spr_xirod_font_rus`,
który ma pełną łacinę. Polskie litery tylko do nich dopisujemy.

Exe (`tools/build.py`):
- nowa sekcja `.ngpl` za `.reloc` z polskimi napisami (UTF-8, zero na końcu);
- każde `mov [esp], adres` / `mov [esp+4], adres` rosyjskiej wersji dostaje adres polskiej
  (albo angielskiej, gdy brak tłumaczenia). Build sprawdza, że każde takie miejsce ma
  wpis w relokacjach, więc ASLR działa;
- mapy znaków czterech fontów sprite'owych (221, 190, 158 i 99 znaków) dostają na końcu
  brakujące polskie litery;
- weryfikacja: każdy wpis w każdym języku odczytany z powrotem z wyniku, a poza
  podmienionymi adresami i nagłówkiem plik jest bajt w bajt taki sam.

data.win:
- 88 nowych liter (16 w pięciu fontach, 8 w wielkim `spr_big_font`) na dwóch nowych
  stronach tekstur, po jednej na grupę tekstur fontu, dopisanych do list stron w TGIN
  (nowa lista w bloku, wskaźnik w strukturze grupy przestawiony);
- nowe pozycje TPAG i nowe kopie struktur sześciu sprite'ów z dłuższą listą klatek;
  wskaźnik w liście SPRT idzie na kopię, stara zostaje nieużywana;
- drugi chunk `TPAG` przed TXTR (pełna lista TPAG + nasze pozycje, sprite'y, listy grup,
  pozycje stron), nowe wskaźniki za listą TXTR i obrazki PNG na końcu chunku TXTR —
  wszystkie trzy wstawki są wielokrotnościami 0x80 (razem 72 320 B, z czego 57 KB to
  kopia starej listy, w łatce zwykłe kopiowanie z oryginału); przesuwają się tylko dane
  tekstur i dźwięków, a ich wskaźniki (lista TXTR, adresy PNG, lista AUDO) poprawiamy
  o długość wstawek przed nimi;
- weryfikacja: kolejność chunków (dodatkowy TPAG przed TXTR), nowa lista TPAG = stara
  plus nasze pozycje, klatki fontów (stare bez zmian, nowe równe wzorom),
  początki wszystkich PNG i dźwięków pod nowymi adresami, kolejność obrazków, grupy
  tekstur (nowe strony w grupie swojego fontu, reszta bez zmian).

Potwierdzone testem 0.1: nowe klatki gra przyjmuje (szerokości liter były właściwe).
Niepewne: czy runner nie ma innych miejsc, w których liczy na jeden chunk TPAG, i czy
rosyjski slot nie ma innych wyjątków w kodzie.

## Polskie litery

`tools/fonts.py` składa je z liter samej gry: kreska = „é” − „e”, kropka = kropka nad „i”
albo jedna z kropek „Ё”, ogonek = odbita cedylla z „ç” przy prawej nodze, kreska „ł”
dorysowana. Xirod nie ma „é” ani „ç”, więc dostaje znaki zsyntetyzowane z kropek „Ё”.
Podgląd: `tools/fonts.py --preview <plik.png>`.

## Budowanie

Po instalacji testowej katalog gry ma pliki spolszczone, więc build czyta z kopii:

```powershell
.venv\Scripts\python.exe games\katana-zero\tools\extract.py --game backups\katana-zero
.venv\Scripts\python.exe games\katana-zero\tools\review.py
.venv\Scripts\python.exe games\katana-zero\tools\build.py --game backups\katana-zero
.venv\Scripts\python.exe tools\patch.py release --original "backups\katana-zero\Katana ZERO.exe" --built "games\katana-zero\dist\build\Katana ZERO.exe" --relative "Katana ZERO.exe" --original backups\katana-zero\data.win --built games\katana-zero\dist\build\data.win --relative data.win --readme games\katana-zero\docs\INSTALL-patch.txt --out-dir games\katana-zero\dist --game-name katana-zero --package-name Katana-ZERO --version 0.2.0
```

Partie tłumaczenia: `tools/batch.py dump` / `merge` (kolejne wpisy w kolejności gry z rosyjskim
kontekstem; powtórzone angielskie kwestie wypełniają się same).

Paczka 0.2.0: 78 KB (łatka exe 60 KB, łatka data.win 9 KB).

## Pracownia korekty

`translations/structure.yaml` dzieli teksty na 3 grupy po skrypcie GML (opcje, różne, dialogi); rozmów nie da się wydzielić z numerów wierszy.

## Materiał gry

Paczka nie niesie zawartości gry: łatki to polskie napisy, nasze klatki liter (złożone
z pikseli liter gry, w całości związane z lokalizacją) i zmienione adresy. `work/`
(wyciągnięte teksty) jest ignorowany przez Gita.

## Następny krok

Pełne przejście gry przez użytkownika; poprawki według jego uwag
(miejsca najmniej pewne w `docs/translation-decisions.md`).
