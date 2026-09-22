# Neon Abyss — technika

Ustalenia i instrukcje dla osób, które budują paczkę albo poprawiają teksty.
Gracz potrzebuje tylko [README](../README.md).

## Istniejące spolszczenia (2026-09-22)

Neon Abyss (2020) nie ma polskiego: API sklepu Steam dla 788100 wymienia angielski,
chiński uproszczony i tradycyjny, francuski, włoski, niemiecki, hiszpański, japoński
i rosyjski. Polski ma dopiero Neon Abyss 2 (2235200) — łatwo to pomylić w wynikach
wyszukiwania. Nie znalazłem dostępnej paczki fanowskiego spolszczenia.

## DLC Chrono Trap

Na GOG DLC to sam znacznik licencji (`goggame-1891558830.info`, ten sam `buildId`, hashdb
178 B); pliki gry i tabela I2 po instalacji mają te same sumy. Teksty DLC (Chronos, tryb
Chrono Trap, `Seed_endless_Desc`) są w tabeli bazowej i są przetłumaczone.

## Gra i silnik

- GOG, wersja 1.5.0.0 (`PlayerSettings.bundleVersion` „1.5.0.0sRC”), Unity 2018.4.21f1, Mono x64.
- `mscorlib.dll` pełny (4 MB, jest `GetPEKind`) — BepInEx 5.4.23.5 wstaje bez obejść.
- Teksty: I2 Localization, jedno źródło `LanguageSourceAsset` „I2Languages”,
  obiekt 3492 w `globalgamemanagers.assets`. 2784 terminy, 10 języków
  (pierwsza kolumna „Chinese (Mainland China)” bez kodu i wyłączona).
  Układ binarny: terminy od bajtu 56 (klucz, typ, opis, 10 wartości, flagi,
  pusta `Languages_Touch`), potem `CaseInsensitiveTerms`, `OnMissingTranslation`,
  `mTerm_AppName`, lista języków i ustawienia Google (aktualizacja: Never).
- 2681 terminów tekstowych, 2639 do tłumaczenia (reszta to puste pola, `-----`,
  nazwy grafik i jedna ścieżka fontu zapisane jako tekst — `RESOURCE` w `tools/batch.py`).
  Około 17,8 tys. słów angielskich. Kategorie: PuName (przedmioty, 1307), UI, Tips,
  CheatCode, Boss, Tree, Dialogue, Achieve, Seed, Character, Dead.
- Znaczniki: `{0}`, `{[k:Interact]}`, `{[UnlockCost]}`, `<br>`, warianty platform
  `[i2s_PC]`/`[i2s_PS4]`/`[i2s_XBox]` (zachować liczbę i kolejność wariantów).
  Etykiety `[Active Item]`, `[Passive]` i teksty w `<...>` przy ziarnach to zwykły tekst.

## Przełącznik języka

Lista w opcjach jest zaszyta w kodzie, nie brana z I2:

- `NEON.UI.Base.UIMenuSwitcherLanguageValueSource.Awake` wypełnia `Values` podpisami
  „ENGLISH”, „РУССКИЙ”… — plugin dopisuje „POLSKI”;
- `GamePlaySettingsHandler.LanguageReverseMapping(podpis)` → nazwa języka I2,
  ustawiana w `LocalizationManager.CurrentLanguage` i zapisywana w ustawieniach;
- `LanguageMapping` — podobne mapowanie z terminów `UI/English`…;
- `SettingsHandlerBase.InitWithLanguge(switcher, nazwa)` ustawia przełącznik na zapisanym języku.

Plugin łata wszystkie cztery (prefiksy zwracają „Polish” dla „POLSKI”). Klasy gry są
szukane po nazwach, bez referencji do `Assembly-CSharp` — brak klasy to wpis w logu.
`SettingsService.Load` przy pierwszym uruchomieniu bierze `GetSupportedLanguage`
z języka systemu, więc na polskim Windowsie gra może od razu wybrać polski.

## Fonty

Fonty idą przez terminy I2 typu Font: `UI/smallFont` i `UI/BigFont`
(`Fonts & Materials/<atlas>` w Resources). Stan atlasów TMP:

| Atlas | Tryb | Polskie litery | TTF w grze |
| --- | --- | --- | --- |
| EN_12px_PixAntiqua (mały, EN/FR/IT/DE/ES) | statyczny | brak | PixAntiqua — brak |
| EN_70px_ModernBrush (duży) | statyczny | brak | ModernBrush-Regular — komplet |
| RU_12px_tahoma, RU_70px_Terry | statyczne | nie sprawdzone | tahomabd, Terry Junior Deluxe — komplet |
| CHT_12px_Zpix | dynamiczny | dorysuje | Zpix — komplet |

Decyzja verticala: dla polskiego `UI/smallFont` = `CHT_12px_Zpix` (pikselowy, dynamiczny),
`UI/BigFont` = `EN_70px_ModernBrush`, któremu plugin dokłada dynamiczny atlas zapasowy
z `_TTF/ModernBrush-Regular` (`TMP_FontAsset.CreateFontAsset`). PixAntiqua dostaje
zapasowy Zpix, a `TMP_Settings.fallbackFontAssets` — globalny Zpix na teksty z fontem
ustawionym na sztywno. Wszystko z plików gry, paczka nie niesie fontów.

**Uszkodzony atlas CHT_12px_Zpix.** Litera „i” w dymkach dialogów wyświetlała się jako
krzaczek. W wydanej grze atlas ma „i” narysowane poprawnie (593,612, 3×9), ale jego
`m_FreeGlyphRects` nachodzi na 159 narysowanych glifów, w tym na „i”, więc litery
dorysowywane w locie (ą, ę, ł…) lądują na cudzych glifach. Plik Zpix sam rysuje „i”
dobrze (sprawdzone renderem 12 px). Próby naprawy:

- 0.2.1: `ClearFontAssetData` na egzemplarzu z Resources — bez zmian w grze;
- 0.2.2: to samo dla każdego egzemplarza przy `TMP_Text.font` — log pokazał jeden
  egzemplarz, czyli dymki używają tego z Resources, a czyszczenie nie pomaga;
- 0.2.3: prefiks na `TMP_Text.set_font` przy polskim podmienia `CHT_12px_Zpix` na świeży
  atlas z `_TTF/Zpix` (`CreateFontAsset(font, 12, 5, RASTER_HINTED, 1024, 1024, Dynamic)`,
  shader skopiowany z oryginału, czyli TextMeshPro/Bitmap). Chiński dostaje oryginał.
  W logu: „Polski mały tekst dostaje świeży atlas Zpix”.

**Polskie litery w nagłówkach (ModernBrush) — droga do 0.3.1.** Wszystkie atlasy gry to
raster z hintingiem, shader TextMeshPro/Bitmap i filtr Point (EN_70px_ModernBrush: 70 pt,
padding 2, tekstura 1024×512 zapełniona do y=510, więc nie da się do niej dorysować).
Plik ModernBrush ma pełne ą–ż (render 70 px). Kolejne próby i czego uczą:

- 0.2.0–0.2.3: zapas z `CreateFontAsset(font)` = SDF 90 pt; Bitmap rysuje go jako pusty kontur;
- 0.2.4–0.2.5: zapas rastrowy 70 pt, potem z filtrem Point — dalej zły krój;
- 0.2.6–0.2.9: log pokazał, że `TMP_FontAsset.TryAddCharacters` na atlasach z `CreateFontAsset`
  rzuca NullReferenceException przy `FontEngine.TryAddGlyphsToTexture` (IL 0x1e1), także po
  uzupełnieniu pustych list. **Dorysowywanie w locie do atlasów tworzonych w tej wersji TMP
  nie działa** — TMP po cichu bierze literę z kolejnego zapasu (globalny Zpix), stąd Zpix
  w nagłówku. Silnik fontów sam w sobie działa (`LoadFontFace` Success, glify Ę/Ś/Ł są);
- 0.3.0: zapasowy atlas statyczny złożony ręcznie — `CreateFontAsset(..., Static)`, a litery
  „ĄĆĘŁŃÓŚŹŻąćęłńóśźż„”–—…” renderowane pojedynczo wewnętrznym
  `FontEngine.TryAddGlyphToTexture` (refleksja) do własnej tekstury Alpha8, tabele glifów
  i znaków wypełnione ręcznie. Log: wszystkie wyrenderowane; w grze nadal Zpix;
- 0.3.1: zapasowe atlasy, ich tekstury i materiały dostają `HideFlags.DontUnloadUnusedAsset`,
  a zapas jest doklejany przy każdym `TMP_Text.font` i `LoadFontAsset`. **Potwierdzone
  w grze** („SZCZĘŚLIWA ZŁOTA MONETA” w całości ModernBrushem). Log pokazał po jednym
  egzemplarzu atlasów gry, więc to nie przeładowanie atlasu gry — najpewniej
  `UnloadUnusedAssets` zwalniał nasze obiekty tworzone w locie, a lista zapasów wskazywała
  na zniszczony atlas. Ochrona przed zwolnieniem jest tu kluczowa;
- 0.3.2: usunięta diagnostyka (próbne `TryAddCharacters` zaśmiecało log wyjątkami).

Świeży atlas Zpix dla dymków i globalny zapasowy Zpix zostały dynamiczne (`CreateFontAsset`
+ uzupełnione listy + ochrona przed zwolnieniem); „i” i polskie litery w dymkach działają.
Jeśli gdzieś w małym tekście wyjdzie obcy krój polskiej litery, przerobić je tak jak ModernBrush.

Do sprawdzenia w grze: czy Zpix w małym tekście wygląda dobrze, czy litery
z zapasowego ModernBrusha pasują wysokością do statycznego atlasu.

## Budowanie

```powershell
.venv\Scripts\python.exe games\neon-abyss\tools\extract.py --game "C:\Games\Neon Abyss"
.venv\Scripts\python.exe games\neon-abyss\tools\batch.py stats
.venv\Scripts\python.exe games\neon-abyss\tools\build.py --game "C:\Games\Neon Abyss"
```

`extract.py` przypina SHA-256 `globalgamemanagers.assets`
(`d342ad45…f563`) i zapisuje `work/source.json` (poza Gitem — dziesięć języków gry).
`batch.py` trzyma `pl.json` i `en-pl-review.json` w zgodzie. `build.py` sprawdza klucze
i znaczniki, kompiluje plugin (csc, referencje z `Managed` gry i BepInEksa), składa
`dist/Neon-Abyss-PL-<wersja>.zip` z BepInEksem 5.4.23.5 i kładzie obok źródła BepInEksa.
Plugin: teksty z `pl.tsv`, brakujące i nietekstowe terminy (grafiki, przyciski padów)
z kolumny angielskiej.

## Stan testów

- 2026-09-22: vertical 0.1.0 (84 wpisy) **potwierdzony w grze** przez użytkownika:
  POLSKI w opcjach, polskie litery, gra sama wybrała polski z języka systemu.
- 2026-09-22: pełne tłumaczenie 0.2.0 (2639/2639) zbudowane i zainstalowane
  w `C:\Games\Neon Abyss` (podmienione tylko pliki pluginu i READ-ME). Pełne przejście
  czeka. Co sprawdzić: [decyzje-tlumaczenia.md](decyzje-tlumaczenia.md), „Mniej pewne”.
- Usunięcie: folder `BepInEx`, `winhttp.dll`, `doorstop_config.ini`, `.doorstop_version`,
  `READ-ME.txt`, `BepInEx-LICENSE.txt`.

## Tłumaczenie

`translations/pl.json` to źródło (tylko przetłumaczone klucze), `en-pl-review.json`
generuje `tools/batch.py` (`show`, `put`, `from-review`, `stats`). Partie robocze leżą
w `work/batches/` (poza Gitem). Raport: `.claude/skills/lokalizacja/scripts/l10n_report.py`.

## Materiał gry

Paczka niesie wyłącznie BepInEx, nasz plugin i nasze teksty. Tabela I2 i fonty
są czytane z plików gry w czasie działania.
