"""Build the Polish language file for OTXO.

OTXO is GameMaker compiled to native code: `data.win` carries no bytecode, and
the seven language slots - their file names and their section headers - are
string literals inside OTXO_Release.exe. There is no eighth slot to fill and no
managed code to patch, so Polish has to take one of the seven over. The same
route the Japanese and Turkish fan translations took.

This build takes the **French** slot: a Latin-script language, so the game keeps
using notosans.ttf, whose character map carries all eighteen Polish letters.
In the game's language menu Polish is therefore the French flag.

The file is not written from scratch. It is the English file with its section
header changed and the translated lines spliced in, so anything still untranslated
stays in English rather than going missing - and every blank line and oddity of
the original survives untouched. See script_ini.py.

Never writes into the game directory; output goes to a separate folder.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import script_ini

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.1'
SLOT = 'fre-FR'
SECTION = 'french'
TARGET = f'OTXO_script_english_{SLOT}.ini'

# script_english.ini as shipped, GOG build checked 2026-09-20.
SOURCE_SHA256 = '99b2a4a2bee2502825012d71525fb743de4ffcdb065c859db2709bf53d301b0d'


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: validation assertions are required.')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='The OTXO folder, never written to')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist', help='Separate output directory')
    args = parser.parse_args()

    source = args.game.resolve() / 'script_english.ini'
    destination = args.output.resolve()
    if destination == args.game.resolve() or (destination / 'OTXO_Release.exe').exists():
        raise SystemExit('Choose an output directory outside the game installation.')

    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    if SOURCE_SHA256 and digest != SOURCE_SHA256:
        raise SystemExit(f'script_english.ini: unsupported or already modified.\n'
                         f'  expected SHA-256 {SOURCE_SHA256}\n'
                         f'  got               {digest}\nNothing was written.')

    english = script_ini.load(source)
    assert script_ini.section(source) == 'english'
    translations = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    unknown = [k for k in translations if k not in english]
    assert not unknown, f'Keys not present in the English file: {unknown[:5]}'

    built = script_ini.rewrite(source, SECTION, translations)
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / TARGET
    target.write_bytes(built)

    # --- verification, against the English original ---
    readback = script_ini.load(target)
    assert script_ini.section(target) == SECTION
    assert set(readback) == set(english), 'The set of keys changed.'
    for key, text in readback.items():
        expected = translations.get(key, english[key])
        assert text == expected, f'key {key}: {text!r} != {expected!r}'
    untouched = script_ini.rewrite(source, 'english', {})
    assert untouched == source.read_bytes(), 'The template no longer reproduces the original.'
    assert len(built.split(b'\r\n')) == len(source.read_bytes().split(b'\r\n')), 'Line count changed.'

    print(json.dumps({
        'version': VERSION,
        'slot': SLOT,
        'section': SECTION,
        'translated': len(translations),
        'of_entries': len(english),
        'polish_characters': sum(len(v) for v in translations.values()),
        'bytes': len(built),
        'sha256': hashlib.sha256(built).hexdigest()[:16],
        'output': str(target),
        'install_as': TARGET,
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
