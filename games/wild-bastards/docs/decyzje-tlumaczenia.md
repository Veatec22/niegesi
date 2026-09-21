# Wild Bastards — decyzje tłumaczenia (0.2.0)

Fakty i źródła: `translations/biblia.yaml`. Raport kontrolny: `work/l10n-report.md`.

## Postacie

- **Płeć banitów ustalona z tekstu i tabel francuskiej i włoskiej** (rosyjska jest pusta).
  Kobiety: Pajęcza Rosa, Fletch („archère”), Kaznodzieja/Esther („sacerdotessa”),
  Francisco („Chaste's daughter”), Młoda (trzeci bękart), wycięte z gry Cuffs i Legs.
  Mężczyźni: Billy, Casino, Kaboom, Roswell, Spike, Sędzia, Sierżant, Hopalong,
  Smoky, Rawhide, McNeil, Barrabas, Chaste.
- **„Psze pani” / „panienko” w dialogach to Fletch** — prowadzi bandę, bo pamięta
  przyszłość (francuskie „ange-gardienne”). Stąd np. „Posłałabym też Sędziego”.
- **Przydomki z treścią przetłumaczone, imiona nie.** The Judge → Sędzia, Sarge →
  Sierżant, Preach → Kaznodzieja, Spider Rosa → Pajęcza Rosa (tak jak w verticalu).
  Billy, Casino, Kaboom, Roswell, Spike, Hopalong, Smoky, Rawhide, Fletch zostają.
  „Kaznodzieja” ma żeńską składnię („Kaznodzieja dała”).
- **Rawhide mówi „my” i dziecinnie**: angielskie „The Billy”, „Many Helps”, „Scrubly”
  → „Ten Billy”, „Wielu Pomocy”, „Cieniasny”. To robot z rojem wiewiórek w środku.
- **Smoky wrzeszczy WERSALIKAMI**, gdy ktoś krytykuje jego fasolę — zachowane.
- **Gwara westernowa** oddana potocznym, lekko wiejskim polskim („ano”, „psiakrew”,
  „żeście”, „niech mnie”), bez fonetycznego przekręcania słów. Spike mówi „stary”
  (cockneyowe „mate”), Roswell i Rosa mówią poprawnie i wyniośle, Sędzia wtrąca
  prawniczy język („Przychylam się”, „Orzekam remis”).
- **Wulgaryzmy tej samej siły**: fuck → kurwa/pieprzyć/wyruchać, shit → gówno,
  sumbitch → sukinsyn, goddamn → cholerny.
- **Kwestie z nieznanym adresatem** („…Pals”, „…JailPals”: dzięki za znalezienie)
  są bezrodzajowe, bo ratującym może być każdy banita.
- **Nazwy talentów (asów) i cech ogólnych to rzeczowniki** („Zabójczość”, „Szybkie ręce”,
  „Krzepa”), bo przymiotnik zdradzałby płeć banity.

## Terminy i gry słów

| EN | PL | Dlaczego |
| --- | --- | --- |
| Wild Bastards (banda) | Dzikie Bękarty | „bastards” to też nieślubne dzieci Chaste'a, o których jest fabuła; tytuł gry zostaje |
| Chastener | Karzyciel | Chaste + chasten (karcić) |
| Homestead | Ostoja | raj dla wyrzutków, do którego leci Drifter |
| Drifter, Lucky Lady | bez zmian | nazwy statków |
| mod | przedmiot | „mod” po polsku to modyfikacja gry |
| bunch / gang | grupa / banda | grupa to oddział na mapie planety |
| roadblock / posse / pack | blokada / obława / sfora | |
| Prince | książę | dzieci Chaste'a: McNeil, Francisco, Barrabas |
| Hole in the Wall | Dziura w Murze | kryjówka bandy Butcha Cassidy'ego |
| snuff (Kram) / cramm | tabaka / cramm | cramm to waluta, bez tłumaczenia |
| infamy | niesława | |
| Gunhand | rewolwerowiec | |
| Yellowbelly | cykor | yellowbelly = tchórz, wróg za tarczą |
| Cranker | korbiarz | gatling na korbę |
| Bushwhacker | czatownik | czatuje w krzakach |
| Mortician | grabarz | przywołuje duchy |
| Ironclad | żelaźniak | |
| Blaster (grenadier) | wysadzacz | |
| Stinger | żądłak | |
| Gunbarrel / gunbucket | lufa | z verticalu; opis „Wygląda jak beczka” |
| Jackbox | skrzynka-pułapka | z verticalu (jack-in-the-box) |
| Kyote | kojot | |
| Earsplitter | uszorwacz | |
| Pepperbox | pieprzniczka | polska nazwa tej broni |
| Cruxmas | Gwiazdka Cruxa | Jorge Crux to tutejszy Jezus |
| Stitch | Szew | dziura w przestrzeni |

## Okazje wykorzystane

- „Bought the farm” (Hopalong chciał kupić farmę i zginął): „dostałeś kawałek ziemi,
  tylko nie taki, jak chciałeś”, „poszedł wąchać kwiatki od spodu”.
- Mały Jeb cenzuruje przekleństwa i niewinne słowa: „żałosne worki ch-słów”,
  „możecie ż-słowo do woli” (e-word = eat).
- „Manwidth” Casino (manpower + bandwidth): „przepustowości na chłopa”.
- Zarzuty listów gończych: Cephaloculpa → „Głowobójstwo”, Paletticide →
  „Podniebienniobójstwo”, Jaywalking → „Łażenie po jezdni”.
- Sarge „What's the charge?” → „Jaki zarzut?”, Sędzia „Sustained” → „Przychylam się”.

## Świadome odstępstwa od oryginału

- Opisy z liczbami przebudowane na „Nazwa: <d>”, żeby nie odmieniać liczebników
  („Nietykalność po zabójstwie, sekundy: <d>”).
- „Send: {0} for {1} jumps” → „Wyślij: {0}. Liczba skoków: {1}.” — imiona
  w placeholderach zostają w mianowniku.
- Kilka nazw skrócono pod UI (np. „Czapka z folii”, „Bomba migdałowata”, „Handlarz”).
- Dni tygodnia skrócone („pon.”), am/pm → „rano” / „po poł.”.

## Mniej pewne (sprawdź w grze)

- **Mówiący w dialogach** — klucze go nie podają. Najwięcej ryzyka: sceny
  wprowadzające (FletchIntro, SpikeIntro, RoswellIntro, PreachIntro), gdzie rozmawia
  kilka osób. Jeśli ktoś mówi o sobie w złym rodzaju, wystarczy nazwa sceny.
- **Ekran banity**: długie nazwy asów i opisy przedmiotów („Sojuszniczy zaprawiony
  rewolwerowiec”, „Ponowne losowanie znalezionych przedmiotów: <d>”).
- **Mapa sektora (zdarzenia SME)**: opisy z kilkoma liczbami i przyciski wyboru.
- **Status banity**: „Rany”, „Zmęczenie”, „Naładowanie”, „Rozproszenie” — rzeczowniki
  zamiast przymiotników; sprawdzić, czy czytają się naturalnie na karcie.
- **Karty z czasem**: „rano” / „po poł.” zamiast am/pm i skróty dni.

## Raport kontrolny

Stan `work/l10n-report.md`: brak tłumaczeń 0, tokeny 0, terminy 0 (wyjątki opisane
w biblii). Zostaje: 93 zgłoszenia spójności (ten sam angielski w różnych miejscach,
np. „Tough” jako cecha wroga i jako nazwa asa — celowo różnie), 6 „resztek”
angielskich (nazwy własne: Grizzly, Casino, Legs, Las Calaveras .45, Calavera Uno/Dos),
10 liczebników przy placeholderach (liczba zawsze po dwukropku), 50 długości
(nazwy przedmiotów i asów — do obejrzenia w grze), 10 wielkich liter (nazwy własne)
i 9 typografii (proste cudzysłowy w `<sprite name="…">`).
