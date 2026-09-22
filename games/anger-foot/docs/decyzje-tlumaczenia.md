# Anger Foot — decyzje tłumaczenia (0.3)

Przegląd istniejącego tłumaczenia 0.2 według skilla lokalizacji: biblia, raport,
lektura wszystkich 1100 kwestii dialogowych i poprawki. Zmieniono 210 wpisów.
Styl i terminologia z 0.2 zostały; to poprawki, nie nowe tłumaczenie.

## Postacie
- **Płeć mówiących i adresatów wzięta z tabeli gry.** Każda kwestia ma pole mówiącego
  i adresata z płcią („NPC (Female)” > „Player”). Raport sprawdził wszystkie dialogi:
  zero rozjazdów w formach „-łem/-łam” i „-łeś/-łaś”.
- **Anger Foot — rodzaj męski** w zwrotach do gracza („Pomogłeś temu miastu”).
  Tabela podaje tylko „Player”, ale rosyjska wersja gry konsekwentnie używa form
  męskich („ты опоздал”).
- **Pizza Świnia — odmiana żeńska, rodzaj męski.** „Pizza Świni”, „Pizza Świnio!”, ale
  „Pizza Świnia próbował nas zabić”, bo w tabeli to postać męska. Zostawione z 0.2.
- **Baron Mazi / Umysł Brudu — rodzaj męski**, choć tabela podaje „Neutral”. Nazwy
  są męskie, więc formy męskie brzmią naturalnie.

## Terminy
Bez zmian wobec 0.2; teraz spisane w `translations/biblia.yaml`.

| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| Shit City | Zasrane Miasto | ta sama siła co oryginał | decyzja (0.2) |
| Pollution Gang | Gang Smrodu | krócej i zabawniej niż „zanieczyszczeń” | decyzja (0.2) |
| the CEO | Prezeska | szefowa, Office Boss (Female) | tabela |
| goon | zbir | | decyzja (0.2) |
| sneakers | buty / sneakersy | w mowie „buty”, w modzie „sneakersy” | decyzja (0.2) |

## Poprawki
- **Wielkie litery po polsku** (188 wpisów): nazwy osiągnięć, celów, butów, poziomów,
  znajdziek i ról w napisach końcowych dostały pisownię zdaniową („Nie mogłem się
  powstrzymać”, „Pościg się zaczyna”, „Kierownik projektu”). Wielka litera została
  przy nazwach własnych świata: gangi, bossowie, Wieża Zbrodni, Śmieciowa Góra,
  Laboratorium Zielonej Rzeki, Dzielnica Pizzy, Klub Rozpusta, Riwiera Mozzarelli,
  Cheddarowy Potok, Rurowe Miasto, Giełda Glocków, Hotel Zapalczywych, Więzienie
  Smrodu, Doły Mazi, Szambowe Rozlewiska oraz angielskie nazwy bloków.
- **Nazwy poziomów w opisach osiągnięć w cudzysłowie**, bo pisane małą literą
  zlewałyby się ze zdaniem: „Spuść wodę w „Nowym początku”.”
- **Liczebniki przy {0}.** Rzeczowniki nieosobowe przebudowane tak, żeby pasowały do
  każdej liczby: „Wytęp karaluchy: {0}”, „Zabij węże: {0}”, „Zalicz strzały w głowę: {0}”,
  „Ukończ poziom w czasie poniżej {0} s”, „kopiąc mniej niż {0} razy”.
  „Zabij {0} zbirów/wrogów” zostało, bo forma męskoosobowa jest poprawna dla 2 i więcej.
- **Błędy sensu:** „No overtime pay” to „Nadgodziny niepłatne”, a nie „Żadnych
  nadgodzin”; „You're giving me away!” to „Wydasz mnie!” (udaje trupa), a nie
  „Zdradzasz moją kryjówkę”; „Włącz pada” → „Włącz pad”.
- **Idiomy:** „Świeć, Pizza Świnio, nad jego duszą...” („May Pizza Pig rest his soul”),
  „Cztery w pamięci...” („Carry the four”), „ukradł nam ubrania z grzbietu”,
  „Bo jak nie... ...to kopnę tę stertę butów” („Or else... I'll kick...”).
- **Drobne:** „Aromat to bonus” (zamiast „dodatkowy bonus”), „Mnie też to zaraz czeka”,
  „Ponętnego i Zmysłowego” (Voluptuous), „#harujemy”, „tajnej sody z tajnym sosem”.

## Okazje wykorzystane
- **Song/bong** (twórcy prosili o adaptację): „UWIELBIAM TEN UTWÓR!” → „JA TEŻ
  UWIELBIAM TEN TOWAR!”. Wcześniej „kawałek/bonga”, bez przesłyszenia.
- **Trash Fest / Cash Fest:** „Szajs Fest” / „Hajs Fest”. Rym jak w oryginale;
  wcześniej „Śmieć Fest” / „Kasa Fest”.
- **Developer / developing a hunger:** „Pracuję w dziale rozwoju.” / „Rozwija mi się
  apetyt.” Wcześniej „deweloper”, czyli po polsku budowlaniec, bez gry słów.
- **Lactose / lack toes** („Good luck translating this”): po polsku przez Gluta Glinę,
  byłego szefa Gangu Przemocy — „Szkoda tylko, że nie trawię glutenu.” / „Miałem
  podobny problem w poprzednim gangu.” / „Nie trawiłem Gluta.” To najodważniejsza
  zmiana: znika aluzja do fetyszu stóp (postać dalej patrzy na stopy, ale tekst tego
  nie tłumaczy). Wersja dosłowna z 0.2: „Mam nietolerancję laktozy” / „Nie zniosłem
  braku palców u stóp”.
- Zostawione z 0.2, bo dobre: „Na drugi etat kradnę koty” (catburglar), „Zmiany
  kryminatyczne są prawdziwe”, „Ale z ciebie KĄSEK!”, „...przed niewystępowaniem”,
  „D.P.P.K.G.S.”, „Kupkowo”.

## Świadome odstępstwa od oryginału
- „Kopnąłeś {0} razy.” zostaje, choć przy 1 dałoby „1 razy”. Karta po poziomie
  z liczbą kopnięć; przebudowa na „Kopnięcia: {0}” zabiłaby ton.

## Mniej pewne (sprawdź w grze)
- **Ustawienia → Pad:** trzy opcje wspomagania celowania mają 31–34 znaki
  („Przyciąganie wspomagania celowania”). Czy mieszczą się obok suwaka?
- **Ekran śmierci:** „NACIŚNIJ DOWOLNY PRZYCISK, BY ZACZĄĆ OD NOWA” (44 znaki) — czy
  nie wychodzi poza ekran.
- **Wybór celu poziomu (gwiazdki):** nowe „Wytęp karaluchy: 20”, „Ukończ poziom
  w czasie poniżej 45 s” — czy dwukropek i „s” dobrze wyglądają w tej ramce.
- **Kanały, bar Gangu Rozpusty:** para „laktoza/Glut” — czy żart się broni, czy wrócić
  do dosłownej wersji.

## Raport kontrolny
`work/l10n-report.md` po poprawkach: płeć 0, adresat 0, terminy 0, tokeny 0, brak 0,
liczebniki 0 (wyciszone w biblii z uzasadnieniem), angielskie resztki 0 (onomatopeje
i skróty wyciszone), spójność 0 (dwa celowe warianty „Default” i „Continue”),
typografia 0 (spacje na końcu to literówki w oryginale).
Zostało: długość 14 (dialogi w dymkach zawijają się same; opcje ustawień
wyżej w „sprawdź w grze”), wielkie litery 5 (nazwy własne: Worek Glina, Dzielnica
Pizzy, imiona nurka).
