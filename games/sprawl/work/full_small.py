from full_helpers import save
save('EnemyNames','''BERSERKER	Berserker
SPOT	Dron bojowy Okami
NINJA	Jednostka skryta Ghost
VECTOR	Elitarny infiltrator
RAIL_TURRET	Automatyczna wieżyczka G.O.R.
SHOTGUNNER	Ciężki żołnierz elitarnego oddziału Oni
OGRE	Ciężki mech klasy O.H.G.R
GRUNT	Żandarmeria junty
SPECTRE	Lekki mech klasy Spectre
BOSS_TWO	Prototyp 2501
BOSS_TWO_LAUNCHER	Prototyp 2501 (wyrzutnia)
BOSS_TWO_RAIL	Prototyp 2501 (działo szynowe)
BOSS_TWO_WEAKPOINT	Prototyp 2501 (słaby punkt)
BIG_DRONE	Prototyp 3502
RIOT	Policjant prewencji Bull
REAPER	SIX „ŻNIWIARZ”
REAPER_WP	SIX „ŻNIWIARZ” (słaby punkt)
SMOL_DRONE	Dron Sendai
BOSS_THREE	Suzumebachi
BOSS_THREE_EYE	Suzumebachi (oko)
BOSS_THREE_GUN	Suzumebachi (działo)
BOSS_THREE_LAUNCHER	Suzumebachi (wyrzutnia)
BOSS_THREE_TAIL	Suzumebachi (ogon)''')
save('Dialogue_Update_Subs','''REAPER_E3M1_INTRO	Cybermózgi nigdy nie umierają! [Obłąkańczy śmiech]
REAPER_E3M3_INTRO	Tatuś już ci nie pomoże! Cała ta wieża i tak się zawali. Zginiesz tutaj!
REAPER_E3M2_TAUNT_A	Mógłbym cię tu zatrzymać, ale co w tym zabawnego? Do zobaczenia na górze, SEVEN. [Obłąkańczy śmiech]
REAPER_E3M3_DAMAGE_03	Nie umrę po raz drugi!
REAPER_E3M3_INTRO_02	Gdybyś tylko mogła poczuć tę moc! Nic mnie nie powstrzyma!
REAPER_E3M2_WORM_B	Przekaż temu, kto szepcze ci do ucha: nie dosięgnie mnie. Niech przestanie próbować.
REAPER_E3M2_WORM_A	Ten robak i tak lepiej na tym wyjdzie martwy.
REAPER_DAMAGE_02	Dlaczego nadal walczysz? Po co? To koniec! Po prostu zdechnij!
REAPER_E3M3_DAMAGE_01	Myślisz, że wygrywasz? Nie bądź głupia!
ANNOUNCER_HORDE_WEAPON	[Nadzorca] Na ołtarzu pojawiła się nowa broń!
ANNOUNCER_HORDE_INTRO	[Nadzorca] Symulacja walki rozpocznie się za: trzy, dwa, jeden.''')
save('World_String_Table','''GENERIC_CALL_LIFT	wezwij windę <img id="Interact"/>
GENERIC_DISABLE_SHIELD_02	wyłącz osłonę <img id="Interact"/>
GENERIC_DISABLE_SHIELD_TWO	wyłącz osłonę <img id="Interact"/> (wymagane dwa)
GENERIC_DISABLE_SHIELD	wyłącz barierę <img id="Interact"/>
E1M2_SWITCH_HUNT_DOORS	włącz zasilanie drzwi <img id="Interact"/> (wymagane trzy)
GENERIC_LIFT_POWER	włącz zasilanie windy <img id="Interact"/>
E3M3_LOWER_CORE	opuść rdzeń <img id="Interact"/> (wymagane dwa)
E2M2_LOWER_PLATFORM	opuść platformę <img id="Interact"/> (wymagane cztery)
GENERIC_BLAST_DOORS	otwórz drzwi pancerne <img id="Interact"/>
E1M4_LIFT_GEN	otwórz drzwi do generatora windy <img id="Interact"/>
E1M2_EXIT	otwórz wyjście <img id="Interact"/> (wymagane dwa)
GENERIC_OVERLOAD_FAN	przeciąż wentylator <img id="Interact"/>
GENERIC_OVERLOAD_FOUR_NEEDED	przeciąż generator <img id="Interact"/> (wymagane cztery)
E2M4_OVERLOAD_POWERGRID	przeciąż sieć energetyczną <img id="Interact"/> (wymagane cztery)
GENERIC_RAISE_PLATFORM	podnieś platformę <img id="Interact"/>
GENERIC_RAISE_PLATFORM_TWO_NEEDED	podnieś platformę <img id="Interact"/> (wymagane dwa)
GENERIC_RAISE_WALLS	podnieś ściany <img id="Interact"/>
GENERIC_ENABLE_DOOR_TWO	przywróć zasilanie drzwi <img id="Interact"/> (wymagane dwa)
E3M1_TEST_LASER	przetestuj laser <img id="Interact"/>''')
import json
from full_helpers import ROOT
rows=json.loads((ROOT/'en-pl-review.json').read_text(encoding='utf-8'))
langs={'100/200':'100/200','Auto':'Automatycznie','Chinese':'Chiński','English':'Angielski','French':'Francuski','German':'Niemiecki','Italian':'Włoski','Japanese':'Japoński','Korean':'Koreański','Portuguese (Brazilian)':'Portugalski (Brazylia)','Spanish':'Hiszpański','Turkish':'Turecki','Ukranian':'Ukraiński'}
save('', '\n'.join(r['key']+'\t'+langs[r['english']] for r in rows if r['namespace']==''))
save('WeaponNames','\n'.join(r['key']+'\t'+r['english'].replace('�BORMA�','„BORMA”').replace('(PROTO)','(PROTOTYP)') for r in rows if r['namespace']=='WeaponNames'))
