# Boomerang X — technika i stan prac

## Stan: próbka 0.1 metodą łatania bajtów

38 z 360 wpisów przetłumaczonych. W grze działa wersja podmieniająca
`Assembly-CSharp.dll` (1,8 MB) — opis metody w docstringu `tools/build.py`.

## Metoda pluginowa — zablokowana (20 września 2026)

Plugin jest napisany i kompiluje się poprawnie (`plugin/Plugin.cs`,
`tools/build_plugin.py`). Zastępuje trzy łatki na bajtach trzema łatkami Harmony'ego:

- `localization_manager.get_translation` — podaje nasz tekst zamiast
  „LOCALIZATION ERROR"; dla wpisów nieprzetłumaczonych wraca do angielskiego.
  Uwaga: metoda bierze **cały wiersz tabeli**, nie nazwę tekstu, więc kluczem jest
  `phrase.id`.
- `font_manager.get_font` — podmienia język na rosyjski, jedyny krój z ogonkami.
- `options_screen.on_reading_save_complete` — dopisuje jedenastą pozycję do listy
  języków, przez refleksję, więc działa i z TMP_Dropdown, i ze zwykłym.

Plugin nie rusza pola `description`, które przy łataniu bajtów musiało udawać kolumnę
polską. Nie wymaga też wymieniania notatek między wierszami, żeby tekst się zmieścił.

**Blokadą jest okrojony `mscorlib`.** Gra jest zbudowana z managed strippingiem, więc
preloader BepInEksa wywraca się na `Module.GetPEKind` — dokładnie tak samo jak
Skate Story, mimo że to Unity 2020.1, a tamto Unity 6. Podstawienie kompletu pełnych
bibliotek Unity 2020.1.17 przez `dll_search_path_override` zawiesza grę przed pierwszym
ekranem, identycznie jak w Skate Story.

Wniosek wspólny dla obu gier: droga przez podstawianie bibliotek jest zamknięta.
Pozostaje własna wersja BepInEksa bez tego wywołania albo własny punkt wejścia,
który pomija wykrywanie platformy. Do decyzji.

## Własny punkt wejścia — działa, ale okrajanie sięga głębiej (21 września 2026)

`tools/loader/NieGesiLoader.cs` to nasz zamiennik punktu wejścia BepInEksa: odtwarza
jego `PreloaderRunner.PreloaderPreMain` krok po kroku, tylko platformę ustala sam,
bez `Module.GetPEKind`. Całość idzie przez refleksję, więc biblioteka nie kompiluje się
przeciw BepInEksowi i nie zawiera ani linijki jego kodu.

**Sam punkt wejścia działa bez zarzutu.** Kolejne uruchomienia przechodziły coraz dalej,
za każdym razem wywracając się na następnym elemencie wyciętym z runtime'u gry:

1. `Module.GetPEKind` w `mscorlib` — obejście: nasz punkt wejścia. **Przeszło.**
2. `System.Linq.IGrouping` w `System.Core` — obejście: podstawienie tej jednej
   biblioteki przez `dll_search_path_override`. **Przeszło**, powstał `BepInEx/config`.
3. `AmbiguousMatchException..ctor(string, Exception)` w `mscorlib` — potrzebne
   statycznemu konstruktorowi `HarmonyLib.AccessTools`. **Ściana.**

Trzeciej pozycji nie da się obejść naszą drogą: brakujący element siedzi w `mscorlib`,
a podstawienie pełnej `mscorlib` zawiesza grę przed pierwszym ekranem (sprawdzone tu
i w Skate Story, osobno i w komplecie kilkunastu bibliotek).

Wniosek: **to nie jest jeden brakujący element, tylko cały wycięty runtime.** BepInEx
i Harmony zakładają pełne środowisko .NET; gra budowana z managed strippingiem go nie ma.
Każde obejście odsłania następny brak. Dokładanie bibliotek po jednej to wyliczanka
bez końca, a podstawienie całego rdzenia gra odrzuca.

Co zostaje, gdyby ktoś chciał wrócić do tematu:

- własna wersja BepInEksa i Harmony'ego zbudowana pod okrojony profil — duży projekt,
  wymaga .NET SDK i utrzymywania forka dwóch bibliotek;
- inny mod loader, który nie wymaga pełnego runtime'u (niesprawdzone);
- zostawienie tych gier przy podmianie plików.

Boomerang X zostaje przy próbce 0.1 z łataniem bajtów. Punkt wejścia zostaje w repo,
bo jest sprawny i może się przydać przy grze okrojonej mniej agresywnie.

## Wersja 1.0 — pełne tłumaczenie i dostarczanie łatką (21 września 2026)

359 z 360 wierszy tabeli. Jednego nie da się pokryć osobno, bo **tabela gry ma
zduplikowany klucz** `difficulty_select_prompt` z dwoma różnymi tekstami; oba
dostają to samo polskie zdanie, które pasuje w obu miejscach.

Terminologia mocy: Flux → **Strumień**, Slingshot → **Zryw**, Scattershot →
**Odłamki**, Needle → **Igła**, Blaze → **Żar**, Oblivion Comet →
**Kometa Zapomnienia**.

Tepan mówi bez rodzaju gramatycznego. W oryginale jest konsekwentnie „they",
a polszczyzna wymusza wybór przy każdym czasie przeszłym — kwestie są przepisane
tak, żeby wyboru nie robić („udało mi się zobaczyć" zamiast „widziałem").
To decyzja literacka do potwierdzenia przy korekcie.

Pojemność notatek to 55 843 znaki przy potrzebie około 18 000, więc miejsca jest
z zapasem. 42 wiersze nie mieściły się we własnej notatce i pożyczyły miejsce
od innych — `lend_room` układa to sam.

### Dostarczanie

Plik po spolszczeniu **waży dokładnie tyle co oryginał**, bajt w bajt: 1 806 336 B.
Każda poprawka jest wpisywana na miejsce bajtów tej samej długości, a teksty wchodzą
do istniejących literałów, dopełniane spacjami.

Paczka z całym plikiem ważyłaby 580 KB, ale byłaby w całości cudzym kodem z naszymi
napisami w środku — czyli dokładnie tym, czego zabrania zasada z `AGENTS.md`.
Dlatego wysyłamy **łatki różnicowe: 14 KB na kod i 753 B na czcionki**.

```powershell
.venv\Scripts\python.exe games\boomerang-x\tools\build.py --source backups\boomerang-x\BOOMERANG X_Data\Managed\Assembly-CSharp.dll
.venv\Scripts\python.exe games\boomerang-x\tools\fonts.py --source backups\boomerang-x
.venv\Scripts\python.exe tools\patch.py release --original "backups\boomerang-x\BOOMERANG X_Data\Managed\Assembly-CSharp.dll" --built "games\boomerang-x\dist\BOOMERANG X_Data\Managed\Assembly-CSharp.dll" --relative "BOOMERANG X_Data/Managed/Assembly-CSharp.dll" --original "backups\boomerang-x\BOOMERANG X_Data\resources.assets" --built "games\boomerang-x\dist\BOOMERANG X_Data\resources.assets" --relative "BOOMERANG X_Data/resources.assets" --readme games\boomerang-x\docs\INSTALL-patch.txt --out-dir games\boomerang-x\dist --game-name boomerang-x --package-name Boomerang-X --version 1.1
```

`build.py` nie składa już archiwum — od paczki jest `tools/patch.py release`,
ten sam dla wszystkich gier dostarczanych łatką.

**Paczka ma dwie łatki i obie są konieczne.** Fonty gry prawie nie mają polskich
liter, więc bez fallbacku z `fonts.py` (w `resources.assets`) są kwadraty. Wyszło
21.09, gdy pierwsze wydanie z samym DLL-em trafiło na czystą grę: wcześniejsze testy
szły z `resources.assets` już przerobionym przez `fonts.py` i to maskowało brak.

## Wersja 1.1 — zestaw fontów łaciński zamiast rosyjskiego (21 września 2026)

W 1.0 polskie litery w menu były o połowę za małe („WYBóR", „KOńCA"). Przyczyna
leży w foncie, nie w zamianie na wielkie litery (TMP używa `char.ToUpper`, które
polskie litery obsługuje). Przycisk zestawu rosyjskiego, `Abys-Regular SDF`, ma
**same wersaliki**: `a` i `A` to ten sam kształt. Polskich liter nie ma wcale,
więc wszystkie brał z fallbacku `beer money` jako prawdziwe minuskuły. Wysokość
względem stopnia pisma:

| Font | A | a / o | polskie |
| --- | --- | --- | --- |
| Abys-Regular (przyciski RU) | 0,76 | 0,76 (wersaliki) | brak |
| Dead Stock (przyciski EN) | 0,86 | 0,55 / 0,46 | Ó 0,96, ó 0,65, Ł, ł własne |
| Sure Shot (tekst EN) | 0,71 | 0,39 / 0,38 | Ó, ó, Ł, ł własne |
| beer money (fallback) | 0,57 | 0,35 / 0,35 | wszystkie |

Od 1.1 `get_font` daje polskiemu **zestaw łaciński**, ten sam co angielski.
Menu wygląda jak angielskie (Dead Stock: wersaliki plus kapitaliki), `ó ł` są
z samego fontu, a reszta z fallbacku ma rozmiar zbliżony do kapitalików. Fallbacki
z `fonts.py`: Dead Stock → beer money SDF, obie warstwy Sure Shot - title →
odpowiednie warstwy beer money - title. `Sure Shot SDF` ma `beer money SDF`
w fallbackach od twórców.

Nie da się zwiększyć samych polskich znaków w `beer money SDF` (`TMP_Character.m_Scale`),
bo ten sam font jest fallbackiem zwykłego tekstu, gdzie rozmiar już pasuje. Gdyby
ą ę ś przy przyciskach dalej wyglądały na małe, droga to osobna kopia beer money
tylko dla Dead Stock, ze skalą ok. 1,5.

Aplikator od 1.1 aktualizuje starszą wersję spolszczenia: jeśli plik gry nie jest
oryginałem, ale leży obok odłożona kopia oryginału o właściwej sumie, łatka idzie
na kopię. Sprawdzone na grze z wgraną 1.0.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Boomerang X PL”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

*Part of [Nie gęsi](../../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **Boomerang X** (GOG build). Two original
files are pinned by SHA-256 and the tools refuse anything else:
`Assembly-CSharp.dll` at `1c0ac29aad888faa7439ec57ea7da4976a74c6936aefd7b388a3e9fe904e0b40`
and `resources.assets` at `f663c3c3ba23f7534572f35cf5e8e38fa30846a5d7203aba04b8eb69418dd247`.

**Status: vertical slice installed and seen running. The eleventh language works.
The font gap it exposed has been patched and is waiting on a second look.**
38 of 360 rows are translated, the rest fall back to English.

The first screenshot showed `Polski` as the eleventh entry, `Język:` correct,
and the category buttons rendering `UłATWIENIA` and `D□WI□K` — the button font
has `ł` and `ó` but no `ą ć ę ń ś ź ż`. See *Fonts*. Two fonts have since been
given a fallback to `beer money SDF`; that has not been looked at in the game yet.

### How the game stores text

There is no data file. All 360 rows of the localization table are IL inside one
method, `SheetData.Init`, which builds an array of `Data` objects. Every row is
the same instruction sequence, so [`tools/table.py`](../tools/table.py) reads the
table by walking the IL — no decompiler, no recompile.

`Data` carries `id`, `description`, `max_char_limit`, `asian_char_limit` and
eleven language columns: English, an English source column for the Asian
languages, then French, German, Spanish, Russian, Brazilian Portuguese,
Japanese, Korean, Traditional Chinese, Simplified Chinese. The `language` enum
has ten values plus `LENGTH = 10`.

### Where the Polish lives, and why

A twelfth column is not available: the table's shape comes from `Data`'s field
list, and widening it would mean inserting a field and renumbering metadata.
Taking French away was rejected — the point is an eleventh language, not a
swapped one.

So Polish goes into `description`, the developers' note about each row.
Confirmed by scanning every method body: `description`, `max_char_limit` and
`asian_char_limit` are written by `Data..ctor` and **read by nothing**. The
notes never reach a player and never limit one, and all 360 of them together
hold 55 843 characters against roughly 19 200 needed. Each note is also its own
`#US` entry — checked, no description literal is shared with anything else in
the assembly — so each can be overwritten where it lies.

Seventeen notes are shorter than the row's own English text, and four of them
badly so: `comet_glossary_entry` has 58 characters of note against 232 of
English. Squeezing those would have mutilated the glossary and Tepan's lines.
It is not necessary. A note is dead storage referenced once, by its own row, so
two rows can **exchange** notes by swapping the `ldstr` operands in `Init` —
four bytes each, still no growth. The build does this automatically: a row that
outgrows its note borrows one from a row with room to spare, and the whole
table fits even if the Polish runs 40% longer than the English. In this build
34 rows swapped; `comet_glossary_entry` ended up with 617 characters.

Three code patches then make the game reach for it. All are written over bytes
of the same length, so the file never grows and no metadata moves:

| Patch | Method | Change |
| --- | --- | --- |
| 1 | `localization_manager.get_translation` | The default arm of the switch logged an error and returned `"LOCALIZATION ERROR"` — 16 bytes at file offset 383710. Replaced by `ldarg.1; ldfld Data::description; ret` plus nops. Any language index past the ninth now returns the Polish text. |
| 2 | `font_manager.get_font` | The default arm returned `null`. One byte at 270235 — the `br.s` offset — points it at `russian_font_set` instead. Russian keeps its own arm of the switch and is not affected. |
| 3 | `options_screen.on_reading_save_complete` | Two literal `10`s bound the loops that fill the language dropdown (offsets 372734 and 372783). Both are 11, so index 10 gets an entry and a font. |

### Fonts

`font_set` has five slots and the game picks one per piece of text:
`get_font(0)` is `menu_button_font`, `get_font(1)` is `menu_text_font`, then
trick notifications and the two arena-title layers. Each is loaded lazily by
name — `Resources.Load("Fonts & Materials/" + <name>)` — so the assignment is
data, not code.

Of the eleven font assets in the game, **only the `beer money SDF` family covers
all of `ąćęłńóśźżĄĆĘŁŃÓŚŹŻ`**. `Sure Shot SDF` and `Dead Stock SDF` carry exactly
`ł ó Ł Ó` and nothing else Polish; `Abys-Regular SDF` and the CJK fonts carry
none. All are static atlases (`m_AtlasPopulationMode = 0`), so a missing glyph
is a box unless a fallback supplies it.

The Russian set is the one to borrow, but it is not uniform:

| Slot | Latin set | Russian set | Polish? |
| --- | --- | --- | --- |
| `menu_button_font` | Dead Stock SDF | **Abys-Regular SDF** | no — zero Polish letters |
| `menu_text_font` | Sure Shot SDF | beer money SDF | yes |
| `trick_notification_font` | Dead Stock SDF | **Abys-Regular SDF** | no |
| `arena_title_font` / `_bg` | Sure Shot - title | beer money - title | yes |

That is exactly what the first screenshot shows: `Język:` and `Polski` come from
`menu_text_font` and are correct, while the category buttons drop `ź` and `ę`.

The game already solves this kind of gap by itself: `Sure Shot SDF` carries a
fallback list of `JejuHallasan`, `beer money`, `ardclaowaisongg30` and
`851CHIKARA`, so a Latin menu can still show CJK. `Abys-Regular SDF` and
`Dead Stock SDF` have no fallback list at all. Adding `beer money SDF` to Abys
would fix the Polish buttons and change nothing else, because a fallback is only
consulted for characters the font does not have — today those render as boxes
for everyone. `beer money SDF` is a strict superset of Abys for what Russian
needs (64/64 Cyrillic, 58/58 ASCII letters against Abys's 56/58).

One thing the screenshot does **not** settle: the buttons currently show
`ł` where Abys has no `ł` at all, so they are still on the Latin set's
`Dead Stock SDF`. The text switched to Polish but that font did not follow.
Whether the buttons pick up the Russian set once Polish comes from the save,
rather than from a dropdown change mid-session, needs a restart to tell.

Checked while patching: `menu_option` stores the choice as a plain int under the
name `language` with no clamp, `set_language` does not validate, and the two
loops above are the only places in the assembly that count languages with a
literal ten.

### Building

Requirements: Python 3.11 and the original DLL. The virtual environment lives at
the repository root.

```powershell
.venv\Scripts\python.exe games\boomerang-x\tools\build.py --source "C:\Games\Boomerang X"
```

The build refuses any file that is not the original, so an already patched game
cannot be built from — point `--source` at `backups/boomerang-x` in that case.
Output: `games/boomerang-x/dist/BOOMERANG X_Data/Managed/Assembly-CSharp.dll`
(`dist` is not tracked by Git). It asserts the file size is unchanged, then
re-reads the built DLL and checks every string back out of it, row by row and
in order. `borrowed_room` in the output lists the rows that swapped notes.

The fonts are a separate, one-off step, because it rewrites an 836 MB file:

```powershell
.venv\Scripts\python.exe games\boomerang-x\tools\fonts.py --source "C:\Games\Boomerang X"
```

It adds `beer money SDF` to the fallback list of `Abys-Regular SDF` and
`Dead Stock SDF` and writes `dist/BOOMERANG X_Data/resources.assets`, then reads
every font back to check that the two lists grew, that no other font's list
moved, and that no font's own glyphs changed. The text never needs this step
rerun - only `build.py` does.

Installing for a test, and putting the original back:

```powershell
.venv\Scripts\python.exe tools\install.py --game "C:\Games\Boomerang X" --built games\boomerang-x\dist --backup backups\boomerang-x
.venv\Scripts\python.exe tools\install.py --game "C:\Games\Boomerang X" --backup backups\boomerang-x --restore
```

### Translation files

- [`translations/pl.json`](../translations/pl.json) — row id to Polish text. The build reads only this.
- [`translations/en-pl-review.json`](../translations/en-pl-review.json) — all 360 rows with the English, the Polish, the developers' note as context and the authors' `max_char_limit`. Regenerate with `tools/review.py --source <original DLL>` after editing `pl.json`. Rows not yet translated have an empty `polish`.

### What the vertical covers

38 rows: the main menu, the pause menu, the options screen down to the five
category buttons, the first level's name, the first three tutorial plaques, the
health-platform plaque, and Tepan's first line. Between them they use every
Polish letter — `ąćęłńóśźż` — plus `Ł`, `Ń` and `Ż` in capitals, which the level
name renders. `tutorial_plaque_heal_bottom` is deliberately a full sentence that
does not fit its own note, so the borrowing is exercised somewhere visible.

To test, start the game and go to **Options → Language**. The eleventh entry
should read **Polski**. What the screenshots have to settle:

1. Is there an eleventh entry at all, and is it spelled with a Polish `s`?
2. Does the menu text render with its tails and strokes, or do letters drop out?
3. The level title **WYBRZEŻE ENTACCAŃSKIE** — do the capitals survive?
4. The tutorial plaques, and the health-platform one especially: the borrowed
   note is the only thing giving it room for a whole sentence.
5. Tepan's first line, for the dialogue font and the `|pause|` timing.
6. Quit, restart, and see whether the game comes back in Polish.

### What still has to be proven

- **Nothing has been seen running.** The build verifies bytes, not pixels.
- **The fallback fix has not been seen running.** `Abys-Regular SDF` and
  `Dead Stock SDF` now list `beer money SDF`, which covers every Polish letter,
  but whether TMP actually reaches for it on these screens is the next thing a
  screenshot has to show.
- **The button font did not follow the language.** The text turned Polish while
  the buttons stayed on the Latin set's `Dead Stock SDF`, which Russian never
  uses. Picking the language from the dropdown mid-session may not refresh the
  font the way starting with it saved does. A restart tells which.
- **Two rows share the id `difficulty_select_prompt`** with different English
  text. The build writes the same Polish into both.
- Whether the choice survives a restart, and whether anything outside this table
  is hardcoded English, are open.

### Game material

This directory contains translation text and tooling only — no executables, no
game assets. Nothing here is affiliated with or endorsed by the game's authors;
*Boomerang X*, its text and its characters belong to them.

### License

[MIT](../../../LICENSE), same as the rest of the repository.
