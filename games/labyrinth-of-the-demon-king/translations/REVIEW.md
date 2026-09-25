# Labyrinth of the Demon King — korekta pełnego przekładu

1120/1120 wpisów lokalizacji, wersja 0.2. Użytkownik potwierdził vertical
i zlecił pełny przekład. Pełna kampania nie została jeszcze sprawdzona wizualnie.

Otwórz `en-pl-review.html` w przeglądarce: wyszukiwanie działa po EN, PL,
identyfikatorze i uwagach. Filtr „Tylko z uwagami” wyodrębnia miejsca do oceny.
Źródłem jest `en-pl-review.json` — jedyny plik tłumaczenia (decyzja 0021). Korekty
z pracowni nanosi `tools/corrections.py`, potem `tools/review.py` i `tools/build.py`.

## Terminologia

| EN | PL |
| --- | --- |
| Demon King | Król Demonów |
| Labyrinth | Labirynt |
| Warden / Jailer | Strażnik / Dozorca |
| Tower of Repetition | Wieża Powtórzeń |
| Tower of Crushing Assembly | Wieża Miażdżenia |
| Tower of Lamentation | Wieża Lamentu |
| Tower of No Interval | Wieża Nieustającej Męki |
| Hell of… | Piekło… (spójnie z nazwą wieży) |
| King's Court | Królewski Sąd |
| guard / parry | garda / parowanie |
| blunt / slash / pierce | obuchowe / cięte / kłute |
| rot / poison / bleed | zgnilizna / trucizna / krwawienie |
| Bloodletter | Krwawnik |
| Chrysanthemum Blade | Ostrze Chryzantemy |
| Ritual / Purifying Incense | kadzidło rytualne / oczyszczające |
| Gem Wheel | koło z klejnotem (kolor zgodny z opisem) |
| butsudan / shirikodama / mon | zachowane terminy świata gry |

Nazwy broni japońskich i istot pozostają rozpoznawalne. Dialogi kappy są
potoczne; kapłana — spokojniejsze; współczesne listy zachowują wulgarny rejestr.
Głos głównego bohatera jest męski. Służąca i kocia handlarka mówią w rodzaju
żeńskim na podstawie kontekstu. Locres nie zawiera podpisów mówców; niepewne
przypisania oznaczono w review do sprawdzenia w grze.

## Priorytety korekty

- **Zagadki:** pierwszeństwo mają sens, kierunki, liczby i kolejność. Zeznania
  Królewskiego Sądu nie udają rymowanego wiersza kosztem wskazówek.
- **Łączone komunikaty:** `There is…` przyjmuje formę `Znajdujesz: `,
  aby nazwa przedmiotu mogła pozostać w mianowniku. Zachowano końcowe spacje.
- **Źródłowe duplikaty:** osiem wpisów powtarzało zdanie o zamkniętych drzwiach
  dwa razy w jednym tekście. PL zawiera jedno zdanie; oznaczono to w review.
- **Cons.:** skrót roboczo przetłumaczony jako „Zużyw.” — potrzebny kontekst UI.
- **Osiągnięcia:** część dowcipów zaadaptowano swobodniej. Do oceny przy obrazie
  i opisie konkretnego osiągnięcia. Teksty klientów Steam/GOG są poza paczką.

Znaczniki, placeholdery i liczby podziałów CRLF weryfikuje build. Identyfikatory
oraz hashe źródłowe locres pochodzą z gry; nietłumaczone nowe wpisy po aktualizacji
mogą pozostać angielskie. Nie oznacza to uszkodzenia pozostałego przekładu.
