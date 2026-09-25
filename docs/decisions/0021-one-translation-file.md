# Jeden plik tłumaczenia na grę: en-pl-review.json

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)
Zastępuje [0015](0015-unify-pl-json-too.md).

Każda gra trzyma polskie teksty w jednym pliku: `translations/en-pl-review.json`
w formacie [0013](0013-one-review-file-format.md). `pl.json` znika z repo. Buildy czytają
review przez wspólne `tools/translations.py`; jeśli paczka potrzebuje płaskiej mapy
(np. `pl.json` obok pluginu), build tworzy ją w `dist/`, nie w repo. Eksport pracowni
nanosi się na ten jeden plik.

Powód: dwa pliki z tym samym polskim tekstem rozjeżdżały się (Laika: 3 wpisy
z innym brzmieniem w review niż w paczce), a panel pokazuje review. Review było
śledzeniem zmian w gicie; tę rolę przejęła pracownia. Review ma wszystko, co `pl.json`,
oraz EN, kontekst i uwagi, a część buildów już z niego czytała.

Migracja gry: mapa zbudowana z review musi być identyczna z dotychczasowym `pl.json`
(te same pary w tej samej kolejności), dopiero wtedy `pl.json` znika. Wejście builda
się nie zmienia, więc i wynik — sprawdzalne bez plików gry. Rozjazdy wyrównuje się
przed migracją na korzyść pliku, z którego zbudowano wydaną paczkę.

Stan 2026-09-25: wszystkie 26 gier zmigrowane. Po drodze: Laika przejęła w review
3 brzmienia z `pl.json`; Boomerang X ma jeden wpis dla dwóch wierszy tabeli z tym samym
kluczem; z review wypadły puste wiersze gier (bez EN i PL: OTXO 104, Wild Bastards 117,
Turbo Overkill 17, Void Bastards 4, Anger Foot 2), których build nie używał; Dread
Templar ma wpis na pole (`klucz/text`, `klucz/name`); Heat Signature trzyma w review
też gramatykę nazw przedmiotów (dawne `items.json`, rodzaj w polu `gender`), a partie
`parts/` zniknęły. Buildy sprawdzono na plikach (wejście równe dawnemu `pl.json`),
bez gier; pierwsza przebudowa każdej paczki jest zarazem testem.

Płaski identyfikator dla niepustego namespace przestaje być formatem repo; to sprawa
wewnętrzna builda danej gry (otwarta kwestia 6 specyfikacji odpada).

## Rozważone warianty

- **Ujednolicić `pl.json` do płaskiej mapy i trzymać oba pliki (0015)**: odrzucone.
  Nadal dwa miejsca na ten sam tekst i narzędzie, które musi pilnować ich zgodności.
- **Zostawić `pl.json`, a review generować**: odrzucone. Panel potrzebuje EN, kontekstu
  i uwag, których `pl.json` nie ma, więc źródłem i tak byłby plik z tymi polami.
