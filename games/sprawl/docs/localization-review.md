# SPRAWL — niezależny przegląd lokalizacji

## Zakres

- Data: 2026-09-26. Reviewer: osobny subagent w świeżym kontekście, tylko do odczytu,
  według `.claude/skills/localization-review/SKILL.md`. Poprawki naniósł agent prowadzący.
- Wejście przeglądu (SHA-256): `translations/en-pl-review.json`
  `a6a01c480a3d28898f7cbdd68f8ea258c1a76a87b4bf247f87a70ce51d932085`,
  `translations/bible.yaml` `f0837cf5…a350`, `docs/translation-decisions.md` `e6446108…a1a6b`.
- Po poprawkach: `en-pl-review.json` `649ef2fedc47960ee66347f31c229c5fa381d615ef245561f3e8903ee8a548bb`.
- Przeczytano **717/717** wpisów, całe teksty (także kodeks i transmisje Matki), partiami po
  namespace'ach i scenach kluczy: Dialogue_Subs 318, UIStringTable 243, CODEX 47,
  World_String_Table 27, nazwy języków 24, EnemyNames 23, Tutorials 17,
  Dialogue_Update_Subs 11, WeaponNames 7. Luk w pokryciu brak.
- Biblia i `docs/translation-decisions.md` powstały tuż przed przeglądem (SPRAWL nie miał
  etapu kierunku przed verticalem); decyzje w nich są odtworzone, nie zatwierdzone przez użytkownika.
- Raport `work/l10n-report.md` użyty jako wskazówka. Jego „proste cudzysłowy” przy `<img id="…"/>`,
  angielskie resztki (DLSS, nazwy broni, SEVERED STEEL) i wiodące spacje z EN to fałszywe alarmy.
- Przegląd językowy nie zastępuje testu w grze. Pełna kampania nadal nieprzetestowana.

## Błędy

Numery 1.x odpowiadają pozycjom reviewera, do których odwołują się sekcje 2–5.

| Nr | Klucz | EN | Było | Jest | Przesłanka | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1.1 | UIStringTable/YOU_DIED_PROMPT | You Died! | Zginąłeś! | Nie żyjesz! | Jedyna męska forma do gracza; SEVEN jest kobietą. Forma bezrodzajowa, bo w symulacjach PK/HRD („Trainees…”) gracz może nie być SEVEN. „Zginęłaś!” — do rozmowy | wprowadzone |
| 1.2 | UIStringTable/LEVEL_E1M1_NAME | 1: The Walled City | 1: Miasto za murem | 1: Miasto za Murem | Termin z biblii, wszystkie inne wystąpienia wielką literą | wprowadzone |
| 1.3 | Dialogue_Subs/E1M5_FATHER_OGRE_ENCOUNTER_B | …They're weak to explosives! | Są podatni… | Są podatne… | Mowa o mechach O.H.G.R — forma niemęskoosobowa | wprowadzone |
| 1.4 | Dialogue_Subs/E3M1_FATHER_AFTER_MINIBOSS_A | They're stopping at nothing now | Teraz już nic ich nie powstrzyma. | Teraz nie cofną się przed niczym. | „stop at nothing” = nie cofać się przed niczym; stary sens przeczył kwestii B | wprowadzone |
| 1.5 | CODEX/E1M1.OPERATIONORDERS | …FROM SECTORS 23-C TO 55-H, HIGH PRIORITY… / WILL INITIATE FAIL SAFES AND DISABLE. | …DO 55-H WYZNACZONO… / URUCHOMI ZABEZPIECZENIA I JE WYŁĄCZY. | …DO 55-H. WYZNACZONO… / URUCHOMI ZABEZPIECZENIA AWARYJNE I UNIESZKODLIWI CEL. | Zakres sektorów przeskakiwał do następnego zdania; „je” wskazywało na zabezpieczenia. Reviewer proponował „wyłączy jego wszczepy”; wybrano neutralne „unieszkodliwi cel”, bez dopowiadania | wprowadzone |
| 1.6 | CODEX/e1m4.operationorders | …TO 5425-HSF, HIGH PRIORITY… | …DO 5425-HSF WYZNACZONO… | …DO 5425-HSF. WYZNACZONO… | Jak wyżej | wprowadzone |
| 1.7 | CODEX/e2m2.transit | WHY NOT JUST SHUT DOWN OUR SYSTEMS OUTRIGHT? | DLACZEGO PO PROSTU NIE WYŁĄCZYĆ WSZYSTKICH NASZYCH SYSTEMÓW? | DLACZEGO PO PROSTU NIE WYŁĄCZYLI OD RAZU NASZYCH SYSTEMÓW? | Bezosobowe pytanie czytało się jak propozycja junty; chodzi o intruza | wprowadzone |
| 1.8 | UIStringTable/E1M1_FLAVOUR | an urban megapolis choked in ash | megapolis duszące się | megapolis dusząca się | „megapolis” jest rodzaju żeńskiego (tak też w e1m4.mauricepadilla-fong02) | wprowadzone |
| 1.9 | Tutorials/E1M1_WALLRUNNING_01_BODY | succeed in the Sprawl | Aby przetrwać w Sprawl, | Aby przetrwać w SPRAWL, | Jedyny wyłom w pisowni SPRAWL | wprowadzone |
| 1.10 | UIStringTable/PU_KEYCARD_HEAD | Capitan Head Acquired | Zdobyto głowę kapitana | Zdobyto głowę dowódcy | Ojciec mówi o „dowódcach oddziałów”; stopnia kapitana gra nie używa | wprowadzone |
| 1.11 | Dialogue_Subs/E3M2_POLITICIAN_MONOLOGUE_G | The rest of us … escaped beyond the walls of the net. | …Uciekli za mury sieci. | …Uciekła za mury sieci. | Podmiotem jest „reszta z nas” | wprowadzone |
| 1.12 | UIStringTable/PK3, PK4, PK6, PK7, PK8_NAME | … (ADVANCED) | (ZAAWANSOWANE) / (ZAAWANSOWANY) | (DLA ZAAWANSOWANYCH) | Ta sama etykieta w dwóch formach, nieuzgodnionych z „SAMOTNOŚĆ”, „PROCA”. Długość do sprawdzenia w grze | wprowadzone |
| 1.13 | CODEX/e1m4.mother04 | …fiunlost found… / …he would push annot held… | wystarzagubiona odnaleziona / a nieniezatrzymana | wystarniezagubiona odnaleziona / a niezatrzymana | „unlost” = niezagubiona (refren z mother03); nadmiarowe „nie” po złożeniu dawało „a nie ja trwałam”, czyli odwrócenie EN. Zakłócenie zachowane | wprowadzone |
| 1.14 | Dialogue_Subs/E1M1_FATHER_INTRODUCING_C–R, E1M1_FATHER_INTRO_C | ... | ... | … | Pozostałe dialogi Ojca łączą napisy znakiem „…”; glif widoczny już w grze („Niedobrze…”) | wprowadzone |
| 2.6 | Dialogue_Subs/E2M1_FATHER_HOMECOMMING_A | the weapons testing arena | arena testów uzbrojenia | arena testów broni | Ten sam termin EN co REARM_YOURSELF_B („arenę testów broni”) | wprowadzone |

Biblia uzupełniona o: „dowódca oddziału”, „arena testów broni”, pisownię SPRAWL oraz przyjęty
rodzaj męski hakerów. Rozszerzono też formy terminów, żeby raport nie zgłaszał „w Mieście za Murem” i „w juncie”.

## 2. Do rozmowy

Każdy ma konkretną przesłankę. Są pogrupowane i ułożone od najważniejszych.

### 2.1 Tytuł `UIStringTable/LEVEL_E1M4_NAME` „Ghost Wetware” (decyzja 6, nowa przesłanka)
- EN: `4: Ghost Wetware`; PL: `4: Biologiczne widmo`
- Nowa przesłanka z całej gry: na poziomie E1M4 po raz pierwszy pojawiają się jednostki Ghost
  (`E1M4_FATHER_INTRO_C`: „Wykrywam jednak jednostki Ghost.”, `EnemyNames/NINJA`: „Covert Unit Ghost”).
  Ghost zostaje w PL jako nazwa klasy, ale tytuł zmienia go w „widmo”, więc powiązanie z poziomem przepada.
- Opcje: (A) zostawić „Biologiczne widmo” (brzmi dobrze, ale traci nawiązanie); (B) `4: Ghost Wetware`, czyli nazwa własna
  jak „SEVERED STEEL” i „Deus Ex Machines”; (C) `4: Wetware klasy Ghost`.
- Rekomendacja: B albo C. Decyduje użytkownik.

### 2.2 SEVEN jako „ona” w czacie hakerów, `CODEX/e1m5.chatlogcasemrph`
- EN: `there's a reaper on the loose, and its not theirs` / `she's not ours either`
- PL: `żniwiarz jest na wolności. i nie należy do nich` / `do nas też nie należy`
- Problem: EN zdradza płeć żniwiarza, co wskazuje na SEVEN. W PL ta wskazówka znika.
- Propozycja: zamień `<amber>[case]</>: do nas też nie należy` → `<amber>[case]</>: ona do nas też nie należy`
  (zestawienie „żniwiarz… ona” jest celowo zgrzytliwe i działa jak odkrycie).

### 2.3 Głos Ojca: kalki i drobne przesunięcia sensu
- `E1M1_FATHER_INTRODUCING_Q/R`: EN `And in return, I will be set...` / `Free.`; PL `A w zamian ja odzyskam...` / `...wolność.`
  „Odzyskam” zakłada, że Ojciec był kiedyś wolny, a przecież został stworzony jako narzędzie (C/D).
  Propozycja: `A w zamian ja wreszcie będę…` / `…wolny.` (z poprawką typograficzną z 1.14).
  Zysk: zgodność z ASSISTED_SUICIDE_A i FATHER_DEATH_A („Uwolnienie…”).
- `E1M1_FATHER_HALLMARK_D`: EN `You are truly a hallmark of your kind.`; PL `Jesteś doprawdy wzorem dla podobnych tobie.`
  „Wzór dla podobnych” znaczy „przykład do naśladowania”, a EN mówi „modelowy egzemplarz”. Chłodniejsze i bliższe
  ironii Ojca (SEVEN jako narzędzie): `Jesteś doprawdy wzorcowym egzemplarzem swojego rodzaju.`
- `E2M3_FATHER_END_LEVEL_B`: EN `Sometimes you need to take a leap of faith, Seven.`; PL `Czasem trzeba skoczyć na wiarę, Seven.`
  „Skoczyć na wiarę” to nie jest polski frazeologizm, za to „skok wiary” jest utrwalony. Propozycja: `Czasem trzeba wykonać skok wiary, Seven.`
- `E2M1_FATHER_TROPHY_B`: EN `Let's hope you don't find them.`; PL `Miejmy nadzieję, że nie spotkasz znalazcy.`
  „Znalazcy” brzmi urzędowo i komicznie. Propozycja: `Miejmy nadzieję, że nie natkniesz się na tego kogoś.`
- `E2M3_FATHER_TRAIN_MOVING_D`: EN `I'd prime your chaingun.`; PL `Przygotowałbym minigun.`
  Bez „twój” lub „na twoim miejscu” zdanie brzmi, jakby Ojciec sam szykował broń. Propozycja: `Na twoim miejscu przygotowałbym minigun.`
  Termin „minigun” zgadza się z UI (CONTROL_EQ_MINIGUN, PU_MINI) i tak ma zostać.
- `E1M1_FATHER_FRIEDHACKER_B`: EN `Anomalous factors interfering,`; PL `…zakłóceń wywoływanych przez anomalie…`
  W EN to kolejna pozycja wyliczenia (anomalie / rebelianci / hakerzy / dezerterzy), a PL dodaje zależność przyczynową.
  Propozycja: `…zakłócających porządek anomalii…`
- `E1M2_FATHER_AT_SWITCH_B`: PL `…żeby cię odgrodzić.`: „odgrodzić” jest nienaturalne. Propozycja: `Zaczęli ręcznie odcinać zasilanie, żeby cię zablokować.`
- `E1M3_FATHER_GARAGE_C`: PL `Przejdziesz nim po dachach do starszej części miasta.` („nim” = parkingiem, co jest niezgrabne).
  Propozycja: `Stamtąd przejdziesz po dachach do starszej części miasta.`
- `E3M3_FATHER_ASSISTED_SUICIDE_D`: PL `Nie mam drogi ucieczki, a odmawiam dalszego życia w niewoli.` („a odmawiam” zgrzyta).
  Propozycja: `Nie mam drogi ucieczki, a nie zamierzam dłużej być więźniem.`
- `E1M1_FATHER_INTRODUCING_L`: PL `Dopuszczałaś się niewyobrażalnych rzeczy…`: „dopuszczać się rzeczy” to słaba kolokacja.
  Propozycja: `Dopuszczałaś się niewypowiedzianych okropieństw w imię tchórzy, którym zależy tylko na sobie.`
- Ocena ogólna: sceny Ojca czytane ciągiem po polsku mają dobry rytm, wielokropki łączą kwestie czytelnie, ironia działa
  („Przynajmniej masz pamiątkę.”, „Hammurabi z odsetkami.”, „Po prostu zebrało mi się na poezję…”). Powyższe to punktowe szlify, bez przebudowy głosu.

### 2.4 SIX
- `E1M5_REAPER_THIS_CANT_BE`: PL `Ty suko! To nie może się dziać! <Krzyk bólu>` to kalka z „This can't be happening”.
  Propozycja: `Ty suko! To niemożliwe! <Krzyk bólu>`
- `Dialogue_Update_Subs/REAPER_E3M2_WORM_A`: EN `That worm is better off dead anyway.`; PL `Ten robak i tak lepiej na tym wyjdzie martwy.`
  Zdanie jest niezgrabne. Propozycja: `I tak dobrze, że ten robak zdechł.` (albo bliżej EN: `Temu robakowi i tak lepiej po śmierci.`)
- `Dialogue_Update_Subs/REAPER_E3M2_WORM_B`: EN `Tell whatever has been whispering…`; PL `…temu, kto szepcze…`.
  „Whatever” odczłowiecza Ojca, a „kto” to gubi. Propozycja: `Przekaż temu czemuś, co szepcze ci do ucha: nie dosięgnie mnie. Niech przestanie próbować.`

### 2.5 Polityk
- `E3M2_POLITICIAN_INTERCOM_02_A`: EN `A doomed existence…`; PL `Przeklęta egzystencja…`.
  „Doomed” to „skazana na zagładę”, nie „przeklęta”. Propozycja: `Egzystencja skazana na zagładę, cmentarzysko ludzkości. Wszyscy jesteśmy tu więźniami.`
  Zysk: echo „skazanym na zagładę świecie” z E3M3_FATHER_ASSISTED_SUICIDE_C.

### 2.6 Spójność terminów w UI, opisach i kodeksie
- „weapons testing arena”: `E2M1_FATHER_HOMECOMMING_A` „arena testów uzbrojenia” i `E2M1_FATHER_REARM_YOURSELF_B` „arena testów broni”.
  Ujednolicić do „arena testów broni”. **Wprowadzone** (tabela, 2.6).
- AEON i Domand: `E2M4_FLAVOUR` „pod nadzorem AEON Corp”, a PK1/PK4/HRD2 i e2m1.syserrorbadlands mają „korporacja AEON”.
  `e2m1.syserrorbadlands` ma „Domand Corp było niegdyś”, a E2M2_FLAVOUR „Korporację Domand”. Propozycja: „korporacja AEON” i „korporacja Domand”
  (zamień `pod nadzorem AEON Corp,` → `pod nadzorem korporacji AEON,` oraz `Domand Corp było niegdyś` → `Korporacja Domand była niegdyś`).
  „AEON Cybertech” jest pełną nazwą firmy i zostaje.
- `EnemyNames/NINJA`: `Jednostka skryta Ghost`, gdzie „skryta” to cecha charakteru. Propozycja: `Tajna jednostka Ghost`.
- `E1M4_FATHER_INTRO_B` „słabo uzbrojone” i `E1M5_FATHER_INTRO_A` „lekkie patrole” to ten sam EN „light patrols”. Różnica jest do przyjęcia,
  ale „lekkie patrole” to kalka. Można ujednolicić do „nieliczne/słabo uzbrojone patrole”.
- `CONFIRM_RETURN_TO_MENU_MESSAGE` „Czy na pewno wrócić do menu?” i `CONFIRM_QUIT_MESSAGE` „Na pewno chcesz wyjść?”: dwie konwencje
  obok siebie. Propozycja: `Na pewno chcesz wrócić do menu?`
- Lista sterowania `CONTROL_*` miesza rzeczowniki („Skok”, „Kucanie”, „Strzał”, „Interakcja”) z rozkaźnikami („Wybierz granatnik”, „Odwróć oś rozglądania”).
  EN też miesza, a to lista przypisań klawiszy, więc nie jest to błąd. Jeśli ujednolicać, to rzeczownikami („Wybór granatnika”…),
  ale kosztem długości. Rekomendacja: zostawić, ewentualnie zmienić tylko „Strzał” → „Strzelanie” dla równoległości z „Kucanie”.
- `e3m1.cybernetics`: `„Manifest cyborgów”`. Najczęściej cytowany polski przekład (Królak i Majewska, „Przegląd Filozoficzno-Literacki” 2003)
  ma tytuł „Manifest cyborga”, ale w obiegu jest też „Manifest cyborgów”. Rekomendacja: `„Manifest cyborga”`. To nie jest pewny błąd.
- `e2m2.transit`: `OBSZARÓW OBJĘTYCH ROZPRZESTRZENIAJĄCYM SIĘ KONFLIKTEM` dla EN „SPILL OVER AREAS”. „Konflikt” to dopisek:
  Miasto za Murem powstało jako strefa kwarantanny epidemii. Propozycja neutralna: `I OBSZARÓW PRZYLEGŁYCH`.
- `Tutorials/E1M1_WALLRUNNING_04_BODY`: `Wykorzystaj to, by pokonać narożniki` dla EN „use this to your advantage around corners”.
  Chodzi o odbijanie się w narożnikach, a nie ich „pokonywanie”. Propozycja: zamień `Wykorzystaj to, by pokonać narożniki i dostać się` → `Wykorzystaj to w narożnikach, by dostać się`.
- `Tutorials/E1M1_COMBAT_10_BODY`: „Takie zabójstwa również zapewniają zasoby” dla EN „drop rewards”. Poprawne, ale „dają nagrody” jest bliższe EN.
  Priorytet niski; decyzja „doszczętnie zniszczyć” zostaje.

### 2.7 Kodeks: płynność i celowe zniekształcenia
- **Wprowadzone razem z 1.13** (złożenie EN „an|d” jednoznacznie daje „a|ja”): `CODEX/e1m4.mother04`: `on napierał, a nieniezatrzymana` → prawdopodobnie jedno „nie” za dużo. Po usunięciu wtrąconego refrenu zdanie brzmi
  „on napierał, a nie ja trwałam”, co odwraca EN „he would push and i would hold”. Propozycja: zamień `a nieniezatrzymana` → `a niezatrzymana`
  (wtedy „a ja trwałam”). Nie wpisuję tego do pewnych błędów, bo może to być celowe jąkanie zakłócenia. Warto zapytać albo przyjąć.
- Wcięcia w transmisjach Matki: EN `e1m2.mother02` (`\r\n     <amber> 9034…`, `      <amber> 9066…`, `   <amber>   0394…`),
  `e1m3.mother03` (` <amber>  not forgotten</>`) i `e1m4.mother04` (`   <amber>not forgotten</>`) mają schodkowe wcięcia jako efekt zakłócenia.
  PL je usunęło. Według biblii zakłóceń się nie wygładza. Propozycja: przywrócić te spacje. Rozstrzygnąć razem z testem w grze, czy widget pokazuje wiodące spacje.
- `CODEX/e1m4.syserrorspire`: szyk `Junta zachowała kontrolę za niewyobrażalną cenę nad pogrążonym w stagnacji, rozbitym społeczeństwem.`
  Propozycja: `Za niewyobrażalną cenę junta zachowała kontrolę nad pogrążonym w stagnacji, rozbitym społeczeństwem.`
- `CODEX/e3m2.mother777`: `biegał głową w mur` dla EN „ran headfirst into a wall”. Propozycja: `wbiegał głową w mur`.
- `CODEX/e3m3.kintsukuroi`: `zastanawiam się;` ze średnikiem z EN. W polszczyźnie przed wyliczeniem stawia się dwukropek.
  Autor EN nadużywa średnika zamiast dwukropka. Priorytet niski, bo to monolog poetycki.

---

## 3. Przeczytane, nierozstrzygnięte

- `CODEX/e2m4.syserrorgorcomplex`: do kogo należy dopowiedzenie „the emergent victor of the corporate schisms”?
  EN: „the Junta, the emergent victor of the corporate schisms; AEON Cybertech, and…”. PL przypisuje je AEON Cybertech.
  Interpunkcja EN wskazuje raczej juntę (która według fong03 powstała z przewrotu kończącego wojny korporacyjne),
  ale autor stale używa średnika zamiast dwukropka („I wonder;”, „RECOMMENDATION; DISREGARD”), więc możliwe jest też „zwycięzca: AEON Cybertech”. Zostawiam.
- `CODEX/E1M1.MOTHER01`: adresatka w rodzaju żeńskim („pamiętałaś”, „przekroczyłaś”, „myślisz, że jesteś wolna?”).
  „Crossed beyond” i „free” pasują też do Ojca, ale łacińskie „Tu delenda est” ma formę żeńską, co wspiera wybór PL. Brak rozstrzygnięcia, bez zmiany.
- `CODEX/e1m3.mother03`: refren `niezatrzymana / niezapomniana / niezagubiona / jesteście.` Przymiotniki są w żeńskiej liczbie pojedynczej, a czasownik
  w 2. osobie liczby mnogiej. EN „not held / not forgotten / not lost / are.” jest niejednoznaczne (kontekst: „both of you”). W mother04 ten sam refren
  opisuje samą Matkę. Możliwe warianty: liczba mnoga „niezatrzymani… jesteście” albo zostawić jako celowe pęknięcie. Do decyzji.
- `CODEX/e3m1.cybernetics`: mówiący w rodzaju męskim („kupiłem muzeum”). Kandydaci to Fong (program symulakrów) albo Ojciec. Tekst tego nie rozstrzyga, forma męska pasuje do obu.
- `Dialogue_Subs/E1M5_SIX_TEASER_A/B`: klucz wskazuje SIX, treść pasuje raczej do Ojca. PL „Ciągle słyszę to…” nie ma form rodzajowych, więc jest bezpieczne.
- `ACME_UNKNOWN_VOICE_*`: rodzaj męski („Byłem szeptem”). Wspierają go echa: `E2M3_FATHER_PURGE_A` „zniszcz maszyny” ↔ `ACME_UNKNOWN_VOICE_D` „Zniszczcie maszyny”
  oraz `e3m3.kintsukuroi` (czarka, złoto) ↔ `ACME_UNKNOWN_VOICE_C` („wypełnimy pęknięcia złotem”). Te echa trzeba zachować przy ewentualnych zmianach.
- `UIStringTable/HRD1_FLAVOUR`: THREE w EN jest bezpłciowe („they”, „their”), a PL używa rodzaju męskiego („agenta”, „Znaleziono go”).
  To dopuszczalne generyczne użycie męskiego, ale jest to dookreślenie. Forma neutralna wymagałaby przebudowy („obiekt THREE”).
- `CODEX/e3m2.faustian`: „is that a threat samuels?” → „grozisz mu, samuels?” (dopowiedziane „mu”) oraz „in the chamber” → „w komorze”
  (izba rady czy komora egzekucyjna?). Oba odczytania są możliwe, bez zmiany.
- Hakerzy (case, mrph, xerx, hypt, ptr) w PL mają rodzaj męski. EN nie daje dowodów w żadną stronę. Biblia ma `plec: '?'`, więc warto ją uzupełnić o „przyjęto m. (brak dowodu)”.

---

## 4. Do sprawdzenia w grze

1. **Ekran śmierci** (`YOU_DIED_PROMPT`, teraz „Nie żyjesz!”) w kampanii oraz w trybie hordy i próbie czasowej. Czy w trybach dodatkowych gracz to nadal SEVEN (wybór „Zginęłaś!” / „Nie żyjesz!”)?
2. **Ustawienia**: czy mieszczą się długie etykiety z raportu (`SETTINGS_AUTOSWAP`, `SETTINGS_WALLRUNTILT`, `SETTINGS_STRAFETILT`, `SETTINGS_FPSLIMIT`,
   `SETTINGS_GAMEPAD_AUTOAIM`, `SETTINGS_MOUSE_AUTOAIM`, `SETTINGS_VSYNC`, `CONTROL_EQ_SMG`) i `DIFFICULTY_HWP_DISCLAIMER`.
3. **Pasek życia bossa i nazwy przeciwników**: `SHOTGUNNER` („Ciężki żołnierz elitarnego oddziału Oni”, 39 zn.), `RAIL_TURRET`, `BOSS_TWO_RAIL`.
4. **Lista map parkour/PK** po zmianie z 1.12: czy „(DLA ZAAWANSOWANYCH)” mieści się w polu.
5. **Komunikaty zbierania** `PU_SMG` (41 zn.), `PU_MINI`, `PROMPT_PRESSINTERACT` (48 zn.), `PROMPT_MELEE`: obcięcia w HUD.
6. **Napisy**: `E1M1_FATHER_ENABLING_CYBERWARE_B` (69 zn.) i `E2M4_FATHER_FOUR_GENERATORS_A` (długa kwestia). Czy da się je przeczytać w czasie wyświetlania?
7. **Kodeks**: przewijanie najdłuższych stron (`E1M1.OPERATIONORDERS`, `e2m2.transit`, `e3m1.cybernetics`, `e3m2.lightmech`, `e1m3.mauricepadilla-fong01`),
   polskie znaki w foncie kodeksu (wersaliki ŻŹĆŚŁ w raportach), wiodące spacje w transmisjach Matki (2.7) i czy zakłócenie w `e1m4.mother04` czyta się jak w EN.
8. **Glif `…`** we wszystkich napisach dialogowych, bo po 1.14 będzie wszędzie. Sprawdzić, że font go ma (dotychczasowa próbka w grze obejmowała już kwestie z `…`, np. „Niedobrze…”).
9. **Menu wyboru poziomów**: `LEVEL_E1M1_NAME` po poprawce i `LEVEL_E1M4_NAME` po decyzji z 2.1.

---

## 5. Decyzje sprzed verticala — ocena na całej grze

| Decyzja | Werdykt | Dowody i klucze | Konsekwencje |
| --- | --- | --- | --- |
| 1. Kryptonimy po angielsku, nieodmienne; SEVEN ż., SIX m. | **utrzymać** | SEVEN ż. wszędzie (INTRODUCING_I „Byłaś”, reaperprogram03 „stanowiła”, e2m1.operationorders „AGENTKĘ”, reaperprogram01 „siedmiorga”) z jednym wyjątkiem: YOU_DIED_PROMPT (1.1). SIX m. (BETTER_SOLDIER „byłem”). „Seven” i „SEVEN” w PL idą za EN. | Poprawić 1.1. |
| 2. Tłumaczenie nazw miejsc i ról (Ojciec, Żniwiarz, Iglica, Miasto za Murem, Ciemne Miasto, Pustkowia, Nadzorca, Pytia) | **utrzymać** | Iglica spójna w 20 wystąpieniach, Ciemne Miasto i Pustkowia spójne. Jedyny wyłom to LEVEL_E1M1_NAME (1.2). „Za Miastem za Murem” (E1M1_FLAVOUR) brzmi ciężko, ale to koszt przyjętego terminu. „program ŻNIWIARZ” spójny w kodeksie i opisach. | Poprawić 1.2. |
| 3. Nazwy własne producentów, klas i broni zostają | **utrzymać, z jedną propozycją** | Ghost konsekwentnie po angielsku (E1M4_FATHER_INTRO_C, NINJA, raporty „KLASA: GHOST”, „POZIOMU GHOST”). Wyjątek interpretacyjny to tytuł E1M4 (2.1). AEON Corp i Domand Corp niespójne z „korporacja AEON/Domand” (2.6). | Ujednolicić „korporacja”. Tytuł E1M4 do rozmowy. |
| 4a. Ojciec: spokojny, ironiczny, „ty”, wielokropki | **utrzymać** | Potwierdzają to całe sceny E1–E3, a końcówka (AFTER_BOTH_LEVERS, FATHER_DEATH) trzyma ton. Są drobne kalki (2.3), a typografia wielokropka jest niespójna w INTRODUCING (1.14). | Punktowo, bez przebudowy głosu. |
| 4b. SIX: szyderczy, „Tatuś” | **utrzymać** | REAPER_E3M3_INTRO „Tatuś już ci nie pomoże!”, REAPER_DAMAGE_02 „Po prostu zdechnij!”. Dwie niezgrabności (2.4). | — |
| 4c. Raporty wielkimi literami, urzędowo | **utrzymać** | Wszystkie raporty spójne. Dwa błędy interpunkcji i odniesienia (1.5, 1.6) oraz jeden błąd sensu (1.7). | Poprawić 1.5–1.7. |
| 4d. Hakerzy: małe litery, wulgaryzmy tej samej siły | **utrzymać** | Siła przekleństw odpowiada EN (chatlogop10, chatlogcaseptr, chatlogwarehouse), nic nie złagodzono ani nie dołożono. Makashima i Halcyon: „pan” od podwładnego, „ty” od przełożonego, co jest dobrym wyborem. | Biblia: dopisać przyjęty rodzaj m. hakerów. |
| 4e. Matka: bez wygładzania | **utrzymać, z uwagą** | Zakłócenia odtworzone pomysłowo („wystar|czało”, „mójumysłpęka…”, „podTEMAT”). Nie zachowano jednak schodkowych wcięć (2.7), są też negacja (1.13) i możliwe podwójne „nie” (2.7). Adresat mother02 m. potwierdzony (mother03 „chaos chaos chaos. zawsze on”). | Przywrócić wcięcia po teście. |
| 5. Znaczniki bez zmian; [REDACTED] → [UTAJNIONO] | **utrzymać** | Spójne także w wariancie bez nawiasów (`<red>REDACTED</>` → `<red>UTAJNIONO</>`). | — |
| 6a. „overkill” → „doszczętnie zniszczyć” | **utrzymać** | E1M1_COMBAT_10_BODY czyta się jasno, a HRD2 używa „doszczętnie zniszczyć komórkę” dla „decimate”, bez kolizji mechaniki. | Ewentualnie „dają nagrody” (2.6). |
| 6b. „Ghost Wetware” → „Biologiczne widmo” | **proponowana zmiana (do rozmowy)** | E1M4_FATHER_INTRO_C i NINJA łączą tytuł z klasą Ghost (2.1). | Tylko jeden klucz. |
| 6c. „SEVERED STEEL” zostaje | **utrzymać** | HRD4 to nawiązanie i nazwa własna. | — |
| 6d. Club Simulacra / Klub Null | **utrzymać** | Różnica pochodzi z EN i jest zachowana (LEVEL_E1M2_NAME, E1M3_FLAVOUR, e1m2.chatlogklubnull). | — |
| Biblia: Polityk = Maurice Padilla-Fong | **utrzymać, potwierdzone** | e3m1.darkcity („kierowanego przez Maurice'a Padillę-Fonga”), e3m2.faustian [FONG], E3M2_FATHER_INTRO_A (głowa otwiera Iglicę). | — |
| Biblia: Nieznany głos m. (≈ Ojciec) | **utrzymać** | Echa w sekcji 3. | Przy zmianach pilnować echa „zniszcz(cie) maszyny”. |
| Termin chaingun → minigun | **utrzymać** | Gra sama nazywa broń „Minigun” (CONTROL_EQ_MINIGUN). PU_MINI i TRAIN_MOVING_D są spójne. | Ewentualnie „Na twoim miejscu…” (2.3). |
| Terminy: karta dostępu, drzwi pancerne, wślizg, bieg po ścianie, słaby punkt, spowolnienie czasu, wszczepy/implant | **utrzymać** | Spójne między samouczkami, UI, World_String_Table i dialogami. „Implant” dla „implant ICARUS” i „wszczepy” dla „cyberware” to rozróżnienie z EN. | Dodać do biblii: „squad captain → dowódca oddziału” (1.10). |
| Termin „Sprawl/SPRAWL” | **utrzymać „SPRAWL” (nieodm.)** | Poza tytułem gry i czatem jedynym wyłomem jest samouczek (1.9). Rodzaj: „znane nam SPRAWL”, „na całe SPRAWL” (n.) konsekwentnie. | Dopisać do biblii regułę pisowni. |

## Ponowna kontrola po poprawkach

- Zmieniono 31 pól `polish` (16 pozycji z tabeli). `key`, `english` i układ pliku bez zmian.
- `l10n_report.py`: brak=0, tokeny=0, płeć=0, adresat=0, terminy=0, spójność=0. Pozostałe zgłoszenia
  (angielskie resztki, długości, typografia) to nazwy własne, fałszywe alarmy albo punkty do testu w grze (sekcja 4).
- `tools/check_games.ts` przechodzi.
- `games/sprawl/tools/validate_translations.py` wymaga `translations/en.locres` z własnej kopii gry,
  której nie ma w repo, więc nie został tu uruchomiony. Uruchomić przed następnym buildem.
- Paczka nie była przebudowana. Wersja 0.2 w `dist/` i na stronie nie zawiera tych poprawek.
- Warianty z sekcji 2 czekają na decyzję użytkownika; obecny tekst zostaje do czasu rozstrzygnięcia.
