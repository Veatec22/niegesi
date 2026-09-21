# Shotgun Cop Man — technika

Ustalenia i instrukcje dla osób, które budują paczkę albo poprawiają teksty.
Gracz potrzebuje tylko [README](../README.md).

## Jak działa spolszczenie

Gra stoi na Unity 2022.3.47f1 (Mono, x64) i trzyma teksty w I2 Localization,
wkompilowanym w `Assembly-CSharp.dll`. Plugin BepInEx 5 ([`plugin/Plugin.cs`](../plugin/Plugin.cs))
w czasie działania gry dokłada polski jako jedenasty język tabeli I2. Menu wylicza
języki dynamicznie, więc nowy pojawia się w **Options → Language** bez dalszych łatek.
Żaden plik gry nie jest podmieniany.

Plugin wiąże się po nazwach klas, nie po sumach kontrolnych. Przy starcie loguje
wersję gry i Unity, a teksty, których nie ma w spolszczeniu, zostawia po angielsku
i zapisuje w logu ich liczbę. Poprawny start zostawia w `BepInEx/LogOutput.log`
linię „Polski dodany jako jezyk 11 z 11".

## Pliki

| Plik | Do czego |
| --- | --- |
| [`translations/pl.json`](../translations/pl.json) | Polskie teksty, 485 wpisów kluczowanych identyfikatorem terminu I2. Tu poprawia się tłumaczenie. |
| [`translations/en-pl-review.json`](../translations/en-pl-review.json) | Zestawienie EN/PL do korekty; zmiany w `pl.json` trzeba nanieść także tutaj. |
| [`plugin/Plugin.cs`](../plugin/Plugin.cs) | Plugin BepInEx. |
| [`tools/build_plugin.py`](../tools/build_plugin.py) | Kompiluje plugin, zamienia `pl.json` na `pl.tsv` i składa paczkę. |
| [`docs/INSTALL-plugin.txt`](INSTALL-plugin.txt) | Instrukcja dla gracza, w paczce jako `READ-ME.txt`. |
| [`tools/build.py`](../tools/build.py), [`docs/INSTALL.txt`](INSTALL.txt) | Stara droga z wersji 0.1: podmiana `resources.assets`. Zastąpiona pluginem, zostaje dla porównania. |

## Budowanie paczki

Potrzebny jest Python 3.11 ze środowiskiem w katalogu głównym repozytorium, kompilator
C# (`csc.exe` z Visual Studio 2022 albo .NET Framework 4) oraz zainstalowana gra — z jej
katalogu `Managed` brane są biblioteki do kompilacji. Skrypt niczego w grze nie zmienia.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe games\shotgun-cop-man\tools\build_plugin.py --game "C:\SteamLibrary\steamapps\common\Shotgun Cop Man"
```

Wynik: `dist/Shotgun-Cop-Man-PL-<wersja>.zip` z BepInEksem 5.4.23.5, jego licencją,
pluginem, `pl.tsv` i `READ-ME.txt`. Obok leży archiwum źródeł BepInEksa tej wersji,
bo wymaga tego jego licencja (LGPL-2.1). Katalog `dist` nie trafia do Gita.

## Stan testów

Sprawdzone na Steamie, wersja gry 1.0.4 (`PlayerSettings.bundleVersion`, build Steama
20572164): wybór polskiego i teksty potwierdzone w grze. Nagrane głosy
i opisy osiągnięć wyświetlane przez klienta Steam zostają po angielsku — nie są
częścią tabeli I2.

## Materiał gry i licencja

Repozytorium zawiera wyłącznie teksty tłumaczenia i narzędzia — żadnych plików gry.
*Shotgun Cop Man*, jego teksty i postacie należą do autorów gry; projekt nie jest
z nimi powiązany. Paczka działa tylko z legalnie posiadaną kopią gry.
Tłumaczenie i narzędzia: [MIT](../../../LICENSE), jak reszta repozytorium.
