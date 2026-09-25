# Szkice zapisuje się i odrzuca tylko w grze

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)
Zastępuje zapis „wszystkich gier” z [0009](0009-corrections-settle-against-main.md).

Lista gier działa jak zestawienie w raporcie: każda gra ma swój kafelek, a gra
z niezapisanymi szkicami jest na nim wyraźnie oznaczona wraz z ich liczbą. Informacja
pochodzi ze szkiców w tej przeglądarce, nie z bazy i nie z main. Na liście nie ma
zapisu ani odrzucania. Żeby zapisać albo porzucić szkice, użytkownik wchodzi do gry.

Zapis zawsze dotyczy jednej gry: jedna transakcja, kontrola rewizji i aktualności main,
jak w [0012](0012-reconciliation-in-edge-function.md). Nie ma pytania o atomowość wielu gier.

## Rozważone warianty

- **„Zapisz wszystkie”, osobna transakcja i wynik dla każdej gry**: odrzucone.
  Zapis bez wejścia do gry nie pokazuje kontekstu szkiców ani zmian na main.
- **„Zapisz wszystkie” jako jedna transakcja wszystko albo nic**: odrzucone. Jedna
  nieaktualna gra blokowałaby resztę, a sprawdzenie wielu gier naraz obciąża limit GitHuba.
