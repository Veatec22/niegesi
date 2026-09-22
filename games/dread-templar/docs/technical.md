# Dread Templar — technika

Ustalenia i instrukcje dla osób, które budują paczkę albo poprawiają teksty.
Gracz potrzebuje tylko [README](../README.md).

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Dread Templar PL”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

*Part of [Nie gęsi](../../../README.md) — Polish translations of games that never got one.*

An unofficial Polish translation of **Dread Templar**.

It covers all 636 text entries in the game: menus, settings, controls, the tutorial, in-game messages, dialogue, cutscenes, level and boss names, weapons and every rune description.

### How it works

Every line of text in the game lives in a single JSON object stored as a TextAsset in `resources.assets`, keyed by language code, then category, then entry id:

```json
{ "eng": { "menu": { "mnt_004": { "text": "Options" } } } }
```

The game ships nine languages - and **an empty `"pol"` block** sitting between `"rus"` and `"por"`. The slot exists in the data, the developers never filled it. This translation fills it; the other nine blocks are copied through byte for byte.

Polish turns out to be half-built all the way down. Of the four methods in `Assembly-CSharp` that map a language code to something, three - `GlobalVars.SetLanguage`, `SaveLanguageStr` and `InitialGameLanguage` - already handle `pol`. That is why a Polish Windows makes the game pick Polish up by itself the moment the block has content in it.

What is missing is the menu, and two things had to be built.

**The button.** The options menu holds ten language buttons: `LanguagePick_eng_00` through `jan_08` under `Language_ToggleGroup`, plus `LanguagePick_ita_03` - a complete Italian button the developers switched off and moved out to the sibling `Language_Toggle_Panel`. Enabling it alone is not enough: the grid is a `GridLayoutGroup` that only lays out its own children, and the menu indexes its buttons through `LanguageToggleGroup.filterToggle`, a serialized array of exactly nine. So the button is moved back under the grid, appended to that array as index 9, and given the code `pol`, index 9 and the label `Polski`.

**The lookup.** `LanguageToggleGroup.LoadCurLanguage` turns the saved code into an index into that array, and its switch knows only the original nine - an unknown code falls through to 0. With Polish saved, the menu ticks English, and ticking English writes `eng` back over the saved language. One method body is therefore replaced: the compiler's hash switch over nine strings, 447 bytes, becomes a plain if-chain over ten, 234 bytes, padded with nops to exactly the same length so that no other offset in the assembly moves. Nothing else in the file changes.

The same options menu is baked into 33 scene files, one per level, so all 33 are patched. No shader, model or piece of scene geometry is touched, and the nine original languages come through unchanged.

### Who the files are for

| Audience | Files | Use |
| --- | --- | --- |
| Game developer | [`translations/pl.json`](../translations/pl.json), [`translations/en-pl-review.json`](../translations/en-pl-review.json) | Dropping Polish into the project properly. `pl.json` is exactly the shape of one language block in the game's own JSON — it can be pasted in as `"pol"` with no conversion. The review file pairs every English entry with its translation. |
| Players | The built `DreadTemplar_Data` folder | Drag and drop over the game folder. Build it yourself as below — there is no prebuilt download at the moment. See [INSTALL.txt](../docs/INSTALL.txt). |
| Translation contributors | [`translations/pl.json`](../translations/pl.json), [`tools/build.py`](../tools/build.py) | Editing the strings and rebuilding from your own original game files. |

### Building

Requirements: Python 3.11 and an unmodified `DreadTemplar_Data` folder from a supported build. The tool never writes into the game directory and never launches the game. The virtual environment lives at the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe games\dread-templar\tools\build.py --game "C:\Games\Dread Templar\DreadTemplar_Data"
```

Output: `games/dread-templar/dist/DreadTemplar_Data/` with the patched `resources.assets`, `Managed/Assembly-CSharp.dll` and the 33 scene files — about 750 MB, because a scene file has to be shipped whole to change seven objects in it. The `dist` directory is not tracked by Git. `--only level1` patches just one scene and is much faster to iterate on.

All 35 source files are pinned by SHA-256 in [`tools/build.py`](../tools/build.py); any other version of the game — or an already patched file — is refused, and nothing is written. After a game update the layout has to be re-checked, not just the checksums.

[`tools/extract.py`](../tools/extract.py) dumps the English source text and refreshes the review file. [`tools/scene.py`](../tools/scene.py) and [`tools/assembly.py`](../tools/assembly.py) hold the scene and assembly surgery; each explains its own reasoning at the top.

For testing on a real installation, [`tools/install.py`](../../../tools/install.py) at the repository root copies a build over the game and keeps the originals in `backups/`.

### Verification

The build checks itself against the untouched originals and refuses to write otherwise:

- every object in `resources.assets` compared by path id - only the text asset differs;
- the nine original language blocks byte-identical;
- the Polish block read back from the rebuilt asset equal to `pl.json`, entry for entry;
- 636 entries in, 636 out, the same keys and the same fields as English;
- every rich-text tag (`<color=...>`, `<size=...>`, `<sprite=...>`) preserved in the same order as in the source string;
- in each scene, exactly seven objects changed - the button, its transform, its language component, its label, the grid's transform, the panel it left and the array that indexes it - and every other object byte-identical;
- the button confirmed, after the rebuild, to be the tenth child of the grid and the tenth entry of the array;
- in the assembly, every changed byte inside the one replaced method body, and the file the same size.

### Polish letters

They render. The menu shows `Dźwięk`, `Zarządzanie danymi` and `Zatwierdź` correctly, verified in game.

This contradicts an earlier reading of the font assets here, which counted the character table of `LiberationSans SDF` - the fallback the decorative fonts lean on - found 250 characters ending at Latin-1, and concluded Polish could not be drawn. Something further down the fallback chain covers it; the large `SourceHanSerifTC` atlas, which carries Latin Extended-A, is the likely source and is a serif, which is why it blends into the menu's own serif. The conclusion was wrong, and only in-game evidence settled it.

`build.py --no-diacritics` still exists as a fallback for any screen that turns out not to render them. `pl.json` always holds properly spelled Polish; the stripping happens at build time and never touches the source text.

### Testing status

Polish text loads and the menu renders it, diacritics included — confirmed in game. Not yet confirmed: that the button now appears inside the grid, that the choice survives a restart, and that the in-game pause menu behaves like the title screen's. Nothing beyond the menus has been read in place, so long strings may still overflow their boxes.

### Game material

This directory contains translation text and tooling only — no executables, no game assets. Nothing here is affiliated with or endorsed by T19 Games or Fulqrum Publishing; *Dread Templar*, its text and its characters belong to their authors.

### License

[MIT](../../../LICENSE), same as the rest of the repository.
