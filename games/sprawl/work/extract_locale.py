from game_pak import GamePak
from pathlib import Path
import re
p=GamePak(r'C:\Games\SPRAWL_GOG\Sprawl\Content\Paks\Sprawl-WindowsNoEditor.pak')
for base in ['Sprawl/Content/StringTables/LocaleInfo_PC','Sprawl/Content/StringTables/LocaleInfo_Console','Sprawl/Content/Textures/UI/Flags/ukraine']:
 for ext in ['.uasset','.uexp']:
  data=p.extract(base+ext); target=Path('games/sprawl/work/assets')/(base+ext);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
  print(base+ext,len(data)); print([x.decode() for x in re.findall(rb'[\x20-\x7e]{3,}',data)][:120])
