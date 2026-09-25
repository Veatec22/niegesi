---
name: localization-direction
description: Ustal kierunek polskiej lokalizacji gry przed verticalem, po pozytywnej analizie technicznej. Przygotuj próbkę EN/PL i omów z użytkownikiem istotne decyzje o tonie, głosach postaci i terminach; zapisz ustalenia dla tłumacza i reviewera.
---

# Kierunek lokalizacji przed verticalem

Cel: użytkownik ma zobaczyć konkretne możliwości językowe, zanim zaczniesz vertical
i utrwalisz styl w pełnym tłumaczeniu. To mała próba redakcyjna na tekstach gry,
nie build ani techniczne potwierdzenie verticala.

## Przygotuj propozycję

1. Przeczytaj `games/<gra>/docs/technical.md`, istniejącą biblię i decyzje.
   Zachowaj uzgodnienia z wcześniejszych rozmów; nie pytaj o nie ponownie.
2. Przeczytaj [zasady redakcji](../localization/EDITORIAL.md). Zbierz z ekstrakcji
   krótką, spójną wymianę dialogową oraz przykłady menu/ustawień, instrukcji i opisów,
   o ile występują. Zwykle wystarczy 10–20 wpisów. Dobierz materiał pokazujący
   rzeczywisty wybór: humor, formalność, nazwy mówiące, kontrast postaci.
   Nie twórz dialogów, których nie ma w grze. Gdy materiał jest skąpy, nazwij ograniczenie.
3. Zachowaj klucze, kontekst i pełne EN. Ustal mówiącego, adresata oraz kolejność
   tam, gdzie są dowody; samo sortowanie kluczy nie odtwarza sceny. Późniejsze teksty
   mogą pomóc ocenić ton, ale nie zdradzaj użytkownikowi fabuły bez potrzeby.
4. Przygotuj rekomendowane PL i tylko tam, gdzie wybór ma znaczenie, alternatywę.
   Opisz po polsku, co zmienia wariant: dystans między postaciami, dosadność, rytm,
   czytelność mechaniki albo skojarzenie nazwy. Nie przedstawiaj błędnego przekładu
   jako równorzędnego wariantu gustu.

## Rozmowa i zapis

Zapisz próbkę i propozycje w `games/<gra>/docs/translation-decisions.md`, w sekcji
„Przed verticalem”. Dla każdego tematu podaj klucze/scenę, EN, rekomendację PL,
ewentualny wariant, uzasadnienie i status: **propozycja**, **decyzja agenta** lub
**uzgodnione z użytkownikiem**. Zwykle wystarczą 3–5 tematów, bez sztucznego minimum.
Nie wpisuj wariantów jako obowiązujących tłumaczeń do pliku tłumaczenia (`en-pl-review.json`).

Przedstaw użytkownikowi tę konkretną próbkę i zapytaj o istotne wybory przed verticalem.
Nie rób ankiety o każdą nazwę czy przecinek. Jeśli wcześniejsze ustalenia wystarczają
albo nie ma znaczących wariantów, opisz przyjęty kierunek i przejdź dalej.
Jeśli postawiłeś pytanie o kierunek, poczekaj na odpowiedź przed zależnym tłumaczeniem;
w tym czasie można kontynuować niezależne przygotowanie techniczne. Milczenie
nie zmienia propozycji w uzgodnienie. Gdy użytkownik zleca wybór agentowi, zdecyduj.

Po odpowiedzi uzupełnij `translations/bible.yaml` według
[formatu biblii](../localization/BIBLE.md): ton gry, głosy postaci z przykładami,
terminy, granice adaptacji i odrzucone warianty. `zrodlo: uzytkownik` stosuj tylko
do faktycznych ustaleń użytkownika, nie do własnych propozycji. Resztę oznacz
jako decyzję agenta lub nieustalony fakt wymagający kontekstu.

Przekaż kierunek do [skilla tłumaczenia](../localization/SKILL.md) i wykonaj vertical
obejmujący menu, ustawienia i początek gry zgodnie z AGENTS.md. Pełne tłumaczenie
nadal wymaga potwierdzenia działania verticala przez użytkownika.

## Granice

- Nie wymuszaj rozbudowanej biblii dla gry z kilkoma napisami i bez dialogów.
- Próbka ustala punkt wyjścia. Po fullu reviewer ponownie oceni decyzje na całości.
- Zasady branżowe są już w `EDITORIAL.md`; nie czytaj całej bibliografii przy każdej
  grze. Sięgaj do źródeł, gdy potrzebujesz rozstrzygnąć konkretną niepewność.
