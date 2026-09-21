# Anger Foot — technika i stan prac

## Wersja 0.2 — metoda pluginowa

1774 z 1776 wpisów tekstowych po polsku; pozostałe dwa są puste również w oryginale.
Spolszczenie dokładane jest w czasie działania gry przez plugin BepInEx.
Żaden plik gry nie jest podmieniany, paczka waży 708 KB zamiast 193 MB.

Użytkownik potwierdził działanie w grze 20 września 2026: przycisk języka na ekranie
tytułowym pokazuje POLSKI, teksty podmieniają się poprawnie.

## Jak gra trzyma teksty

Unity 2019.4.35f1, Mono. Każda kwestia to osobny `LocalizedString : ScriptableObject`
w `resources.assets`, z listą dwunastu tłumaczeń indeksowaną pozycją języka
w kolejności alfabetycznej `LocalizationLanguage.SpreadsheetKey`:

```
CHINESE SIMPLIFIED, CHINESE TRADITIONAL, FRENCH, GERMAN, ITALIAN, JAPANESE,
KOREAN, PORTUGUESE BRAZILIAN, RUSSIAN, SPANISH, SPANISH LATAM, TURKISH
```

Slot włoski (indeks 4) jest **pusty i niedostępny w menu** — rekord języka istnieje,
tekstu nigdy w nim nie było. To jego przejmujemy. `SpreadsheetKey` musi zostać
`ITALIAN`, bo po nim liczona jest pozycja tłumaczenia w każdym wpisie; zmiana
przesunęłaby wszystkie indeksy.

Rekord języka to `LocalizationLanguage : ScriptableEnum` (w `Assembly-CSharp-firstpass.dll`)
z polami `Supported`, `NativeName`, `SpreadsheetKey`, `LanguageTag`, `SteamAPIName`,
`GOGAPIName`, `FontOverride`.

## Co robi plugin

`plugin/Plugin.cs`, dwie łatki Harmony:

- **`LocalizationManager.Initialize` (prefix)** — przemianowuje rekord włoski:
  `NativeName` na „Polski", `LanguageTag` na `pl`, `Supported` na prawdę.
  Dzieje się to przed zbudowaniem listy języków, więc polski pojawia się w menu.
- **`LocalizedString.GetTranslation` (postfix)** — podmienia zwracany tekst,
  gdy aktualnym językiem jest przejęty slot.

Przechwycenie gettera zamiast wypełniania tablic ma tę zaletę, że nie trzeba czekać
na wczytanie zasobów ani wymuszać `EnsureInstancesAreLoaded` — gra pyta, my odpowiadamy.

## Dlaczego GUID, a nie termin

**Terminy w tej grze się powtarzają: 1518 unikalnych na 1776 wpisów.** Rozpoznawanie
kwestii po `Term` podstawiłoby części dialogów cudzy tekst. GUID-y są unikalne
co do jednego (1776/1776), więc plugin mapuje właśnie po nich.

`translations/pl.json` jest kluczowane `path_id` obiektu Unity, którego w czasie gry
nie widać. `tools/build_plugin.py` przy składaniu paczki czyta oryginalny
`resources.assets`, wyciąga dla każdego wpisu GUID i tworzy `pl.tsv` w postaci
`GUID<TAB>tekst`. Źródłem tłumaczenia pozostaje ten sam `pl.json`, co przy starej
metodzie, więc korekty językowe działają bez zmian.

## Budowanie

```powershell
.venv\Scripts\python.exe games\anger-foot\tools\build_plugin.py --game "C:\Games\Anger Foot"
```

Build sprawdza, czy wszystkie przetłumaczone wpisy znalazły swój GUID, czy GUID-y się
nie powtarzają i czy do archiwum nie wpadł żaden plik gry. Wynik: `dist/Anger-Foot-PL-0.2.zip`
oraz archiwum źródeł BepInEksa obok, wymagane przez LGPL.

Plugin nie ma przypiętej sumy kontrolnej gry — wiąże się po nazwach klas, więc
powinien przeżyć aktualizację i działać także na wydaniu ze Steama.

## Poprzednia metoda

Wersja 0.1 podmieniała `resources.assets` i `sharedassets0.assets` (193 MB).
Opis w [README](../README.md) i `docs/INSTALL.txt`. Zostaje jako zapis drogi;
paczki nie publikujemy, bo zawierała przepisane zasoby wydawcy.
