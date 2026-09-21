from game_pak import GamePak
from pathlib import Path
import re
p=GamePak(r'C:\Games\SPRAWL_GOG\Sprawl\Content\Paks\Sprawl-WindowsNoEditor.pak')
for name in p.files:
 if name.endswith('.uasset') and ('/UI/' in name or '/UserInterface/' in name or 'GameInstance' in name):
  data=p.extract(name)
  if any(x in data for x in [b'SetCurrentCulture',b'GetCurrentCulture',b'Flags/UK',b'CultureName',b'LanguageIndex']):
   print(name)
   print([x.decode(errors='replace') for x in re.findall(rb'[\x20-\x7e]{4,}',data) if any(y in x.lower() for y in [b'lang',b'cultur',b'flag',b'save'])])
   target=Path('games/sprawl/work/assets')/name; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
   target.with_suffix('.uexp').write_bytes(p.extract(name[:-7]+'.uexp'))
