# Pracownia czyta stan gry prosto z main

Status: przyjęte · Data: 2026-09-25 · Temat: [pracownia korekty](0003-editorial-workspace.md)

Repo jest publiczne, więc pracownia pobiera teksty gry z gałęzi main na GitHubie bez
tokena i bez importu przez użytkownika. Najpierw ustala SHA ostatniego commita, a pliki
czyta z tego konkretnego commita, więc cache GitHuba nie pomiesza stanów. Pracownia tylko
czyta z GitHuba, nigdy do niego nie pisze. Widzi wyłącznie to, co wypchnięto na main.
Lokalne i niewypchnięte zmiany są dla niej niewidoczne.

## Rozważone warianty

- **Plik importu wgrywany w panelu** (pierwotna propozycja z 0003): odrzucony.
  Ręczny krok przy każdej zmianie w repo, a pracownia ma być miejscem, do którego
  po prostu się zagląda.
- **GitHub Action wysyłająca dane do Supabase po pushu**: odrzucona. Wymaga sekretu
  w repo, a przy publicznym repo zbędna.

## Konsekwencje

Gdyby repo stało się prywatne, odczyt wymaga tokena tylko do odczytu, trzymanego
jako sekret po stronie Supabase.
