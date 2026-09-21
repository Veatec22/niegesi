"""Wyciągnij tabelę I2 z Neon Abyss do work/source.json. Nie zmienia plików gry.

    .venv\\Scripts\\python.exe games\\neon-abyss\\tools\\extract.py --game "C:\\Games\\Neon Abyss"

Źródło I2 (LanguageSourceAsset „I2Languages”) to obiekt 3492 w globalgamemanagers.assets.
Układ LanguageSourceData: terminy, potem lista języków, potem ustawienia Google.
Wynik to cudza treść (dziesięć języków gry) — work/ jest poza Gitem.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path

import UnityPy

ROOT = Path(__file__).resolve().parents[1]
DATA = 'NeonAbyss_Data'
ASSETS = 'globalgamemanagers.assets'
SHA256 = 'd342ad45b2ceb1a80e92f98313f4aa6d2eb8771b2a8b56540703ffea57baf563'
OBJECT = 3492
HEADER = 56  # PPtr GameObject, m_Enabled, PPtr Script, m_Name, flagi źródła


class Reader:
    def __init__(self, raw, position):
        self.raw, self.pos = raw, position

    def number(self):
        value = struct.unpack_from('<i', self.raw, self.pos)[0]
        self.pos += 4
        return value

    def text(self):
        size = self.number()
        assert 0 <= size <= len(self.raw) - self.pos
        value = self.raw[self.pos:self.pos + size].decode('utf-8')
        self.pos = (self.pos + size + 3) & ~3
        return value


def parse(raw):
    reader = Reader(raw, HEADER)
    terms = []
    for _ in range(reader.number()):
        key, kind, description = reader.text(), reader.number(), reader.text()
        values = [reader.text() for _ in range(reader.number())]
        flags = reader.number()
        reader.pos = (reader.pos + flags + 3) & ~3
        assert reader.number() == 0, key  # Languages_Touch
        terms.append({'key': key, 'type': kind, 'description': description, 'values': values})
    reader.number()  # CaseInsensitiveTerms + OnMissingTranslation
    reader.number()
    reader.text()    # mTerm_AppName
    languages = []
    for _ in range(reader.number()):
        languages.append({'name': reader.text(), 'code': reader.text(), 'flags': reader.number()})
    return terms, languages


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', type=Path, required=True, help='katalog gry (ten z NeonAbyss.exe)')
    args = parser.parse_args()

    path = args.game / DATA / ASSETS
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SHA256:
        raise SystemExit(f'Inna wersja {ASSETS}: {digest}, oczekiwano {SHA256}.')

    env = UnityPy.load(str(path))
    raw = next(o for o in env.objects if o.path_id == OBJECT).get_raw_data()
    terms, languages = parse(raw)
    assert raw[32:44] == b'I2Languages\0'
    assert [lang['code'] for lang in languages][3] == 'en-US'
    assert len({t['key'] for t in terms}) == len(terms)
    assert all(len(t['values']) == len(languages) for t in terms)

    out = ROOT / 'work' / 'source.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'languages': languages, 'terms': terms}, ensure_ascii=False, indent=1) + '\n',
                   encoding='utf-8')
    print(json.dumps({'terms': len(terms), 'languages': [lang['code'] for lang in languages],
                      'output': str(out)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
