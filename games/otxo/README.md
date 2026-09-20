# OTXO PL

*Część [Nie gęsi](../../README.md) — polskie tłumaczenia gier, które własnego nigdy nie dostały.*

Nieoficjalne polskie tłumaczenie **OTXO**. Komplet: 1364 wpisy, czyli wszystko, co gra ma do powiedzenia — menu, ustawienia, samouczek, 102 trunki, dialogi wszystkich postaci z plaży, lore Pisma Bekatuy, cały dziennik bohatera, nazwy broni i statystyki przebiegu. Pozostałe 104 klucze są w oryginale puste albo symboliczne i zostają nietknięte.

## Jak to działa

Teksty OTXO leżą w zwykłych plikach INI obok pliku wykonywalnego — jeden na język, UTF-8, CRLF, jedna sekcja i linie `<numer>="<tekst>"`:

```
script_english.ini                    [english]             1468 wartości
OTXO_script_english_fre-FR.ini        [french]
OTXO_script_english_ger-DE.ini        [german]
OTXO_script_english_por-BR.ini        [portuguese]
OTXO_script_english_rus.ini           [russian]
OTXO_script_english_spa-ES.ini        [spanish]
OTXO_script_english_zho-CN.ini        [chinese-simplified]
```

Sama podmiana tekstu jest więc trywialna. Problemem jest **ósmy slot, którego nie ma**. OTXO to GameMaker skompilowany do kodu natywnego: w `data.win` nie ma chunków z bytecode'em, a nazwy tych sześciu plików i siedem nazw sekcji to literały wewnątrz `OTXO_Release.exe`. Nie ma czego rozszerzyć bez łatania kodu maszynowego, a dopisanie `script_polish.ini` niczego nie uruchomi, bo nikt go nie szuka.

Polski **przejmuje więc slot chiński** — tą samą drogą poszedł fanowski mod japoński. W menu języka polski jest zatem pod **chińską flagą**.

> **Uwaga o tym, co ten mod naprawdę robi.** To nie jest dołożenie ósmego języka, tylko **podmiana lokalizacji chińskiej**. Po zainstalowaniu gra nie ma już chińskiego — pod chińską flagą jest polski. Dla kogoś, kto instaluje polskie tłumaczenie, strata jest zerowa, ale warto to wiedzieć przed podmianą pliku, a nie po. Oryginał wraca przez przywrócenie kopii zapasowej. Innego wyjścia nie ma: siedem slotów to literały w kodzie natywnym, a chiński jest jedynym, który rysuje interfejs czcionką z pliku, więc jako jedyny umie polskie znaki.

Wybór slotu nie jest dowolny i zdecydowały o nim czcionki, co potwierdził test w grze (patrz *Status testów*). OTXO trzyma 29 wypalonych czcionek w `data.win` i większość z nich nie umie napisać po polsku:

| czcionka | krój | glifów | polskie znaki |
| --- | --- | --- | --- |
| `font1`, `font2`, `font6` — menu | ITC Avant Garde Gothic | 190 | tylko `ó` |
| `font1_rus` — wariant rosyjski | Noto Sans Mono | 273 | tylko `ó` |
| `font4`, `font5`, `dialoguefont1` — dialogi | Courier New Baltic | 437 | **komplet** |

Czcionki menu mają ASCII i Latin-1, więc `ó` się narysuje, a `ę`, `ź`, `ł` już nie. Rodzina Courier New Baltic ma komplet, ale obsługuje dialogi, nie menu — i nie da się jej tam podstawić bez ruszania kodu natywnego.

Ratunkiem jest obiekt `obj_font_loader`, który **dogrywa czcionki z plików TTF leżących obok pliku wykonywalnego**: `notosans.ttf` i `yahei.ttf`. Sprawdziłem tablice znaków obu — **każdy z nich ma wszystkie osiemnaście polskich liter**. Chiński jest jedynym slotem, który rysuje interfejs czcionką z dysku zamiast wypaloną, więc to jedyna droga do pełnych ogonków bez przerabiania tekstur w `data.win`.

Slot wybiera się parametrem: `build.py --slot ger-DE` zbuduje to samo dla niemieckiego.

Plik nie powstaje od zera. Budowa bierze plik angielski jako szablon, podmienia nagłówek sekcji i wstawia przetłumaczone wartości w istniejące linie. Dzięki temu wpisy jeszcze nieprzetłumaczone zostają po angielsku, zamiast zniknąć, a każda pusta linia i każda dziwność oryginału przeżywa bez zmian — a jest ich sporo: osiem kluczy nie ma wartości w cudzysłowie, jedna linia niesie znak za zamykającym cudzysłowem, część plików ma inne zestawy kluczy niż angielski, a francuski powtarza cztery klucze.

## Dla kogo są te pliki

| Odbiorca | Pliki | Zastosowanie |
| --- | --- | --- |
| Autor gry | [`translations/en-pl-review.json`](translations/en-pl-review.json) | Każdy wpis z kluczem, angielskim oryginałem i tłumaczeniem. Klucze są te same, których używa gra. |
| Gracze | Zbudowany `OTXO_script_english_zho-CN.ini` | Jeden plik do podmiany. Patrz [INSTALL.txt](docs/INSTALL.txt). |
| Korekta | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Poprawianie tekstów i przebudowa. |

## Budowanie

```powershell
.venv\Scripts\python.exe games\otxo\tools\extract.py --game "C:\Games\OTXO"
.venv\Scripts\python.exe games\otxo\tools\build.py --game "C:\Games\OTXO"
```

`extract.py` odświeża plik korektorski, `build.py` zapisuje `dist/OTXO_script_english_zho-CN.ini`. Źródłowy `script_english.ini` jest przypięty sumą SHA-256 w [`tools/build.py`](tools/build.py); inna wersja gry zostaje odrzucona i nic się nie zapisuje.

Instalacja do testów przez [`tools/install.py`](../../tools/install.py) z katalogu głównego — odkłada oryginał do `backups/otxo/`.

## Weryfikacja

Build sprawdza się względem oryginału i bez tego nie zapisze pliku:

- przepisanie angielskiego pliku bez żadnego tłumaczenia daje go **bajt w bajt** — dowód, że szablon niczego nie gubi;
- zbudowany plik ma dokładnie ten sam zestaw kluczy co angielski i tyle samo linii;
- każda wartość odczytana z powrotem jest albo tłumaczeniem z `pl.json`, albo nietkniętym angielskim oryginałem;
- nagłówek sekcji to `[chinese-simplified]`, czyli ten, którego szuka gra dla tego slotu;
- żaden tekst nie zawiera cudzysłowu ani znaku nowej linii, które rozwaliłyby linię.

To weryfikacja plików, nie test w grze.

## Status testów

**Test w grze, slot francuski (1.106): przejęcie slotu działa, czcionka nie.** Menu główne wyświetliło się po polsku — *Nowy przebieg*, *Opcje*, *Wyjdź do pulpitu* — co dowodzi, że gra czyta podmieniony plik i że przejęcie slotu jest właściwą drogą. Ale `ę`, `ź` i `Ź` nie narysowały się wcale: „Język" wyszło jako „J zyk", „Wyjdź do pulpitu" jako „Wyjd  do pulpitu". To zgadza się co do znaku z tablicą glifów `font1`/`font2`/`font6` odczytaną z `data.win`.

Po tym teście slot zmieniono na chiński, bo tylko on rysuje interfejs czcionką dogrywaną z `yahei.ttf`, a ta ma komplet polskich liter. Francuski przywrócono do oryginału.

**Test w grze, slot chiński (1.106): działa, z pełnymi ogonkami.** Menu wyświetliło *Nowy przebieg*, *Opcje*, *Język*, *Wyjdź do pulpitu* i *ZATWIERDŹ* — `ę`, `ź` i `Ź` narysowały się poprawnie. Potwierdza to, że gra przy chińskim rysuje interfejs czcionką dogrywaną z `yahei.ttf`, a nie wypaloną w `data.win`, i że prosi o zakres znaków obejmujący Latin Extended-A. Droga jest otwarta na pozostałe 1416 wpisów.

Po tym teście przetłumaczono całą resztę. **Pełna wersja jest zbudowana i zainstalowana, ale w grze niesprawdzona.** Do obejrzenia zostaje: łamanie dłuższych zdań w opisach trunków i w dzienniku (najdłuższy wpis ma 157 znaków), ekran statystyk po przebiegu, oraz czy wybór języka utrzymuje się między uruchomieniami.

### Otwarta sprawa: flaga

Polski siedzi pod chińską flagą, bo ósmego slotu nie da się dołożyć bez łatania kodu natywnego. Tańsze rozwiązanie kosmetyczne jest w zasięgu: flagi to jeden sprite `sprFlags`, siedem klatek po 100×50 px, wszystkie na stronie tekstur 1 pod znanymi współrzędnymi. Tekstury są w formacie QOI spakowanym BZip2 — `bz2` jest w bibliotece standardowej, a QOI to kilkadziesiąt linii kodu. Przemalowanie klatki chińskiej na polską flagę nie wymaga przesuwania niczego w `data.win`, o ile nowy obrazek zmieści się w tej samej liczbie bajtów.

## Materiał gry

Katalog zawiera wyłącznie teksty tłumaczenia i narzędzia — żadnych plików gry. Nic tu nie jest powiązane z autorami *OTXO* ani przez nich firmowane; gra, jej teksty i postacie należą do nich.

## Licencja

[MIT](../../LICENSE), jak reszta repozytorium.
