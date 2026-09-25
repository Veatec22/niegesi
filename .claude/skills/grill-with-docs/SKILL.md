---
name: grill-with-docs
description: Bezlitosne przepytywanie użytkownika z planu lub projektu, aż do wspólnego zrozumienia, z zapisem słownika pojęć i decyzji architektonicznych na bieżąco. Używaj, gdy użytkownik chce przegrillować pomysł, projekt narzędzia albo sposób pracy.
disable-model-invocation: true
---

# Grillowanie z dokumentacją

Adaptacja `grilling` + `domain-modeling` z [mattpocock/skills](https://github.com/mattpocock/skills)
(MIT) do Not Geese: po polsku, decyzje w `docs/decisions/`, słownik w `docs/glossary.md`.

## Drzewo decyzji

Przepytuj użytkownika, aż dojdziecie do wspólnego zrozumienia. Traktuj temat jak
**drzewo decyzji**: każda decyzja otwiera decyzje, które od niej zależą.

Pracuj w **rundach**. **Front** to decyzje, których warunki wstępne są już rozstrzygnięte —
pytania, które możesz zadać teraz, bez zgadywania odpowiedzi na inne. W jednej rundzie
zadaj cały front: ponumeruj pytania i przy każdym daj swoją rekomendację. Potem czekaj.

```
❓ **P1. <tytuł>**: <treść, warianty, konkretny przykład z repo lub gry>

➡️ <rekomendacja i jednozdaniowe uzasadnienie>

---

❓ **P2. <tytuł>**: …
```

Pytanie zależne od innego pytania z tej samej rundy należy do następnej rundy.
Po odpowiedziach przelicz front. Pokaż krótko, co zamknięto i co się odblokowało.

Rundy trzymaj na 3–6 pytań. Jeśli front jest większy, zacznij od decyzji, które
najwięcej odblokowują albo najtrudniej je odwrócić.

## Fakty zbierasz sam, decyzje należą do użytkownika

Jeśli pytanie wymaga faktu z repo, plików gry, dokumentacji albo cudzego kodu — ustal go
sam albo przez subagenta. Nie pytaj o to, co możesz sprawdzić. Trwające rozpoznanie
blokuje tylko pytania od niego zależne; resztę frontu zadawaj od razu.

Decyzje przedstawiaj użytkownikowi i czekaj. Brak odpowiedzi na pytanie to nie akceptacja
rekomendacji — pytanie zostaje otwarte. Nie odpowiadaj za użytkownika.

## Język pojęć

Czytaj `docs/glossary.md`, jeśli istnieje. W trakcie rozmowy:

- **Konfrontuj ze słownikiem.** Gdy użytkownik używa pojęcia inaczej niż słownik —
  powiedz to od razu: „Słownik mówi, że *wpis* to X, a ty chyba masz na myśli Y”.
- **Wyostrzaj rozmyte słowa.** „Tekst”, „linijka”, „kwestia”, „string” — zaproponuj jedno
  pojęcie i nazwij, czym różni się od sąsiednich.
- **Testuj scenariuszami.** Wymyślaj konkretne przypadki brzegowe na prawdziwych grach:
  aktualizacja gry zmienia EN, ten sam klucz w dwóch rozmowach, poprawka w panelu
  i jednocześnie w repo.
- **Sprawdzaj z kodem.** Gdy użytkownik mówi, jak coś działa, zweryfikuj w repo.
  Rozbieżność pokaż wprost.

Gdy pojęcie się ustali, dopisz je od razu do `docs/glossary.md` według
[GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md). Nie zbieraj na koniec. Słownik zawiera tylko
pojęcia — bez implementacji, bez decyzji, bez notatek.

## Decyzje

Zapisuj decyzję w `docs/decisions/` według [ADR-FORMAT.md](ADR-FORMAT.md) tylko wtedy,
gdy spełnia wszystkie trzy warunki:

1. **Trudno ją odwrócić** — zmiana zdania później realnie kosztuje.
2. **Zaskoczy bez kontekstu** — przyszły czytelnik zapyta „czemu tak?”.
3. **Wynika z prawdziwego wyboru** — były sensowne alternatywy.

Drobiazgi rozstrzygnięte w rundzie zostają w rozmowie i w końcowym podsumowaniu.
Zanim zaproponujesz decyzję, przeczytaj istniejące pliki w `docs/decisions/` — nie wracaj
do odrzuconych wariantów bez nowego argumentu, a jeśli masz nowy, powiedz, co się zmieniło.

Decyzję zapisuj po jawnym „tak” użytkownika, nie po własnej rekomendacji.

## Koniec

Sesja kończy się, gdy front jest pusty: każda gałąź odwiedzona, nic nie założone po cichu.
Wtedy podsumuj: zapisane decyzje (z linkami), nowe pojęcia, pozostałe otwarte kwestie,
i zapytaj, czy doszliście do wspólnego zrozumienia. Nic nie wdrażaj przed potwierdzeniem.
Następnym krokiem zwykle jest `/to-spec`.
