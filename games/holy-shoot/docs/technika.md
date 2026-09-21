# Holy Shoot — analiza 2026-09-21

## Stan: pełne tłumaczenie 0.2.0 (1286/1286)

Vertical potwierdzony w grze na 0.1.2/0.1.3: Polski w selektorze od startu, wybór
zostaje po restarcie, teksty z paka się wyświetlają. 0.2.0 niesie wszystkie 1286
wpisów; mechanizm bez zmian poza usunięciem zapasowego odpytywania w Lua (log 0.1.3
potwierdził, że pierwszy zadziałał prehook `Create`). Pełne przejście gry czeka.

Tłumaczenie: `tools/batch.py` (`show`, `put` plików `przestrzeń|klucz @@ tekst`,
`from-review`), partie w `work/tsv/` (poza gitem, jak cały `work/`). Źródłem jest
`translations/pl.json` — mapa `"przestrzeń|klucz": "tekst"`. `en-pl-review.json`
jest z niej generowany razem z angielskim oryginałem; poprawki wprowadzone w nim
przenosi `batch.py from-review`, a build odmawia pracy, gdy oba pliki się rozjadą.
Teksty diagnostyczne twórców bez przestrzeni nazw (`Steam Stat Saved…`, `MapOrigin…`)
są przepisane dosłownie. Standard: skill `lokalizacja`, biblia `translations/biblia.yaml`,
decyzje `docs/decyzje-tlumaczenia.md`, raport `work/l10n-report.md`.

## Jak działa paczka

Trzy części, żadna nie podmienia pliku gry:

1. **`pakchunk99-NieGesiPL_P.pak`** z jednym plikiem
   `PVD/Content/Localization/Game/pl/Game.locres` (tylko przetłumaczone wpisy).
2. **Pusty kontener IoStore** `pakchunk99-NieGesiPL_P.utoc`/`.ucas` (202 i 64 bajty),
   `tools/iostore_empty.py`. Bez niego UE 5.7 tego paka nie montuje: w 0.1.2
   `FileExists` widział `en/Game.locres` gry, a naszego `pl/Game.locres` nie.
   Kontener ma jeden chunk, pusty nagłówek kontenera (wersja 5, zero pakietów).
   Układ TOC v8 i nagłówka skopiowano z `PVD-Windows.utoc` gry; build odczytuje
   wynik z powrotem. Bez kompresji, indeksu katalogów, szyfrowania i podpisu.
3. **UE4SS + `plugin/main.lua`**: dopisuje Polski (kod `pl`, indeks 10) do
   szablonów, z których gra buduje menu: domyślny obiekt panelu
   `WB_T1_PVDSettingsMenu_C` („Language Codes”), kopie panelu osadzone
   w szablonach `WB_T1_PVDMainMenu` i `WB_T1_PVD_PauseMenu` oraz szablon
   przełącznika `WB_T1_OptionSwitcher_Language` („Option Names”).
   Wyzwalacz: prehook `UWidgetBlueprintLibrary::Create` (blueprinty tworzą nim
   menu); szablon menu pauzy, wczytywany później, łata kolejne wywołanie. Zapis wyboru i zmianę kultury
   robi sama gra (`SetCurrentLanguageAndLocale`, savegame NiceSettings).

### Czego się nauczyliśmy (żeby nie powtarzać)

- `NotifyOnNewObject` na klasach blueprintów i hooki na `Construct`/`OnInitialized`
  w tej grze nie zadziałały ani razu.
- Patchowanie gotowego menu jest za późne: przełącznik buduje wskaźnik (kreski)
  z liczby opcji przy tworzeniu, a zapisany indeks 10 bez kodu w mapie daje
  „OPTION MISSING” i powrót do `en`. Trzeba zmieniać szablony przed utworzeniem.
- Parametr `-culture=pl` (0.1.0) nie jest instalacją — nie spełnia verticala.

UE4SS **v3.0.1-1140-gf58e8f84**, MIT; archiwum runtime SHA-256
`b954f036b10e9abb0c0c41599311ab1accc53e30515aeed7e48ee22c5b3b1280`.
[Wydania](https://github.com/UE4SS-RE/RE-UE4SS/releases),
[źródło przypiętej wersji](https://github.com/UE4SS-RE/RE-UE4SS/tree/f58e8f84).
W paczce tylko loader (`dwmapi.dll`, który gra importuje), `UE4SS.dll`,
ustawienia z wyłączonymi konsolami i licencja; bez modów cheat/debug.

### Fonty

Zbadano cmap trzech BebasPro (Regular/Bold/BoldItalic) i obu łacińskich NotoSans
(Regular/BoldItalic). Każdy zawiera `ąćęłńóśźżĄĆĘŁŃÓŚŹŻ`; .ufont ma czterobajtowy
nagłówek długości przed OTF/TTF. Nie potrzeba dołączać cudzego fontu.
Polskie litery w menu i ustawieniach potwierdzone w grze na próbce.

### Build i testy

`.venv/Scripts/python.exe games/holy-shoot/tools/build.py` — sprawdza runtime UE4SS,
odczyt locres, paka i kontenera IoStore oraz listę 12 plików ZIP bez zasobów gry.
Wynik: `dist/Holy-Shoot-PL-0.2.0.zip` i `build-report.json`.
`tools/test_selector.py` (zależność `lupa`) sprawdza logikę Lua na atrapach:
patch szablonów, brak duplikatów, szablon pauzy wczytany później, zmieniony
schemat. To nie jest test w grze.

## Źródła i werdykt

[Steam](https://store.steampowered.com/app/2881660/?l=polish) oznacza polski jako nieobsługiwany. Wyszukiwania „Holy Shoot” + spolszczenie, translation mod, tradução i українізатор nie przyniosły dostępnej paczki PL ani przydatnego tłumaczenia fanowskiego. Nie jest to dowód, że nigdy nie powstały.

Warto ruszać: teksty dają się odczytać, są w standardowym locres. Vertical z próbką 37 z 1286 wpisów potwierdzony w grze.

## Instalacja i format

Lokalnie `C:\SteamLibrary\steamapps\common\Holy Shoot`, Steam app 2881660, build 24334618. `DefaultGame.ini` podaje v.r.1.0.002; nie jest to wersja potwierdzona w menu. EXE zawiera UTF-16 `++UE5+Release-5.7`.

`Windows/PVD/Content/Paks/PVD-Windows.pak` ma format 12, nieszyfrowany indeks, mount `../../../`, 4614 plików. Towarzyszą mu IoStore `.utoc/.ucas`; teksty nie wymagają ich edycji. Angielski `PVD/Content/Localization/Game/en/Game.locres` ma 108883 bajty, format 3 i 1286 wpisów. Liczba obejmuje także placeholdery i teksty diagnostyczne, nie tylko teksty gracza.

Czytnik paka pochodzi ze SPRAWL-a, z lokalnym dopuszczeniem zbadanego formatu 12. Dekompresja korzysta z lokalnej biblioteki Oodle FModela; biblioteka nie trafia do paczki. Konfiguracja ma InternationalizationPreset=All. Manifest zawiera fonty Roboto i fallbacki silnika, ale nie dowodzi to obsługi polskich znaków w rzeczywiście używanym foncie UI.

## Odtworzenie

Uruchom z katalogu repo `.venv\Scripts\python.exe games/holy-shoot/tools/extract.py --pak "C:\SteamLibrary\steamapps\common\Holy Shoot\Windows\PVD\Content\Paks\PVD-Windows.pak" --oodle "<lokalny oodle-data-shared.dll>"`, następnie `.venv\Scripts\python.exe games/holy-shoot/tools/build.py`.

Build używa istniejących kodeków SPRAWL-a, zapisuje pak v11 z jednym częściowym zasobem `pl/Game.locres`, weryfikuje odczyt locres i paka, zgodność review i identyfikatorów oraz placeholdery. ZIP niesie ten pak, pusty kontener IoStore, UE4SS z naszym skryptem i READ-ME.txt. Nie niesie tekstur, scen, bibliotek gry ani pozostałych tekstów. Brak wpisu zostawia natywny angielski tekst (potwierdzone w grze).
