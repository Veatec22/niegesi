import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parents[1]/'tools'))
from translations import load_entries,polish_by_key,update_polish  # noqa: E402
ROWS=load_entries(ROOT)
def group(name):return [r for r in ROWS if r['key'].split('/')[0]==name]
def show(name,start=0,end=10000):
 p=polish_by_key(ROOT)
 for i,r in enumerate(group(name)):
  if start<=i<end and r['key'] not in p:print(str(i)+' '+r['english'].replace('\n','\\n'))
def put(name,lines):
 p=polish_by_key(ROOT);rs=group(name);new={}
 for line in lines.strip('\n').splitlines():
  idx,value=line.split('\t',1);key=rs[int(idx)]['key'];assert key not in p,key;new[key]=value.replace('\\n','\n')
 update_polish(ROOT,new);print(name,len(polish_by_key(ROOT)))
