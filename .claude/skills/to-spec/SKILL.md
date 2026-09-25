---
name: to-spec
description: Zamień dotychczasową rozmowę (zwykle po grillowaniu) w specyfikację w docs/specs/. Bez przepytywania — sama synteza tego, co już ustalono.
disable-model-invocation: true
---

# Specyfikacja z rozmowy

Adaptacja `to-spec` z [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).
Nie mamy issue trackera, więc specyfikacja trafia do pliku `docs/specs/<slug>.md`.

Nie przepytuj użytkownika. Zsyntetyzuj to, co już wiesz z rozmowy, repo, słownika
(`docs/glossary.md`) i decyzji (`docs/decisions/`). Używaj pojęć ze słownika
i nie łam przyjętych decyzji. Jeśli czegoś brakuje, wpisz to jako otwartą kwestię,
nie zgaduj.

## Kroki

1. Przeczytaj słownik, decyzje tematu i odpowiednie miejsca w kodzie.
2. Wyznacz **szwy testowe**: miejsca, w których sprawdzimy zachowanie z zewnątrz.
   Preferuj istniejące, możliwie wysoko i możliwie mało. Potwierdź je z użytkownikiem
   jednym pytaniem, zanim napiszesz resztę.
3. Napisz specyfikację według szablonu i podlinkuj ją z dokumentu tematu w `docs/decisions/`.

## Szablon

```md
# <Tytuł>

Status: gotowa do realizacji · Data: RRRR-MM-DD · Decyzje: <linki>

## Problem
<Z perspektywy użytkownika.>

## Rozwiązanie
<Z perspektywy użytkownika.>

## Historie użytkownika
<Długa, numerowana lista: „Jako <kto> chcę <co>, żeby <po co>”. Pokryj wszystkie
aspekty, łącznie z błędami, konfliktami i przypadkami brzegowymi.>

## Decyzje wykonawcze
<Moduły do zbudowania lub zmiany i ich interfejsy, model danych, kontrakty API
i formaty plików wymiany, konkretne interakcje. Bez ścieżek plików i fragmentów kodu —
szybko się starzeją. Wyjątek: kształt danych lub maszyna stanów z prototypu, jeśli
opisuje decyzję dokładniej niż proza.>

## Testy
<Co jest dobrym testem (zachowanie z zewnątrz, nie implementacja), które moduły,
na jakich prawdziwych danych gier, wzorce z repo.>

## Poza zakresem

## Otwarte kwestie
```
