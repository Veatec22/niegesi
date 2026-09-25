# Hyper Light Drifter — decyzje tłumaczenia (0.1.0)

Gra opowiada obrazem i nie ma dialogów, więc tekst to wyłącznie interfejs: 110 wpisów
menu i 16 podpowiedzi. Postaci i form zwracania się nie ma; podpowiedzi mówią do gracza
na „ty”, w trybie rozkazującym („Przytrzymaj”, „Tnij”).

## Miejsce polskiego
- **Polski zamiast włoskiego, na liście jako „POLSKI”.** Kody języków są w exe na sztywno
  (7 pozycji). Włoski ma ten sam łaciński font co angielski; rosyjski odpada, bo jego
  font rysuje cyrylicę w miejscu „ó”. Włoskiego w tej wersji nie ma.

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| dash | zryw | krótkie (pole na 11 znaków), oddaje doskok; „unik” sugerowałby samą obronę | decyzja |
| gun(s) | broń palna | gra odróżnia broń ładowaną cięciami od miecza — jak DE „Schusswaffe”, IT „arma da fuoco” | pliki gry |
| warp | teleportować się | tak robią wersje FR, ES i DE | pliki gry |
| Home (Warp Home) | dom | centralne miasto, do którego się wraca; „baza” brzmiałaby militarnie | decyzja |
| gear | wyposażenie / sprzęt | „sprzęt” tam, gdzie liczy się długość | decyzja |
| Newcomer | Nowicjusz | nazwa trybu, w zdaniach bez odmiany („w trybie Nowicjusz”) | decyzja |
| Boss Rush | Maraton bossów | opisowe, a „boss” w polskich grach zostaje | decyzja |
| Fully Loaded / Mid-Range / Naked | Pełny zestaw / Średni zestaw / Na golasa | to zestawy wyposażenia w Maratonie; FR/ES/DE przetłumaczyły „Mid-Range” jako zasięg i wyszło bez sensu | decyzja |
| achievements / trophies | osiągnięcia / trofea | terminy polskiego Steama i PlayStation | decyzja |
| co-op | kooperacja | | decyzja |
| Credits | Twórcy | krótkie, jak w polskich wydaniach | decyzja |

## Okazje wykorzystane
- „Naked” → „Na golasa”: tak samo potoczne jak oryginał, a opis pod spodem mówi wprost
  „Nic poza pistoletem”.

## Świadome odstępstwa od oryginału
- „SFX Volume / Music Volume” → „Efekty / Muzyka” — pole na 15 znaków; FR i IT też mają
  jedno słowo.
- „Minutes” → „min”: gra składa „N Minutes since last save” i nie ma form mnogich,
  a skrót pasuje do każdej liczby („2 min”, „5 min”). „Minute” → „minuta”.
- „Warp Home to change gear” → „Wróć do domu, by zmienić sprzęt” — pełne „Teleportuj się
  do domu…” było dwa razy dłuższe od oryginału.
- „Quit To Title” → „Wyjdź do menu głównego” (ekran tytułowy to w tej grze menu główne).
- Nazwy klawiszy w konfiguracji jako rzeczowniki wersalikami: CELOWANIE, LECZENIE, ZRYW,
  ZMIANA BRONI (12 znaków przy uwadze „11 chars max”; niemiecki ma tu 14).
- Font gry to same wersaliki, więc wielkość liter w tłumaczeniu nie jest widoczna.
- Bez polskich cudzysłowów i półpauz — w foncie ich nie ma (i nie są potrzebne).

## Mniej pewne (sprawdź w grze)
- **Polskie litery w ogóle** — pierwsza gra z literami w nowej sekcji exe. Jeśli w miejscu
  ą, ć, ę, ł, ń, ś, ź, ż jest pusto, a „ó” widać, runner nie przyjmuje współrzędnych poza
  prostokątem fontu. Jeśli rozsypie się cały font menu — nie przyjmuje PNG.
- Ogonki pod „ą/ę” (sięgają dwa piksele pod linię) — czy nie są ucięte w menu wyboru trybu
  („Łagodniejsze wyzwanie.”, „Mniej sprzętu, więcej wyzwania.”).
- Ustawienia: „Rodzaj zrywu” z wartościami „Za kursorem / Za ruchem”, „Tryb ekranu”
  z „Pełny ekran / Okno maks.” — najwęższe pola.
- Konfiguracja klawiszy: „ZMIANA BRONI”, „INTERAKCJA”, „Klaw.+mysz”.
- Licznik zapisu w menu wczytywania: „Mniej niż minuta / 5 min od ostatniego zapisu”.
- Pierwsze podpowiedzi w grze: leczenie („Użyj … by się uleczyć”), podnoszenie przedmiotów,
  „Tnij wrogów i przedmioty, by ładować broń palną”.

## Raport kontrolny
`work/l10n-report.md`: 11 zgłoszeń. Poprawione 1 (długość podpowiedzi o zmianie sprzętu).
Zostały fałszywe alarmy: „Standard”, „MENU”, „Reset”, „XBOX 360/ONE/PS4” identyczne
z oryginałem celowo; „Standard” / „Standardowe” to dwa różne miejsca (tryb gry i schemat
sterowania); „Celuj / Strzelaj” wielką literą, bo to osobne etykiety przy ikonach;
brak spacji na końcu „Wybierz broń w ekwipunku” — w oryginale to przypadkowa spacja.

## Niezależny przegląd (2026-09-25)
Pełny raport: `docs/localization-review.md`. Wszystkie decyzje powyżej utrzymane.
Poprawione: „Broń palna w pełni naładowana…” (brakowało „fully”) i „Odblokowano Średni
zestaw…” (spójnie z nazwą zestawu). Otwarte do decyzji użytkownika: moment wyświetlania
REMINDERGUN, „SPECJALNY”/„STRZAŁ” w konfiguracji, „Brak” dla N/A, forma trybów sterowania
i rodzaj „Wyłączona” przy kooperacji — obecny tekst zostaje do rozstrzygnięcia.
