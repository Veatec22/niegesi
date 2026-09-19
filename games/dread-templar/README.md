# Dread Templar PL

*Part of [Nie gęsi](../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **Dread Templar**.

It covers all 636 text entries in the game: menus, settings, controls, the tutorial, in-game messages, dialogue, cutscenes, level and boss names, weapons and every rune description.

## How it works

Every line of text in the game lives in a single JSON object stored as a TextAsset in `resources.assets`, keyed by language code, then category, then entry id:

```json
{ "eng": { "menu": { "mnt_004": { "text": "Options" } } } }
```

The game ships nine languages — and **an empty `"pol"` block** sitting between `"rus"` and `"por"`. The slot exists in the data, the developers never filled it. This translation fills it; the other nine blocks are copied through byte for byte.

The options menu is a second problem. It carries ten language buttons, `LanguagePick_eng_00` through `LanguagePick_jan_08` — plus `LanguagePick_ita_03`, a complete Italian button that was switched off and left in the scene. That leftover becomes the Polish one: its `m_IsActive` flag goes to 1, the language code it carries changes from `ita` to `pol`, and its label changes from `Italiano` to `Polski`. All three edits happen to keep their byte length, so the scene files are spliced in place instead of being re-serialized.

The same options menu is baked into 33 scene files, one per level, so all 33 are patched. No executable, DLL, shader or piece of scene geometry is modified.

## Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/pl.json`](translations/pl.json), [`translations/en-pl-review.json`](translations/en-pl-review.json) | Dropping Polish into the project properly. `pl.json` is exactly the shape of one language block in the game's own JSON — it can be pasted in as `"pol"` with no conversion. The review file pairs every English entry with its translation. |
| Players | The built `DreadTemplar_Data` folder | Drag and drop over the game folder. Build it yourself as below — there is no prebuilt download at the moment. See [INSTALL.txt](docs/INSTALL.txt). |
| Translation contributors | [`translations/pl.json`](translations/pl.json), [`tools/build.py`](tools/build.py) | Editing the strings and rebuilding from your own original game files. |

## Building

Requirements: Python 3.11 and an unmodified `DreadTemplar_Data` folder from a supported build. The tool never writes into the game directory and never launches the game. The virtual environment lives at the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe games\dread-templar\tools\build.py --game "C:\Games\Dread Templar\DreadTemplar_Data"
```

Output: `games/dread-templar/dist/DreadTemplar_Data/` with the patched `resources.assets` and the 33 scene files — about 750 MB, because a scene file has to be shipped whole to change three bytes in it. The `dist` directory is not tracked by Git. `--only level1` patches just one scene, which is enough to pick the language once and much faster to iterate on.

All 34 source files are pinned by SHA-256 in [`tools/build.py`](tools/build.py); any other version of the game — or an already patched file — is refused, and nothing is written. After a game update the layout has to be re-checked, not just the checksums.

[`tools/extract.py`](tools/extract.py) dumps the English source text and refreshes the review file.

## Verification

The build checks itself against the untouched originals and refuses to write otherwise:

- every object in `resources.assets` compared by path id — only the text asset differs;
- the nine original language blocks byte-identical;
- the Polish block read back from the rebuilt asset equal to `pl.json`, entry for entry;
- 636 entries in, 636 out, the same keys and the same fields as English;
- every rich-text tag (`<color=…>`, `<size=…>`, `<sprite=…>`) preserved in the same order as in the source string;
- in each scene, the changed bytes confined to the three known windows — the active flag, the language code and the label.

## Known problem: Polish letters

**The fonts shipped with the game cannot render Polish.** Every font asset was checked: `LiberationSans SDF`, which is the fallback everything else falls back to, has 250 characters — ASCII, Latin-1 and punctuation. That covers French, German, Spanish and Portuguese, and stops exactly one block short of Polish. The decorative fonts are ASCII-only and already lean on the fallback for anything accented.

So `ó` renders, and `ą ć ę ł ń ś ź ż` come out as empty boxes. The fix is to extend the `LiberationSans SDF` atlas with 18 glyphs, which is a separate piece of work. Until then, `build.py --no-diacritics` strips the marks and produces readable, if incorrect, Polish.

`pl.json` always holds properly spelled Polish. The stripping happens at build time and never touches the source text.

## Testing status

Structurally verified as above. Nothing has been confirmed in game yet — in particular whether the language index the toggle carries is what picks the text, and whether the in-game pause menu behaves once Polish is selected.

## Game material

This directory contains translation text and tooling only — no executables, no game assets. Nothing here is affiliated with or endorsed by T19 Games or Fulqrum Publishing; *Dread Templar*, its text and its characters belong to their authors.

## License

[MIT](../../LICENSE), same as the rest of the repository.
