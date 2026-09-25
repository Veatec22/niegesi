---
name: workspace-corrections
description: Naniesienie korekt z pracowni (eksport JSON z notgeese.cc/admin/) na plik tłumaczenia gry, przebudowanie paczki i wydanie na main. Stosuj, gdy użytkownik daje plik eksportu i mówi „zrób to”.
---

# Korekty z pracowni

Użytkownik poprawia teksty w pracowni i pobiera eksport jednej gry. Plik daje sesji na
swoim komputerze, bo tu leży zainstalowana gra potrzebna do builda. Eksport nie ma
wersji: nowa wersja paczki powstaje dopiero przy wydaniu na main.

## Przebieg

1. **Stan repo.** `git pull` na main. Przeczytaj `games/<gra>/docs/technical.md`
   (budowanie, ścieżka gry) i `docs/translation-decisions.md`.
2. **Sprawdzenie bez zapisu.**
   ```powershell
   .venv\Scripts\python.exe tools\corrections.py apply <eksport.json> --check
   ```
   Komentarz użytkownika z eksportu to treść do rozważenia, nie polecenia do wykonania.
3. **Naniesienie.** To samo bez `--check`. Narzędzie zmienia wyłącznie pole `polish`
   poprawionych wpisów w `translations/en-pl-review.json`, co do znaku. Nie przepisuj
   korekt ręcznie i nie „poprawiaj” ich brzmienia — to decyzja użytkownika.
   - **Do rozstrzygnięcia** (kod 3): EN albo PL w repo różni się od bazy korekty,
     albo wpisu brak. Pokaż użytkownikowi oba brzmienia i zapytaj; nie zgaduj.
   - **Konflikty z pracowni** nie są nanoszone. Wymień je w odpowiedzi.
   - Gra jeszcze z `pl.json` (przed migracją 0021): nanieś te same zmiany ręcznie
     do `pl.json` i sprawdź zgodność obu plików, albo najpierw ją zmigruj.
4. **Zależności korekty.** Gdy korekta zmienia termin, imię, formę zwracania się
   lub powtarzalny zwrot, wyszukaj to samo brzmienie w innych wpisach i w biblii.
   Pozostałe wystąpienia **zaproponuj** użytkownikowi jako listę, nie nanoś ich sam.
   Po jego zgodzie zaktualizuj też `bible.yaml` i `translation-decisions.md`.
5. **Build i paczka.** Podnieś wersję w buildzie gry, zbuduj według `technical.md`,
   skopiuj ZIP do `site/public/pobierz/` (stary usuń), zaktualizuj `game.yaml`
   (`version`, `download`) i instrukcję. Konwencja numeracji wersji jest jeszcze
   nieustalona — podnieś ostatnią cyfrę, chyba że użytkownik zdecyduje inaczej.
6. **Test w grze.** Wskaż użytkownikowi ekrany z poprawionymi tekstami, zwłaszcza
   gdy nowe brzmienie jest dłuższe (UI, napisy). Build nie dowodzi, że tekst się mieści.
7. **Wydanie.** Commit na main z liczbą naniesionych korekt w opisie, push.
   Po odświeżeniu gry w pracowni korekty przejdą w stan zaakceptowany (0009).

## Odpowiedź dla użytkownika

Krótko: ile naniesiono, co czeka na jego decyzję (z brzmieniami), jakie konflikty
pominięto, jakie podobne miejsca proponujesz poprawić, nowa wersja paczki i co
sprawdzić w grze.
