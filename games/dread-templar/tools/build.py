"""Build Polish game files for Dread Templar from an unmodified installation.

Three edits:

  resources.assets - all of the game's text lives in one JSON TextAsset keyed by
  language code. The developers left an empty "pol" block in it; this fills it.
  The other nine blocks are copied through untouched.

  level* - every scene carrying the options menu holds a disabled leftover
  Italian language button, parked outside the button grid. It becomes the Polish
  one: reparented into the grid, appended to the array the menu indexes, and
  given the code "pol", index 9 and the label "Polski". See scene.py.

  Managed/Assembly-CSharp.dll - one method body, LanguageToggleGroup's lookup
  from saved code to button index, replaced with one that also knows "pol". The
  rest of the engine already handles Polish. See assembly.py.

Never writes into the game directory; output goes to a separate folder.
"""
import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path
import UnityPy

sys.path.insert(0, str(Path(__file__).resolve().parent))
import assembly
import game
import scene as scenes

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.1'
ASSEMBLY = 'Managed/Assembly-CSharp.dll'

# The build this was made against: GOG, checked 2026-09-19.
ORIGINAL = {
    'resources.assets': 'c07cd097c654c4c2c4d98149a61d5220ea7198386c2fb32da735b6065154ae3a',
    ASSEMBLY: '7099377fd381a9f51d668624cb8a3edd6a66c563e99153c2650391afa477423c',
    'level1': '78aeb896a65937128b2e72af20a7efa9877a3cb8af10e23179a97d13879ab41c',
    'level2': '4f60f7bf49b30ff45a3b415fa4f155decfcf426bc6e25101c36c4ab7cc78e55e',
    'level3': '0e35bdaabee973f1f485b6097a2477285784c9bb9351a547a78af718baf0049e',
    'level5': '9beb144f9222e088669c339d7cad4fcae67ee50fc42fff44e85406bf351d7886',
    'level6': '114b44103afa8ec7153bdea77ae0f37b2bb2d5f6cd5abd01bd050ed557a908be',
    'level7': '93a200e8b7870b5c9d869c8fc3057e838c1d7b4e9843b8e397bf8081e2758740',
    'level8': 'd9fcb8cf9820aeab2bc5ce7cad7a327a0d8566d0cfd917212c0dff4d291134fc',
    'level9': 'e454ea44171303b9877f90da746102fc8685b6be957baebb0ab2f3a93f9caf59',
    'level10': '23b09d8e474832be277f1243d85bf7c19f3e7f96ed15ab71b9fa9cb37e7c1d70',
    'level11': 'aea9a707df4f1359eaf41de37330dcfcce1fa080697f05810b81de2c8a587a50',
    'level12': '483addc167e1715a5c1d20a23132b1a6950b16f5f2d6909aec8cefd6b958f067',
    'level13': '7dca07a7faf89fba7639e0038b40f0b251382070df1458fa8fd3dbf678433bb6',
    'level14': '53aa63a24e9c809385ad68366daa762f4b7fa8528527feb0f6b979908fdd49bd',
    'level15': '62c2b5d9557037f793a23cbbfa16e9bfe1e038e2b125f207053466efe789bdb4',
    'level16': '646710cad227d353dc7ca09d860209703b1c4b4654c2d87d072cb316b46b7576',
    'level17': 'c6521e8883cd897f0045b020e7765972aa810f1ef92425eea308a9e154f821c7',
    'level18': 'acb3d71cabaffdffb85bae63c271bddb9f765f2172898ff5f2ab366d94074288',
    'level19': 'f750e263466dd2ad27790d09e7b7818c8a4d38c765a46b67b329d2a6150c4717',
    'level20': '4e14aee3b1c0659b69bff1f6bc1f5358ca558eee77c5d2eb729784579f439741',
    'level21': '35b18de2e15002923ad9f79d2d84aa6834bca34f4d19f8ce3719cecd9348b96b',
    'level22': 'eada2b4a090f3bde9c81839b3ef7889116c67d3b0c26592e8d97a51aadc68a99',
    'level23': 'b3891c5d310f0a5641f76f7c817f1c7aeebc3309055cf72b4b4cf6f1f8a80753',
    'level24': '346ff92527e005ce68258c187b8b16d521f5f4931fa04c66db276a951fc1c23b',
    'level25': '2c86d81e897825a9fcbaa0419dfa6a7aa536a1b95179843b1622603515d20e64',
    'level26': '56805f2ab35c2de66b1c395926da05271515b35479f9741174729a7c9e7c573f',
    'level27': '487bbf49da8f9e2636c92e82fc8fa46aca514c9c1d044fa2a7f99da4d464110c',
    'level28': '29139602646f762e8315d26b13f4884e2bed5c5ff213a980333f2e4f8a268c31',
    'level29': '3db43076e18738411d9d32b9509da407ecea134b5e348f01fa5541719cbac68d',
    'level30': '2a5a9bce8958652197f7df80d0c5da3eb7a88aac6aa6e17fa37a7001a9e9824f',
    'level31': 'cdef758b593352c797ed0f2258acd165b735badd5e58e58624e0b83e20942d8f',
    'level32': 'e0dee2c98e8712294b246223c8d96fe924c4cc7ee367d211319cae94ad3376a6',
    'level33': '482d152c4e61401d1d5733f57c69b1bd2de59d8a447eeed4ab47acca786baece',
    'level39': '04e8cd649f7feda7cca399c9eeb43af2d08aab026b254ba596e8b299b6d49ed6',
}
SCENES = [name for name in ORIGINAL if name.startswith('level')]

DIACRITICS = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')


def check(path, name):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != ORIGINAL[name]:
        raise SystemExit(f'{name}: unsupported or already modified file.\n'
                         f'  expected SHA-256 {ORIGINAL[name]}\n'
                         f'  got               {digest}\nNothing was written.')


def render(polish):
    """The Polish block as the game's own JSON writes it: tabs, CRLF, 4-space top level."""
    lines = ['    "pol": {']
    for index, category in enumerate(game.CATEGORIES):
        lines.append(f'\t\t"{category}": {{')
        keys = list(polish[category])
        for number, key in enumerate(keys):
            lines.append(f'\t\t\t\t"{key}": {{')
            fields = list(polish[category][key].items())
            for position, (field, value) in enumerate(fields):
                body = json.dumps(value, ensure_ascii=False)
                lines.append(f'\t\t\t\t\t"{field}": {body}' + (',' if position < len(fields) - 1 else ''))
            lines.append('\t\t\t\t}' + (',' if number < len(keys) - 1 else ''))
        lines.append('\t\t\t}' + (',' if index < len(game.CATEGORIES) - 1 else ''))
    lines.append('    }')
    return '\r\n'.join(lines)


def verify_scene(original, built):
    """Everything about the built scene that the patch was supposed to change, and nothing else."""
    before, after = scenes.Scene(original), scenes.Scene(built)
    assert before.raw.keys() == after.raw.keys(), 'Objects were lost or added.'

    button = after.find(scenes.TOGGLE_NAME)
    grid = after.find(scenes.GRID_NAME)
    grid_transform = after.component(grid, 'RectTransform')
    transform = after.component(button, 'RectTransform')
    _, children = after.children_at(grid_transform)
    assert len(children) == 10 and children[-1] == transform, children

    manager = next(c for c in after.components(grid) if after.objects[c].type.name == 'MonoBehaviour'
                   and len(after.raw[c]) == 164)
    count = struct.unpack_from('<i', after.raw[manager], 32)[0]
    assert count == 10, count
    toggle = struct.unpack_from('<q', after.raw[manager], 32 + 4 + 12 * 9 + 4)[0]
    assert toggle in after.components(button), 'The array points outside the Polish button.'

    mapping = next(c for c in after.components(button)
                   if after.objects[c].type.name == 'MonoBehaviour' and len(after.raw[c]) == 60)
    assert after.raw[mapping][48:56] == scenes.CODE_TO
    assert struct.unpack_from('<i', after.raw[mapping], 56)[0] == scenes.POLISH_INDEX

    raw = after.raw[button]
    at = 4 + 12 * struct.unpack_from('<i', raw, 0)[0] + 4
    length = struct.unpack_from('<i', raw, at)[0]
    assert raw[at + 4 + (length + 3 & ~3) + 2] == 1, 'The Polish button is not enabled.'

    label = next(c for kid in after.children_at(transform)[1]
                 for c in after.components(struct.unpack_from('<q', after.raw[kid], 4)[0])
                 if after.objects[c].type.name == 'MonoBehaviour' and scenes.LABEL_TO in after.raw[c])
    old_parent = next(i for i in before.raw
                      if before.objects[i].type.name == 'RectTransform'
                      and transform in before.children_at(i)[1])

    differing = {i for i in before.raw if before.raw[i] != after.raw[i]}
    expected = {button, transform, mapping, label, manager, grid_transform, old_parent}
    assert differing == expected, sorted(differing ^ expected)
    return len(differing)


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: validation assertions are required.')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='Original "DreadTemplar_Data" folder, never written to')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist', help='Separate output directory, never the game directory')
    parser.add_argument('--only', nargs='*', metavar='SCENE', help='Patch only these scenes (default: all of them)')
    parser.add_argument('--no-diacritics', action='store_true',
                        help='Strip Polish diacritics, for fonts that cannot render them')
    args = parser.parse_args()

    source, destination = args.game.resolve(), args.output.resolve()
    if destination == source or (destination / 'DreadTemplar.exe').exists() or destination.name.endswith('_Data'):
        raise SystemExit('Choose an output directory outside the game installation.')
    if args.only:
        unknown = set(args.only) - set(SCENES)
        assert not unknown, f'Not scenes carrying the options menu: {sorted(unknown)}'
    chosen = [s for s in SCENES if not args.only or s in args.only]

    for name in ['resources.assets', ASSEMBLY] + chosen:
        check(source / name, name)

    polish = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    assert list(polish) == game.CATEGORIES, list(polish)
    if args.no_diacritics:
        polish = {c: {k: {f: (v.translate(DIACRITICS) if isinstance(v, str) else v)
                          for f, v in e.items()} for k, e in entries.items()}
                  for c, entries in polish.items()}

    out = destination / 'DreadTemplar_Data'
    (out / 'Managed').mkdir(parents=True, exist_ok=True)

    # --- the localization JSON ---
    obj, raw, body_at, body, end = game.text_asset(source / 'resources.assets')
    empty = '    "pol": {\r\n\r\n\r\n    }'
    assert body.count(empty) == 1, 'The empty Polish block is not where it was.'
    patched = body.replace(empty, render(polish))
    assert len(patched) > len(body)
    obj.set_raw_data(raw[:body_at] + game.write_string(patched.encode('utf-8')) + raw[end:])
    (out / 'resources.assets').write_bytes(obj.assets_file.save())

    # --- the language button, in every scene carrying the options menu ---
    for name in chosen:
        scenes.patch(source / name, out / name)

    # --- the menu's lookup from language code to button index ---
    rewritten, where = assembly.patch(source / ASSEMBLY)
    (out / ASSEMBLY).write_bytes(rewritten)

    # --- verification, against the untouched originals ---
    before = {o.path_id: o.get_raw_data() for o in UnityPy.load(str(source / 'resources.assets')).objects}
    after = {o.path_id: o.get_raw_data() for o in UnityPy.load(str(out / 'resources.assets')).objects}
    assert before.keys() == after.keys(), 'Objects were lost or added.'
    assert [k for k in before if before[k] != after[k]] == [game.TEXT_PATH_ID]

    original, built = game.load(source / 'resources.assets'), game.load(out / 'resources.assets')
    assert original['pol'] == {}
    for language in game.LANGUAGES:
        if language != 'pol':
            assert original[language] == built[language], f'{language} was modified.'
    assert built['pol'] == polish, 'The Polish block does not read back as written.'
    entries = sum(len(built['pol'][c]) for c in game.CATEGORIES)
    assert entries == sum(len(original['eng'][c]) for c in game.CATEGORIES)

    touched = [verify_scene(source / name, out / name) for name in chosen]

    old, new = (source / ASSEMBLY).read_bytes(), (out / ASSEMBLY).read_bytes()
    assert len(old) == len(new), 'The assembly changed size.'
    changed = [i for i, (a, b) in enumerate(zip(old, new)) if a != b]
    assert all(where['method_at'] <= i < where['method_at'] + where['body_size'] for i in changed)

    print(json.dumps({
        'version': VERSION,
        'entries': entries,
        'polish_characters': sum(len(str(v)) for c in game.CATEGORIES for e in built['pol'][c].values() for v in e.values()),
        'diacritics': not args.no_diacritics,
        'languages': len(built),
        'scenes_patched': len(chosen),
        'scene_objects_changed': sorted(set(touched)),
        'assembly_bytes_changed': len(changed),
        'output': str(out),
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
