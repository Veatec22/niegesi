"""Read-only: dump the official I2 languages next to review keys (work/ref-<code>.json).

Used as evidence for the translation bible (speaker gender, ambiguity).
The output is game content for local analysis only and is ignored by git.
"""
import argparse
import json
from pathlib import Path
import UnityPy

from build import parse, parse_languages

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--game', type=Path, required=True)
    args = ap.parse_args()
    env = UnityPy.load(str(args.game/'Shotgun Cop Man_Data/resources.assets'))
    raw = next(o for o in env.objects if o.path_id == 4903).get_raw_data()
    entries, tail = parse(raw)
    languages, _ = parse_languages(tail)
    for index, (name, code, _flags) in enumerate(languages):
        out = {key: texts[index] for key, _kind, texts, _f, _t in entries if index < len(texts)}
        target = ROOT/'work'/f'ref-{code or name}.json'
        target.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(name, code, len(out), target.name)


if __name__ == '__main__':
    main()
