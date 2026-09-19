"""Build the Polish localization resource for SPRAWL.

The game keeps one .locres per culture under Content/Localization/Game/. Eleven
were shipped; Polish was not, although the project's own Game.locmeta lists `pl`
among its 32 target cultures. There is no language selector in the build - the
engine takes the culture from the operating system - so a Polish Windows asks
for `pl` already and falls back to English for want of a file.

So the whole translation is one file: pl/Game.locres. It carries only the keys
that are translated; the rest fall back to English, exactly as the game's own
Ukrainian file does with the 46 keys it leaves out.

Never writes into the game directory; output goes to a separate folder.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import locres

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.1'
CULTURE = 'pl'
INSIDE = f'Sprawl/Content/Localization/Game/{CULTURE}/Game.locres'

# en/Game.locres as shipped in Sprawl-WindowsNoEditor.pak, GOG build checked 2026-09-19.
SOURCE_SHA256 = '514cdb17b9add2a80828bed6178da326e77f0bbef766a8cd9fa6cc44d06c65f7'


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: validation assertions are required.')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--source', type=Path, default=ROOT / 'translations/en.locres',
                        help="The game's own en/Game.locres, extracted from the pak")
    parser.add_argument('--output', type=Path, default=ROOT / 'dist', help='Separate output directory')
    args = parser.parse_args()

    digest = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if digest != SOURCE_SHA256:
        raise SystemExit(f'{args.source.name}: unsupported or already modified source.\n'
                         f'  expected SHA-256 {SOURCE_SHA256}\n'
                         f'  got               {digest}\nNothing was written.')

    english = locres.load(args.source)
    available = english.texts()

    rows = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    translations = {(row['namespace'], row['key']): row['polish'] for row in rows}
    assert len(translations) == len(rows), 'Duplicate namespace/key in pl.json.'
    unknown = [k for k in translations if k not in available]
    assert not unknown, f'Keys not present in the English resource: {unknown[:5]}'

    polish = locres.translate(english, translations)
    data = locres.dump(polish)

    destination = args.output.resolve() / Path(INSIDE).parent
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / 'Game.locres'
    target.write_bytes(data)

    # --- verification: read the built file back and compare it to what went in ---
    built = locres.load(target)
    assert built.version == english.version
    assert built.texts() == translations, 'The built resource does not read back as written.'
    by_key = {(n, e.key): e for n, e in english.entries()}
    for namespace, entry in built.entries():
        original = by_key[(namespace, entry.key)]
        assert entry.key_hash == original.key_hash, entry.key
        assert entry.source_hash == original.source_hash, entry.key
    carried = {h for h, _, _ in built.namespaces}
    assert carried <= {h for h, _, _ in english.namespaces}, 'A namespace hash was invented.'

    print(json.dumps({
        'version': VERSION,
        'culture': CULTURE,
        'translated': len(translations),
        'of_entries': sum(len(e) for _, _, e in english.namespaces),
        'polish_characters': sum(len(v) for v in translations.values()),
        'namespaces': {name: len(entries) for _, name, entries in polish.namespaces},
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest()[:16],
        'output': str(target),
        'install_as': INSIDE,
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
