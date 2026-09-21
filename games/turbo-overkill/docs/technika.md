# Turbo Overkill — ocena techniczna

21 września 2026. **Warto zrobić vertical; trudność umiarkowana.** Ekstrakcja
jest prosta, plugin wymaga obsługi IL2CPP i własnego rozszerzenia selektora.
Nie rozpoczęto tłumaczenia ani instalacji pluginu.

## Spolszczenia i inne mody

Nie znaleziono dostępnej paczki PL. Sprawdzono wyszukiwania po polsku i angielsku,
w tym Graj po polsku. [Steam](https://store.steampowered.com/app/1328350/Turbo_Overkill/?l=polish)
wymienia polski jako nieobsługiwany. Języki zbiorczych zestawów Steam nie są
dowodem obsługi PL przez samą grę.

Nie znaleziono też dostępnego fanowskiego tłumaczenia dostarczającego użyteczny
pipeline; wyszukiwano m.in. przekłady portugalskie, tureckie i koreańskie.
Lokalne tabele tureckie są częścią instalacji, nie dowodem fanowskiej łatki.

Przydatne są istniejące pluginy tej konkretnej gry:

- [Enhanced Graphics and UI — autor StixsmasterHD4k](https://www.nexusmods.com/turbooverkill/mods/3)
  opisuje instalację BepInEx 6 IL2CPP x64 oraz użycie GameSettings.
- [Ammo regen — opis autora](https://www.nexusmods.com/turbooverkill/mods/4)
  wymaga BepInEx 6 IL2CPP x64; autor deklaruje test w grze.
- [Instrukcja BepInEx dla IL2CPP](https://docs.bepinex.dev/master/articles/user_guide/installation/unity_il2cpp.html)
  potwierdza osobny wariant loadera i generowanie plików przy pierwszym starcie.
- [Wątek dewelopera o lokalizacji](https://steamcommunity.com/app/1328350/discussions/0/5590708606426106672/)
  dokumentuje historyczne problemy wyboru języka i parametr `-language=en`.
  Nie jest to zalecenie usuwania cudzych tabel ani docelowy model PL.

To przesłanki, nie nasz test pluginu. Nie pobierano ani nie uruchamiano tych modów.

## Lokalna kopia

- `C:/Games/Turbo Overkill`, GOG buildId `58328218944594138`.
- Unity **2021.3.11f1**, odczytane z nagłówków bundle.
- **IL2CPP x64:** GameAssembly.dll i il2cpp_data/Metadata/global-metadata.dat,
  metadane v29; brak katalogu Managed.
- Unity Localization + Addressables **1.19.19**, obecny Unity.TextMeshPro.
- `data.unity3d` ma około 5,35 GB. Nie ma potrzeby przepisywania go w celu
  ekstrakcji tabel ani dostarczania go w paczce.

Testy GetPEKind i konstruktorów AmbiguousMatchException dotyczą opisanej w repo
ścieżki Mono. Brak Managed w grze IL2CPP nie oznacza wykrycia tamtego problemu
ze strippingiem. Tutaj potrzebny jest wariant BepInEx Unity.IL2CPP, nie plugin
Pedra skompilowany bez zmian ani eksperymenty z podmianą mscorlib.

Przeczytano `docs/decyzje/0001-dostarczanie-i-instalacja.md`. Obowiązuje plugin
przed podmianą. Dopiero wykazane niepowodzenie tej drogi uzasadnia rozważenie
łatki różnicowej przez tools/patch.py. Nie proponujemy nowego instalatora.

## Teksty

Pliki w `Turbo Overkill_Data/StreamingAssets/aa/StandaloneWindows64/`:
angielski bundle 90 120 B, shared data 30 933 B, locales 2800 B. W instalacji
są tabele en, fr, de, ru, zh, es, tr; nie ma tabeli PL.

| Tabela | Wpisy | Znaki EN |
| --- | ---: | ---: |
| TurboVoices | 606 | 37 943 |
| TurboGame | 195 | 2849 |
| TurboStrings | 682 | 17 033 |
| TurboCodex | 66 | 8672 |
| TurboBestiary | 79 | 4323 |
| TurboItems | 261 | 10 023 |
| TurboEx1 | 339 | 7227 |
| TurboIndodex2 | 105 | 49 089 |
| **Razem** | **2333** | **137 159** |

17 wpisów jest pustych. Odczytano też stabilne identyfikatory wpisów i nazwy
kluczy z SharedTableData. Klucz review to GUID kolekcji + ID wpisu, z osobnymi
polami `table`, `term`, `entry_id`. Pozwala uniknąć kolizji między tabelami.
Nie normalizować kluczy tekstowych: istnieje np. `menu_campaign` z tabulatorem.

Osiem tabel przeszło odczyt i zapis typetree dający identyczne bajty w pamięci.
To potwierdza parser, nie ładowanie zmienionego bundle ani działanie moda.
Zachować `[input:...]`, znaczniki TMP i formatowanie. Nie jest jeszcze ustalone,
czy wszystkie widoczne napisy są w tabelach; surowe napisy w kodzie/teksturach
mogą wymagać osobnego rozpoznania.

## Plugin, selektor i fonty

Docelowa próba: dodanie kultury `pl` oraz tabel PL do systemu Unity Localization
w pamięci, z angielskim fallbackiem. Paczka powinna nieść tylko plugin, teksty,
loader z licencjami i niezbędne legalnie dystrybuowane zależności. Bez zasobów gry.
Konkretny punkt zaczepienia wymaga analizy wygenerowanych interop assemblies.

W metadanych są `UiLanguageSelector` oraz metody `SetLanguage_English`,
`SetLanguage_Chinese`, `SetLanguage_French`, `SetLanguage_German`,
`SetLanguage_Spanish`, `SetLanguage_Russian`, `SetLanguage_Turkish`.
To wskazuje na ręcznie obsługiwane przyciski; samo dodanie locale może nie
wystarczyć. Własne „Polski” musi działać bez zajmowania istniejącego języka.
Wykryto również `GetTranslatedSubtitle`, `LocalizeCommon`, `LocalizedFont`.
Są to nazwy, nie przeanalizowany przepływ wykonywania metod.

Katalog Addressables zawiera LiberationSans SDF, warianty Outline/Drop Shadow
i Fallback. **Nie sprawdzono atlasów ani pokrycia polskich glifów.** Sama nazwa
fontu nie dowodzi obecności ąćęłńóśźż. Trzeba ustalić font faktycznie używany
przez menu i napisy, tryb dynamiczny i fallback. W razie braków preferować
fallback tworzony w pamięci z legalnie dołączonego fontu, nie paczkę z zasobem gry.

## Narzędzia i następny krok

```powershell
.venv/Scripts/python.exe games/turbo-overkill/tools/analyze.py --game "C:/Games/Turbo Overkill"
```

Powstają `work/analysis.json` i `translations/en-pl-review.json` (2333 źródła,
PL puste); `pl.json` jest pusty. Brak paczki wydania jest zamierzony: etap analizy.

Vertical po decyzji użytkownika: start BepInEx IL2CPP, własne „Polski”, przełączenie
EN/PL, restart, krótki dialog, HUD z tokenem przycisku i długi wpis infodeksu.
Grę uruchamia użytkownik. Nie stwierdzono blokera, ale nie obiecujemy jeszcze
działania loadera, selektora ani fontów na tej instalacji.
