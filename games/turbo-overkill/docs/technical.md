# Turbo Overkill — technika i stan prac

21 września 2026. **Pełne tłumaczenie 0.2.0 zbudowane i zainstalowane lokalnie.**
Selektor, polskie menu i fonty potwierdził użytkownik na verticalu 0.1.3.
Przetłumaczono 2316/2333 wpisów, czyli wszystkie niepuste. 17 wpisów ma pusty oryginał
i nie trafia do `pl.json`, więc gra pokazuje tam pusty tekst jak w EN. Dialogi,
infodeks i sklep w 0.2.0 czekają na test w grze. Gry nie uruchamiano.

ZIP: `dist/Turbo-Overkill-PL-0.2.0.zip`, 34 260 048 B.
SHA-256: `4f567f1dfb46bcc056c8f0238790139172439d42378c27cd32d36251e3a0b4a6`.
Paczka i `BepInEx-source-6.0.0-pre.2.zip` leżą też w `site/public/pobierz/`.
W `games/catalog.yaml` gra jest na liście **testowe**; na gotowe przenosi ją użytkownik.

## Spolszczenia i inne mody

### Awaria startu 0.1 i poprawka 0.1.1

Użytkownik zgłosił crash. Dwa zrzuty WER (`Turbo Overkill.exe.39080.dmp`
i `.40040.dmp`, 14:02–14:03) odczytano offline przez Microsoft ClrMD 2.2.332302
z DAC dołączonym do runtime 6.0.7. Oba: access violation w coreclr +0x1d1fdd,
`System.ExecutionEngineException`, ramka `Il2CppSystem.Collections.Generic.Dictionary<...>.ContainsKey`.
Log moda kończy się po `Translated=157; English fallback (missing PL)=2159`.
Tabele i loader zdążyły się załadować; `Polski ready` nie występuje.

Podejrzana granica ABI: sprawdzanie klucza `ValueTuple<LocaleIdentifier,string>`
przez generyczny wrapper IL2CPP. W 0.1.1 usunięto ten odczyt słownika z pluginu.
Natywne `RegisterTableOperation` samo tworzy i sprawdza klucze; ponownej
rejestracji pilnuje flaga resetowana przed `SendLocaleChangedEvents`, które
czyści cache przed wywołaniem `GetInitializationOperation`. Dodano logi etapów
rejestracji, aby następny test wskazał ewentualne kolejne blokery.

Nie ma samodzielnego testu regresji wywołującego rzeczywistą granicę IL2CPP
bez uruchomienia gry. Odczyt obu zrzutów potwierdza miejsce awarii, ale nie
dowodzi usunięcia crasha. Agent nie uruchamia gry; 0.1.1 wymaga próby użytkownika.
Kompilacja i walidacja ZIP przeszły, instalacja została sprawdzona sumami.
Logi, poprzedni plugin i ZIP zachowano w `work/crash-0.1/`.
Z logu wynika `Application.version=1.0`; nie uznawać tego za udany test gry.

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

Przeczytano `docs/decisions/0001-delivery-and-installation.md`. Obowiązuje plugin
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

## Plugin, selektor i fonty — vertical 0.1

`plugin/Plugin.cs` używa BepInEx **6.0.0-pre.2 Unity.IL2CPP win-x64**.
Biblioteki interop wygenerowano offline z lokalnego GameAssembly i metadanych
przez Cpp2IL + Il2CppInteropGenerator dołączone do tego wydania BepInEx.
To odczyt plików PE, nie ładowanie natywnego kodu gry. Pierwszy start u gracza
wygeneruje jego własne interop; do paczki nie trafiają nasze kopie.

Plugin po inicjalizacji ładuje osiem angielskich tabel asynchronicznie i tworzy
ich kopie w pamięci z LocaleIdentifier `pl`. Zmienia tylko wpisy obecne w
`pl.json`, a 2159 niepustych wpisów bez PL zachowuje w EN i raportuje ich liczbę.
Zachowuje natywny format SmartString oraz metadane. Kontroluje, czy kopia nie
współdzieli modyfikowanych danych wpisu z EN. Utrzymuje referencje do operacji
EN, ponieważ SharedTableData musi pozostać załadowana.

`RegisterTableOperation` rejestruje kopie według nazwy i GUID. Harmony Prefix
na `LocalizationSettings.GetInitializationOperation` odtwarza cache po zmianie
języka, zanim zostaną powiadomione komponenty UI. Locale ma dodatkowo fallback
do EN na wypadek nowych tabel. Przy niezgodności plugin loguje błąd, zdejmuje
własne poprawki i próbuje wrócić do EN; nie sprawdza sum kontrolnych gry.

W metadanych są `UiLanguageSelector` oraz metody `SetLanguage_English`,
`SetLanguage_Chinese`, `SetLanguage_French`, `SetLanguage_German`,
`SetLanguage_Spanish`, `SetLanguage_Russian`, `SetLanguage_Turkish`.
Z `data.unity3d` odczytano tylko wybrane bloki z level1 i małych plików
sharedassets (bez rozpakowywania całych 5,35 GB). Selektor w level1 ma siedem
UGUI Button z persistent listenerami SetLanguage_*. Przyciski zajmują pionowy
panel 800 jednostek. Plugin klonuje angielski przycisk, tworzy **nowy** onClick
(usuwa także persistent listener kopii), ustawia „Polski” i własną flagę 32×20
generowaną z kolorów. Rozmieszcza osiem przycisków w istniejącym panelu, zostawia
automatyczną nawigację. Nie zajmuje żadnego oryginalnego języka.

Kliknięcie korzysta najpierw z natywnej metody English, aby zachować zamykanie
panelu i bezpieczne ustawienie po usunięciu pluginu, następnie wybiera locale PL.
Własny PlayerPrefs `NieGesi.TurboOverkill.Locale` przechowuje wybór; powrót do
innego języka aktualizuje go. Zachowanie po restarcie wymaga testu użytkownika.

Odczytano cmap fontów z sharedassets0/1: Oxanium, Russo One, Roboto i TheNeue
mają pełny zestaw polskich znaków. Disket Mono, ZeF RAVE oraz część TapeFont
mają braki. Menu używa **UGUI Text (Legacy)**, nie samego TMP. Plugin sprawdza
HasCharacter tylko dla polskich liter aktualnego tekstu; przy braku wybiera
lokalny Oxanium-Regular, awaryjnie Arial z Windows. Font nie trafia do ZIP.
Po wyjściu z PL przywraca podmienione fonty, o ile gra sama nie zmieniła ich
wcześniej. Atlasy TMP oraz wygląd scen nie są potwierdzone testem w grze.

Paczka obejmuje wszystkie pliki oficjalnego BepInEx, jego LICENSE, źródła obok
ZIP oraz licencję i third-party notices .NET runtime z commitu
`0ec02c8c96e2eda06dc5b5edfdbdba0f36415082` (wersja odczytana z coreclr.dll).
Plugin 18 432 B; większy rozmiar ZIP wynika z runtime IL2CPP/.NET. Nie ma
w paczce zasobów, interop, dummy assemblies ani bibliotek bazowych Unity.

## Narzędzia i następny krok

```powershell
.venv/Scripts/python.exe games/turbo-overkill/tools/analyze.py --game "C:/Games/Turbo Overkill"
.venv/Scripts/python.exe games/turbo-overkill/tools/prepare_interop.py
.venv/Scripts/python.exe games/turbo-overkill/tools/build_plugin.py
.venv/Scripts/python.exe games/turbo-overkill/tools/install_local.py --game "C:/Games/Turbo Overkill"
```

`analyze.py` zachowuje istniejące PL przy ponownej ekstrakcji. Przed interop
potrzebne są rozpakowane `vendor/bepinex/il2cpp-pre2` i biblioteki bazowe z
`https://unity.bepinex.dev/libraries/2021.3.11.zip` w `work/unity-libs`.
Kompilator: Roslyn z Visual Studio 2022, offline generator używa zainstalowanego
hosta dotnet. Kod źródłowy generatora: `tools/GenerateInterop.cs`.

Build sprawdza zgodność review, tokeny `[input:...]`, placeholdery `{val}`,
znaczniki i liczbę końców wierszy. ZIP ma ścisłą listę dozwolonych plików;
pliki loadera są bajtowo identyczne z oficjalnym archiwum. Sprawdzenie CRC
i porównanie wszystkich 233 składników paczki przeszło. Wynik szczegółowy:
`work/build-report.json`.

Zainstalowano 233 nowe pliki. 137 istniejących plików zachowało rozmiary i mtime;
żadnego nie podmieniano. Lista dodanych plików i ich SHA-256:
`backups/turbo-overkill/install-receipt.json` w głównym repo. Lokalny pomocnik
odmawia nadpisywania obcego loadera lub zmienionych plików. Powrót:

```powershell
.venv/Scripts/python.exe games/turbo-overkill/tools/install_local.py --game "C:/Games/Turbo Overkill" --restore
```

Usuwa tylko pliki wymienione w pokwitowaniu i nadal zgodne z ich sumami;
puste katalogi i cache wygenerowane przez BepInEx zostawia. To narzędzie
do lokalnych testów, nie nowy instalator dla gracza.

**Następny krok: test pełnej wersji przez użytkownika.** Napisy dialogów
w kampanii (długość, ucięcia), infodeks z długimi nagraniami audio i bestiariuszem
(akapity, przewijanie), sklep wszczepów i broni. Przy problemie `BepInEx/LogOutput.log`
i screen. Po teście uzupełnić `tested_on` wersją z menu lub GOG Galaxy.

Materiał gry (oryginalne teksty, nazwy, postacie, fonty) należy do twórców.
Spolszczenie jest nieoficjalne. MIT w repo obejmuje nasze teksty i narzędzia,
nie zasoby wydawcy. Dubbing i oryginalne pliki lokalizacji nie są dystrybuowane.

---

## Dawne README

Treść, która do 2026-09-21 stała w README gry (nagłówek: „Turbo Overkill — analiza spolszczenia”). README jest teraz
krótką instrukcją instalacji dla gracza, wyświetlaną na stronie; ustalenia przeniesione
bez zmian, poza poprawionymi linkami względnymi. Część może być nieaktualna —
obowiązuje to, co wyżej w tym pliku, i instrukcja w paczce.

Kandydat do spolszczenia: 2333 wpisy w ośmiu tabelach, w tym 2316 niepustych.
Zakres obejmuje menu, dialogi, HUD, przedmioty, bestiariusz i rozbudowany infodeks.
Werdykt: warto przygotować vertical przez plugin BepInEx IL2CPP.

Nie znaleziono dostępnego spolszczenia. Nie ma jeszcze paczki do instalacji.
Lokalna gra nie została zmodyfikowana ani uruchomiona przez agenta.

Największe niewiadome to dodanie własnej pozycji „Polski” do selektora,
polskie znaki w fontach i uruchomienie pluginu na tej kopii GOG. Pierwsza próba
powinna objąć selektor, restart, menu, dialog i dłuższy wpis infodeksu.

[Analiza i źródła](../docs/technical.md) · [EN/PL do dalszej pracy](../translations/en-pl-review.json).

## Brak Polskiego w selektorze — 0.1.2

Screen użytkownika pokazuje siedem oryginalnych języków. Log 0.1.1 potwierdza
rejestrację wszystkich tabel i `Polski ready`, następnie `NotSupportedException:
Method unstripping failed` w `PersistentCallGroup.GetListener`, wywołanym przez
`GetPersistentMethodName`. Plugin wyłączył się przed utworzeniem przycisku.
To nie przewijanie ani za mały panel.

W 0.1.2 selektor czyta istniejące pola `m_PersistentCalls.m_Calls[i].m_MethodName`
zamiast usuniętej metody. Nadal rozpoznaje natywne przyciski po SetLanguage_*,
a osiem przycisków rozmieszcza w istniejącym panelu bez przewijania.

Kontrola Mono.Cecil łańcuchów wywołań do interop: stara DLL ma jedną ścieżkę
kończącą się stubem `Method unstripping failed` (GetListener), nowa ma zero
na 150 odwiedzonych metod. To wykrywa konkretny brak metody, nie potwierdza
wyglądu panelu ani wszystkich możliwych błędów runtime. Narzędzie i logi
w `work/offline/CheckCalls.cs` oraz `work/selector-0.1.1/`.
Zbudowano ZIP i zainstalowano 0.1.2; agent gry nie uruchamiał.
Następny test: ponowny start, Polski widoczny jako ósma opcja, wybór języka.

## Fonty i konsola — 0.1.3

Użytkownik potwierdził działanie selektora i polskie menu. Screen pokazuje
obce, małe ń/ź między kapitalikami Disket. Cmap Disket Mono nie zawiera tych
glifów (ani części pozostałych polskich znaków), choć Unity HasCharacter może
uwzględniać font systemowy i nie wykrywa braku. N/n i Z/z mają tę samą wysokość
w oryginalnym Disket — alfabet łaciński wygląda tam jak wielkie litery.

Dla PL zastępujemy całe napisy w znanych ograniczonych fontach (Disket,
ZeF RAVE, TapeFont High/LowQuality) fontem Oxanium-Regular z lokalnej gry.
Dotyczy też napisów bez ogonków, żeby menu było spójne. Dla Disket wielkość
liter zachowuje ToUpperInvariant, z pominięciem tagów, tokenów w nawiasach
kwadratowych i placeholderów w klamrach. Nie zmieniamy źródłowych tłumaczeń.
To zastępczy krój dla PL, nie dopisanie glifów do oryginalnego Disket.

Paczka zawiera BepInEx/config/BepInEx.cfg z wyłączoną konsolą i aktywnym logiem
do pliku. Lokalna instalacja zachowała wszystkie pozostałe ustawienia;
porównanie ConfigParser wykazało jedną zmianę: Logging.Console.Enabled
true -> false. Pierwotna konfiguracja w backups/turbo-overkill/originals/.
Nowy ZIP ma 234 pliki, plugin 19 968 B. Potrzebny test nowego wyglądu po restarcie.

## Pełne tłumaczenie — 0.2.0

Wszystkie osiem tabel ma polski tekst. Do dopisywania partii służy `work/batch.py`
(`show` wypisuje brakujące wpisy tabeli, `put` dopisuje wiersze `indeks<TAB>tekst`).
Review `translations/en-pl-review.json` jest zsynchronizowane z `pl.json`.

Ustalenia terminologiczne i postacie:
- S.A.M.M. mówi do Johnny'ego „sir”/„pan”, forma męska. Pozostali mówią na „ty”.
- Ripper mówi w formie żeńskiej.
- SYN jest kobietą: głos Patricii Summersett, w grze „her”, „madame”, „brońcie
  swojej matki”. Nazwa „SYN” jest nieodmienna („bez SYN”, „SYN pochłonęła”).
  Forma męska zostaje tylko tam, gdzie rządzi rzeczownik („wirus SYN”, „program
  SYN, który…”). Wyjątkiem jest gra słów żołnierza „syna skurwysyna”.
- Dyrektor (Exec) to kobieta: głos DB Cooper, a Ripper mówi „boss lady”. Kwestie
  Dyrektora mają formy żeńskie albo bezosobowe, a etykieta zostaje „Dyrektor”.
  Źródło obsady: english-voice-over.fandom.com (Turbo Overkill), bio DB Cooper na thegdex.com.
- Street Cleaner → czyściciel ulic, Regulator → Regulator, biocore → biordzeń,
  Vermilion Front → Cynobrowy Front, TitanCell → ogniwo Tytana,
  chainsaw leg → piłonoga. Nazwy przeciwników jak w bestiariuszu.
- Wulgaryzmy oddane z podobną siłą jak w oryginale.

Walidator w `build_plugin.py` porównuje też liczbę nowych linii. Wyjątek dotyczy
czterech nagrań-dialogów w TurboIndodex2 (Jazz, Exec/Jazz, Ripper/Exec, Exec/Doc).
Oryginał łamie tam wiersze ręcznie i dokłada wcięcie. W PL takie kontynuacje
połączono, bo pole tekstowe samo zawija tekst. Walidator akceptuje brak właśnie
tych złamań: nowa linia + wcięcie. Wpis Superior Maw w TurboStrings ma w oryginale
dosłowne `\n` jako tekst; PL odtwarza to samo.
