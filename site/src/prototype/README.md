# Pracownia — prototyp do wyrzucenia

Pytanie: który układ ułatwia korektę — porównanie EN/PL, czytanie rozmowy czy jedna
kwestia na ekranie — i czy szkic, zapis oraz eksport są wystarczająco rozróżnione?

Uruchom z katalogu repo: `npm --prefix site run dev`.
Otwórz `http://localhost:4321/admin/prototype/?variant=A` (port według komunikatu Astro).

- A: grupy w bocznym panelu, EN/PL w dwóch kolumnach.
- B: grupy nad tekstem, polski tekst pierwszy, rozmowa do czytania.
- C: boczne grupy i jedna kwestia na ekranie.

Warianty przełącza dolny pasek lub strzałki klawiatury poza polami tekstowymi.
Parametr `variant` przechodzi przez URL. Wszystkie warianty korzystają z tej samej pracy.

Lista 26 gier pochodzi z obecnej strony. W prototypie podłączony jest wyłącznie SCM:
485 prawdziwych wpisów z lokalnego review. Nie jest to odczyt GitHuba. Grupowanie
jest propozycją według kluczy; sekwencja Pedro według decyzji 0010, mówcy odtworzeni
z biblii, nieustalone oznaczone. Nie tworzono jeszcze produkcyjnego structure.yaml.

Sprawdź:

1. Otwórz SCM, popraw PL w Menu; użyj „Akceptuj pozostałe”. Korekta pozostaje szkicem.
2. Odśwież kartę, otwórz SCM i sprawdź szkic. „Zapisz grę” symuluje bazę lokalnie.
3. Otwórz sekwencję Pedro, przełącz warianty i tryb tylko PL.
4. „Sprawdź sytuacje” → Konflikt albo Nieaktualny szkic. Rozstrzygnij i zapisz.
5. Eksportuj JSON z komentarzem; eksport nie zmienia stanów. Szkice nie są eksportowane.
6. „Agent naniósł korekty” symuluje pojawienie się zapisanych korekt na main.
7. „Wyczyść demonstrację” resetuje tylko dane tego prototypu.

Szkice i symulacja bazy leżą w localStorage pod `notgeese:prototype:editorial:v1`.
Wyjątek od domyślnie nietrwałego prototypu: właśnie trwałość szkiców jest przedmiotem
oceny. Brak realnego logowania, Supabase, wysyłania e-maili i mutacji repo. Zapis
wszystkich pokazuje ten sam przepływ dla jednej podłączonej gry; nie dowodzi obsługi
atomowego zapisu wielu gier. Eksport jest oznaczony `prototype-local`, bez SHA main.
Nie należy go traktować jako gotowych poprawek produkcyjnych.

Trasa istnieje tylko w trybie developerskim; produkcyjny `getStaticPaths` zwraca
pustą listę. Kod do usunięcia po wyborze układu; nie przenosić go do produkcji jako
gotowej implementacji. Zgodnie z instrukcją repo nie tworzono brancha ani commita.

Werdykt: czeka na ocenę użytkownika. Decyzje i otwarte kwestie:
[specyfikacja](../../../../docs/specs/editorial-workspace.md).

## Sprawdzenie (2026-09-25)

W przeglądarce: lista 26 gier, szkic zachowany po przeładowaniu, akceptacja pozostałych
nie nadpisuje korekty, zapis demonstracyjny, pobranie JSON, oba rozstrzygnięcia
konfliktu/starego szkicu w podstawowym przepływie, warianty A/B/C. Brak błędów JS,
brak poziomego przepełnienia przy szerokości 390 px. Build Astro poprawny; brak trasy,
kodu prototypu i tekstów próbki w produkcyjnych HTML/JS/CSS. To weryfikacja prototypu,
nie test produkcyjnego backendu lub reguł RLS.

## Ocena użytkownika (2026-09-25)

Kierunek prototypu przyjęty jako punkt wyjścia. Na prośbę użytkownika wzmocniono identyfikator i wyróżnienie edytowanego wpisu, podpisy EN/PL zastąpiono flagami SVG z dostępnymi nazwami, a stany otrzymały różne etykiety: pustą, wypełnioną, z czerwonym obramowaniem i czerwoną. Szkic ma osobną przerywaną etykietę.


Doprecyzowanie: identyfikator wpisu jest wyraźnym nagłówkiem bez ramki i tła etykiety; mówca poniżej. Wartości EN/PL są pogrubione i pochylone. Co drugi wpis ma subtelne tło, a aktywny zachowuje osobne wyróżnienie.

Dalsza ocena: akceptacja tylko widocznej strony (po filtrze), 50/100/200 wpisów z zapamiętaniem wyboru, cofnięcie wszystkich niezapisanych zmian gry. Tryb redakcji obok czytania PL. Wspólne etykiety w filtrze i wpisach: do wdrożenia czarna z białym tekstem, konflikt z czerwonym obrysem i ikoną Lucide triangle-alert. Zweryfikowano zakres akceptacji, zachowanie zapisanych danych po cofnięciu, trwałość rozmiaru strony oraz widok mobilny.

Robocza interpretacja przycisku zapisz uwagę: Zatwierdź poprawkę potwierdza tekst wpisu, nie dodaje komentarza. Edycja zostaje szkicem do potwierdzenia; zapis gry blokuje niepotwierdzone szkice. Sprawdzono edycję, potwierdzenie, zapis i cofnięcie kolejnej edycji bez utraty zapisanej korekty.

Uwaga (2026-09-25, przejęcie): build produkcyjny zostawia w `dist/_astro/` osierocony
arkusz `_prototype_*.css`, bo import CSS we frontmatterze trafia do bundla mimo braku
trasy. Tylko style, bez tekstów, nieładowany przez żadną stronę. Znika razem
z usunięciem prototypu. Zdanie powyżej o braku kodu prototypu w CSS jest przez to nieścisłe.
