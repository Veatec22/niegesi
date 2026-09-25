# DEADBOLT — niezależny przegląd lokalizacji PL

Recenzent: osobny agent w świeżym kontekście, tryb tylko do odczytu (2026-09-25).
Środowisko nie pozwoliło mu zapisać pliku, więc raport przepisał agent prowadzący
bez zmian treści; stan po poprawkach — sekcja na końcu.

## Zakres

- Wejście (SHA-256, prefiksy): pl.json 6C623D862ED6D778, en-pl-review.json A2514A5538ABD8A5,
  bible.yaml 9007177D460441BD; plus translation-decisions.md, technical.md, l10n-report.md, oryginalne `dia_*.json`.
- **618 wpisów, przeczytane 618.** pl.json ↔ en-pl-review.json: te same klucze i PL; znaczniki
  `&y& &r& &b& &w& &dk& &!& #` zgodne liczbowo we wszystkich wpisach; brzegowe spacje różnią się tylko celowo (s1743, s1724).
- Pokrycie JSON: wszystkie pola Name/Description/Dialogue w 8 plikach; nieprzetłumaczone celowo 8 wartości
  (imiona Puff, Roland, Sir Stela, Ibzan, Timur, Vall ×2 oraz „ror2 when”).
- Pokrycie STRG: 120 kandydatów spoza pl.json to testowe/debugowe napisy, klucze logiki, wewnętrzne nazwy
  broni/wrogów, klawisze, nazwy z `bez_tlumaczenia`, „The Bloody Mary”, „Sir Stela”, „Tridead”, „Stop suckin lmao!”.
- Grupy: UI/ustawienia/sterowanie/statystyki 108, podpowiedzi klawiszy 56, cele i HUD 16, misje 47, broń 53,
  ulepszenia 8, osiągnięcia 45, nazwy wrogów 18, porady 14, okrzyki/sceny/bossowie 79, dia_fp (misje 0–28) 107,
  sejfy/notatki/finał 52, kasety 14, napisy końcowe 1.
- Luki: bez gry. Złożenia PICKUP, `Kill &r&`, `seconds left`, `EXIT VENT` sprawdzone w kodzie; pozostałe wg technical.md.
  Brak kontekstu: mówiący w s2594, s2646; odniesienie „he knows” w dia_lv3_7.

## Błędy pewne (zgłoszone jako proponowane)

1. **s1526** `'&!&: PICKUP ` + nazwa broni wersalikami (oPControl_Draw_73, `weapon[type, 0]`) — „PODNIEŚ KOSA/MINA/KUSZA”.
   Propozycja: `'&!&: PODNIEŚ - `.
2. **s2598** „Roland... I think he's here...!” — mówiący dzwoni do Rolanda, „he” to żniwiarz; obecne PL zmienia podmiot.
   Propozycja: „Roland... on chyba tu jest...!”
3. **s1253** „Poor aim” ≠ „kiepski cel”. Propozycja: „Kiepska celność - i kiepski żniwiarz.”
4. **dia_fp map_mission8** „free souls contained” — liczba mnoga zgubiona dla rymu.
   Propozycja: `"Ich leże - odkryte!#Spal popiół, #spal zmarłych#i uwolnij dusze ukryte."`
5. **s1227** „Straże!” — nieidiomatyczne wołanie. Propozycja: „Straż! Co wy wyprawiacie?”

## Decyzje sprzed verticala — werdykty

- Wiersze rymowane z refrenem (użytkownik): **utrzymać** — refren spójny w 8 miejscach i w finale; do poprawy m8 i m14.
- „żniwiarz” (użytkownik): **utrzymać** — działa w okrzykach, kasetach, notatce Timura; para żniwiarz/żniwa wzmacnia fabułę.
- Gangi po angielsku (użytkownik): **utrzymać** — „Zombie Kingz: rozbici” czyta się dobrze.
- „jebany” (użytkownik): **utrzymać** — „fucking” pada raz (s1765); inne przekleństwa w sile EN; wyjątek „GODDAMN” → „PRZEKLĘCIE” (za słabe i sztywne).
- Decyzje agenta: **utrzymać** tryb rozkazujący wersalikami, adaptowane tytuły misji, dwukropek przy doklejanych imionach,
  „Controls” tylko w menu pauzy, proste cudzysłowy, osobę narracji jak w EN, „Płomienie z rykiem budzą się do życia”.
  **Proponowana zmiana:** „Stop suckin lmao!” zostawiony po angielsku. **Brak kontekstu:** „Strzel/zatwierdź” (test w grze).

## Do rozmowy (recenzent, najważniejsze)

1. Piosenka o Styksie (s1766): „Mama śpi, ma zamknięty wzrok” (kolokacja), „krok po krok” (błędna forma, powtórzony „krok”).
   Rekomendacja: „Mama nie patrzy, odwraca wzrok.” / „Pamiętaj: toniemy wolno - to wyrok.”
2. s2607 „Bring... your own...” → „Przynieś... własny...” — zgadza się tylko z „popiołem”, a odpowiedź dotyczy ludzi. Rek.: „Przyprowadź... swoich...”
3. s2600 „It doesn't look well.” → stan Świecy, nie sytuacja. Rek.: „Nie wygląda najlepiej.”
4. m14 „Bliźniaczki dryfują - z żądzy i z bólu” (przyczyna zamiast żywiołu). Rek.: `"&b&Bliźniaczki&!& zgubione - #w morzu żądzy i bólu. #Kobiety bez miłości#nie mogą przy mnie żyć."`
5. s2067 „ODBLOKOWANA” przy nazwach różnych rodzajów. Rek.: „ODBLOKOWANO”.
6. s1763 „PRZEKLĘCIE zimno” (GODDAMN). Rek.: „CHOLERNIE zimno”.
7. s1767 „trochę... sucho” (wystrój, nie wilgotność). Rek.: „surowo” / „ascetycznie”.
8. s1728 „Stop suckin lmao!” wśród polskich porad. Rek.: przetłumaczyć, np. „Przestań dawać ciała lol!”

Niższy priorytet: s1765 „Gdzie on był?” → „Gdzie to było?”; s1759 „coś się wierci” → „ktoś”, „Mroczny-i-Burzowy” → „Ciemny-i-Burzliwy”;
s1761 „powiedziałaby ona” → „- tak by powiedziała”; m11 → „Więcej, więcej, ciągle więcej.”; map_temur „zręczności” → „talentowi konstruktora”;
finał „grim and dim”; dia_lv3_7 rodzaj Świecy (brak kontekstu); s1352 „posiłki w drodze” → „nadjeżdżające posiłki”;
s2235 „Płotka” → „Drobny diler”; s2234 → „Zwróćmy na siebie uwagę…”; s2268 → „Istny horror”; s2376/s2378 → „bez wychodzenia z gry”;
dia_lv1_4 „RÓŻNE / WIĘCEJ RÓŻNYCH” → „GRATY / WIĘCEJ GRATÓW”; dia_lv4_2 „Rozmawiaj” → „Porozmawiaj”;
sterowanie „Wejście na schody” → „Wejdź na schody”, „(osobno)” → „(osobny klawisz)”; s2207 „Zabici:” → „Zabójstwa:”;
pad „L. bumper”/„L. spust” (ew. LB/RB/LT/RT); s2344 „Pompka.” → „Przeładowanie pompowe.”

## Do sprawdzenia w grze (recenzent)

1. Podnoszenie broni: która nazwa jest doklejana, czy linia się mieści.
2. Cele z imieniem: „Zabij: Timur Majsterkowicz”, „Zabij: Amber & Evelyn” (czy `&` się wyświetla), czy pojawia się „Zabij:” z nazwą typu wroga.
3. Ekran Charona: szerokość najdłuższych nazw broni („PISTOLET 9 mm Z TŁUMIKIEM”, „KARABIN ZE STAREGO ŚWIATA”, „STRZELBA SAMOPOWTARZALNA”).
4. Podpowiedzi przy obiektach (fontTiny): „WEJDŹ DO WENTYLACJI”, „OTWÓRZ WYTRYCHEM”, „USIĄDŹ I POROZMAWIAJ”, „ODETNIJ ZASILANIE (CHWILOWO)”, „NASTAW MINUTNIK NA 3 S”; czy „WEŹ NA CEL” (s1388) oznacza snajperkę.
5. Menu sterowania: „Strzel/zatwierdź” i szerokość kolumny.
6. Podsumowanie i osiągnięcia: „Naciśnij 'E', aby kontynuować”, „NAGRODA W DUSZACH: n”, najdłuższe opisy (s2404, s2390).
7. Porada po śmierci: „Liczba zgonów: 7. Spróbuj innej taktyki!”
8. Wybór misji: tytuły, opisy, „Zabij wszystkich nieumarłych.”
9. Płomienie: łamanie `#`, kolor `&y&`, mieszczenie się w teczce (misje 16, 24).
10. Kasety: najdłuższa (s1759) i piosenka (s1766) — puste linie, zwrotki, przewijanie.
11. Dymki: czy s2648 da się przeczytać w czasie wyświetlania.
12. Ostrzeżenie (s1941) i napisy końcowe: czy tekst mieści się na ekranie.

## Stan po poprawkach (agent prowadzący)

- Błędy pewne 1–5: naniesione; s1526 jako `'&!&: WEŹ BROŃ: ` (nazwa broni w mianowniku, sprawdzone w kodzie).
- Do rozmowy 1–3, 5, 7, 8 i cała lista niższego priorytetu poza „grim and dim”, rodzajem Świecy
  i skrótami pada: naniesione (`work/review_fixes.py`).
- 4 (m14) i wiersze w ogóle: użytkownik zdecydował o większej swobodzie; 14 zwrotek przepisanych
  na pełny rym (`work/verses.py`, decyzja w `translation-decisions.md`).
- 6: użytkownik wybrał „CHOLERNIE zimno”.
- Po poprawkach: `review.py` 0 problemów ze znacznikami, raport kontrolny bez nowych uwag
  (m22 „trupów” zamiast „nieumarłych” — celowo, dla rymu), test pluginu bez gry: OK.
- Lista „Do sprawdzenia w grze” pozostaje otwarta — to test użytkownika.
