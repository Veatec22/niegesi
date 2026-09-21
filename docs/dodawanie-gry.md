# Dodawanie nowej gry

Konwencje, których trzymają się wszystkie tłumaczenia w tym repozytorium. Celem jest to,
żeby po roku dało się wrócić do dowolnego tytułu i od razu wiedzieć, gdzie co leży.

## Katalog

Nowa gra to `games/<slug>/`, gdzie `<slug>` to nazwa gry małymi literami z myślnikami
(`shotgun-cop-man`, `anger-foot`). Bez sufiksu `-pl` — całe repozytorium jest polskie.

Minimalna zawartość:

| Ścieżka | Zawartość |
| --- | --- |
| `README.md` | Tylko instalacja dla gracza, po polsku — pokazuje się w panelu gry na stronie. Wzór: `games/shotgun-cop-man/README.md`. |
| `docs/technika.md` | Co obejmuje tłumaczenie, jak gra trzyma teksty, co build podmienia, czego nie rusza, budowanie, stan testów, nota o materiale gry. |
| `docs/INSTALL.txt` | Instrukcja dla gracza: instalacja, przywracanie oryginału, zgodność z wersją gry, zakres. Zwykły tekst, trafia do paczki jako `READ-ME.txt`. |
| `tools/build.py` | Budowanie plików gry z oryginałów. |
| `translations/pl.json` | Polskie teksty. |
| `translations/en-pl-review.json` | Angielski oryginał obok tłumaczenia, do korekty. |

Katalog `dist/` powstaje przy budowaniu i jest ignorowany przez Gita.

## Zasady dla `tools/build.py`

- `ROOT = Path(__file__).resolve().parents[1]` — ścieżki do `translations/` i `docs/`
  liczone od katalogu gry, nie od miejsca uruchomienia.
- Oryginały przypięte przez SHA-256 na górze pliku. Niezgodność = wypisanie oczekiwanej
  sumy i wyjście bez zapisu czegokolwiek.
- Domyślne wyjście: `ROOT / 'dist'`. Nigdy katalog gry.
- Build nie instaluje, nie uruchamia gry i nie pisze niczego poza katalogiem wyjściowym.
- Na końcu weryfikacja: liczba wpisów na wejściu i wyjściu, nienaruszone pozostałe języki,
  obecność polskich tekstów. Build, który nie potrafi udowodnić, że nic nie zepsuł,
  jest do poprawki.

## Format `translations/`

`pl.json` ma klucze takie, jakich używa gra — identyfikator terminu, path ID zasobu,
cokolwiek jest w danym silniku naturalne. Klucz wymyślony na potrzeby tłumaczenia to
dodatkowa warstwa do pomylenia.

`en-pl-review.json` niesie ten sam klucz, angielski oryginał, polskie tłumaczenie i notatkę
kontekstową z oryginału, jeśli gra taką trzyma. Zmiana tekstu w `pl.json` idzie w parze
ze zmianą w pliku korektorskim.

## Testowanie na własnej instalacji

`tools/install.py` podmienia pliki w katalogu gry na zbudowane, a oryginały odkłada
do `backups/<slug>/` (katalog ignorowany przez Gita). Plik, który ma już kopię, nie jest
kopiowany drugi raz, więc dwukrotne uruchomienie nie nadpisze dobrych oryginałów
załatanymi. To narzędzie służy wyłącznie do testów autora — gracz dostaje paczkę
do przeciągnięcia, nie skrypt.

```powershell
.venv\Scripts\python.exe tools\install.py --game "<katalog *_Data gry>" --built games\<slug>\dist\<Nazwa>_Data --backup backups\<slug>
.venv\Scripts\python.exe tools\install.py --game "<katalog *_Data gry>" --backup backups\<slug> --restore
```

## Po dodaniu

Dopisz grę do tabeli w [README.md](../README.md) — zakres, wersja, status testów.
