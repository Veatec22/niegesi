"""Generate a local, searchable EN/PL review page from the canonical review JSON."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    rows = json.loads((ROOT / 'translations/en-pl-review.json').read_text(encoding='utf-8'))
    body = []
    for row in rows:
        ns, key = html.escape(' · '.join(filter(None, [row.get('context', ''), row.get('notes', '')]))), html.escape(row['key'])
        en, pl = html.escape(row['english']), html.escape(row.get('polish', ''))
        body.append(f'<tr><td><small>{ns}</small><code>{key}</code></td><td>{en}</td><td lang="pl">{pl}</td></tr>')
    template = '''<!doctype html>
<html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Skate Story — korekta EN / PL</title>
<style>
body{margin:0;background:#f4f4f0;color:#202622;font:16px/1.5 system-ui,sans-serif}
header{padding:24px 32px;background:#182a26;color:white}h1{margin:0;font-size:26px}
header p{margin:8px 0;color:#d5dfdb}input{box-sizing:border-box;width:100%;max-width:720px;padding:12px;font:inherit;border:1px solid #bbc9c2;border-radius:6px}
main{padding:20px 32px;overflow:auto}table{border-collapse:collapse;width:100%;table-layout:fixed;background:white}
th{text-align:left;background:#e2e9e3;padding:12px}th:first-child{width:20%}td{padding:16px;vertical-align:top;border-bottom:1px solid #d9dfd8;white-space:pre-wrap;overflow-wrap:anywhere}
td+td{border-left:1px solid #e4e8e2}small{display:block;color:#557167}code{font-size:12px}tr[hidden]{display:none}
#count{margin-left:12px;color:#d5dfdb}@media(max-width:800px){main{padding:8px}table{min-width:850px}header{padding:20px}}
</style>
<header><h1>Skate Story · korekta EN / PL</h1>
<p>Pełne tłumaczenie 0.2 · 2305 wpisów. 21 wpisów oznaczono uwagami do korekty. Podgląd bez zapisywania zmian. Do korekty podaj identyfikator wpisu i nowy tekst.</p>
<input id="search" type="search" aria-label="Szukaj w identyfikatorach i tekstach" placeholder="Szukaj tekstu, klucza lub kategorii, np. ch4/, Myślokształt, do korekty…"><span id="count"></span>
</header><main><table><thead><tr><th>Identyfikator</th><th>English</th><th>Polski</th></tr></thead><tbody>__ROWS__</tbody></table></main>
<script>
const rows=Array.from(document.querySelectorAll('tbody tr'));
const data=rows.map(row=>row.textContent.toLocaleLowerCase('pl'));
const search=document.getElementById('search'),count=document.getElementById('count');
function filter(){const query=search.value.toLocaleLowerCase('pl');let shown=0;rows.forEach((row,i)=>{row.hidden=!data[i].includes(query);if(!row.hidden)shown++;});count.textContent=shown+' / '+rows.length;}
search.addEventListener('input',filter);filter();
</script></html>'''
    target = ROOT / 'translations/en-pl-review.html'
    target.write_text(template.replace('__ROWS__', '\n'.join(body)), encoding='utf-8')
    print(target)


if __name__ == '__main__':
    main()
