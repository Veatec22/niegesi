# Kierunek przed verticalem i review po fullu

Status: wdrożone w zakresie wybranym przez użytkownika — kierunek przed verticalem,
osobny reviewer całego fulla i lokalnie zapisane zasady redakcji.
Data: 2026-09-24.

Obowiązujący proces: [AGENTS.md](../../AGENTS.md),
[localization-direction](../../.claude/skills/localization-direction/SKILL.md),
[localization-review](../../.claude/skills/localization-review/SKILL.md).
Wnioski branżowe zapisano w [EDITORIAL.md](../../.claude/skills/localization/EDITORIAL.md);
artykuły są zapleczem, nie obowiązkową lekturą każdej lokalizacji.
Poniższe pomysły o narzędziach, korpusie inspiracji i pilotażu pozostają rekomendacjami;
nie wdrożono zmian skryptów ani przeglądu istniejących gier.

## Ocena obecnego procesu

Zachować kolejność: rozpoznanie dostępnych spolszczeń → analiza techniczna →
vertical potwierdzony przez użytkownika → pełne tłumaczenie → testy i paczka.
Biblia, źródła, plik EN/PL oraz ochrona decyzji użytkownika są dobrym fundamentem.
Potwierdzenie verticala dowodzi działania sprawdzonej próbki, nie kompletności
ekstrakcji ani jakości wszystkich dialogów.

Największa luka: brak osobnej redakcji językowej całych scen. Raport regexowy
nie sprawdza wierności znaczenia, podtekstu, rytmu rozmowy ani głosu postaci.

## Przyjęty przebieg

1. Po pozytywnej analizie technicznej, przed verticalem, zebrać próbkę stylu: rozmowę, tekst UI,
   opis przedmiotu i żart, jeśli występują. Nie trzeba wdrażać późniejszych scen
   w verticalu; wystarczy odczyt tekstów jako materiału referencyjnego.
2. Ustalić profil stylistyczny i przykłady głosu postaci. Przed verticalem
   pokazać użytkownikowi kilka znacząco różnych możliwości, jeśli są potrzebne.
   Rozstrzygnąć ważne wybory na konkretnych przykładach; zwykłe decyzje agent
   podejmuje sam. Następnie vertical i jego potwierdzenie przez użytkownika.
3. Tłumaczyć scenami lub spójnymi grupami funkcjonalnymi. Klucze są identyfikatorami,
   nie dowodem kolejności dialogu. Niepewną kolejność i adresata oznaczać jawnie.
4. Po fullu uruchomić kontrolę techniczną oraz osobnego reviewera całego EN/PL,
   z ponowną oceną decyzji sprzed verticala w świetle całej gry.
5. Czytać całe sceny po polsku pod kątem redakcji, następnie sprawdzić proponowane
   zmiany z oryginałem, biblią i dostępnym kontekstem.
6. Wprowadzić pewne poprawki; użytkownikowi przedstawić małą listę wartościowych
   decyzji stylistycznych. Po poprawkach zsynchronizować pl.json i EN/PL,
   ponowić kontrolę techniczną, zbudować i przeprowadzić testy w grze.

## Kontrakt reviewera

Reviewer pracuje w osobnym kontekście. Dostaje teksty EN/PL, biblię, kontekst scen,
ograniczenia techniczne i zatwierdzone decyzje. Nie potrzebuje historii argumentacji
tłumacza. Ten sam model może wykonać przegląd, ale nie oznacza to niezależności jego
błędów ani gwarancji jakości.

Trzy rodzaje wyniku:

- **Poprawione:** literówki, jednoznaczne błędy sensu lub gramatyki, potwierdzone
  rozbieżności z terminologią. Zapisać klucz, przed/po i uzasadnienie.
- **Do rozmowy:** żarty, rytm, rejestr, adaptacje i drewniane dialogi. Podać scenę,
  EN, aktualne PL, jedną rekomendację, opcjonalnie drugi wariant i koszt zmiany.
  Domyślnie najwyżej 5–10 najważniejszych tematów, bez obowiązku wypełnienia limitu.
- **Do sprawdzenia w grze:** brak adresata, niepewny ton nagrania, limit pola,
  synchronizacja napisów. Wskazać konkretną scenę i sposób rozstrzygnięcia.

Brak obowiązku znajdowania błędów. Każda zmiana wymaga konkretnego powodu.
Nie wygładzać celowej niezręczności, nie dopisywać lore, nie wzmacniać dowcipów
kosztem charakterystyki postaci. Chronić zaakceptowane i odrzucone warianty
użytkownika. Nie przepisywać całego pliku, gdy wystarczy mały zestaw zmian.

## Małe usprawnienia obecnych narzędzi i reguł

- l10n_report.py czyta tylko EN/PL: sam nie dowodzi zgodności z pl.json ani
  kompletności względem ekstrakcji. Sprawdzać to w odpowiednim narzędziu gry.
- Raport pokazuje domyślnie 80 zgłoszeń na sekcję, a tekst skraca do 140 znaków.
  Nadaje się do wskazywania miejsc; pełny przegląd wymaga oryginalnych wpisów.
- Porównanie zbiorów tokenów nie sprawdza ich zagnieżdżenia ani znaczenia.
  Walidację składni dopasować do formatu konkretnej gry.
- Pole max_wiersz w biblii nie jest obecnie używane przez raport. Długość jest
  szacowana relacją PL/EN, a nie rzeczywistym łamaniem napisów.
- Limity Netflixa traktować jako punkt odniesienia dla napisów, nie uniwersalną
  specyfikację gier. Wymiary pola, font, czas wyświetlania i gameplay są rozstrzygające.
- Płeć aktora nie ustala płci postaci; inne lokalizacje są poszlaką, nie dowodem.
- docs/adding-a-game.md nadal opisuje ogólny build przez podmianę i SHA-256.
  Doprecyzować zakres tych reguł względem domyślnej metody pluginowej w AGENTS.md.

## Uczenie się z istniejących polskich lokalizacji

Zbudować mały zbiór przypadków, nie wielką bazę gotowych zamienników. Dla każdego:
gra i wersja, autorzy lokalizacji jeśli znani, scena/klucz/timecode, źródło i kierunek
tłumaczenia, krótki przykład EN/PL, funkcja wypowiedzi, technika adaptacji,
zysk, utrata i warunki stosowania. Oddzielić obserwację od przypisywania intencji
tłumaczowi; tej ostatniej nie znamy bez jego komentarza.

Porównywać tę samą scenę i wariant fabularny. Gry napisanej pierwotnie po polsku
nie przedstawiać jako przykładu tłumaczenia EN→PL; nadal może być wzorcem dialogu.
Analizować też rozwiązania nieudane. Oficjalne wydanie nie jest automatycznie normą.
W repo zachowywać przede wszystkim własne wnioski i odnośniki; pełnych cudzych
tabel nie dodawać. Wynikiem mają być techniki z własnymi przykładami, nie gotowe
cudze kwestie do używania w następnych grach.

## Pilotaż i kryterium wartości

Zacząć od jednej gry: 100–200 kwestii obejmujących kilka pełnych scen i trochę UI.
Porównać wersję przed i po review. Zapisać poprawione błędy, zaakceptowane propozycje,
odrzucone zmiany, regresje i czas użytkownika poświęcony na decyzje.
Osobno śledzić pokrycie: przejrzane wpisy/sceny oraz sprawdzone ekrany w grze.
Nie utożsamiać liczby zmian ani oceny wystawionej przez LLM z jakością.

Materiały branżowe: [notatka źródłowa](../localization-research.md).
