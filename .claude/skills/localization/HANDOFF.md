# Oddanie tłumaczenia — podsumowanie decyzji

Plik: `games/<gra>/docs/translation-decisions.md`. W odpowiedzi do użytkownika
dajesz skrót tego samego. Ten dokument powstaje już przed verticalem i jest
aktualizowany po fullu; nie nadpisuj historii ustaleń nowym szablonem.
Oddziel decyzje agenta, uzgodnienia użytkownika i propozycje oczekujące na rozmowę.
Nie proś ponownie o akceptację rozstrzygniętych punktów.

Pisz konkretnie: co wybrano, dlaczego i skąd to wiadomo. Pomiń oczywistości
(„przetłumaczono menu”). Każdy punkt ma być czymś, co użytkownik może
zakwestionować jednym zdaniem.

## Szablon

```markdown
# <Gra> — decyzje tłumaczenia (<wersja>)

## Postacie
- **SYN — forma żeńska, nazwa nieodmienna.** Głos: Patricia Summersett (obsada),
  „protect your mother” w kwestiach SYN. Dotyczy 60 kwestii i opisów w infodeksie.

## Terminy
| EN | PL | Dlaczego | Źródło |
| --- | --- | --- | --- |
| biocore | biordzeń | jeden wyraz, łatwy do odmiany, zgodny z „rdzeń” | decyzja |

## Okazje wykorzystane
- Gra słów SYN/sin: „to macie tu syna skurwysyna!” (TurboVoices 295).

## Świadome odstępstwa od oryginału
- Ręcznie łamane wiersze w nagraniach połączone — pole zawija samo.

## Mniej pewne (sprawdź w grze)
- Napisy w finale epizodu 3 — najdłuższe kwestie, możliwe ucięcie.

## Review po fullu
Odnośnik do `docs/localization-review.md`: zakres przejrzanego tekstu, luki,
wprowadzone poprawki i ponowna ocena kierunku sprzed verticala.
Oddziel ukończenie przeglądu językowego od statusu testu w grze.

## Do rozmowy
Tylko nierozstrzygnięte propozycje: scena/klucze, EN, obecne PL, rekomendacja,
korzyść i koszt zmiany. Po odpowiedzi przenieś wynik do decyzji i biblii.

## Raport kontrolny
Stan `work/l10n-report.md`: ile zgłoszeń w każdej sekcji, ile poprawiono,
jakie klasy fałszywych alarmów zostały i dlaczego.
```

Kolejność sekcji dowolna; pomijaj puste. Najważniejsza jest sekcja
„Mniej pewne” — prowadzi test użytkownika do miejsc, gdzie ryzyko jest największe.
