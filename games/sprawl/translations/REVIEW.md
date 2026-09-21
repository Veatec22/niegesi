# Uwagi do korekty SPRAWL 0.2

717/717 wpisów otrzymało polską wersję. Plik `en-pl-review.json` zawiera dokładny
angielski oryginał i polski tekst, a `en-pl-review.html` daje podgląd z wyszukiwaniem.
HTML jest tylko do czytania: poprawki wprowadzamy równolegle w `pl.json` i JSON-ie
do review, a potem odświeżamy HTML przez `tools/review.py`.

## Terminologia

- SEVEN, SIX, FIVE i pozostałe kryptonimy zostają po angielsku. Do SEVEN zwracamy
  się w rodzaju żeńskim, do SIX w męskim.
- Father → Ojciec; Reaper → Żniwiarz; Spire → Iglica; Walled City → Miasto za Murem;
  Dark City → Ciemne Miasto; Badlands → Pustkowia; Bullet Time → spowolnienie czasu.
- SPRAWL, AEON, NCO, ICARUS, nazwy producentów i oznaczenia modeli broni pozostają
  nazwami własnymi. Ghost, Spectre i O.H.G.R pozostają oznaczeniami klas jednostek.
- Wpisy Mother mają żeńską narratorkę; Pythia → Pytia. Ich urywane zdania, powtórzenia
  i wtrącenia zakłóceń są celowe. Nie należy wygładzać ich jak zwykłych opisów.
- Raporty zachowują wielkie litery, rozmowy hakerów potoczność i przekleństwa.
  Znaczniki kolorów, migotania i ikon przycisków muszą pozostać nienaruszone.

## Miejsca warte szczególnej uwagi

- `Tutorials/E1M1_COMBAT_10_BODY`: „overkill” opisuje szczególny sposób zabicia
  przeciwnika; przyjęto „doszczętnie zniszczyć”, bez sugerowania osobnego przycisku.
- `UIStringTable/LEVEL_E1M4_NAME`: „Ghost Wetware” → „Biologiczne widmo”; tytuł jest
  interpretacyjny. „SEVERED STEEL” zostaje jako nazwa nawiązująca do innej gry.
- `UIStringTable/LEVEL_E1M2_NAME` i `E1M2_FLAVOUR` / `E1M3_FLAVOUR`: oryginał używa
  zarówno Club Simulacra, jak i Klub Null. Zachowano tę różnicę zamiast zmieniać lore.
- W uszkodzonych transmisjach pozostają łacińskie zdania oraz ciągi kodów.
  To zamierzone elementy źródła, podobnie jak `ß` w adresie połączenia kodeksu.
- Długie wpisy kodeksu, opisy poziomów i ustawień wymagają sprawdzenia w grze pod
  kątem przewijania, łamania wierszy i czytelności. Walidacja plików tego nie potwierdza.

Selektor, polska flaga, zapamiętywanie wyboru oraz próbka początku gry zostały
potwierdzone przez użytkownika. Pełna kampania nie została jeszcze przetestowana.
