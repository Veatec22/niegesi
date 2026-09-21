"""Build a separate Polish I2 language. Never installs or launches the game."""
import argparse
import hashlib
import json
import re
import struct
import zipfile
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
SHA256 = '4a81ed99cd1e8e5e4665bde87b80d4bd551bf95c088c1b3a80ed2ecfbb9764fd'
DATA = 'My Friend Pedro - Blood Bullets Bananas_Data'
OBJECT = 2279
VERSION = '0.2'


def number(n):
    return struct.pack('<i', n)


def text(s):
    raw = s.encode('utf-8')
    return number(len(raw)) + raw + bytes(-len(raw) % 4)


class Reader:
    def __init__(self, raw, position=0):
        self.raw, self.pos = raw, position

    def number(self):
        n = struct.unpack_from('<i', self.raw, self.pos)[0]
        self.pos += 4
        return n

    def text(self):
        n = self.number()
        assert 0 <= n <= len(self.raw) - self.pos
        result = self.raw[self.pos:self.pos+n].decode('utf-8')
        self.pos = (self.pos+n+3) & ~3
        return result


def parse(raw):
    r = Reader(raw, 284)
    languages = [(r.text(), r.text(), r.number()) for _ in range(r.number())]
    middle = raw[r.pos:r.pos+8]
    r.pos += 8
    rows = []
    for _ in range(r.number()):
        key, kind, description = r.text(), r.number(), r.text()
        values = [r.text() for _ in range(r.number())]
        n = r.number()
        assert n == len(languages) == len(values)
        flags = raw[r.pos:r.pos+n]
        r.pos = (r.pos+n+3) & ~3
        extra = r.number()
        assert extra == 0
        rows.append((key, kind, description, values, flags, extra))
    assert len({row[0] for row in rows}) == len(rows)
    return raw[:284], languages, middle, rows, raw[r.pos:]


def encode(prefix, languages, middle, rows, tail):
    out = bytearray(prefix + number(len(languages)))
    for name, code, flags in languages:
        out += text(name) + text(code) + number(flags)
    out += middle + number(len(rows))
    for key, kind, description, values, flags, extra in rows:
        out += text(key) + number(kind) + text(description) + number(len(values))
        out += b''.join(text(v) for v in values)
        out += number(len(flags)) + flags + bytes(-len(flags) % 4) + number(extra)
    return bytes(out) + tail


def main():
    if not __debug__:
        raise RuntimeError('Validation requires Python without -O.')
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--original', type=Path, required=True)
    ap.add_argument('--extract', action='store_true', help='Create EN/PL review from existing translations only')
    args = ap.parse_args()
    assert hashlib.sha256(args.original.read_bytes()).hexdigest() == SHA256, 'Unsupported or modified original'
    env = UnityPy.load(str(args.original))
    obj = next(o for o in env.objects if o.path_id == OBJECT)
    raw = obj.get_raw_data()
    prefix, langs, middle, rows, tail = parse(raw)
    assert encode(prefix, langs, middle, rows, tail) == raw
    assert len(langs) == 10 and len(rows) == 721 and all(x[1] != 'pl' for x in langs)
    pl_path = ROOT / 'translations/pl.json'
    pl = json.loads(pl_path.read_text(encoding='utf-8')) if pl_path.exists() else {}
    english = {row[0]: row[3][0] for row in rows}
    assert pl.keys() <= english.keys()
    tokens = lambda s: re.findall(r'<[^>]+>|\[[^\]]+\]|\{[^}]+\}|\|', s)
    for key, value in pl.items():
        assert value and '\ufffd' not in value and '[TEST' not in value, key
        assert not any(ord(c) < 32 and c != '\n' for c in value), key
        # This single bracketed label is visible text, not an animation command.
        if key == 'inNoMap':
            assert value.startswith('[') and value.endswith(']') and english[key] == '[Not mapped]'
        else:
            assert tokens(value) == tokens(english[key]), key
    review = [{'key': k, 'english': vs[0], 'polish': pl.get(k, ''),
               'status': 'translated' if k in pl else 'english_fallback', 'context': desc}
              for k, _, desc, vs, _, _ in rows]
    review_path = ROOT / 'translations/en-pl-review.json'
    if args.extract:
        review_path.write_text(json.dumps(review, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(json.dumps({'entries': len(rows), 'translated': len(pl)}))
        return
    assert json.loads(review_path.read_text(encoding='utf-8')) == review, 'Regenerate review with --extract'
    assert pl.keys() == english.keys(), 'Full build requires every term'
    patched_rows = [(k, t, d, vs + [pl.get(k, vs[0])], flags + b'\0', extra)
                    for k, t, d, vs, flags, extra in rows]
    patched = encode(prefix, langs + [('Polish', 'pl', 0)], middle, patched_rows, tail)
    assert parse(patched) == (prefix, langs + [('Polish', 'pl', 0)], middle, patched_rows, tail)
    before = {o.path_id: o.get_raw_data() for o in env.objects}
    obj.set_raw_data(patched)
    out = ROOT / 'dist' / DATA / 'resources.assets'
    assert out.resolve() != args.original.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(obj.assets_file.save())
    after = {o.path_id: o.get_raw_data() for o in UnityPy.load(str(out)).objects}
    assert before.keys() == after.keys()
    assert [key for key in before if before[key] != after[key]] == [OBJECT]
    assert after[OBJECT] == patched
    for old, new in zip(rows, parse(after[OBJECT])[3]):
        assert old[:3] == new[:3] and old[3] == new[3][:10] and old[4] == new[4][:10]
    package = ROOT / 'dist' / f'My-Friend-Pedro-PL-{VERSION}.zip'
    with zipfile.ZipFile(package, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(out, f'{DATA}/resources.assets')
        archive.write(ROOT / 'docs/INSTALL.txt', 'READ-ME.txt')
    with zipfile.ZipFile(package) as archive:
        assert archive.testzip() is None
        assert hashlib.sha256(archive.read(f'{DATA}/resources.assets')).digest() == hashlib.sha256(out.read_bytes()).digest()
    print(json.dumps({'version': VERSION, 'translated': len(pl), 'total': len(rows), 'languages': 11,
                      'zip': str(package),
                      'output': str(out), 'sha256': hashlib.sha256(out.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    main()
