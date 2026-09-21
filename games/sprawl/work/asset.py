from pathlib import Path
import struct
from game_pak import Reader
class Asset:
 def __init__(self,path):
  self.path=Path(path); self.h=self.path.read_bytes(); self.b=self.path.with_suffix('.uexp').read_bytes()
  self.names=[]; r=Reader(self.h); r.at=struct.unpack_from('<I',self.h,45)[0]
  for _ in range(struct.unpack_from('<I',self.h,41)[0]):self.names.append(r.string());r.at+=4
  self.imports=[];at=struct.unpack_from('<I',self.h,69)[0]
  for i in range(struct.unpack_from('<I',self.h,65)[0]):
   cp,cn,outer,name=struct.unpack_from('<QQiQ',self.h,at+28*i);self.imports.append((self.names[cp],self.names[cn],outer,self.names[name]))
  self.exports=[];at=struct.unpack_from('<I',self.h,61)[0]
  for i in range(struct.unpack_from('<I',self.h,57)[0]):
   p=at+104*i;c,s,t,o,n,nnum,flags,size,off=struct.unpack_from('<iiiiIIIqq',self.h,p)
   self.exports.append(dict(name=self.names[n],cls=c,outer=o,size=size,offset=off,at=p,body=self.b[off-len(self.h):off-len(self.h)+size]))
 def obj(self,i):return self.exports[i-1]['name'] if i>0 else self.imports[-i-1][3] if i<0 else 'NULL'
if __name__=='__main__':
 a=Asset(next(Path('games/sprawl/work/assets').rglob('WB_MainMenuPanel.uasset')))
 for i,e in enumerate(a.exports):
  if any(x in e['name'] for x in ['Lang','Flag','Default__WB']):
   print(i+1,e['name'],e['size'],e['offset'],e['body'][:32].hex())
   Path('games/sprawl/work/'+str(i+1)+'.bin').write_bytes(e['body'])
 a=Asset('games/sprawl/work/assets/Sprawl/Content/StringTables/LocaleInfo_PC.uasset')
 print('NAMES',list(enumerate(a.names)));print('IMPORTS',[(i+1,v) for i,v in enumerate(a.imports)]);print('EXPORTS',[(e['name'],e['at'],e['size'],e['offset']) for e in a.exports])
