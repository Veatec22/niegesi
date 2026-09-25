# Nie gęsi

> *A niechaj narodowie wżdy postronni znają, iż Polacy nie gęsi, iż swój język mają.*
> — Mikołaj Rej, 1562

Unofficial Polish translations of indie games. This private working repository holds
translation sources, build tools, review files and installation instructions for each game.
Translations are produced with machine assistance and reviewed in-game by the user.

Versioned sources contain translation text and tooling. Game assets and release packages
are built locally from an installed copy and kept in ignored output and backup folders.

## Games

| Game | Coverage | Version | Status |
| --- | --- | --- | --- |
| [Shotgun Cop Man](games/shotgun-cop-man/) | 485 entries: UI, controls, tutorials, dialogue, level editor and achievements | 0.3.1 | Separate Polish language via plugin; confirmed in-game |
| [Anger Foot](games/anger-foot/) | 1774/1776 entries: UI, tutorials, dialogue, levels, shoes, achievements and credits | 0.3 | Uses the empty Italian slot; title screen and menu tested |
| [Dread Templar](games/dread-templar/) | 636 entries: UI, tutorials, dialogue, cutscenes, levels, bosses and runes | 0.1 | Uses the existing empty pol slot, a menu button and a method patch |
| [SPRAWL](games/sprawl/) | 717/717 entries: UI, HUD, dialogue, codex, tutorials and interactions | 0.2 | Separate Polish language and flag; vertical confirmed, full campaign playtest pending |
| [My Friend Pedro](games/my-friend-pedro/) | 721/721 entries: dialogue, UI, tutorials, HUD, achievements and barks | 0.3.1 | Separate Polish language; vertical confirmed, full campaign playtest pending |
| [Skate Story](games/skate-story/) | 2305/2305 entries: all chapters, epilogue, dialogue, UI, items, objectives and poetry | 0.3 | Full ZIP built and installed; vertical confirmed, full campaign playtest pending |
| [OTXO](games/otxo/) | 1364 entries: UI, tutorial, 102 drinks, dialogue, lore, journal and statistics | 0.2 | Polish replaces Chinese, the slot that loads an external font |
| [Labyrinth of the Demon King](games/labyrinth-of-the-demon-king/) | 1120/1120 entries; menus, dialogue, notes, items and maps | 0.2, PAK + minimal IoStore overlay | Vertical confirmed in-game; full campaign review pending |
| [Turbo Overkill](games/turbo-overkill/) | 2316/2333 entries: menus, HUD, tutorials, objectives, all dialogue, gear, codex, audio logs and level editor | 0.2.0 | Separate Polish language and flag; vertical confirmed, full campaign playtest pending |
| [Void Bastards](games/void-bastards/) | 2480/2480 entries: menus, HUD, comics, B.A.C.S. and pirate dialogue, items, upgrades, star map events, traits, achievements and Tydy DLC | 0.2.1 | Separate Polish language; missing Polish glyphs composed at runtime; vertical confirmed, full playthrough pending |
| [Wild Bastards](games/wild-bastards/) | 4426/4426 entries: menus, HUD, dialogue, tutorials and hints, outlaws with aces, stunts and weapons, items, planet traits, planet and sector map events, achievements | 0.2.0 | Polish added as an extra I2 language with its own menu button; dynamic font fallback from the game's TTFs; vertical confirmed, full playthrough pending |
| [Holy Shoot](games/holy-shoot/) | 1286/1286 entries: menus and settings, tutorials, perks and upgrade tree, weapons, challenges, characters, intro and voice-line subtitles | 0.2.0 | Overlay pak with an empty IoStore companion plus UE4SS Lua patch adding Polski to the language selector; vertical confirmed, full playthrough pending |
| [Neon Abyss](games/neon-abyss/) | 2639/2639 entries: menus, 600+ items, weapons, pets and sets, tips and lore, unlock tree, bosses, bar and office dialogue, seeds, cheat codes and achievements | 0.3.2 | BepInEx plugin adds Polish to I2 and to the hard-coded language switcher; Polish glyphs from the game's own fonts; vertical confirmed, full playthrough pending |
| [BPM: Bullets Per Minute](games/bpm/) | 859/859 entries: menus and settings, HUD, hints, latency test, items, trials, enemies, valkyries and credits | 1.0 | Overlay pak in the unused Japanese slot, renamed Polski; Polish letters added to two game fonts; delivered as creating patches built from the player's own paks; vertical confirmed, full playthrough pending |
| [Somber Echoes](games/somber-echoes/) | 111/1507 extracted entries: menu, opening narration and selected tutorials | 0.1 vertical | Text-only overlay pak using English; built and installed, in-game test pending |
| [Katana ZERO](games/katana-zero/) | 2851/2851 entries: menus and settings, startup screens, UI, target dossiers, all dialogue, TV news and credits | 0.2.0 | GameMaker YYC: Polish takes the Russian slot via a new exe section; Polish glyphs added to the sprite fonts in data.win with a second TPAG chunk; delivered as difference patches; vertical confirmed, full playthrough pending |
| [NOT A HERO](games/not-a-hero/) | Technical investigation: external dialogue INIs, raster menu localization and embedded UI strings; text count pending | — | GOG / Chowdren; Polish glyph support and asset mapping unresolved, no build or in-game test |
| [Hyper Light Drifter](games/hyper-light-drifter/) | 126/126 entries: menus, settings and controls, game modes and Boss Rush, save notices and in-game hints (the game has no dialogue) | 0.1.0 | GameMaker YYC: Polish takes the Italian slot in the text files; the font's empty Polish glyph cells get letters drawn in a new exe section; delivered as difference patches; in-game test pending |
| [Cyber Hook](games/cyber-hook/) | 702/702 entries: menus, settings and controls, tutorial, Dron and Numero dialogue between worlds, world and level names, marathon mode, ending and Lost Numbers DLC | 0.2.0 | Unity Mono: BepInEx plugin serves Polish in place of English from the game's CSV language table; missing Polish letters composed at runtime from the game's own TMP font atlases; vertical confirmed in game, full playthrough pending |
| [Broforce](games/broforce/) | 397/397 entries: menus, settings and controls, world map regions and threat levels, HUD, results, versus, custom campaigns, boss captions and ending | 0.2.0 | Unity Mono: BepInEx plugin adds Polish as an extra language in the game's own language system; missing letters composed at runtime in bitmap fonts and as extruded meshes for the 3D titles; vertical confirmed in game, full playthrough pending |
| [Laika: Aged Through Blood](games/laika-aged-through-blood/) | 3470/3470 entries: menus and settings, tutorials, achievements, all story, side-quest and village dialogue, flashbacks, quest journal, items, recipes, cassettes, character and place names | 0.2.0 | Unity Mono: BepInEx plugin adds Polish as a separate language to the game's M2H Localization sheets; the game's fonts already carry Polish letters, fallbacks composed at runtime; vertical confirmed in game, full playthrough pending |
| [Rain World](games/rain-world/) | 4913/4913 entries with Downpour and The Watcher: menus, options, Remix, Expedition, hints, region and creature names, iterator conversations, pearl readings, echoes, chatlogs and broadcasts, and the Downpour developer commentary | 0.2.0 | Unity Mono with the game's own BepInEx and Remix mod system: a Remix mod whose plugin registers Polish as a new language and reads plain-text dialogue and chatlogs; texts in the game's own format, the game's fonts already have Polish letters; vertical tested in game, full build installed, full playthrough pending |
| [I Am Your Beast](games/i-am-your-beast/) | 1581/1581 entries: menus, HUD, tutorial, all voiced cutscenes, enemy barks, Support Group and Cold Sweat packs, credits | 0.2.0 | Runtime text replacement via plugin (no Unity localization system); vertical confirmed, full playthrough pending |
| [Heat Signature](games/heat-signature/) | 2536/2536 entries: menus and settings, tutorial, HUD, items and traits, missions and clauses, liberation, hints, event log, leaderboards and all dialogue files | 0.2.0 | GameMaker YYC; native D3D9 plugin translates before line wrapping, including templated sentences and inflected item names; sprite fonts from the open Xolonium; vertical confirmed, full playthrough pending |
| [DEADBOLT](games/deadbolt/) | 619/619 entries: menus, settings and controls, mission select, hints and objectives, weapons, achievements, enemy barks, all flame verses, notes and safes, cassette tapes, credits and text on graphics | 0.2.0 | GameMaker 1.4 VM: native d3d9.dll proxy patches the game data in memory before the runner parses it (strings, Polish glyphs in three pixel fonts, labels on graphics); no game file replaced; vertical confirmed, full playthrough pending |

Each game's Polish README is a short player-facing description and installation guide.
Technical findings belong in `docs/technical.md`; `game.yaml` records counts, release
version, package type and test status, and also supplies the site in `site/`.

## Layout

```
games/<slug>/
  README.md                       player-facing description, in Polish
  game.yaml                       metadata, coverage, package and test status
  docs/technical.md                 technical findings and build instructions
  docs/INSTALL.txt                player instructions, packaged as READ-ME.txt
  tools/build.py                  builds files and a release ZIP into dist/
  translations/pl.json            Polish translation source
  translations/en-pl-review.json English and Polish side by side
```

Games under investigation may have extraction tools and review scaffolding before a
release builder exists. A completed translation must include a ZIP containing the game's
folder layout and `READ-ME.txt`; loose output files alone are not a completed release.

Tools are generally local to each game because storage formats and patching methods vary.
Shared conventions are documented in [AGENTS.md](AGENTS.md) and
[docs/adding-a-game.md](docs/adding-a-game.md).

## Building

Use Python 3.11 and the original game files. Create the environment at the repository root:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

Follow the selected game's technical documentation. For example:

```powershell
.venv/Scripts/python.exe games/shotgun-cop-man/tools/build.py --original "D:/Backup/Shotgun Cop Man_Data/resources.assets"
.venv/Scripts/python.exe games/anger-foot/tools/build.py --game "D:/Backup/Anger Foot_Data"
```

Builds write to the game's local `dist/`, never to its installation. Builders pin the
supported original files by SHA-256 and refuse modified or unsupported inputs. A game
update requires inspecting the format again, not merely replacing a checksum.

`tools/install.py` is a separate local testing helper. It backs up originals before
replacing game files and preserves existing backups. Close the game before installation
or restoration. Agents never launch games: the user tests rendering and gameplay.

## Game material and license

Game names, original text and characters belong to their respective creators. These
translations are unofficial and are not affiliated with or endorsed by the studios.
The [MIT license](LICENSE) covers this repository's translation text, tools and documentation.
