---
name: localization-review
description: Niezależny przegląd całej polskiej lokalizacji po fullu. Sprawdź sens EN/PL, zredaguj dialogi i ponownie oceń decyzje sprzed verticala na podstawie całej gry. Oddziel pewne poprawki od wariantów do rozmowy; nie zastępuje testu w grze.
---

# Reviewer po pełnym tłumaczeniu

To osobny przegląd wszystkich tekstów objętych full, nie ponowne obejrzenie próbki.
Przeczytaj [zasady redakcji](../localization/EDITORIAL.md) i
[pułapki polszczyzny](../localization/PITFALLS.md).

## Uruchomienie i odpowiedzialność

Agent prowadzący uruchamia osobnego subagenta w świeżym kontekście (bez historii
tłumaczenia; jeśli narzędzie udostępnia `fork_turns`, wybierz `none`). Przekazuje:

- ten skill, katalog gry i zakres pełnego tłumaczenia;
- kompletny plik tłumaczenia `en-pl-review.json` (w starszych grach także `pl.json`), biblię i `docs/translation-decisions.md`;
- kontekst scen, materiały gry i ograniczenia z `docs/technical.md`;
- wynik aktualnego `l10n_report.py`, jako wskazówki, nie zastępstwo tekstów.

Reviewer pracuje tylko do odczytu i zwraca ustalenia agentowi prowadzącemu;
nie uruchamia kolejnego reviewera ani nie zapisuje tłumaczeń równolegle z nim.
Agent prowadzący zapisuje wynik, nanosi poprawki i prowadzi rozmowę z użytkownikiem.
Bez dostępnego subagenta nazwij brak niezależnego przeglądu; własnego rereadu
nie przedstawiaj jako ukończonego review przez osobnego agenta.

## Pełny zakres

Na początku ustal liczbę i identyfikatory wpisów do sprawdzenia, korzystając
z istniejącego formatu gry (np. `table` + `term`, nie zawsze samo `key`). Porównaj
EN/PL z dostępną ekstrakcją (i z `pl.json`, jeśli gra go jeszcze ma); zgłoś braki i rozjazdy zamiast zgadywać,
która wersja jest aktualna. Nie zmieniaj wspólnych formatów na potrzeby przeglądu.

Czytaj pełne wpisy, scenami i grupami funkcjonalnymi. Duży materiał podziel na
partie i zapisuj pokrycie kluczy/scen, żeby móc wznowić przegląd bez luk. Sam raport
automatyczny ma limity wyświetlania i skraca teksty. Nie pozwala zadeklarować całości.
Po partiach wykonaj syntezę terminów, głosów postaci i decyzji dla całej gry.
Brak kontekstu nie oznacza błędu: oznacz wpis jako przeczytany, ale nierozstrzygnięty.

## Dwa przebiegi i ponowna ocena decyzji

1. **Wierność i poprawność.** Sprawdź sens, negacje, warunki, ilości, pominięcia,
   dopiski, referencje do postaci, rodzaj, adresata, terminy i składnię znaczników.
   Kontroluj instrukcje mechanik równie uważnie jak dialogi. Raport regexowy jest
   pomocą; nie rozumie znaczenia ani wszystkich formatów placeholderów.
2. **Redakcja.** Przeczytaj scenę po polsku bez ciągłego podglądania EN; oceń rytm,
   riposty, podtekst i głosy postaci. Każdą proponowaną zmianę sprawdź potem z EN,
   kontekstem i biblią. Krótsza albo bardziej ozdobna kwestia nie jest z definicji lepsza.
3. **Decyzje na całości.** Wróć do każdego istotnego ustalenia sprzed verticala:
   tonu, nazw, terminów, relacji i stopnia adaptacji. Czy późniejsze sceny je
   potwierdzają? Czy termin nie ma innego znaczenia, a głos postaci nie został
   nadmiernie uproszczony? Daj werdykt: **utrzymać**, **proponowana zmiana** albo
   **brak kontekstu**, z kluczami/przykładami i zakresem konsekwencji.

Pewne błędy można poprawić automatycznie tylko przy konkretnym uzasadnieniu.
Wariant stylistyczny albo niepewna interpretacja trafia do rozmowy. Ustaleń
użytkownika nie nadpisuj. Możesz ponownie otworzyć taki temat, jeśli pełna gra
dostarczyła nowych dowodów lub wyraźnego problemu: pokaż wcześniejszy wybór,
nową przesłankę i rekomendację. Sam inny gust nie uzasadnia powrotu do odrzuconego wariantu.

## Wynik i domknięcie przez agenta prowadzącego

Zapisz `games/<gra>/docs/localization-review.md`:

- **Zakres:** data i identyfikacja sprawdzonych tekstów (np. SHA-256 plików wejściowych),
  liczba wszystkich/przeczytanych wpisów, partie/sceny i luki. Przy dużej grze manifest
  pokrycia może leżeć w `work/`; w raporcie podsumuj wynik i pozostałe ograniczenia.
- **Błędy:** klucz, EN, obecne PL, poprawione PL, przesłanka i status
  (proponowane / wprowadzone / odrzucone z uzasadnieniem). Reviewer nie deklaruje
  wprowadzenia zmian, których agent prowadzący jeszcze nie wykonał.
- **Decyzje sprzed verticala:** werdykty z poprzedniej sekcji, także decyzje utrzymane.
- **Do rozmowy:** scena/klucze, EN, aktualne PL, rekomendacja, opcjonalnie drugi
  wariant, zysk i koszt. Zgrupuj powtarzalne problemy. W rozmowie pokaż zwykle
  5–10 najważniejszych tematów; ten limit nie ogranicza zakresu przeglądu ani raportu.
- **Do sprawdzenia w grze:** konkretne sceny/ekrany i co ma rozstrzygnąć test.

Agent prowadzący weryfikuje przesłanki i nanosi pewne poprawki do pliku tłumaczenia.
Przedstawia użytkownikowi warianty stylistyczne i oczekuje na rozstrzygnięcie zmian,
których nie zlecono mu wybierać samodzielnie. Do tego czasu zostawia obecny tekst.
Nie musi wstrzymywać niezależnych poprawek ani technicznego builda.
Wybory i odrzucenia aktualizują biblię oraz `docs/translation-decisions.md`.

Po integracji ponownie sprawdź zmienione kwestie i ich zależności, zgodność plików,
tokeny i raport kontrolny; użyj istniejących walidatorów/builda gry. Zmiana globalnego
terminu lub głosu postaci wymaga sprawdzenia wszystkich dotkniętych wystąpień/scen.
Zapisz zakres ponownej kontroli oraz stan po poprawkach. Nie zapętlaj pełnych rewrite'ów.
Raport bez nierozpatrzonych partii może kończyć etap czytania, lecz otwarte propozycje
i brak testu w grze nadal muszą być jawne przy [oddaniu](../localization/HANDOFF.md).
