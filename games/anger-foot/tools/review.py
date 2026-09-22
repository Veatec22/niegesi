"""Write translations/en-pl-review.json: English beside Polish, with speaker and addressee.

Source of truth is translations/pl.json (keyed by path_id). English, context notes,
speaker and addressee come from work/ref-all.json, produced by work/ref-extract.py
from the original resources.assets. Key format: `<path> [<speaker> > <addressee>]`,
so the l10n report can match speakers by regex.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ref = json.loads((ROOT / 'work/ref-all.json').read_text(encoding='utf-8'))
pl = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))
rows = []
for pid, r in sorted(ref.items(), key=lambda kv: kv[1]['path']):
    key = r['path'] + (f" [{r['speaker']} > {r['to']}]" if r['speaker'] else '')
    rows.append(dict(id=int(pid), key=key, english=r['en'], polish=pl.get(pid, ''), context=r['note']))
(ROOT / 'translations/en-pl-review.json').write_text(
    json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(rows), 'rows,', sum(1 for r in rows if r['polish']), 'translated')
