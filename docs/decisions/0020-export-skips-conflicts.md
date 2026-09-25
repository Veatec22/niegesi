# Eksport pomija konflikty i wypisuje je osobno

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Konflikt w grze nie blokuje eksportu. Lista `corrections` zawiera wyłącznie korekty
do wdrożenia, czyli gotowe do naniesienia. Wpisy w konflikcie trafiają do osobnej listy
`conflicts` z EN i PL zapisanymi w pracowni oraz z EN i PL z main, żeby agent i użytkownik
widzieli, czego eksport nie obejmuje. Agent niczego z tej listy nie nanosi.
Okno eksportu pokazuje liczbę pominiętych konfliktów przed pobraniem.

Wyniki pracy bez wpisu na main ([0017](0017-removed-entries-kept-for-manual-cleanup.md))
nie trafiają do żadnej z list.

## Rozważone warianty

- **Blokada eksportu całej gry do rozstrzygnięcia konfliktów** (wariant prototypu):
  odrzucone. Jeden sporny wpis wstrzymywałby naniesienie wszystkich gotowych korekt.
