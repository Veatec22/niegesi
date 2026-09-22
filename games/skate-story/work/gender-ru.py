"""Porównanie form rodzajowych 1. i 2. osoby: rosyjska kolumna gry vs pl.json.

Wypisuje wpisy, w których RU mówi „я …ла” a PL „-łem” (albo odwrotnie), oraz to samo dla „ты”.
To poszlaka, nie wyrok: rosyjscy tłumacze też pracowali bez kontekstu.
Wymaga work/ref-all.json z work/ref-extract.py.
"""
import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / 'work/ref-all.json').read_text(encoding='utf-8'))
p = json.loads((ROOT / 'translations/pl.json').read_text(encoding='utf-8'))

def ru_g(t, pron):
    t = re.sub(r'<[^>]+>|\*\w+\*', ' ', t)
    g = set()
    for s in re.split(r'[.!?\n…]', t):
        if re.search(r'\b' + pron + r'\b', s, re.I):
            if re.search(r'\b\w{2,}(?:ла|лась)\b', s): g.add('k')
            if re.search(r'\b\w{2,}[аеиоуыяё](?:л|лся)\b|\b(?:шёл|пришёл|нашёл|ушёл|пошёл|вошёл|мог|смог|помог|лёг|съел)\b', s): g.add('m')
    return g

NOT = {'stołem', 'kołem', 'aniołem', 'popiołem', 'czołem', 'dołem', 'tyłem', 'pomysłem', 'hasłem', 'masłem', 'złam', 'połam', 'reklam', 'wysyłam'}
def pl_g(t, m, f):
    g = set()
    if [w for w in re.findall(m, t, re.I) if w.lower() not in NOT]: g.add('m')
    if [w for w in re.findall(f, t, re.I) if w.lower() not in NOT]: g.add('k')
    return g

M1, F1 = r'\b\w+ł(?:em|bym)\b', r'\b\w+ł(?:am|abym)\b'
M2, F2 = r'\b\w+ł(?:eś|byś)\b', r'\b\w+ł(?:aś|abyś)\b'
for k, v in d.items():
    if k not in p: continue
    r1, p1 = ru_g(v['Russian'], 'я'), pl_g(p[k], M1, F1)
    r2, p2 = ru_g(v['Russian'], 'ты'), pl_g(p[k], M2, F2)
    if (r1 and p1 and not r1 & p1) or (r2 and p2 and not r2 & p2):
        print(k, '|', v['TYPE'], '| ja RU', r1, 'PL', p1, '| ty RU', r2, 'PL', p2)
        print('   RU:', v['Russian'].replace('\n', ' ')[:150])
        print('   PL:', p[k].replace('\n', ' ')[:150])
