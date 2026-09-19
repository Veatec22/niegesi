# Anger Foot PL

*Part of [Nie gęsi](../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **Anger Foot**.

It covers 1774 of the 1776 text entries in the game — menus, settings, tutorials, dialogue, level names, shoes, star goals, achievements, news tickers and credits. The remaining two are empty in the original as well.

## How it works

Anger Foot ships English plus twelve translated languages. One of those twelve, **Italian, is an empty slot**: the language record exists in the files, but only 1 of 1776 texts was ever filled in, and the language is neither selectable nor advertised on the store pages.

This package takes that slot over:

- the Italian `LocalizationLanguage` record is relabelled — `NativeName` becomes `Polski`, `LanguageTag` becomes `pl`, `SteamAPIName` becomes `polish`, and `Supported` is switched on so the language joins the rotation;
- the Polish text is written into the matching translation slot of every text entry.

One field must **not** change: `SpreadsheetKey` stays `ITALIAN`. The game sorts its languages alphabetically by that key and then uses the resulting position as a plain array index into each entry's translations. Renaming the key to `POLISH` moves the language from index 4 to index 6, and every language after it reads somebody else's text — Polish shows Korean lines, Japanese shows Polish ones. The key is internal and never displayed.

No executable, DLL or scene is modified. The other eleven languages and English stay byte-identical.

## Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/pl.json`](translations/pl.json), [`translations/en-pl-review.json`](translations/en-pl-review.json) | Adding Polish to the project properly. The JSON is keyed by the text asset's path ID; the review file pairs every English source string with its Polish translation and the original context note. |
| Players | The built `Anger Foot_Data` folder | Drag and drop over the game folder. Build it yourself as below — there is no prebuilt download at the moment. See [INSTALL.txt](docs/INSTALL.txt). |
| Translation contributors | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Editing the strings and rebuilding from your own original game files. |

## Building

Requirements: Python 3.11 and an unmodified `Anger Foot_Data` folder from a supported build. The tool never writes into the game directory and never launches the game. The virtual environment lives at the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe gamesnger-foot	oolsuild.py --game "D:\Backup\Anger Foot_Data"
```

Output: `games/anger-foot/dist/Anger Foot_Data/` with the two patched files. The `dist` directory is not tracked by Git. Pass `--output` to put it elsewhere.

Both source files are pinned by SHA-256 in `tools/build.py`; any other version of the game — or an already patched file — is refused, and nothing is written. After a game update the layout has to be re-checked, not just the checksums.

[`tools/extract.py`](tools/extract.py) dumps every text entry from an original `resources.assets` back to JSON, which is how the source data and the review file were produced.

## Verification

The build was checked against the untouched originals:

- 1776 text entries in, 1776 out, same path IDs;
- 30 842 objects in the asset file, same IDs, only text entries changed size;
- 0 values changed in any of the other eleven languages;
- 1774 Polish slots present and matching `pl.json`.

## Testing status

The language record, the title screen and the menu were verified in game. A full playthrough has not been done, so layout problems in long strings, and the phrasing of individual jokes, still need review. Polish diacritics fall back to a substitute font in some styles — cosmetic, not fixable from the text side.

The translation keeps the original's crude register and profanity. Gang names, level names and shoe names are translated where they are jokes and left alone where they read as ordinary place names.

## Game material

This directory contains translation text and tooling only — no executables, no game assets. Nothing here is affiliated with or endorsed by Free Lives or Devolver Digital; *Anger Foot*, its text and its characters belong to their authors.

## License

[MIT](../../LICENSE), same as the rest of the repository.
