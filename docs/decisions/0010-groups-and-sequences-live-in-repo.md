# Grupy i sekwencje są zapisane w repo

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Podział na grupy i sekwencje każdej gry leży w repo, w pliku obok tłumaczeń. Są tam reguły
według prefiksów kluczy, ręczne przypisania i sekwencje z mówcami. Przygotowuje go agent,
a pracownia go czyta. Pierwsza wersja pracowni nie przenosi wpisów
między grupami ([0018](0018-no-group-moves-in-first-version.md)); zmiany podziału robi agent w repo. Uporządkowanie przetrwa
utratę bazy, a agent przy dotłumaczeniu wie, do której rozmowy należy nowa kwestia.

## Format

`translations/structure.yaml`. Poniżej pierwotny szkic; obowiązujący format opisuje
[specyfikacja](../specs/editorial-workspace.md#plik-struktury), wzór w Shotgun Cop Manie:

```yaml
groups:
  - id: menu
    name: Menu
    match: ['^m[A-Z]']
  - id: dialogi
    name: Dialogi
    match: ['^pSpeech', '^satanSpeech', '^PedroDLCSpeech']
sequences:
  - id: pedro-dlc
    name: Spotkanie z Pedro
    group: dialogi
    order: pewna          # z numeracji kluczy
    speakers: odtworzone  # z treści, nie z gry
    lines:
      - [PedroDLCSpeech1, bohater]
      - [PedroDLCSpeech2, pedro]
```

Wpis trafia do pierwszej pasującej grupy. Wpis bez dopasowania trafia do grupy
„Do uporządkowania”, a gra bez pliku struktury ma wszystkie wpisy w jednej grupie,
w kolejności pliku. Mówcy odwołują się do postaci z `bible.yaml`. Sekwencja to tylko
prawdziwa rozmowa: okrzyki bohatera w SCM (`pSpeech0–11`) nią nie są.

## Rozważone warianty

- **Grupy tylko w Supabase, edytowane w panelu**: odrzucone. Łamie 0005, a agent
  nie widziałby struktury.
