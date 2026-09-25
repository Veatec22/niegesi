# Rozliczanie stanu gry działa w Edge Function

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Otwarcie gry wywołuje Edge Function. Funkcja pobiera pliki gry z main (z konkretnego SHA),
stosuje reguły z [0009](0009-corrections-settle-against-main.md), zapisuje nowe stany
w jednej transakcji bazy i zwraca przeglądarce gotowy widok. Reguły rozliczania są w jednym
miejscu po stronie serwera. Karta przeglądarki zamknięta w trakcie nie zostawi stanu
rozliczonego w połowie.

## Rozważone warianty

- **Rozliczanie w przeglądarce**: odrzucone. Reguły po stronie klienta, a zapis
  wielu stanów z karty przeglądarki nie jest atomowy.
