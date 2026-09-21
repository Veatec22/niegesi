import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROWS=json.loads((ROOT/'translations/en-pl-review.json').read_text(encoding='utf-8'))
def group(name):return [r for r in ROWS if r['key'].split('/')[0]==name]
def show(name,start=0,end=10000):
 p=json.loads((ROOT/'translations/pl.json').read_text(encoding='utf-8'))
 for i,r in enumerate(group(name)):
  if start<=i<end and r['key'] not in p:print(str(i)+' '+r['english'].replace('\n','\\n'))
def put(name,lines):
 pth=ROOT/'translations/pl.json';p=json.loads(pth.read_text(encoding='utf-8'));rs=group(name)
 for line in lines.strip('\n').splitlines():
  idx,value=line.split('\t',1);key=rs[int(idx)]['key'];assert key not in p,key;p[key]=value.replace('\\n','\n')
 pth.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(name,len(p))
