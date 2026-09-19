"""Build a Polish language asset from a supported, unmodified game asset.
Never installs or starts the game. Output must be a separate directory.
"""
import argparse
import hashlib
import json
import re
import struct
import sys
import zipfile
from pathlib import Path
import UnityPy

ORIGINAL_SHA256 = '064c07138b7f5e133733c4b8ec8449457407c1f7a2cfec9b6d9c218960bfea83'
VERSION = '0.1'
ROOT = Path(__file__).resolve().parents[1]

def parse(raw):
    pos = 56
    def integer():
        nonlocal pos
        value = struct.unpack_from('<i', raw, pos)[0]
        pos += 4
        return value
    def string():
        nonlocal pos
        length = integer()
        assert 0 <= length <= len(raw) - pos
        value = raw[pos:pos + length].decode('utf-8')
        pos = (pos + length + 3) & ~3
        return value
    entries = []
    for _ in range(integer()):
        key, kind = string(), integer()
        languages = [string() for _ in range(integer())]
        length = integer()
        flags = raw[pos:pos+length]
        pos = (pos + length + 3) & ~3
        touch = [string() for _ in range(integer())]
        entries.append((key, kind, languages, flags, touch))
    return entries, raw[pos:]

def integer(n):
    return struct.pack('<i', n)

def string(s):
    data = s.encode('utf-8')
    return integer(len(data)) + data + b'\0' * (-len(data) % 4)

def parse_languages(tail):
    # CaseInsensitiveTerms (aligned bool), OnMissingTranslation, empty mTerm_AppName.
    assert tail[:12] == b'\0\0\0\0\3\0\0\0\0\0\0\0'
    count = struct.unpack_from('<i', tail, 12)[0]
    position = 16
    rows = []
    for _ in range(count):
        fields = []
        for _ in range(2):
            length = struct.unpack_from('<i', tail, position)[0]
            position += 4
            fields.append(tail[position:position+length].decode('utf-8'))
            position = (position + length + 3) & ~3
        flags = tail[position:position+4]
        position += 4
        rows.append((*fields, flags))
    return rows, position

def main():
    if not __debug__:
        raise RuntimeError('Run without -O: validation assertions are required.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original', type=Path, required=True, help='Unmodified resources.assets from a backup')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist', help='Separate output directory, never the game directory')
    args = parser.parse_args()
    source = args.original.resolve()
    destination = args.output.resolve()
    if (destination / 'Shotgun Cop Man.exe').exists() or destination.name.endswith('_Data') or source == destination / 'Shotgun Cop Man_Data' / 'resources.assets':
        raise ValueError('Choose an output directory outside the game installation.')
    if hashlib.sha256(source.read_bytes()).hexdigest() != ORIGINAL_SHA256:
        raise ValueError(f'Unsupported or modified original asset. Expected SHA-256 {ORIGINAL_SHA256}. No output was written.')
    translations = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
    env = UnityPy.load(str(source))
    obj = next(o for o in env.objects if o.path_id == 4903)
    raw = obj.get_raw_data()
    
    original, tail = parse(raw)
    language_rows, language_end = parse_languages(tail)
    assert len(language_rows) == 10 and not any(row[1] == 'pl' for row in language_rows)
    new_language_tail = (tail[:12] + integer(11) + tail[16:language_end]
                         + string('Polish') + string('pl') + b'\0'*4 + tail[language_end:])
    assert translations.keys() == {x[0] for x in original}, {x[0] for x in original} - translations.keys()
    
    patched = bytearray(raw[:56] + integer(len(original)))
    for key, kind, languages, flags, touch in original:
        langs = languages.copy()
        if key in translations:
            # waitForInput uses literal angle brackets, not a rich-text tag.
            tokens = lambda value: re.findall(r'\[[^\]]+\]|</?(?:b|i|size|color|sprite)(?:=[^>]*)?>|\{[^}]+\}', value)
            assert tokens(langs[0]) == tokens(translations[key]), key
            langs.append(translations[key])
        assert len(languages) == len(flags) == 10
        flags = flags + b'\0'
        if touch:
            assert len(touch) == 10
            touch = touch + [translations[key]]
        patched += string(key) + integer(kind) + integer(len(langs))
        patched += b''.join(string(s) for s in langs)
        patched += integer(len(flags)) + flags + b'\0' * (-len(flags) % 4)
        patched += integer(len(touch)) + b''.join(string(s) for s in touch)
    patched += new_language_tail
    obj.set_raw_data(bytes(patched))
    output = destination / 'Shotgun Cop Man_Data' / 'resources.assets'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(obj.assets_file.save())
    
    # Reopen the serialized asset and compare every object, not just the text table.
    check = UnityPy.load(str(output))
    before = {o.path_id: o.get_raw_data() for o in UnityPy.load(str(source)).objects}
    after = {o.path_id: o.get_raw_data() for o in check.objects}
    assert before.keys() == after.keys()
    assert [k for k in before if before[k] != after[k]] == [4903]
    entries, new_tail = parse(after[4903])
    new_language_rows, new_language_end = parse_languages(new_tail)
    assert new_language_rows[:10] == language_rows
    assert new_language_rows[10] == ('Polish', 'pl', b'\0'*4)
    assert new_tail[new_language_end:] == tail[language_end:]
    for old, new in zip(original, entries):
        assert old[:2] == new[:2]
        assert old[2] == new[2][:10] and len(new[2]) == 11
        assert old[3] == new[3][:10] and len(new[3]) == 11
        assert new[4] == (old[4] + [translations[old[0]]] if old[4] else [])
        assert new[2][10] == translations[old[0]]
    assert dict((row[0], row[2]) for row in entries)['LangName'][0] == 'English'
    print(json.dumps({'translated':len(translations), 'terms':len(entries), 'languages':len(new_language_rows), 'original_language_values_preserved':len(entries)*10, 'objects_verified':len(after), 'output':str(output), 'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}))

    archive = destination / f'Shotgun-Cop-Man-PL-{VERSION}.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as package:
        package.write(output, 'Shotgun Cop Man_Data/resources.assets')
        package.write(ROOT / 'docs/INSTALL.txt', 'READ-ME.txt')
    with zipfile.ZipFile(archive) as package:
        assert package.testzip() is None
        assert package.read('Shotgun Cop Man_Data/resources.assets') == output.read_bytes()
    print(archive)

if __name__ == '__main__':
    main()
