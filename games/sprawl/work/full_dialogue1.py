from full_helpers import save
import json
from pathlib import Path
rows=json.loads(Path('games/sprawl/work/dialogue_pending.json').read_text(encoding='utf-8'))
text='''[Nieznany głos] Jeśli tego słuchasz, już nie żyję.
[Nieznany głos] Byłem szeptem w wielu miejscach, przemawiającym wieloma głosami.
[Nieznany głos] Mam nadzieję, że odbudujemy ten rozbity świat i wypełnimy pęknięcia złotem.
[Nieznany głos] Nadszedł czas. Powstańcie. Zniszczcie maszyny.
[Nieznany głos] Junta została pokonana. Jedna osoba stała się symbolem, powstała i stawiła opór.
[Nieznany głos] Symbol całej ich potęgi obrócił się w popiół. Iglica.
[Nieznany głos] Oddała życie za was wszystkich. Nazywała się SEVEN.
[Nadzorca] Obszar został zablokowany.
[Nadzorca] Blokada obszaru zniesiona.
[Nadzorca] Uwaga! Wyciek toksycznego chłodziwa.
[Nadzorca] Blokada windy zniesiona. Proszę udać się na środek.
Zasilanie przekierowane.
Wróć do wieży łączności.
Odblokowałem drogę do windy.
Dobrze.
Otworzyłem drzwi na platformie.
Przejdź do następnego generatora.
Dobrze. Wróć na plac i użyj dźwigni.
Zajmę się odblokowaniem bramy sektora, ale to trochę potrwa.
Gdy sygnał zostanie wysłany, dowiedzą się, że tam jesteś.
To dopiero początek czegoś większego od ciebie.
I doczekasz się zemsty.
Siły rządowe mają dość…
…zakłóceń wywoływanych przez anomalie…
…rebeliantów…
…hakerów…
…zaginionych wojskowych dezerterów, takich jak ty.
Taki właśnie los cię czekał…
Dopóki nie wkroczyłem ja.
W pobliżu jest generator. Przywróci zasilanie dźwigni na wieży łączności przed tobą…
…i da mi dostęp do ostatniej windy zaopatrzeniowej. To twoja droga ucieczki z tego piekła.
Za tą bramą są dwa generatory.
Połączą mnie z pozostałymi podsystemami…
…i dadzą mi dostęp do ostatniej windy zaopatrzeniowej.
To będzie twoja droga ucieczki z tego piekła.
Zauważyłem żołnierza modlącego się do swojego boga, więc postanowiłem go wysłuchać.
Zostawił ci prezent. Idź do świątyni i sprawdź, co to.
Tam. Użyj dźwigni.
Ty suko! Wreszcie cię znalazłem, SEVEN. Czas umierać!
Dobrze. Teraz użyj karty, by dostać się do dwóch pomieszczeń z dźwigniami.
Twoja żądza krwi jest naprawdę… nienasycona.
Nie mamy tu wielkiego wyboru.
Zablokowali naszą główną trasę.
To jedyna możliwa droga okrężna.
Chyba zorientowali się, że ktoś włamał się do ich systemów.
Zaczęli ręcznie odcinać zasilanie, żeby cię odgrodzić.
Wchodzisz do kompleksu magazynów.
Kiedyś dostarczały pomoc do Miasta za Murem.
Wyznaczyłem trasę przez główny tunel wyjazdowy.
Udaj się tam.
Wolałbym uniknąć miejskich ulic.
Komórki rebeliantów i cywile próbowali stawić opór, gdy usłyszeli, co wydarzyło się za murami.
Nie mieli żadnych szans.
Spodziewaj się silnego oporu.
Opuściłem dźwig.
Może nie potrafię wyłączyć blokad…
…ale powinnaś móc nad nimi przeskoczyć.
Zastanawiam się, czy wiesz, ilu już zabiłaś.
I ilu jeszcze zabijesz.
Interesujące…
Zamknęli ten klub.
Musisz znaleźć kartę dostępu i użyć dwóch przełączników, żeby odblokować wyjścia.
Albo i nie…
Jest droga przez starszą część miasta.
Musisz dostać się na dachy.
Ten parking wielopoziomowy ci to umożliwi.
Połóż się na pace tej ciężarówki.
Przemkniesz w ten sposób obok strażników.
Ta była kiedyś twoją ulubioną, prawda…
Jeden z głowy.
Dwa. Został jeden.
Trzy. Dobrze, drzwi powinny się teraz otworzyć.
Dobrze. Jeszcze jeden.
Chyba jeszcze nie wiedzą, że to ty…
Ale dowiedzą się, gdy zwiadowcy odkryją, że wybiłaś cały elitarny oddział.
To ta karta dostępu.
Zablokowali dostęp do autostrady.
Musisz przywrócić zasilanie drzwi.
Szukaj trzech przełączników połączonych przewodami.
Najpewniej znajdują się za drzwiami tych magazynów.
Dobra robota. Ale to jeszcze nie koniec.
Musisz wrócić do parkingu.
Ulicami już nie przejdziesz.
Musisz obrać tę samą drogę co sprawca tego dzieła.
Natychmiast zejdź z ulicy.
Ten parking wielopoziomowy to nasza jedyna szansa.
Przejdziesz nim po dachach do starszej części miasta.
Nie mogę obejść tego zamka, ale namierzyłem kartę dostępu.
Zgubił ją oddział, który napotkał…
…opór.
Obecnie znajduje się w mieszkaniu kilka przecznic od ciebie.
Na drodze do niego rozstawiono posiłki wroga.
Zlikwiduj ich.
Winda prowadząca do głównej oczyszczalni znajduje się tuż pod tobą.
Nie przestajesz mnie zadziwiać.
Muszą już jednak wiedzieć, że tylko jedna osoba mogła spowodować wszystkie te…
…straty.
Wykrywam kilka oddziałów przerzucanych… drogą powietrzną.
Jedyna droga do celu prowadzi prosto przed siebie…
…ale z ich łączności wynika, że zamierzają wysłać jeszcze cztery oddziały…
…w najbliższą okolicę.
Przebij się za wszelką cenę.
Te mieszkania zostały już przetrząśnięte.
Patrole wroga są przeważnie słabo uzbrojone.
Wykrywam jednak jednostki Ghost.
Najwyraźniej sięgają po mocniejszy arsenał.
Tak czy inaczej, nasz cel pozostaje ten sam.
Ucieczka.
Musisz przywrócić zasilanie tej windy.
W pobliżu jest przełącznik, który powinien otworzyć ci dostęp do generatora.
Najlepsza droga ucieczki z miasta prowadzi przez zakłady uzdatniania wody pod ulicami.
Jest tylko jedno wejście.
Piwnica niedokończonego budynku w tym sektorze.
Masz się tam dostać za wszelką cenę.
Dotrzyj do centralnego węzła uzdatniania.
Tunel odpływowy zaprowadzi cię do jednej z niewielu martwych stref w SPRAWL.
Stamtąd będę mógł niepostrzeżenie przejąć transport.
Dobrze. Wracaj pod ziemię. Drzwi powinny się teraz odblokować.
Dekapitacja? Nie to miałem na myśli…
Wróć do centralnego węzła uzdatniania.
Wstępne skany oczyszczalni wykazują tylko lekkie patrole.
To dobry znak.
Wciąż mamy szansę doprowadzić cię do Iglicy.
Cóż, to też sposób na zdobycie ich optyki.
Miejmy nadzieję, że to zadziała…
Centralny węzeł uzdatniania jest zablokowany.
Namierzyłem dwóch dowódców oddziałów proszących o natychmiastową ewakuację.
Protokoły ich wszczepów odpowiadają protokołom tych zamków.
Musisz ich znaleźć.
Potrzebujemy ich optyki, by otworzyć te drzwi.
Niedobrze…
Celuj w granaty! Są podatni na materiały wybuchowe!
Ciężki mech klasy O.H.G.R.
W ich sieci bojowej nie ma informacji o jego rozmieszczeniu.
Wiedzą już, że to ty, i wysyłają ciężki sprzęt.
Przynajmniej masz pamiątkę.
Wsiądź na tę łódź. Zawiozę cię tak blisko następnego pomostu, jak się da.
<Krzyk bólu>
Zawsze byłem lepszym żołnierzem. Ty byłaś tylko ich nową zabawką.
Zginiesz tutaj, Seven. Wreszcie z tobą skończę.
Nie, nie, nie, nie!
Nie skończę z tobą szybko! Będziesz cierpieć.
Ty suko! To nie może się dziać! <Krzyk bólu>
Myślisz, że przede mną uciekniesz, Seven?! <Obłąkańczy śmiech>
Nigdy nie byłaś jedną z nas. Jesteś tylko mięsem.'''.splitlines()
assert len(text)==145,len(text)
save('Dialogue_Subs','\n'.join(r['key']+'\t'+t for r,t in zip(rows[:145],text)))
for i,r in enumerate(rows[145:],145):print(str(i)+'\t'+r['key']+'\t'+r['english'])
