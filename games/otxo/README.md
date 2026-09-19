# OTXO PL

*Część [Nie gęsi](../../README.md) — polskie tłumaczenia gier, które własnego nigdy nie dostały.*

Nieoficjalne polskie tłumaczenie **OTXO**. W toku: 52 z 1468 wpisów, czyli pionowy plaster na sprawdzenie całej drogi, zanim ruszy reszta tekstu.

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

Polski **przejmuje więc slot francuski** — tą samą drogą poszły fanowskie tłumaczenia japońskie i tureckie, tyle że na slocie chińskim. Wybór padł na francuski, bo to alfabet łaciński, więc gra zostaje przy `notosans.ttf`, którego tablica znaków zawiera wszystkie osiemnaście polskich liter. W menu języka polski jest zatem pod **francuską flagą**.

Plik nie powstaje od zera. Budowa bierze plik angielski jako szablon, podmienia nagłówek sekcji i wstawia przetłumaczone wartości w istniejące linie. Dzięki temu wpisy jeszcze nieprzetłumaczone zostają po angielsku, zamiast zniknąć, a każda pusta linia i każda dziwność oryginału przeżywa bez zmian — a jest ich sporo: osiem kluczy nie ma wartości w cudzysłowie, jedna linia niesie znak za zamykającym cudzysłowem, część plików ma inne zestawy kluczy niż angielski, a francuski powtarza cztery klucze.

## Dla kogo są te pliki

| Odbiorca | Pliki | Zastosowanie |
| --- | --- | --- |
| Autor gry | [`translations/en-pl-review.json`](translations/en-pl-review.json) | Każdy wpis z kluczem, angielskim oryginałem i tłumaczeniem. Klucze są te same, których używa gra. |
| Gracze | Zbudowany `OTXO_script_english_fre-FR.ini` | Jeden plik do podmiany. Patrz [INSTALL.txt](docs/INSTALL.txt). |
| Korekta | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Poprawianie tekstów i przebudowa. |

## Budowanie

```powershell
.venv\Scripts\python.exe games\otxo\tools\extract.py --game "C:\Games\OTXO"
.venv\Scripts\python.exe games\otxo\tools\build.py --game "C:\Games\OTXO"
```

`extract.py` odświeża plik korektorski, `build.py` zapisuje `dist/OTXO_script_english_fre-FR.ini`. Źródłowy `script_english.ini` jest przypięty sumą SHA-256 w [`tools/build.py`](tools/build.py); inna wersja gry zostaje odrzucona i nic się nie zapisuje.

Instalacja do testów przez [`tools/install.py`](../../tools/install.py) z katalogu głównego — odkłada oryginał do `backups/otxo/`.

## Weryfikacja

Build sprawdza się względem oryginału i bez tego nie zapisze pliku:

- przepisanie angielskiego pliku bez żadnego tłumaczenia daje go **bajt w bajt** — dowód, że szablon niczego nie gubi;
- zbudowany plik ma dokładnie ten sam zestaw kluczy co angielski i tyle samo linii;
- każda wartość odczytana z powrotem jest albo tłumaczeniem z `pl.json`, albo nietkniętym angielskim oryginałem;
- nagłówek sekcji to `[french]`, czyli ten, którego szuka gra;
- żaden tekst nie zawiera cudzysłowu ani znaku nowej linii, które rozwaliłyby linię.

To weryfikacja plików, nie test w grze.

## Status testów

Plaster zbudowany i zainstalowany, oryginał w kopii zapasowej. **W grze jeszcze niesprawdzony.** Otwarte pytania, na które odpowie dopiero uruchomienie:

1. czy przejęty slot faktycznie wczytuje nasz plik,
2. czy polskie znaki się rysują — wpisy 3–10 to nazwy pięter wielkimi literami z `Ń`, `Ż`, `Ł`, `Ź`, dobrane właśnie pod ten test,
3. czy wybór języka zapisuje się między uruchomieniami,
4. czy dłuższe polskie napisy mieszczą się w interfejsie.

## Materiał gry

Katalog zawiera wyłącznie teksty tłumaczenia i narzędzia — żadnych plików gry. Nic tu nie jest powiązane z autorami *OTXO* ani przez nich firmowane; gra, jej teksty i postacie należą do nich.

## Licencja

[MIT](../../LICENSE), jak reszta repozytorium.
