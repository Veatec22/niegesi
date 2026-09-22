# Anger Foot — technika i stan prac

## Wersja 0.3 — przegląd skillem lokalizacji (2026-09-22)

Tłumaczenie przeszło standard `.claude/skills/lokalizacja`: biblia
(`translations/biblia.yaml`), raport kontrolny (`work/l10n-report.md`) i spis decyzji
(`docs/decyzje-tlumaczenia.md`). Zmieniono 210 wpisów, metoda dostarczania bez zmian.

Tabela gry podaje przy każdej kwestii mówiącego i adresata z płcią, np.
`NPC (Female)` > `Player`. `work/ref-extract.py` zrzuca je razem z rosyjskim,
francuskim, niemieckim i hiszpańskim do `work/ref-all.json` (poza gitem, treść wydawcy):

```powershell
.venv\Scripts\python.exe games\anger-foot\work\ref-extract.py "C:\Games\Anger Foot\Anger Foot_Data\resources.assets"
```

`tools/review.py` składa z tego i z `pl.json` plik `translations/en-pl-review.json`
w formacie repo (`key`, `english`, `polish`, `context`), z kluczem
`<ścieżka> [mówiący > adresat]` — po nim raport sprawdza płeć. Źródłem prawdy dalej
jest `pl.json`; review po każdej zmianie regeneruje się tym skryptem.

Test w grze wersji 0.3: nie robiony, zmiany są wyłącznie tekstowe.

## Wersja 0.2 — metoda pluginowa

1774 z 1776 wpisów tekstowych po polsku; pozostałe dwa są puste również w oryginale.
Spolszczenie dokładane jest w czasie działania gry przez plugin BepInEx.
Żaden plik gry nie jest podmieniany, paczka waży 708 KB zamiast 193 MB.

Użytkownik potwierdził działanie w grze 20 września 2026: przycisk języka na ekranie
tytułowym pokazuje POLSKI, teksty podmieniają się poprawnie.

## Jak gra trzyma teksty

Unity 2019.4.35f1, Mono. Każda kwestia to osobny `LocalizedString : ScriptableObject`
w `resources.assets`, z listą dwunastu tłumaczeń indeksowaną pozycją języka
w kolejności alfabetycznej `LocalizationLanguage.SpreadsheetKey`:

```
CHINESE SIMPLIFIED, CHINESE TRADITIONAL, FRENCH, GERMAN, ITALIAN, JAPANESE,
KOREAN, PORTUGUESE BRAZILIAN, RUSSIAN, SPANISH, SPANISH LATAM, TURKISH
```

Slot włoski (indeks 4) jest **pusty i niedostępny w menu** — rekord języka istnieje,
tekstu nigdy w nim nie było. To jego przejmujemy. `SpreadsheetKey` musi zostać
`ITALIAN`, bo po nim liczona jest pozycja tłumaczenia w każdym wpisie; zmiana
przesunęłaby wszystkie indeksy.

Rekord języka to `LocalizationLanguage : ScriptableEnum` (w `Assembly-CSharp-firstpass.dll`)
z polami `Supported`, `NativeName`, `SpreadsheetKey`, `LanguageTag`, `SteamAPIName`,
`GOGAPIName`, `FontOverride`.

## Co robi plugin

`plugin/Plugin.cs`, dwie łatki Harmony:

- **`LocalizationManager.Initialize` (prefix)** — przemianowuje rekord włoski:
  `NativeName` na „Polski", `LanguageTag` na `pl`, `Supported` na prawdę.
  Dzieje się to przed zbudowaniem listy języków, więc polski pojawia się w menu.
- **`LocalizedString.GetTranslation` (postfix)** — podmienia zwracany tekst,
  gdy aktualnym językiem jest przejęty slot.

Przechwycenie gettera zamiast wypełniania tablic ma tę zaletę, że nie trzeba czekać
na wczytanie zasobów ani wymuszać `EnsureInstancesAreLoaded` — gra pyta, my odpowiadamy.

## Dlaczego GUID, a nie termin

**Terminy w tej grze się powtarzają: 1518 unikalnych na 1776 wpisów.** Rozpoznawanie
kwestii po `Term` podstawiłoby części dialogów cudzy tekst. GUID-y są unikalne
co do jednego (1776/1776), więc plugin mapuje właśnie po nich.

`translations/pl.json` jest kluczowane `path_id` obiektu Unity, którego w czasie gry
nie widać. `tools/build_plugin.py` przy składaniu paczki czyta oryginalny
`resources.assets`, wyciąga dla każdego wpisu GUID i tworzy `pl.tsv` w postaci
`GUID<TAB>tekst`. Źródłem tłumaczenia pozostaje ten sam `pl.json`, co przy starej
metodzie, więc korekty językowe działają bez zmian.

## Budowanie

```powershell
.venv\Scripts\python.exe games\anger-foot\tools\build_plugin.py --game "C:\Games\Anger Foot"
```

Build sprawdza, czy wszystkie przetłumaczone wpisy znalazły swój GUID, czy GUID-y się
nie powtarzają i czy do archiwum nie wpadł żaden plik gry. Wynik: `dist/Anger-Foot-PL-0.3.zip`
oraz archiwum źródeł BepInEksa obok, wymagane przez LGPL.

Plugin nie ma przypiętej sumy kontrolnej gry — wiąże się po nazwach klas, więc
powinien przeżyć aktualizację i działać także na wydaniu ze Steama.

## Poprzednia metoda

Wersja 0.1 podmieniała `resources.assets` i `sharedassets0.assets` (193 MB).
Opis w [README](../README.md) i `docs/INSTALL.txt`. Zostaje jako zapis drogi;
paczki nie publikujemy, bo zawierała przepisane zasoby wydawcy.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Anger Foot PL”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

*Part of [Nie gęsi](../../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **Anger Foot**.

It covers 1774 of the 1776 text entries in the game — menus, settings, tutorials, dialogue, level names, shoes, star goals, achievements, news tickers and credits. The remaining two are empty in the original as well.

### How it works

Anger Foot ships English plus twelve translated languages. One of those twelve, **Italian, is an empty slot**: the language record exists in the files, but only 1 of 1776 texts was ever filled in, and the language is neither selectable nor advertised on the store pages.

This package takes that slot over:

- the Italian `LocalizationLanguage` record is relabelled — `NativeName` becomes `Polski`, `LanguageTag` becomes `pl`, `SteamAPIName` becomes `polish`, and `Supported` is switched on so the language joins the rotation;
- the Polish text is written into the matching translation slot of every text entry.

One field must **not** change: `SpreadsheetKey` stays `ITALIAN`. The game sorts its languages alphabetically by that key and then uses the resulting position as a plain array index into each entry's translations. Renaming the key to `POLISH` moves the language from index 4 to index 6, and every language after it reads somebody else's text — Polish shows Korean lines, Japanese shows Polish ones. The key is internal and never displayed.

No executable, DLL or scene is modified. The other eleven languages and English stay byte-identical.

### Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/pl.json`](../translations/pl.json), [`translations/en-pl-review.json`](../translations/en-pl-review.json) | Adding Polish to the project properly. The JSON is keyed by the text asset's path ID; the review file pairs every English source string with its Polish translation and the original context note. |
| Players | The built `Anger Foot_Data` folder | Drag and drop over the game folder. Build it yourself as below — there is no prebuilt download at the moment. See [INSTALL.txt](../docs/INSTALL.txt). |
| Translation contributors | [`translations/pl.json`](../translations/pl.json), [`tools/build.py`](../tools/build.py) | Editing the strings and rebuilding from your own original game files. |

### Building

Requirements: Python 3.11 and an unmodified `Anger Foot_Data` folder from a supported build. The tool never writes into the game directory and never launches the game. The virtual environment lives at the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe gamesnger-foot	oolsuild.py --game "D:\Backup\Anger Foot_Data"
```

Output: `games/anger-foot/dist/Anger Foot_Data/` with the two patched files. The `dist` directory is not tracked by Git. Pass `--output` to put it elsewhere.

Both source files are pinned by SHA-256 in `tools/build.py`; any other version of the game — or an already patched file — is refused, and nothing is written. After a game update the layout has to be re-checked, not just the checksums.

[`tools/extract.py`](../tools/extract.py) dumps every text entry from an original `resources.assets` back to JSON, which is how the source data and the review file were produced.

### Verification

The build was checked against the untouched originals:

- 1776 text entries in, 1776 out, same path IDs;
- 30 842 objects in the asset file, same IDs, only text entries changed size;
- 0 values changed in any of the other eleven languages;
- 1774 Polish slots present and matching `pl.json`.

### Testing status

The language record, the title screen and the menu were verified in game. A full playthrough has not been done, so layout problems in long strings, and the phrasing of individual jokes, still need review. Polish diacritics fall back to a substitute font in some styles — cosmetic, not fixable from the text side.

The translation keeps the original's crude register and profanity. Gang names, level names and shoe names are translated where they are jokes and left alone where they read as ordinary place names.

### Game material

This directory contains translation text and tooling only — no executables, no game assets. Nothing here is affiliated with or endorsed by Free Lives or Devolver Digital; *Anger Foot*, its text and its characters belong to their authors.

### License

[MIT](../../../LICENSE), same as the rest of the repository.
