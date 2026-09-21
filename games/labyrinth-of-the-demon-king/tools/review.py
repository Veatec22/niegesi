"""Build a standalone searchable EN/PL review; never alter translation text."""
import html
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def main():
    rows=json.loads((ROOT/'translations/en-pl-review.json').read_text(encoding='utf-8'))
    polish=json.loads((ROOT/'translations/pl.json').read_text(encoding='utf-8'))
    assert {x['key']:x['polish'] for x in rows}==polish
    rendered=[]
    for i,row in enumerate(rows):
        notes=row.get('notes','')
        rendered.append('<tr data-note="'+('1' if notes else '0')+'"><td>'+str(i+1)+'<br><small>'+html.escape(row['key'])+'</small></td><td class="text">'+html.escape(row['english'])+'</td><td class="text" lang="pl">'+html.escape(row['polish'])+'</td><td>'+html.escape(notes)+'</td></tr>')
    page='''<!doctype html><html lang="pl"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Labyrinth of the Demon King — review EN/PL</title>
<style>body{font:16px/1.5 system-ui;margin:0;color:#e9e4d8;background:#161818}
header{position:sticky;top:0;background:#222725;padding:16px 24px;border-bottom:1px solid #687067}
h1{font-size:21px;margin:0 0 8px}input[type=search]{font:inherit;padding:6px;width:min(600px,90%)}
label{margin:0 16px}table{border-collapse:collapse;width:100%;table-layout:fixed}th,td{padding:12px;border:1px solid #3b423e;vertical-align:top;text-align:left}
th:nth-child(1){width:12%}th:nth-child(2),th:nth-child(3){width:34%}th:nth-child(4){width:20%}
small{font-size:11px;overflow-wrap:anywhere;color:#adb9ac}.text{white-space:pre-wrap;overflow-wrap:anywhere}tr[data-note="1"]{background:#302e23}
p{margin:6px 0;color:#b8c3b6}a{color:#a9d1ae}</style>
<header><h1>Labyrinth of the Demon King — pełny przekład EN/PL</h1>
<p>1120 wpisów. Vertical potwierdzony w grze; pełna kampania czeka na przegląd.
Korekty zgłaszaj z identyfikatorem wpisu. Ta strona służy do podglądu.</p>
<input id="q" type="search" placeholder="Szukaj w EN, PL, identyfikatorze lub uwagach" aria-label="Szukaj">
<label><input id="notes" type="checkbox"> Tylko z uwagami</label><span id="count"></span></header>
<table><thead><tr><th>Numer / klucz</th><th>English</th><th>Polski</th><th>Uwagi</th></tr></thead><tbody>'''+''.join(rendered)+'''</tbody></table>
<script>const rows=Array.from(document.querySelectorAll('tbody tr'));
const search=document.querySelector('#q'),notes=document.querySelector('#notes'),count=document.querySelector('#count');
function filter(){const q=search.value.toLocaleLowerCase('pl');let n=0;for(const r of rows){r.hidden=!(r.textContent.toLocaleLowerCase('pl').includes(q)&&(!notes.checked||r.dataset.note==='1'));if(!r.hidden)n++;}count.textContent=n+' / '+rows.length;}
search.addEventListener('input',filter);notes.addEventListener('change',filter);filter();</script></html>'''
    output=ROOT/'translations/en-pl-review.html';output.write_text(page,encoding='utf-8')
    print(f'Review: {len(rows)} rows, {sum(bool(x.get("notes")) for x in rows)} notes; {output}')

if __name__=='__main__':main()
