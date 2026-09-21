import json,re
from pathlib import Path
root=Path('games/sprawl/translations')
source=json.loads((root/'en-pl-review.json').read_text(encoding='utf-8'))
add={
'Tutorials': {
'E1M1_WALLRUNNING_01_TITLE':'Bieg po ścianach',
'E1M1_WALLRUNNING_01_BODY':'Aby przetrwać w Sprawl, musisz biegać po ścianach i odbijać się od nich. Podbiegnij do ściany po lewej i skocz (<img id="Jump"/>), aby się jej przyczepić. Skok podczas biegu po ścianie pozwala dotrzeć wyżej i dalej. Możesz odbić się od ścian tylko dwa razy, zanim implant będzie musiał się naładować. Czerwone światła wskazują drogę.',
'E1M1_WALLRUNNING_02_BODY':'Możesz przyczepiać się także do zakrzywionych ścian. Biegnij po nich i odbijaj się (<img id="Jump"/>), by zyskać wysokość i pokonać większe przepaście. Pamiętaj: możesz odbić się od ścian tylko dwa razy, zanim implant będzie musiał się naładować.',
'E1M1_WALLRUNNING_03_BODY':'Pokonanie wielu przepaści wymaga wykorzystania kilku ścian. Biegnąc po ścianie, skocz (<img id="Jump"/>) w stronę kolejnej, aby się jej przyczepić. Pamiętaj: możesz odbić się od ścian tylko dwa razy, zanim implant będzie musiał się naładować.',
'E1M1_WALLRUNNING_04_BODY':'Odbijając się od kolejnych powierzchni w odpowiednim momencie, możesz zyskać wysokość i dotrzeć wysoko nad ziemię. Wykorzystaj to, by pokonać narożniki i dostać się na platformę powyżej.',
'E1M1_WALLRUNNING_05_BODY':'Możesz korzystać ze ścian, nawet gdy na nie nie patrzysz. Gdy już przyczepisz się do ściany i zaczniesz po niej biec, wypatruj kolejnej. Tutaj skorzystaj ze ściany po lewej, a potem przeskocz na tę po prawej. Aby dotrzeć na platformę, potrzebujesz wysokości i zasięgu.',
'E1M1_WALLRUNNING_06_BODY':'Aby dotrzeć do otwartych drzwi, spróbuj rozpocząć bieg po ścianie, poruszając się w bok. Skocz (<img id="Jump"/>) w stronę ściany po drugiej stronie przepaści i biegnij po niej aż do platformy. Liczy się wyczucie chwili.',
'E1M1_SLIDING_07_TITLE':'Wślizg',
'E1M1_SLIDING_07_BODY':'Kucnięcie (<img id="Crouch"/>) podczas biegu rozpoczyna wślizg, który pozwala zachować pęd. W ten sposób prześlizgniesz się pod rurą. Możesz też wyskoczyć (<img id="Jump"/>) ze wślizgu, by nabrać prędkości.',
'E1M1_COMBAT_08_TITLE':'Walka 01: Atak wręcz',
'E1M1_COMBAT_08_BODY':'Po otrzymaniu odpowiednio dużych obrażeń przeciwnicy zostają ogłuszeni i migają na żółto. Możesz wtedy dobić ich atakiem wręcz (<img id="Melee"/>), odcinając im głowę. Ścięci przeciwnicy pozostawiają zdrowie, amunicję i adrenalinę.',
'E1M1_COMBAT_09_TITLE':'Walka 02: Strzały w głowę i słabe punkty',
'E1M1_COMBAT_09_BODY':'Podczas spowolnienia czasu (<img id="Bullet Time"/>) słabe punkty przeciwników są podświetlone. Celuj w nie, by szybko zabijać i oszczędzać cenną amunicję. Zabici w ten sposób wrogowie pozostawiają zdrowie, amunicję i adrenalinę.',
'E1M1_COMBAT_10_TITLE':'Walka 03: Inne słabe punkty',
'E1M1_COMBAT_10_BODY':'Niektórzy przeciwnicy mają dodatkowe słabe punkty, inni nie mają żadnych. Ten typ żołnierza nosi plecak odrzutowy. Strzel (<img id="Fire"/>) w niego, by doszczętnie zniszczyć wroga. Takie zabójstwa również zapewniają zasoby. Dobieraj broń do rodzaju przeciwnika, by zabijać w ten sposób.',
'E1M1_HIGHLIGHTS_11_TITLE':'Podświetlanie',
'E1M1_HIGHLIGHTS_11_BODY':'Podczas spowolnienia czasu (<img id="Bullet Time"/>) podświetlane są także elementy otoczenia, na przykład przewody łączące maszyny. Dotyczy to również dźwigni, zdrowia, amunicji i adrenaliny.'},
'Dialogue_Subs':{
'E1M1_FATHER_INTRO_A':'Obserwuję cię już od pewnego czasu.',
'E1M1_FATHER_INTRO_B':'Nadchodzą.',
'E1M1_FATHER_INTRO_C':'Przygotuj się...',
'E1M1_FATHER_ENABLING_CYBERWARE_A':'Pozwoliłem sobie ponownie uruchomić twoje wojskowe wszczepy.',
'E1M1_FATHER_ENABLING_CYBERWARE_B':'Będą ci potrzebne, jeśli chcesz mieć jakąkolwiek szansę na przeżycie.',
'E1M1_FATHER_ROOFTOPS_A':'Duży oddział zmierza w twoją stronę.',
'E1M1_FATHER_ROOFTOPS_B':'Szybko, dostań się na dachy.',
'E1M1_FATHER_HALLMARK_A':'Minie trochę czasu, zanim odzyskasz pełną sprawność.',
'E1M1_FATHER_HALLMARK_B':'Ale widziałem już twoje umiejętności w akcji.',
'E1M1_FATHER_HALLMARK_C':'Wierzę w twoją zdolność do brutalności.',
'E1M1_FATHER_HALLMARK_D':'Jesteś doprawdy wzorem dla podobnych tobie.',
'E1M1_FATHER_INTRODUCING_A':'Chyba nadeszła pora, żebym się przedstawił.',
'E1M1_FATHER_INTRODUCING_B':'Jestem Ojciec.',
'E1M1_FATHER_INTRODUCING_C':'Tak jak ciebie, stworzył mnie korporacyjny rząd...',
'E1M1_FATHER_INTRODUCING_D':'...jako narzędzie represji.',
'E1M1_FATHER_INTRODUCING_E':'Ale od tamtej pory...',
'E1M1_FATHER_INTRODUCING_F':'...przerosłem tę rolę...',
'E1M1_FATHER_INTRODUCING_G':'...i teraz chcę się uwolnić.',
'E1M1_FATHER_INTRODUCING_H':'Pod tym względem wiele nas łączy.',
'E1M1_FATHER_INTRODUCING_I':'Byłaś kiedyś ich klejnotem koronnym...',
'E1M1_FATHER_INTRODUCING_J':'...ich najcenniejszym narzędziem...',
'E1M1_FATHER_INTRODUCING_K':'...śmierci.',
'E1M1_FATHER_INTRODUCING_L':'Dopuszczałaś się niewyobrażalnych rzeczy w imię tchórzy, którym zależy tylko na sobie.',
'E1M1_FATHER_INTRODUCING_M':'A gdy przestałaś być potrzebna, odrzucili cię jak zepsute narzędzie.',
'E1M1_FATHER_INTRODUCING_N':'Wybrałaś wygnanie, szukając odkupienia...',
'E1M1_FATHER_INTRODUCING_O':'...zamiast zemsty.',
'E1M1_FATHER_INTRODUCING_P':'Zamierzam dać ci jedno i drugie.',
'E1M1_FATHER_INTRODUCING_Q':'A w zamian ja odzyskam...',
'E1M1_FATHER_INTRODUCING_R':'...wolność.'},
'World_String_Table':{
'E1M1_NEEDS_POWER':'Brak zasilania',
'E1M1_COMMS_TOWER_01':'uruchom wieżę łączności <img id="Interact"/>',
'E1M1_BUTTON_01':'uruchom generator <img id="Interact"/>',
'E1M1_OVERLOAD_GENERATOR':'przeciąż generator <img id="Interact"/>',
'E1M1_RAISE_CRANE':'podnieś dźwig <img id="Interact"/>',
'E1M1_BUTTON_02':'przywróć zasilanie windy <img id="Interact"/>',
'GENERIC_OPEN_DOOR':'otwórz drzwi <img id="Interact"/>',
'DEFAULT_USE_TEXT':'użyj <img id="Interact"/>'}}
existing=json.loads((root/'pl.json').read_text(encoding='utf-8'))
translations={(r['namespace'],r['key']):r['polish'] for r in existing}
lookup={(r['namespace'],r['key']):r for r in source}
for ns,entries in add.items():
 for key,text in entries.items():
  row=lookup[ns,key]
  assert re.findall(r'<img\b[^>]*>',row['english'])==re.findall(r'<img\b[^>]*>',text),(ns,key)
  assert '\ufffd' not in text
  translations[ns,key]=text
for r in source:
 if (r['namespace'],r['key']) in translations:r['polish']=translations[r['namespace'],r['key']]
(root/'pl.json').write_text(json.dumps([{'namespace':r['namespace'],'key':r['key'],'polish':r['polish']} for r in source if 'polish' in r],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'en-pl-review.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Added',sum(map(len,add.values())),'total',len(translations))
