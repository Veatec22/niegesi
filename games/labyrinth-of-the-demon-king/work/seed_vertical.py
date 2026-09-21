"""One-time editorial seed by review row; production builds use stable game keys."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
review=json.loads((root/'translations/en-pl-review.json').read_text(encoding='utf-8'))
rows={
0:'"Nienawidzę tego miejsca. Skończyło się jedzenie. Do picia też niewiele zostało. Skóra ciągle mnie swędzi. Nikt nie przyjdzie nas uratować. Dłużej tego nie zniosę. Spróbuję stąd odejść.\r\n\r\nNawet nie wiem, gdzie teraz jesteśmy, ale gdzieś tam musi być coś lepszego niż tutaj" ',
1:'"Dotarłem do budynku bramnego, ale ktoś zabił wyjście deskami. Próbowałem je oderwać, lecz nie mam już siły. Nie potrafię nawet wyciągnąć katany ze ściany. Coś porusza się na górze. Muszę być cicho. Taki głód. Słabość. Ledwo się ruszam. Nie wiem, co robić...\r\n\r\nJeśli to czytasz, dla mnie nie ma już nadziei. Dla ciebie też. Poddaj się. Nie warto walczyć."  ',
2:'"Jeśli ktoś zatruje zamkowe jedzenie, wina spadnie na niego. \r\n\r\nMuszę tylko zdobyć klucz do spiżarni. Wtedy dostanie za swoje..."',
3:'"Tamonten stoi na północy w czarnej zbroi, trzymając pagodę pełną bogactw dla godnych.\r\n\r\nKōmokuten czeka na zachodzie. Odziany w białe szaty włada nagami, pradawnymi istotami o wężowych ciałach.\r\n\r\nNa południu stoi Zōchōten, a jego czerwona aura płonie jasnym blaskiem. Pomnaża mądrość i umiar księżniczki, a włócznią przeszywa serca złoczyńców.\r\n\r\nNa wschodzie zaś jest Jikokuten. Gra na niebieskiej biwie, by zabawiać księżniczkę, a jego trójząb czeka w pogotowiu."',
4:'"Ten drań kucharz znów próbuje zabrać mi pokój. \r\n\r\nUważa, że powinien należeć do niego, bo leży tuż przy kuchni. Twierdzi, że to niesprawiedliwe, że musi spać na drugim piętrze.\r\n\r\nAle to mój pokój. Mój. Nikomu nie pozwolę go sobie odebrać."',
5:'"Ten dziwny grzyb rośnie już dalej w korytarzu.\r\n\r\nCokolwiek robimy, nie potrafimy się go pozbyć.\r\n\r\nRozrasta się błyskawicznie. Znajdujemy go wszędzie. Przysięgam, że widzę, jak się porusza. Wciąż wydaje ten dziwny dźwięk. Przeraża mnie."',
6:'"Czterej Niebiańscy Królowie chronią księżniczkę przed dalszą krzywdą. Dopóki pozostaje bezpieczna, filar tej wieży nie runie, a zamek będzie trwał wiecznie."',
7:'"Próbowaliśmy wody, ognia, alkoholu. Nawet rąbaliśmy to siekierą, lecz niemal nic mu nie szkodzi.\r\n\r\nSłyszałem pogłoski, że od soli grzyb usycha i ginie. Ale nie mamy soli. Nie możemy dostać się do spiżarni. Klucz zaginął. Jesteśmy za słabi, żeby wyważyć drzwi."',
8:'(+ kierunek) Unik',9:'(PRZYTRZYMAJ) Silny atak',10:'(PRZYTRZYMAJ) Sprint',11:'(PRZEŁĄCZ) Sprint',
16:'Klucz do drugiego piętra',24:'Gorzki grzyb. Po zjedzeniu odnawia wytrzymałość.',28:'Butelka sake. Uśmierza ból.',
30:'Zwykły napierśnik ashigaru wyższej rangi. Wybito na nim godło klanu Takeda.',
36:'Świeża miska ramenu kappy. Bardzo pożywna.',37:'Tykwa z herbatą z żeń-szenia. Orzeźwiający napój, który leczy ciało.',38:'Tykwa z matchą. Mogę ją napełnić w herbaciarni.',
41:'Silny atak przebija gardę wroga. Niektóre bronie pozwalają też po nim rozpocząć kolejną serię ciosów.\r\n\r\nKopnięcie przebija gardę i odrzuca przeciwnika. ',
52:'Klucz do zbrojowni w pierwszej wieży.',55:'Klucz.',76:'Sakiewka suszonych, zmielonych grzybów. Po spożyciu w pełni odnawiają wytrzymałość.',89:'Worek pełen soli.',
106:'OSIĄGNIĘCIA',107:'NA PEWNO CHCESZ TO ZROBIĆ?',108:'PANCERZ',109:'PROPORCJE OBRAZU',110:'ATAK',111:'EFEKTY ATAKÓW',112:'Odblokowano osiągnięcie: {Name}',
137:'Antidotum',144:'Pancerz',145:'Klucz do zbrojowni',146:'Strzała',148:'Strzały',153:'Dźwięk',154:'DO TYŁU',155:'DZWON',159:'BEZ RAMEK',161:'KUP',
178:'Zabite deskami.',179:'Zabite deskami.',180:'Zabite deskami.',181:'Zabite deskami. ',182:'Zabite deskami. ',185:'Zabite deskami. Nie otworzę.',186:'Zabite deskami. Nie otworzę.',
188:'Butelka sake',189:'Pudełko kul (x5)',190:'Złamana katana',192:'Posążek Buddy',194:'Kula (x1)',
198:'Ale ty... nie jesteś samurajem. \r\n\r\nPrzybywasz tu, by pomścić swojego pana… \r\n\r\nCzym mógł zasłużyć na taką wierność? ',
203:'WYBIERZ MIEJSCE ZAPISU',204:'WYBIERZ ZAPIS DO WCZYTANIA',205:'PRZERYWNIKI FILMOWE',206:'WSPINAJ SIĘ',207:'ZAMKNIJ',208:'WALKA',209:'POŁĄCZ',210:'SERIE CIOSÓW',211:'STEROWANIE',212:'ZWŁOKI',213:'TWÓRCY',214:'KUCNIJ',
230:'Wybierz język',238:'Zamknij',242:'Kompas',243:'Kompas',244:'Ukończ samouczek',254:'Kucnij',256:'Usuwa wszelkie dolegliwości.',
259:'DIALOGI',260:'CZY CHCESZ WYJŚĆ?',261:'UNIK',262:'DRZWI',267:'Strzęp dziennika',268:'Brudne bandaże',269:'Nic nie rób',270:'Nic nie rób',271:'Unik',
277:'EFEKTY',278:'WEJDŹ',279:'WYPOSAŻ',280:'WYCIĄGNIJ KOMPAS',281:'POCHODNIA/KOMPAS (PRZYTRZYMAJ)',282:'WYJŚCIE',283:'WYJŚCIE',284:'WYJŚCIE',293:'Wyjdź',294:'Wyjdź',295:'Wyjdź',297:'DO PRZODU',299:'LIMIT KLATEK',300:'PEŁNY EKRAN',301:'GRZYB',
309:'Nie sparujesz takich ruchów jak pchnięcia i kopnięcia. \r\n\r\nMusisz zejść im z drogi, zanim cię dosięgną.',
324:'Budynek bramny',325:'Ogólne',327:'Herbata z żeń-szenia',334:'Żegnaj',340:'Witaj, przyjacielu.',342:'WISIELEC',343:'OTWÓR',344:'JAK GRAĆ',354:'Toporek',363:'Zdrowie',376:'Witaj, wędrowcze.',377:'Witaj...',
401:'Hm? Wykonaj silny atak ORAZ kopnięcie, żeby przejść dalej.',414:'Nie mogę tamtędy iść',416:'Jeszcze nie mogę tego podnieść.',417:'Z tej strony nie dam rady tego popchnąć.',424:'Czuję się wypoczęty.',434:'Trzeba wspiąć się po tej linie.',435:'Trzeba wspiąć się po tej linie.',448:'Nie zabłądziłem. Przybyłem pomścić mojego pana.',
457:'IKONY',458:'ULEPSZ',459:'STEROWANIE',460:'INTENSYWNE ZIARNO FILMOWE',461:'INTERAKCJA',462:'EKWIPUNEK',463:'EKWIPUNEK',464:'ODWRÓĆ OŚ X',465:'ODWRÓĆ OŚ Y',466:'PRZEDMIOTY',
470:'W takim przypadku musisz przebić jego gardę silnym atakiem albo kopnięciem.',472:'Kadzidło: ',475:'Sterowanie',476:'Czynność',477:'Czynność',478:'Interakcja',489:'W środku jest pusto.',
507:'SKOK',510:'Skok',515:'Jeśli tylko trzymasz broń przed twarzą i czekasz, aż cię uderzy, skończysz z ostrzem w brzuchu...\r\n\r\nMusisz sparować we właściwej chwili.',517:'KOPNIĘCIE',521:'Kopnięcie',526:'ODEJDŹ',527:'W LEWO',528:'WCZYTAJ',529:'WCZYTAJ GRĘ',530:'CZUŁOŚĆ ROZGLĄDANIA',532:'Język',533:'Latarnia',534:'Ostatnie miejsce zapisu:',535:'Ostatni zapis w slocie:',537:'Odejdź',539:'Lekki atak',
540:'Lekkie ataki — podstawowe ciosy. Przeciwnik może je zablokować.\r\n\r\nSilne ataki — wymagają przygotowania, ale zadają większe obrażenia i przebijają gardę przeciwnika.\r\n\r\nParowanie — wymaga wyczucia chwili, lecz na moment ogłusza przeciwnika i pozwala szybko odpowiedzieć ciosem. \r\n\r\nPchnięcia/kopnięcia — zarówno twoje, jak i wroga, przebijają gardę przeciwnika i odrzucają go.',
543:'MAPA',544:'MAPA',545:'GŁÓWNA GŁOŚNOŚĆ',548:'MUZYKA',552:'Mapa',576:'Grzyb',577:'Sakiewka grzybów',588:'NOWA GRA',589:'DALEJ',590:'NIE',591:'BRAK MAPY TEGO OBSZARU',592:'BRAK',597:'NOTATKI',605:'Nie',606:'Nie',609:'Nie.',615:'Brak',616:'Brak',
625:'Nasz przyjaciel znów spróbuje cię uderzyć, tym razem atakami, których nie da się sparować. Uniknij jego ciosów 3 razy. ',
630:'OTWÓRZ',631:'OPCJE',641:'Och... Kolejny... \r\n\r\nPrzybywasz po Króla Demonów?',659:'Otwórz ekwipunek',660:'Otwórz ekwipunek',664:'Otwórz mapę',665:'Otwórz ekwipunek, aby wyposażyć talizmany',669:'Inne',672:'OBRAZ',673:'PAROWANIE',674:'PAUZA',675:'PAUZA',676:'PODNIEŚ',677:'PODNIEŚ',681:'UMIEŚĆ PRZEDMIOT',682:'UMIEŚĆ PRZEDMIOT',683:'PREFERUJ POCHODNIĘ',684:'NACIŚNIJ PRZYCISK DO PRZYPISANIA',687:'POPCHNIJ',690:'Klucz do spiżarni',691:'Parowanie',693:'Pauza',700:'Pomódl się',
703:'SZYBKIE LECZENIE',704:'SZYBKA WYTRZYMAŁOŚĆ',705:'WYJDŹ',706:'WYJDŹ DO PULPITU',707:'WYJDŹ DO MENU GŁÓWNEGO',708:'Szybkie użycie (leczenie)',709:'Szybkie użycie (leczenie)',710:'Szybkie użycie (wytrzymałość)',711:'Szybkie użycie (wytrzymałość)',712:'Szybko wyciągnij pochodnię',713:'CZYTAJ',714:'WCZYTAJ PO ŚMIERCI',715:'USUŃ',716:'USUŃ',718:'PRZYWRÓĆ UKŁAD',719:'ROZDZIELCZOŚĆ',720:'WZNÓW',721:'WRÓĆ DO MENU',722:'W PRAWO',
729:'Pamiętaj, że możesz sparować większość ataków, ale nie kopnięcia i pchnięcia. Te przebiją twoją gardę.\r\n\r\nCo prowadzi nas do następnej lekcji...',739:'Odnawia wytrzymałość',748:'Zardzewiała katana',749:'SÓL',750:'ZAPISZ',751:'ZAPISZ I WYJDŹ',755:'POKAŻ CELOWNIK',756:'POKAŻ INTERFEJS',757:'KAPLICZKA',763:'EFEKTY DŹWIĘKOWE',764:'SPRINT (PRZYTRZYMAJ)',765:'SPRINT (PRZEŁĄCZ)',766:'ROZPOCZNIJ',767:'SCHOWEK',768:'POSĄG',769:'POSĄG',770:'PIEŃ',771:'Worek soli',776:'Wybierz język:',777:'Wybrany slot:',781:'Pomiń samouczek',786:'No dobrze. Spróbuj sparować jego cios 3 razy.',
808:'Czasem wróg trzyma gardę albo próbuje sparować twój atak. \r\nJeśli uderzysz zwykłym ciosem, wpadniesz w jego pułapkę.',815:'Wytrzymałość',816:'Rozpocząć nową grę?',818:'Jałowe bandaże',821:'Dziwna notatka',825:'TALIZMAN',826:'ROZMAWIAJ',827:'DOTKNIJ',828:'SALA TRENINGOWA',829:'PRZENIEŚ',830:'TUNEL',831:'TUNEL',832:'OBRÓĆ KOŁO',833:'OBRÓĆ KOŁO',834:'TYP',838:'Talizman',839:'Talizmany',846:'Dziękuję',853:'Drzwi są zamknięte na klucz.',
869:'Pierwszy unik nie zużywa wytrzymałości, ale kolejne wykonane zaraz po nim już tak. Korzystaj z nich rozważnie.',903:'Ta skrzynia jest zamknięta na klucz',904:'Teraz można otworzyć te drzwi',905:'Te drzwi są zamknięte na klucz.',906:'Te drzwi są zamknięte na klucz.',
920:'To ważne. Jeśli tego nie opanujesz, na pewno skończysz w ramenie.\r\n\r\nSparuj jego ciosy trzy razy i możemy iść dalej.',932:'To najważniejsza rzecz, jaką dziś omówimy... Parowanie.\r\n\r\nNasz przyjaciel spróbuje cię uderzyć, a ty musisz sparować jego cios.',939:'Pochodnia',940:'Pochodnia\r\nKompas (PRZYTRZYMAJ)',965:'Odszukaj Króla Demonów i pozbaw go życia.',969:'Ech... Po prostu uniknij jego ataku 3 razy...',971:'INTERFEJS',972:'ZDEJMIJ',973:'UŻYJ',974:'UŻYJ',984:'SYNCHRONIZACJA PIONOWA',988:'Obraz',989:'BROŃ',994:'TRYB WYŚWIETLANIA',995:'W OKNIE',
996:'Poczekaj, aż wróg zacznie wyprowadzać cios, a potem unieś broń i go sparuj.',1007:'Broń',1016:'Cóż... Przebywa tutaj. \r\n\r\nAle nie jesteś pierwszym, który tu przybył...\r\n \r\nWiele dusz zapuszcza się w te strony, pragnąc pomsty za swoich panów, ukochanych lub po prostu za swój honor...',1038:'Kim jesteś?',1043:'Zabierzesz to?',1044:'Zabierzesz to?',1045:'Zabierzesz to?',1046:'Zabierzesz to?',1047:'Zabierzesz je?',1060:'TAK',1070:'Tak',1071:'Tak',1072:'Tak',1080:'Zdobyto mapę: {name}',1089:'Usuwasz zasuwę.',1093:'Jak widzisz, nasz przyjaciel już trzyma gardę. Uderz go silnym atakiem i kopnij.',1096:'Otwierasz drzwi kluczem.',1097:'Otwierasz drzwi kluczem.',1102:'Standardowe nakrycie głowy ashigaru. Wybito na nim godło klanu Takeda.',1110:'[KONIEC]',1114:'[Zachowaj milczenie]',
}
for i in range(490,506):rows[i]='Zamknięte na klucz.'
for i in range(799,806):rows[i]='Coś blokuje te drzwi.'
for i in range(600,604):rows[i]='Zabite gwoździami.'
polish={review[i]['key']:value for i,value in rows.items()}
for item in review:
    item['polish']=polish.get(item['key'],'')
    item['status']='vertical' if item['key'] in polish else 'untranslated'
(root/'translations/pl.json').write_text(json.dumps(polish,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'translations/en-pl-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(polish))
