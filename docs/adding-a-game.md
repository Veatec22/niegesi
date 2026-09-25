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
| `docs/technical.md` | Co obejmuje tłumaczenie, jak gra trzyma teksty, co build podmienia, czego nie rusza, budowanie, stan testów, nota o materiale gry. |
| `docs/INSTALL.txt` | Instrukcja dla gracza: instalacja, przywracanie oryginału, zgodność z wersją gry, zakres. Zwykły tekst, trafia do paczki jako `READ-ME.txt`. |
| `tools/build.py` | Budowanie plików gry z oryginałów. |
| `translations/en-pl-review.json` | Jedyny plik tłumaczenia: klucz, angielski oryginał i polski tekst (decyzja 0021). |

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

`en-pl-review.json` to lista wpisów `{key, namespace?, english, polish, context?, note?,
max_length?}` ([0013](decisions/0013-one-review-file-format.md)). Klucz jest taki, jakiego
używa gra — identyfikator terminu, path ID zasobu, cokolwiek jest w danym silniku
naturalne. Klucz wymyślony na potrzeby tłumaczenia to dodatkowa warstwa do pomylenia.
Para `namespace` + `key` jest unikalna. `context` to notatka z oryginału, jeśli gra taką trzyma.

Build czyta teksty przez `tools/translations.py` (`polish_by_key`, `load_entries`).
Jeśli paczka potrzebuje płaskiej mapy, build tworzy ją w `dist/`, nie w repo — druga
kopia polskich tekstów w repo zawsze w końcu się rozjeżdża
([0021](decisions/0021-one-translation-file.md)). Podział na grupy i rozmowy dla pracowni
leży w `translations/structure.yaml` (format w
[specyfikacji](specs/editorial-workspace.md#plik-struktury)).

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

Sprawdź, czy gra otworzy się w pracowni korekty — walidator stosuje te same reguły co
panel i drukuje tabelę stanu wszystkich gier (uruchamia go też workflow „Gry”):

```powershell
npx -y deno run --allow-read tools/check_games.ts
```

Wygeneruj okładkę i galerię na stronę — bez tego kafelek zostaje zastępczą plamą:

```powershell
.venv\Scripts\python.exe tools\keyart.py --list-shots <slug>   # numery zrzutów ze Steama
.venv\Scripts\python.exe tools\keyart.py --game <slug>
```

Skrypt bierze kapsułę sklepu Steam (grafika z logo) na kafelek i zrzuty do karuzeli
w panelu, zapisuje je w `site/public/keyart/<slug>/` (AVIF + WebP) i uzupełnia
w `game.yaml` `steam_appid`, `year`, link do sklepu oraz `gallery`. `gallery` to
numery zrzutów w kolejności slajdów, 4–6 sztuk; domyślnie pierwsze pięć. Wybierz
zrzuty, które pokazują grę, a nie pięć razy broń w korytarzu, popraw listę
i uruchom skrypt jeszcze raz. Grafiki commitujesz razem z grą.
