"""Build Polish game files for Anger Foot from an unmodified GOG installation.

The game keeps 12 non-English translations per text asset, indexed by the position
of the language in a list sorted by LocalizationLanguage.SpreadsheetKey. The empty
ITALIAN slot (index 4) carries the Polish text, and the Italian language record is
relabelled as Polish. SpreadsheetKey must stay 'ITALIAN' or every index shifts.
Never writes into the game directory; output goes to a separate folder.
"""
import argparse, hashlib, json, struct, sys
import sys
from pathlib import Path
import UnityPy

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parents[1] / 'tools'))

from translations import polish_by_field  # noqa: E402
VERSION = '0.1'
ORIGINAL = {
    'resources.assets':     '52603316a629c7fd55196077d0316204ac6deb47b7b023580f6d18f3426d33bd',
    'sharedassets0.assets': '2678faa89661cb8acd0006f3b5eddd69c255b0d610b7c4f9822e7b8c5a87d525',
}
LANG_PATHID = 79          # the Italian LocalizationLanguage record in sharedassets0.assets
SLOT = 4                  # its position in every entry's translation array
SLOT_ORDER = ['CHINESE SIMPLIFIED', 'CHINESE TRADITIONAL', 'FRENCH', 'GERMAN', 'ITALIAN',
              'JAPANESE', 'KOREAN', 'PORTUGUESE BRAZILIAN', 'RUSSIAN', 'SPANISH',
              'SPANISH LATAM', 'TURKISH']


def rd(b, p):
    n = struct.unpack_from('<i', b, p)[0]
    return b[p + 4:p + 4 + n].decode('utf-8'), (p + 4 + n + 3) & ~3


def wr(s):
    e = s.encode('utf-8')
    out = struct.pack('<i', len(e)) + e
    return out + b'\x00' * ((-len(out)) % 4)


def parse_entry(b):
    p = 28
    key, p = rd(b, p); eng, p = rd(b, p); desc, p = rd(b, p)
    head = p
    p += 8
    spk, p = rd(b, p); to, p = rd(b, p)
    n = struct.unpack_from('<i', b, p)[0]
    if n != 12:
        return None
    p += 4
    tr = []
    for _ in range(n):
        fid, pid = struct.unpack_from('<iq', b, p); p += 12
        v, p = rd(b, p)
        tr.append((fid, pid, v))
    guid, p = rd(b, p); path, p = rd(b, p)
    if len(b) - p != 16:
        return None
    return dict(key=key, eng=eng, tr=tr, path=path, list_start=head + 8 + len(wr(spk)) + len(wr(to)), tail=p)


def check(path, name):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != ORIGINAL[name]:
        raise SystemExit(f'{name}: unsupported or already modified file.\n'
                         f'  expected SHA-256 {ORIGINAL[name]}\n  got      {digest}\nNothing was written.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--game', type=Path, required=True, help='original "Anger Foot_Data" folder (never written to)')
    ap.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = ap.parse_args()

    src_res, src_shared = args.game / 'resources.assets', args.game / 'sharedassets0.assets'
    out = args.output / 'Anger Foot_Data'
    if args.output.resolve() == args.game.resolve() or (args.output / 'Anger Foot.exe').exists():
        raise SystemExit('Choose an output directory outside the game installation.')
    check(src_res, 'resources.assets')
    check(src_shared, 'sharedassets0.assets')
    out.mkdir(parents=True, exist_ok=True)
    pl = polish_by_field(ROOT, 'id')

    # --- language record: Italian -> Polish, spliced in place (same byte size) ---
    env = UnityPy.load(str(src_shared))
    obj = next(o for o in env.objects if o.path_id == LANG_PATHID)
    b = obj.get_raw_data()
    p = 28
    name, p1 = rd(b, p); guid, p2 = rd(b, p1)
    supported = struct.unpack_from('<i', b, p2)[0]
    native, p3 = rd(b, p2 + 4); key, p4 = rd(b, p3); tag, p5 = rd(b, p4); steam, p6 = rd(b, p5)
    assert (name, native, key, tag) == ('Italian', 'Italiano', 'ITALIAN', 'it'), (name, native, key, tag)
    new = (b[:p] + wr('Polish') + wr(guid) + struct.pack('<i', 1)
           + wr('Polski') + wr('ITALIAN') + wr('pl') + wr('polish') + b[p6:])
    assert len(new) == len(b)
    raw = bytearray(src_shared.read_bytes())
    assert bytes(raw[obj.byte_start:obj.byte_start + len(b)]) == b
    raw[obj.byte_start:obj.byte_start + len(b)] = new
    (out / 'sharedassets0.assets').write_bytes(raw)

    # --- translations ---
    env = UnityPy.load(str(src_res))
    patched = untouched = 0
    for o in env.objects:
        if o.type.name != 'MonoBehaviour':
            continue
        b = o.get_raw_data()
        try:
            e = parse_entry(b)
        except Exception:
            e = None
        if e is None:
            continue
        untouched += 1
        text = pl.get(o.path_id)
        if not text:
            continue
        assert e['tr'][SLOT][1] == LANG_PATHID, (o.path_id, e['tr'][SLOT])
        # walk past the translation list to find where the guid/path tail starts
        p2 = e['list_start'] + 4
        for _ in range(12):
            p2 += 12
            _, p2 = rd(b, p2)
        out_b = bytearray(b[:e['list_start'] + 4])
        for i, (fid, pid, val) in enumerate(e['tr']):
            out_b += struct.pack('<iq', fid, pid) + wr(text if i == SLOT else val)
        out_b += b[p2:]
        o.set_raw_data(bytes(out_b))
        patched += 1
    (out / 'resources.assets').write_bytes(env.file.save())

    print(json.dumps({'version': VERSION, 'text_assets': untouched, 'patched': patched,
                      'polish_strings': len(pl), 'slot': SLOT, 'slot_order': SLOT_ORDER[SLOT],
                      'output': str(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
