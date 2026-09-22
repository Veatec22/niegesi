# Katana ZERO — decyzje tłumaczenia (0.2.0)

Mówiący nie jest zapisany przy wpisach, więc płeć i formę zwracania się brałem
z rosyjskiej wersji tej samej kwestii (czas przeszły, „ты/вы”) i z sąsiednich kwestii.

## Postacie
- **Zero — mężczyzna, mówi krótko i chłodno.** Rosyjski: „пришел”, „понял”. Wybory
  odpowiedzi gracza mają formy męskie („Przyszedłem”, „Nie wiedziałem”). Imię zostaje „Zero”.
- **Psychiatra mówi do Zero per „ty”**, Zero do niego też. Rosyjski „ты” w obie strony;
  ton kliniczny, przekleństwa dopiero w złości („NIE PRZERYWAJ MI, KURWA!”).
- **Dziewczynka — forma żeńska, mówi do Zero per „ty”.** Rosyjski: „поняла”, „нарядилась”.
- **Recepcjonistka (hotel Murdower, potem Ośrodek Badań Synergicznych) mówi per „pan”**,
  a Zero odpowiada formami bezosobowymi albo „pani” („Proszę przestać do mnie mówić”).
  Rosyjski „вы”, forma żeńska „расслышала”.
- **Snow — kobieta**, rosyjskie „впечатлена”, „надеялась”. Imię zostaje „Snow”, a nie „Śnieżka”.
- **V — mężczyzna, bardzo wulgarny, wtrąca rosyjskie przekleństwa.** Wtrącenia cyrylicą
  („Сука охуеть”, „Блять”) zostają jak w oryginale; reszta z wulgaryzmami tej samej siły.
- **Kissyface — mężczyzna** („Mr. Kissyface” → „panie Kissyface”).
- **Komedia — mężczyzna** („Nie wiedziałem, że masz sumienie”), mówi potocznie.
  **Tragedia** mówi archaiczną polszczyzną („Usłuchaj mego rozkazu”, „błędne serce”).
- **Kobieta w VIP-ie Chinatown (NULL) — forma żeńska** („Jestem zbyt zmęczona na zemstę”).

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| the Dragon | Smok | chiński smok z przydomka, naturalnie się odmienia; rosyjski ma „Змей” | decyzja |
| Chronos | Chronos (Chronosu, Chronosem) | nazwa leku, odmieniana jak rzeczownik męski | decyzja |
| NULL, Gamma NULL | NULL, NULL Gamma | nazwa programu, zostaje wersalikami | decyzja |
| New Mecca | Nowa Mekka | nazwa miasta, przetłumaczalna i czytelna | decyzja |
| Third District | Trzecia Dzielnica | jak wyżej | decyzja |
| Juncture | Juncture | nazwa władz, bez dobrego polskiego odpowiednika | decyzja |
| dossier | teczka | naturalne w mowie i w UI („Otwórz teczkę”) | decyzja |
| precognition | dar przewidywania | lepiej brzmi w dialogu niż „prekognicja” | decyzja |
| withdrawal | głód | żargon uzależnień, krótkie | decyzja |
| cromag | kroman (kromański) | wojenny epitet od „Cro-Magnon”; zachowuje obelżywy ton | decyzja |
| *Hang up* | *Rozłącz się* | tryb rozkazujący jak inne opcje w gwiazdkach | decyzja |
| Behemoth, Leviathan | Behemot, Lewiatan | polskie formy biblijnych nazw, pluszaki dziewczynki | decyzja |
| Strong Terry | Silny Terry | przydomek osiłka z TV, odmieniany („Silnemu Terry'emu”) | decyzja |
| trick or treat | cukierek albo psikus | utarte polskie tłumaczenie | decyzja |
| PRESS TO EJECT | WYSUŃ KASETĘ | poziom to taśma VHS; krótko, bo pole jest małe | użytkownik |

## Okazje wykorzystane
- Rada Chudych Rysiów w klubie: „Skinny Ricky / Slender Richard” → „Chudy Ryś / Ryszard Chudy”.
- Bramkarze w kasynie: „Bill Betonowa Ściana”, „Mark Moralnie Niezłomny”, „Lenny Wyrozumiały”.
- Licznik dni odmieniony po polsku: „ZOSTAŁO 10 DNI”, „ZOSTAŁY 4 DNI”.
- Karcianka z recepcjonistką zachowuje absurdalne nazwy kart („Zębatka Wiecznego Chaosu”,
  „Kwantowy Biomałż Fraktalnej Katastrofy”) i żart z „kartą pułapki”.

## Świadome odstępstwa od oryginału
- **Cudzysłowy proste "..." zamiast „...”.** Fonty gry nie mają polskich cudzysłowów
  (rosyjskich «» też nie). Półpauzy zamieniłem na łącznik z tego samego powodu.
- Wzrost i waga w teczkach celów w cm i kg, jak w wersji rosyjskiej.
- Tytuły piosenek, marki i nazwy własne (Murdower, Chinatown, Studio 51, Webflix) zostają.
- W kilku kwestiach liczba pauz `*` różni się o jedną od oryginału, bo polski szyk jest inny.

## Mniej pewne (sprawdź w grze)
- **Ustawienia i sterowanie** — najdłuższe napisy („SYNCHRONIZACJA PIONOWA”,
  „PRZEWROT PRZY LĄDOWANIU”, „DLA SŁABSZYCH KOMPUTERÓW”). Rosyjski ma podobne długości,
  więc powinny się zmieścić, ale warto rzucić okiem.
- **Duże napisy i tytuły poziomów (font xirod)** — „ó/Ó” w tym foncie dopiero w 0.2.0,
  np. „POZIOM UKOŃCZONY” i nazwy poziomów w wyborze etapu.
- **Komunikat restartu** „(Naciśnij DOWOLNY PRZYCISK, aby zacząć od nowa)” — dwa razy dłuższy od EN.
- **Rozmowy z wyborem odpowiedzi** w klubie (Electrohead), u V w limuzynie i w bunkrze —
  gęste znaczniki efektów, sprawdź, czy drżenie i kolory trafiają w dobre słowa.
- **Recepcjonistka w Ośrodku Badań Synergicznych** — dużo gałęzi, formy „pan/pani”.

## Raport kontrolny
`work/l10n-report.md` po ostatniej partii: brak tłumaczenia 0, tokeny 0, płeć 0.
Zostały same fałszywe alarmy: angielskie resztki (36 — onomatopeje, nazwy własne, tytuły
piosenek), wielkie litery (22 — nazwy broni, pięter i kart), terminy (4 — odmiana
„Nowej Mekce”, „Behemocie” i tytuł utworu), długość (10 — ustawienia jak wyżej), spójność
(2 — „go/je” zależnie od tego, czy chodzi o dowód, czy o przepustkę).
