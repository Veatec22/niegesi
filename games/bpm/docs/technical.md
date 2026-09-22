# BPM: Bullets Per Minute — technika i stan prac

## Stan: 1.0, pełne tłumaczenie (2026-09-22)

859/859 wpisów. Vertical (menu, ustawienia, HUD, początek gry, polskie litery,
nazwa „Polski” na liście) potwierdzony w grze przez użytkownika. Pełna wersja
zainstalowana aplikatorem z paczki na GOG; przedmioty, próby, dalsze krainy
i napisy końcowe czekają na przejście. Agent nigdy nie uruchamia gry.

Wersja źródłowa: GOG, build `55844760674411649`, `C:\Games\BPM BULLETS PER MINUTE`.

## Istniejące spolszczenia

Oficjalnie brak polskiego — Steam wymienia EN, FR, IT, DE, ES, PT, RU i chiński
uproszczony (w plikach jest też koreański). Nie znaleziono dostępnego fanowskiego
spolszczenia: GRYOnline.pl ma dla gry tylko trainer, na forach Steama są prośby
o rosyjski sprzed oficjalnego wydania, bez narzędzi. Wyszukiwarki twierdzą, że gra
„ma polski” — to nieprawda, sprawdzone w tabeli języków sklepu.

## Silnik i archiwa

Unreal Engine 4 (gildor.org: 4.25; paki mają wersję 11). Jedenaście paków
`pakchunk0*-WindowsNoEditor.pak`, każdy z plikiem `.sig` — **podpisywanie paków
włączone**. Wpisy nieskompresowane (brak nazw metod kompresji w stopce).

**Indeks jest szyfrowany AES-256.** Klucz podawany w sieci
(`766D2004…`) jest fałszywy. Prawdziwy wyciągnięty z exe: kod wpisuje go ośmioma
instrukcjami `mov dword [reg+disp], imm32` przeplatanymi innymi, pod `.text+0xddc33b`.
Klucza nie trzymamy w repo — leży w `work/aes.key` (ignorowany), odtwarzalny skanem
opisanym wyżej. `tools/game_pak.py` czyta indeks i wyciąga pliki.

## Teksty

`BPM/Content/Localization/Game/<kultura>/Game.locres`, wersja 3, 859 wpisów,
~2,3 tys. słów (menu, ustawienia, HUD, przedmioty, podpowiedzi, imiona walkirii,
napisy końcowe). Kultury: en, de, es, fr, it, ko, pt, ru, zh-Hans-CN.
`Game.locmeta` w wersji 0 — bez listy skompilowanych kultur, kultury wykrywa się z katalogów.

## Wybór języka

Język ustawia kod C++ gry: `SetUILanguage(EBPMLanguage)`, enum ma dziesięć pozycji
w stałej kolejności en, fr, it, de, es, **ja**, pt, ru, zh-Hans-CN, ko (tabela kultur
w exe obok `SettingsSaveGameName`). Nowej pozycji nie da się dopisać bez kodu.
`WBP_UISettingPanel` (w `pakchunk0_s10`) bierze listę z `GetLocalizedCultures`
i nazwy z `GetCultureDisplayName`.

Slot **ja** istnieje w enumie, a gra nie ma japońskiego `Game.locres`. Polski tekst
leży więc w `Localization/Game/ja/Game.locres` nakładkowego paka — żaden istniejący
język nie znika. Nazwa na liście pochodzi z ICU: w `icudt64l/lang/en.res` jest jeden
samodzielny napis UTF-16 „Japanese” (nazwa języka `ja` i pisma `Jpan`). Build nadpisuje
go w miejscu na „Polski” dopełnione zerami, więc żadne przesunięcie w pliku się nie
zmienia. To dane Unicode dołączone do silnika, nie treść wydawcy.

Osobny język `pl` nie zadziała: `StoreSettings` zamienia wybraną kulturę na enum
i nieznaną zapisuje jako angielski. Dopisanie pozycji wymagałoby zmiany exe albo
wstrzykiwanej biblioteki (jak UE4SS w Holy Shoot).

## Fonty — brak polskich liter

Żaden font gry nie ma ąćęłńśźż (MotorBlock, Proletariat, RunyTunes, NotoSansJP;
ó/ń tylko w części). Font zapasowy kompozytów `DroidSansFallback` też ich nie ma —
w grze brakujące litery wychodzą jako romb ze znakiem zapytania.

## Polskie litery w fontach

Licencje: MotorBlock (Branum Design) i Proletariat (Peter Wiegel) — „All rights
reserved”; RunyTunes Revisited NF (Nick's Fonts) wprost zakazuje utworów pochodnych;
NotoSansJP — OFL. Paczka nie może więc nieść glifów tych fontów.

`tools/fonts_pl.py` dokłada do `.ufont` 16 liter (ąćęłńśźż + wielkie) jako glify
złożone: odwołanie do litery bazowej fontu (po indeksie) + znak diakrytyczny
narysowany przez nas z kilku punktów (akcent, kropka, ogonek, kreska). Dodane dane
glifów są w całości nasze. Plik wynikowy to jednak cały font z dodatkami — do gracza
trafia przez łatkę, która kopiuje resztę z paka gry na jego dysku.

Font otwieramy z `recalcBBoxes=False`: inaczej fontTools przy zapisie rozkodowuje
i koduje od nowa każdy glif, a łatka musiałaby nieść ich kontury (RunyTunes: 6,6 KB).
Ramki i limity `maxp` nowych glifów liczymy sami z kopii litery bazowej. Po tej
zmianie łatka wnosi do każdego fontu ~800 B nowych glifów plus metadane (cmap,
hmtx, loca, nazwy glifów) — żadnego konturu wydawcy.

Dotyczy fontów runtime: `MotorblockFontRuntime` (25 widżetów: menu, HUD, napisy
końcowe) → `MotorBlockFinalCyr`; `RunyTunesRuntime` (przejścia poziomów, pasek bossa)
→ `RunyTunesRevisitedNF`. `NotoSansJP-Bold_Font` służy tylko testowi rytmu, którego
teksty nie są w `Game.locres`. Font offline `MotorblockFontOffline` (bitmapa) — tylko
`BP_BankOut`.

`tools/render.py` rysuje próbkę tekstu do PNG do oceny kształtów.
`tools/uasset.py` czyta i zapisuje małe pakiety UE4.25 (bajt w bajt przy braku zmian) —
zostaje na wypadek podkrojów w assetach `Font`; w buildzie nieużywany.

## Budowanie i paczka

```powershell
.venv\Scripts\python.exe gamespm	ools\extract.py "<BPM>\WindowsNoEditor"
.venv\Scripts\python.exe .claude\skills\localization\scripts\l10n_report.py gamespm
.venv\Scripts\python.exe gamespm	oolsuild.py
.venv\Scripts\python.exe gamespm	oolselease.py "<BPM>\WindowsNoEditor" 1.0
```

`extract.py` sam znajduje klucz AES w exe i wyciąga do `work/extract` angielski
locres, dwa fonty, `en.res` oraz locresy innych języków (tylko jako odniesienie).
`build.py` → `dist/BPM-PL_P.pak` (locres `ja` z `translations/pl.json`, dwa fonty
z polskimi literami, `en.res` z nazwą „Polski”); wejścia przypięte sumami
w `tools/sources.json`.

`release.py` składa `dist/BPM-PL-<wersja>-latka.zip` (45 KB): dwie łatki formatu 3
(`tools/patch.py`), aplikator `BPM-PL-<wersja>.exe` i `READ-ME.txt` z `docs/INSTALL.txt`.

- Łatka paka tworzy `BPM-PL_P.pak`. Źródło to trzy wycinki `pakchunk0-WindowsNoEditor.pak`
  gracza (dwa `.ufont` i `en.res`, położenie z odszyfrowanego indeksu, wpisy
  nieskompresowane i niezaszyfrowane, dane za 53-bajtowym nagłówkiem wpisu).
  Wnosi 72 KB własnych bajtów: 66 KB to nasz locres, reszta to nowe glify i metadane.
- Łatka podpisu tworzy `BPM-PL_P.sig` jako kopię `pakchunk0_s4-WindowsNoEditor.sig`
  gracza — zero własnych bajtów.

Sumy kontrolne liczone są z wycinków, więc łatka przypina tylko te fragmenty paka,
nie cały 3 GB plik. Wydanie Steam może mieć paki ułożone inaczej — wtedy aplikator
odmówi pracy bez zmian na dysku; niesprawdzone.

Test aplikatora (2026-09-22, GOG): utworzone pliki identyczne co do bajta z buildem,
przywrócenie usuwa oba, ponowne nałożenie i tryb dwukliku z katalogu gry działają.

## Wyniki testów w grze (użytkownik)

- 2026-09-22: sam pak bez `.sig` — gra go ignoruje (PLAY bez zmian, bez błędu).
- 2026-09-22: ten sam pak + `.sig` skopiowany z `pakchunk0_s4` — **montuje się**:
  nadpisany angielski locres pokazuje „GRAJ (TEST EN)” na ekranie wyboru postaci.
  Niezgodność sum bloków z podpisem nie blokuje gry. Font MotorBlock wyświetla
  wielkie litery i nawiasy poprawnie.

- 2026-09-22: pak z `ja` i `pl` — oba języki są na liście (lista jest alfabetyczna,
  więc nowe pozycje lądują w środku). Wybór „Polish” daje angielski: `StoreSettings`
  nie zna `pl` i zostawia `LanguageId = 0`.

- 2026-09-22: wybór „Japanese” — **polski tekst działa** (Język, Gra, Dźwięk po polsku),
  ustawienie trzyma się po zapisie. Litery spoza fontu (ę, ź…) jako romb ze znakiem
  zapytania; ó jest. Pozycja na liście nadal nazywa się „Japanese”.
- 2026-09-22: fonty z dorysowanymi literami — „teraz jest elegancko”.
- 2026-09-22: vertical 513/859 wpisów (menu, ustawienia, HUD, początek gry) — zaakceptowany.

## Jak menu buduje listę (bajtkod, `tools/kismet.py`)

`ExecuteUbergraph_WBP_UISettingPanel`: pętla po `GetLocalizedCultures(Game)`, pozycja =
`GetCultureDisplayName(kultura, true)`. `StoreSettings`: kultura wybranej pozycji →
`EBPMLanguage` przez switch en/fr/it/de/es/ja/pt/ru/zh-Hans-CN/ko, domyślnie 0 (English),
potem `SetUILanguage`. `LoadSettingsIntoWidgets`: odwrotnie, enum → kultura → indeks.
Wniosek: polski musi siedzieć w katalogu `ja`; nazwę pozycji daje ICU
(`Engine/Content/Internationalization/icudt64l/lang/*.res`).

## Następny krok

1. Test pełnej wersji 1.0 i nazwy „Polski” na liście języków — punkty w
   `docs/translation-decisions.md`, sekcja „Mniej pewne”.
2. Czy wystarczy własny, sztuczny `.sig` — pozwoliłoby to obejść się bez łatki podpisu.
3. Wydanie Steam: czy układ `pakchunk0` jest taki sam jak na GOG.
