"""Zrzut tabeli I2 Skate Story ze wszystkimi językami -> work/ref-all.json (poza gitem)."""
import json, sys
from pathlib import Path
import UnityPy
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from i2 import parse, parse_languages
sys.stdout.reconfigure(encoding='utf-8')
env = UnityPy.load(sys.argv[1])
obj = next(o for o in env.objects if o.path_id == 785)
entries, tail = parse(obj.get_raw_data())
langs, _ = parse_languages(tail)
names = [l[0] for l in langs]
print(names)
out = {k: dict(zip(names, vals)) for k, kind, vals, flags, touch in entries}
Path('work/ref-all.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(out))
