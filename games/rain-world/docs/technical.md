# Rain World — ustalenia techniczne

## Stan

- **Etap:** pełne tłumaczenie 0.2.0 zbudowane, zainstalowane do testu (`tools/install.py`)
  i wystawione na stronie (`site/public/pobierz/Rain-World-PL-0.2.0.zip`, 356 KB).
  Vertical 0.1.0 sprawdzony w grze przez użytkownika (2026-09-24: „działa”).
- **Zakres:** 4913/4913 wpisów — 2473 wpisy `strings.txt` (+ `POLISH` na przycisk języka),
  1654 linie rozmów, odczytów pereł, ech, czatlogów i transmisji oraz 787 linii komentarza
  twórców Downpour; razem ok. 62 tys. słów, 401 plików rozmów w `text_pol`.
- **Poza zakresem:** minigra Inv (`mods/moreslugcats/content/text_eng`, istnieje tylko po angielsku
  we wszystkich językach gry), napisy końcowe (`text/credits` — nazwiska, gra ich nie tłumaczy),
  grafiki z napisami. `mods/watcher/pearls` i `pearlslides` to skrypty animacji, bez tekstu.
- **Następny krok:** review językowy zrobiony (`docs/localization-review.md`); test pełnej wersji
  w grze (lista w odpowiedzi do użytkownika i w `docs/translation-decisions.md`).

## Istniejące spolszczenia (sprawdzone 2026-09-23)

- [Polish Translation](https://steamcommunity.com/sharedfiles/filedetails/?id=3465699028) na Steam
  Workshop (Astronomia, 17.04.2025): tylko podstawka, zastępuje angielski, Downpour zapowiedziany.
  Publiczny według API Steama. Dla wersji GOG niedostępny oficjalną drogą.
- spolszczeniemax.com: wpis o „REPT” z 2017 bez działającego linku — agregator, nie liczymy.
- [Ukrainian Localization](https://steamcommunity.com/sharedfiles/filedetails/?id=3761321599) —
  pełne tłumaczenie z DLC jako mod Workshop; dowód, że osobny język przez mod działa. Źródeł nie znalazłem.
- Polska wersja oficjalnej wiki (Miraheze) — źródło nazewnictwa, patrz biblia.

## Gra

- GOG v1.11.8 (build 59599002084023645), Downpour 1.9.16, The Watcher. Unity 2020.3.45, Mono, x64.
- Gra ma **własnego BepInEksa 5.4.17** z MonoMod i `BepInEx.MultiFolderLoader`. Pluginy ładują się
  wyłącznie z włączonych modów: `StreamingAssets/mods/<id>/plugins/*.dll`, lista w
  `StreamingAssets/enabledMods.txt` (ustawia ją menu REMIX). `BepInEx/plugins` gra czyści według
  `whitelist.txt`, więc tam nic nie kładziemy.
- Dodatki (moreslugcats = Downpour, watcher, expedition, jollycoop, rwremix) to też mody w `mods/`;
  gracz włącza je w REMIX.
- `mscorlib` nie jest okrojony — BepInEx gry już działa (jest `BepInEx/LogOutput.log`).

## Jak gra trzyma teksty

Kod: `InGameTranslator`, `Conversation.LoadEventsFromFile`, `Menu.OptionsMenu`.

- **Języki** to `InGameTranslator.LanguageID : ExtEnum` — da się dopisać nowy w czasie działania.
  Folder tekstów: `text/text_` + trzy pierwsze litery nazwy (`LocalizationTranslator.LangShort`),
  czyli dla `Polish` → `text_pol`. Zapis w opcjach trzyma nazwę (`Language<optB>Polish`).
- **strings.txt** — linie `klucz|tekst` rozdzielone CRLF, pierwszy znak pliku to znacznik
  (`0` otwarty, `1` szyfrowany; dziś wszystkie są otwarte). Kluczem jest angielski tekst wpisany
  w kod albo identyfikator (`tips-distract`, `mod_menu_restart`). `LoadShortStrings` wczytuje
  najpierw angielski, potem bieżący język — **ale tylko, jeśli `StreamingAssets/text/text_<jęz>/strings.txt`
  istnieje w podstawce**; pliki z modów dochodzą dopiero za nim. Dlatego plugin doczytuje nasz
  plik sam (postfix na `LoadShortStrings`). `Translate` przy braku klucza zwraca argument, więc
  czego nie ma po polsku, zostaje po angielsku.
- **Rozmowy** — `text_<jęz>/<N>[-<postać>].txt`, zaszyfrowane XOR-em: `Custom.xorEncrypt(tekst,
  54 + N + indeks_języka * 7)` (nazwy bez liczby: suma `znak - '0'` po nazwie), potem pierwszy
  znak zamieniony na `1`. Klucz to wycinek `[54:54+1447]` literału `RWCustom.Custom.encrptString`;
  `rw.py` czyta go z Assembly-CSharp i sprawdza na `1.txt`, nie trzymamy go w repo.
  Plik zaczynający się od `0` gra czyta bez deszyfrowania — nasze pliki są otwartym tekstem.
  Brak pliku w danym języku → gra sama bierze angielski („RETRY WITH ENGLISH”).
  Linia rozmowy może mieć instrukcje: `N : N : tekst`, `N : tekst : N`, `SPECEVENT : …`,
  `PEBBLESWAIT : N`; `<LINE>` to łamanie wiersza. `rw.split_dialogue_line` oddziela tekst od instrukcji.
- Jedyna kolizja nazw między podstawką a dodatkami: `36.txt` — w obu „NOT IN USE”.
- **Nazwy regionów** (`world/<reg>/displayname.txt`) gra tłumaczy przez `strings.txt`
  (`Outskirts|Окраина` w rosyjskim), więc są zwykłymi wpisami `str:`.
- **Fonty:** nieznany język dostaje podstawowe `font` i `DisplayFont` (`InGameTranslator.LoadFonts`),
  a te mają komplet polskich liter (sprawdzone na opisach BMFont w `resources.assets`). Grafik
  z tekstem zależnych od języka gra nie ma.
- **Menu opcji** buduje przyciski języków ze sztywnej tablicy `OptionsMenu.languageOrder`
  (10 języków, dwie kolumny po 220 px, wiersze co 40 px). Etykieta przycisku to
  `Translate(nazwa.ToUpper())` — stąd dodatkowy wpis `POLISH|POLSKI`.

### Czatlogi, transmisje i komentarz twórców (Downpour)

- `MoreSlugcats.ChatlogData.DecryptResult` deszyfruje czatlogi, transmisje Włócznika (`lp_*`)
  i komentarz twórców **bezwarunkowo**, kluczem z indeksem bieżącego języka, czyta przez
  `Encoding.Default` i pomija pierwszą linię (nagłówek). Plugin ma prefix: tekst zaczynający się
  od `0` zwraca bez zmian. Nasze pliki mają więc w pierwszej linii `0-<nazwa>`, dalej otwarty tekst.
- Ścieżka komentarza (`DevCommPath`) przy braku pliku w języku spada na angielski — tak samo
  rozmowy. Rosyjskie pliki komentarza to 28-bajtowe zaślepki: oficjalnie komentarza nikt
  nie tłumaczył, my tłumaczymy.
- Kolor mówiącego w czatlogach bierze się z `colors.txt` przez `Translate(kod)`
  (`Conversation.InitalizePrefixColor`), więc przetłumaczone kody iteratorów (SCS, BZN, PK…)
  są też wpisami `strings.txt` i muszą zgadzać się z prefiksami linii.

## Jak dostarczamy

Mod Remix `niegesi-polski` (`RainWorld_Data/StreamingAssets/mods/niegesi-polski/`):

| Plik | Po co |
| --- | --- |
| `modinfo.json` | Opis dla menu REMIX. Bez `target_game_version` — brak pola = bieżąca wersja, nic nie przypinamy. |
| `plugins/NieGesiRainWorld.dll` | `plugin/Plugin.cs`: rejestruje `LanguageID("Polish")`, dopisuje go do `languageOrder` (transpiler po nazwie pola), doczytuje `text_pol/strings.txt`, przepuszcza otwarte czatlogi przez `DecryptResult`, loguje wersję gry i Unity oraz każdy tekst bez polskiego wpisu. |
| `text/text_pol/strings.txt` | Polskie wpisy `klucz|tekst`, znacznik `0`. |
| `text/text_pol/<plik>.txt` | Rozmowy, perły, echa, czatlogi, transmisje i komentarz twórców: angielski plik z podmienionymi liniami, otwarty tekst ze znacznikiem `0`. |

Paczka nie zawiera BepInEksa (gra ma własny) ani żadnego pliku gry — build to sprawdza.
Gracz włącza mod w REMIX i wybiera język w opcjach. Wyłączenie moda przy wybranym polskim
zostawiłoby w opcjach nieznany język, stąd w instrukcji: najpierw przełącz na angielski.

## Budowanie

```powershell
.venv\Scripts\python.exe games\rain-world\tools\extract.py      # work/en.json z gry (+ mapa literałów)
.venv\Scripts\python.exe games\rain-world\tools\build.py        # dist/niegesi-polski + dist/Rain-World-PL-<wersja>.zip
.venv\Scripts\python.exe games\rain-world\tools\review.py       # translations/en-pl-review.json
.venv\Scripts\python.exe games\rain-world\tools\install.py      # test: kopia moda do gry (--remove usuwa)
```

`extract.py` kompiluje `tools/StrMap.cs` (Mono.Cecil z katalogu gry) i dopisuje do każdego wpisu
klasy, w których tekst stoi w kodzie — to kontekst dla tłumacza i podstawa wyboru próbki.
Klucze w `pl.json`: `str:<klucz strings.txt>` i `dlg:<plik>#<linia>`.

Build odmawia paczki, gdy tłumaczenie gubi znacznik (`<PlayerName>`, `{ERROR}` itd.),
ma znak nowej linii zamiast `<LINE>` albo `|` w tekście.

## Test w grze

- **Vertical 0.1.0** — sprawdzony przez użytkownika 2026-09-24: język POLSKI w opcjach, menu,
  początek Obrzeży.
- **Pełne 0.2.0** — po review językowym (`docs/localization-review.md`, 98 poprawek) zbudowane i zainstalowane, test w grze czeka. Kroki i miejsca najmniej pewne:
  `docs/translation-decisions.md`, sekcja „Mniej pewne”.

## Tłumaczenie

Partie w `work/batches/` (ignorowane) przez `tools/batch.py make|show|merge|status`;
biblia w `translations/bible.yaml`, decyzje w `docs/translation-decisions.md`,
raport kontrolny w `work/l10n-report.md`.

## Nota o materiale gry

`work/` (ignorowany) trzyma odszyfrowane teksty gry i zrzut literałów z Assembly-CSharp —
tylko do analizy. Do repozytorium i paczki trafiają wyłącznie nasze tłumaczenia i kod.
