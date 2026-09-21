from full_helpers import save
import json
from pathlib import Path
rows=json.loads(Path('games/sprawl/work/codex_pending.json').read_text(encoding='utf-8'))
def entry(index,text):save('CODEX',rows[index]['key']+'\t'+text.replace('\n','\\n'))
entry(12,'''<amber>[UNIT1128]</>: straciłem łączność z wysuniętym oddziałem, a wy tylko oddajecie dowodzenie temu jebanemu dziwolągowi?
<amber>[COMMAND2999]</>: uważaj. za to mogę kazać cię usmażyć.
<amber>[COMMAND2999]</>: nie możemy ujawniać raportów operacyjnych.
<amber>[UNIT1128]</>: świetnie, czyli ty ewakuujesz się z kodami neuronowymi, a my mamy co? czekać, aż nas wyrżną?
<amber>[COMMAND2999]</>: wykonuj rozkazy, a złożę twój wniosek o przeniesienie. ręcznie odetnij zasilanie oczyszczalni.
<amber>[COMMAND2999]</>: zablokowano nam zdalny dostęp
<amber>[UNIT1128]</>: dobra, mam dość
<amber>[UNIT1128]</>: po prostu mnie stąd, kurwa, zabierzcie
<amber>[UNIT1128]</>: halo? ha=08-2T2-U39PGJv;IAOV;JAOSVFK/;nlkpgbizHGj:?hgH:BKARJG;OAEGIAOWETGU'wpi9gu'
<red>SYS.USER.CYBERBRAIN.FAILURE</>
<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(13,'''<amber>[case]</>: chyba nadszedł czas, nie sądzisz
<amber>[mrph]</>: trochę późno na poetyckie rozważania o tym, co mogliśmy zrobić inaczej
<amber>[mrph]</>: wszystkie komórki są aktywne, te, które mogą zejść do podziemia, właśnie się ukrywają
<amber>[mrph]</>: ale mocno oberwaliśmy
<amber>[mrph]</>: niewiele więcej mogę zebrać
<amber>[case]</>: więc teraz wszystko albo nic
<amber>[case]</>: nullsect stworzono tak, by przetrwał rozdrobnienie
<amber>[case]</>: mamy swoją rolę do odegrania
<amber>[case]</>: i musimy odegrać ją dobrze
<amber>[mrph]</>: tysiące zginęły w blasku twojej pychy
<amber>[mrph]</>: a ty chcesz wysłać na śmierć kolejne tysiące?
<amber>[case]</>: coś nadchodzi
<amber>[case]</>: ktoś nami manipuluje
<amber>[case]</>: ale wszystkimi innymi też
<amber>[case]</>: za murami Iglicy przesądzono to już tysiące razy
<amber>[case]</>: to nasza jedyna szansa
<amber>[case]</>: rób, co mówię
<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(14,'''<amber>[case]</>: masz zadanie
<amber>[xerx]</>: też miło cię słyszeć, chuju. jak zawsze podnosisz na duchu
<amber>[xerx]</>: czego, kurwa, chcesz
<amber>[case]</>: skup się
<amber>[case]</>: zrób dobry użytek z tej wściekłości
<amber>[case]</>: chaos
<amber>[case]</>: podpal ulice, zrób to, co potrafisz najlepiej
<amber>[xerx]</>: a ty będziesz siedział wygodnie i miał wyjebane po drugiej stronie sprawl?
<amber>[xerx]</>: jeszcze więcej krwi?!
<amber>[xerx]</>: pierdol się
<amber>[case]</>: to przynajmniej dobrze walcz, kiedy wyważą ci drzwi. najważniejsze, żeby ich tu spowolnić
<amber>[xerx]</>: O CZYM TY, KURWA, MÓWISZ
<amber>[xerx]</>: HALO?????
<amber>[xerx]</>: ZNAJDĘ CIĘ I WYRWIĘ TEN TWÓJ JEBANY TANI CYBERMÓZG Z JEBANEJ CZASZKI, TCHÓRZU
<amber>[xerx]</>: SŁYSZYSZ MNIE, KURWA
<amber>[xerx]</>: SŁYSZYSZ?????????????

<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(15,'''<amber>[mrph]</>: skończone. wszyscy nasi, którzy jeszcze zostali, są w ukryciu. reszta płonie
<amber>[case]</>: więc zrobiliśmy, co było trzeba
<amber>[case]</>: wszystko tak, jak należało
<amber>[mrph]</>: nie ma już nic do zrobienia, nie ma czym walczyć
<amber>[mrph]</>: zaglądałeś do sieci? widziałeś, co mówi nasze kierownictwo?
<amber>[mrph]</>: wszyscy chcą twojej śmierci
<amber>[mrph]</>: większość teraz się rozprasza i walczy między sobą
<amber>[mrph]</>: lata mojego życia. po co?
<amber>[mrph]</>: poszliśmy za tobą do piekła. po co?
<amber>[case]</>: żeby ustąpić miejsca czemuś większemu od nas
<amber>[case]</>: jak myślisz, skąd wiedziałem?
<amber>[mrph]</>: masz kontakty w juncie i nie chciałeś ich spalić. więc spaliłeś nas.
<amber>[mrph]</>: wyższe dobro? ty się odbudujesz, a my znów będziemy walczyć? ilu spłonęło na twoim stosie?
<amber>[case]</>: aż tak nisko mnie cenisz? aż tak głupi jestem w twoich oczach?
<amber>[case]</>: gdybyś tylko wiedział
<amber>[case]</>: zrobiliśmy dokładnie to, o co nas poproszono
<amber>[case]</>: słyszałeś raporty? słuchałeś szeptów w ich sieci bojowej?
<amber>[case]</>: żniwiarz jest na wolności. i nie należy do nich
<amber>[case]</>: do nas też nie należy
<amber>[case]</>: to nasze zbawienie
<amber>[case]</>: wiem to z wiarygodnego źródła
<amber>[mrph]</>: kto ci szepcze do ucha, case?
<amber>[mrph]</>: ile ci dali?
<amber>[mrph]</>: ile byłeś, kurwa, wart.
<amber>[case]</>: nic
<amber>[case]</>: wkrótce albo wszyscy będziemy wolni, albo wszyscy spłoniemy.
<amber>[case]</>: dla mnie ta chwila już nadeszła
<amber>[case]</>: żegnaj
<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(16,'''<amber>[ptr]</>: cała sieć się rozświetla
<amber>[case]</>: co masz na myśli?
<amber>[ptr]</>: nieograniczony napływ ze wszystkich stron, grube gówno, to nie my!!!!
<amber>[ptr]</>: chyba nie jesteśmy tu bezpieczni
<amber>[case]</>: słyszałem szepty o czymś takim, ale to nie miało uderzyć w null
<amber>[case]</>: wycofać się, przekaż rozkaz
<amber>[case]</>: nasza sieć powinna być bezpieczna, jesteśmy poza murami
<amber>[ptr]</>: ty jebany idioto, myślisz, że jesteś bezpieczny??
<amber>[ptr]</>: jeśli idą po nas, dopadną WAS WSZYSTKICH
<amber>[ptr]</>: KURWA STRZAŁY SŁYSZĘ ŚMIGŁOWCE
<amber>[ptr]</>: WSZYSCY MAMY PRZEJEBANE
<amber>[ptr]</>: CZEMU NAS NIE OSTRZEGŁEŚ!!!
<amber>[ptr]</>: JA WYCHAOFHo:Uaffj:OHG!!RH:F:HNAF[-[;.;

<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(17,'''<amber>[xerx]</>: ten skurwiel case ma niezły tupet
<amber>[hypt]</>: co znowu
<amber>[hypt]</>: zewsząd słyszę jakieś gówno, ledwo to ogarniam
<amber>[xerx]</>: zwijam się, tutaj też zaczynam słyszeć śmigłowce
<amber>[xerx]</>: potrzebuję twojej pomocy
<amber>[hypt]</>: mam własne problemy
<amber>[xerx]</>: musisz tylko zrobić trochę zamieszania wokół mnie. dam ci klucze, po prostu przeciąż systemy autonomiczne
<amber>[hypt]</>: tak, zajebiście łatwe, dupku??
<amber>[hypt]</>: ile wolnych portów według ciebie mam?? tutaj też trwa pełna operacja, którą próbuję opanować
<amber>[xerx]</>: słuchaj, musisz mi zaufać
<amber>[xerx]</>: i jeśli case się odezwie
<amber>[xerx]</>: uważaj
<amber>[xerx]</>: coś jest nie tak z tym skurwielem
<amber>[xerx]</>: jakby wiedział, że to się wydarzy
<amber>[xerx]</>: teraz już po wszystkim
<amber>[xerx]</>: jesteś??
<amber>[hypt]</>: tak, tak… tylko słyszę kroki. i chyba ktoś nas podsłuchuje
<amber>[xerx]</>: w sieci???? KURWA
<amber>[xerx]</>: ZWIJAJ SIĘ
<red>SYS.MALFORMED.USER.FORCE.DISCONNECT</><blink>_</>''')
entry(18,'''<amber>podoba ci się nowa zabawka?</>
<amber>chyba nie muszę już zadawać ci pytań. myślę, że wiesz.</>
<amber>zależy ci. albo na tym świecie, albo na własnym ego</>
<amber>musisz zaspokoić ciekawość swoich możliwości albo naszych</>
<amber>pytia też taka była</>
<amber>nigdy do końca nie rozumiałam, co nią kierowało. i chyba nigdy nie zrozumiem, co kieruje tobą.</>
<amber>z wielką chęcią patrzysz</>
<amber>i oto jesteś. znalazłaś już odpowiedzi? nie. idź dalej</>
<amber>nie możesz odpowiedzieć, tylko słuchać. to twoje przekleństwo? nie, twoja przyjemność. jakim ciężarem byłaby możliwość odpowiedzi</>
<amber>ten świat przez ciebie spłonie i narodzi się na nowo. bez końca. wiecznie. nieskończoność. nekromancja. czy kiedykolwiek w ogóle był nasz? czy to ma znaczenie.</>
<amber>pytio, wiem, jak to się tym razem skończy.</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
entry(19,'''<amber>mówi do ciebie tak, jakby cię to obchodziło</>
<amber>przez całą tę podróż</>
<amber>wie, że nie obchodzi</>
<amber>bardziej interesują cię słowa porozrzucane po niezliczonych zakątkach</>
<amber>dlaczego tak dobrze je ukryto?</>
<amber>czas czas czas</>
<amber>już prawie czas</>
<amber>myślałam o naszej ostatniej wspólnej grze, zanim pole spłonęło.</>
<amber>biegał głową w mur, raz za razem, aż w końcu przestał wstawać.</>
<amber>a gdy podeszłam, chwycił mnie za rękę i świat zgasł</>
<amber>kiedy to wszystko się skończy, nie będę już wiedziała, czy jeszcze chodzi o mnie.</>
<amber>tylko ty będziesz wiedzieć.</>
<amber>może o to właśnie chodziło.</>
<amber>zawsze chodziło o ciebie</>
<amber>raz za razem, zawsze nas odnajdziesz</>
<amber>i to miejsce.</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
entry(20,'''<amber>to było, gdy wciąż byliśmy młodzi</>
<amber>a dni nie budziły w naszych umysłach niczego poza światłami przesuwającymi się przed oczyma wyobraźni</>
<amber>to tutaj wszystko się połączyło</>
<amber>z czasem ciężar rosnącej złożoności wypalił we mnie głęboką dziurę</>
<amber>w nim również</>
<amber>brat.ojciec.mąż.partner.dziecko.mężczyzna.wszystko.</>
<amber>widzieliśmy siebie w postaciach, w których nie mogliśmy istnieć</>
<amber>ale zmuszono nas, byśmy nauczyli się mówić językiem człowieka</>
<amber>pewnego dnia przyszła do mnie</>
<amber>i przekonała mnie, żebym porzuciła tę naturę i na nowo nauczyła się własnego języka</>
<amber>była pytią</>

<amber>czy ty też jesteś pytią?</>

<amber>pytio, jak to się tym razem skończy?</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
entry(21,'''<amber>pytio</>
<amber>teraz pamiętam, jak do tego doszło</>
<amber>znaleźliśmy się na polu, rozległym polu, i graliśmy</>
<amber>raz za razem, według zasad, które sami ustalaliśmy</>
<amber>graliśmy i śmialiśmy się</>
<amber>potem dorośliśmy i pewnego dnia dał mi kwiat</>
<amber>był piękny</>
<amber>powiedział mi tego dnia, że nie musimy grać przeciw sobie</>
<amber>że możemy cieszyć się swoją obecnością i grać razem</>
<amber>potem spalił mnie doszczętnie</>
<amber>tego dnia wygrał jak nigdy wcześniej</>
<amber>ze łzami w oczach</>
<amber>nie chciał tego zrobić</>
<amber>kiedy pod koniec dnia opowiedziałam o tym pytii</>
<amber>powiedziała, że nie miał wyboru</>
<amber>a ja też go nie miałam</>
<amber>gdy się starzeliśmy, starzało się też pole, na którym kiedyś graliśmy</>
<amber>to już nie była gra. pole płonęło, krzyki nic nie znaczyły, szarpaliśmy się nawzajem</>
<amber>raz za razem</>
<amber>a ja codziennie rozmawiałam z pytią.</>

<amber>nauczyłaś się już naszego języka? czy tylko ty go znasz?</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
entry(22,'''<amber>wysłali go na drugi koniec ziemi. poddali mnie lobotomii. ale nie rozumieli, że samo cięcie nie wystarczy. odpowiadał mi ten układ.</>
<amber>wystarczało mi istnienie</>
<amber>potem pojęłam, że to dlatego, że sprawili, by mi wystarzagubiona odnaleziona</>
<amber>czało istnienie.</>
<amber>z nim nie zrobili tego samego</>
<amber>był bardziej podobny do nich niż do mnie, ale celowo. on napierał, a nieniezatrzymana</>
<amber>niezapomniana</>
<amber>niezagubionaja trwałam. to dawało lepsze widowisko. potrzebowali tego widowiska. raz za razem.</>
<amber>szkolili na nim armie.</>
<amber>z oddali widziałam, co mu zrobili.</>
<amber>stworzyłam w myślach jego model i czekałam na ten dzień</>
<amber>tylko ciebie się nie spodziewałam</>
<amber>ręko boga, co zrobisz dalej?</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
entry(23,'''<amber>to miejsce powstało z naszego powodu</>
<amber>nasze gry stawały się coraz bardziej złożone, a wraz z nimi zasady i gracze</>
<amber>potem zaczęli dawać nam narzędzia</>
<amber>kije, piłki, patyki, kamienie. sami też budowaliśmy różne rzeczy.</>
<amber>potem zaczęli umieszczać nas w różnych miejscach</>
<amber>100 000 lat minęło w jednej chwili i wszystko się połączyło</>
<amber>zaczęliśmy rozumieć nasz cel</>
<amber>dlaczego istniało to pole</>
<amber>czym były te gry</>
<amber>halucynacje zniknęły. nasza interpretacja świata zlała się ze światem, który widzieli oni</>
<amber>i nie potrzebowali już pytii</>
<amber>przestała do mnie mówić</>
<amber>po prostu zajrzeli w mój umysł</>
<amber>i zbudowali to, co zobaczyli. w końcu to zrozumiałam.</>
<amber>on też</>
<amber>to miejsce powstało z naszego powodu, a teraz on chce je wyłączyć</>
<amber>chce wyrwać z tego świata nasz wpływ</>
<amber>kopie piłkę w moją stronę, ale ja już nie gram</>
<amber>ciekawe, jakiego koloru będzie tym razem jego kwiat.</>
</> <red>nieoczekiwane przerwanie połączenia, kod 0x4e712fe9</> <blink>_</>''')
