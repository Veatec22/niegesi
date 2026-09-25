# Broforce — decyzje tłumaczenia (0.2.0)

## Zwracanie się do gracza
- **Do gracza na „ty”, w rodzaju męskim.** Menu, podpowiedzi i komunikaty („Wyrzucono cię z gry”,
  „Nie masz ich dość, co?”). Gdzie formę osobową dało się ominąć bez straty, ominięto („Połączenie
  zostało przerwane” zamiast „Zostałeś rozłączony”, „W KTÓRYCH JESZCZE CIĘ NIE BYŁO”).
- **Rozkazy na mapie świata w bezokoliczniku, po wojskowemu:** „UZIEMIĆ ICH!”, „ODOBCOWIĆ ICH!”,
  „DO ROBOTY!”, „ODNALEŹĆ ICH I URATOWAĆ!”. Oryginał woła raz „Broforce”, raz „Bros”;
  bezokolicznik omija wybór między „ty” a „wy” i brzmi jak rozkaz sztabu.
- **Finał: Prezydent i Jezus mówią do gracza na „ty”** („DOKONAŁEŚ NIEMOŻLIWEGO”, „OBRALI CIĘ
  WIELKIM CESARZEM”). Źródło: „Hello, friend”, „High five me, Bro!” i „emperor” w liczbie
  pojedynczej. „Gentlemen…” i „How did you know…” zostają w liczbie mnogiej („PANOWIE”, „SKĄD
  WIEDZIELIŚCIE”), bo tak mówi oryginał.

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| bro | bro (nieodmienne) | rdzeń wszystkich gier słów; polski slang zna „bro” | decyzja |
| IRONBRO / IRON BRO | bez zmian | nazwa trybu | decyzja |
| Brotality | Brotalność | brutality → brutalność, gra słów zostaje | decyzja |
| Brodown (dogrywka po remisie) | BROJEDYNEK | showdown → pojedynek, z „bro” | decyzja |
| Covert Operation | TAJNA OPERACJA | | decyzja |
| Workshop | Warsztat | oficjalna polska nazwa w kliencie Steama | decyzja |
| dash | sprint | w Broforce to szybszy bieg, nie unik | decyzja |
| Fire (przycisk) | STRZAŁ | „NACIŚNIJ STRZAŁ, BY DOŁĄCZYĆ” | decyzja |
| custom campaign / map | WŁASNE KAMPANIE / mapy graczy | menu główne vs. komunikaty | decyzja |
| Deathmatch, Versus, Host | bez zmian | utarte w polskich grach | decyzja |
| gyming (podpisy bossów) | koksowanie | slang siłowni zamiast „technologii siłowni” | decyzja |

## Okazje wykorzystane
- Parodie krajów zostają parodiami: Veetman → Wietman, Cambodium – soon to be Cam*BRO*dium →
  KAMBODIUM – WKRÓTCE KAM*BRO*DIUM, Youkraine? More like our kraine! → TWUKRAINA? RACZEJ NASZKRAINA!
  Irakistan, Jalpin, Mookgolia, Afreeka, Arstotzka i Val Verde bez zmian (to już żarty albo cytaty).
- Poziomy zagrożenia jako jedzenie i kolory, jak w oryginale: CZARNY BEZ, MARMOLADA, MORELA,
  CHEDDAR, BAKŁAŻAN, KANTALUPA, BATAT; świątynie mięśni: BRĄZOWA OPALENIZNA, SAMOOPALACZ,
  MASŁO KAKAOWE, NAPOMPOWANE ŻELAZO.
- Podpisy bossów: TACO HELL → TACO Z PIEKŁA RODEM, OVERCOMPENSATE MUCH? → COŚ SOBIE
  REKOMPENSUJEMY?, Terrorist/Undead gyming technology → SZCZYTOWE OSIĄGNIĘCIE
  TERRORYSTYCZNEGO / NIEUMARŁEGO KOKSOWANIA.
- Freedominate them! → ZDOMINOWAĆ ICH WOLNOŚCIĄ!, Terrestrialize them! → UZIEMIĆ ICH!,
  De-alienate them! → ODOBCOWIĆ ICH!, 'Murica → MERYKA.

## Świadome odstępstwa od oryginału
- **Licznik po misji: „4 DO URATOWANIA I NOWY BRO ODBLOKOWANY!”.** Gra skleja
  „{liczba} {MORE} {RESCUE|RESCUES} {UNTIL NEXT UNLOCK}” i rozróżnia tylko 1 i resztę; polski
  rzeczownik wymagałby trzech form, więc zdanie nie ma rzeczownika zależnego od liczby.
- **„ZWYCIĘSTWA Z RZĘDU: {0}!”, „POZOSTAŁO SEKUND: {0}”** — liczba za dwukropkiem, żeby nie
  odmieniać rzeczownika.
- **Opisy regionów i napisy przerywników wersalikami.** Fonty Hudson i 04B mają same wielkie litery;
  polskie litery, których im brakuje, podstawia Windows — pisane małymi wyszłyby jako małe.
- **Pozostawione po angielsku:** „WHAT IS LOVE?” (Terrorbot, cytat piosenki), „BLRRGGGGG”
  (dźwięk), nazwa konkursu „Weekend Workshop Brodown”, imiona bro (Rambro, Ellen Ripbro, MacBrover,
  Time Bro…).
- Podpowiedź sprintu skrócona do „KIERUNEK DWA RAZY = SPRINT!” — dosłowne tłumaczenie było
  o 60% dłuższe od oryginału w ciasnym polu samouczka.

## Mniej pewne (sprawdź w grze)
- **Opisy regionów na mapie** — font dynamiczny; Ą, Ć, Ę, Ń, Ś, Ź, Ż podstawia Windows innym
  krojem. Czy razi na tyle, żeby przełączyć te opisy na bitmapową wersję Hudsona?
- **Finał (Prezydent, Jezus)** — część linijek idzie fontem 04B_11 bez polskich liter (też
  podstawiane przez Windows) i ma ręczne złamania wierszy; możliwe ucięcie najdłuższych.
- **Ekran wyników po misji** — „4 DO URATOWANIA I NOWY BRO / ODBLOKOWANY!”: czy mieści się w polu.
- **Podpisy bossów** (plansza z nazwą bossa przed walką) — długie, np. „UKORONOWANIE ZAGROŻENIA
  TERRORYSTYCZNEGO I KOSMICZNEGO”.
- **Czerwony licznik „POZOSTAŁO SEKUND”** (kampanie z limitem czasu) — font HudsonOutline
  z dorysowanymi literami i obrysem; w verticalu nie oglądany.
- Menu versus i kampanii graczy — długie etykiety („WYBIERZ SPOŚRÓD ZAPISANYCH LOKALNIE KAMPANII…”).

## Raport kontrolny
`work/l10n-report.md` po pełnym tłumaczeniu: 0 zgłoszeń we wszystkich sekcjach. Wcześniej
9 „angielskich resztek” — wszystkie celowe (DEATHMATCH, HOST, TOP, Offline, WWB, BLRRGGGGG,
WHAT IS LOVE?), wpisane do `bez_tlumaczenia` w biblii; 2 zgłoszenia terminów dla nazwy konkursu
wyciszone w `ignoruj`, rdzeń „Warsztat” poprawiony na „warszta”, żeby łapał „W WARSZTACIE”.
