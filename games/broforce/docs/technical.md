# Broforce — notatki techniczne

## Istniejące spolszczenia (stan na 2026-09-23)

Gra oficjalnie ma 9 języków (Steam, GOG): angielski, francuski, włoski, niemiecki,
hiszpański, portugalski (BR), japoński, koreański, chiński uproszczony. Polskiego
nie ma. Nie znalazłem dostępnego fanowskiego spolszczenia ani innego fanowskiego
tłumaczenia z narzędziami (wątek „TRANSLATION OF YOUR GAME” na forum Steama to tylko
deklaracje sprzed oficjalnej lokalizacji). Społeczność modderska działa na Unity Mod
Managerze (BroMaker, GameBanana), ale nic z tekstami.

## Gra

- Wydanie GOG, build 57322835742607320, `C:\Games\Broforce`.
- Unity 2017.4.7f1, Mono, 64-bit. `mscorlib.dll` pełna (zawiera `GetPEKind`),
  więc BepInEx 5 wstaje bez obejść.

## Jak gra trzyma teksty

Własny system `Localisation.LanguageManager` (singleton `BitCode.Singleton<T>`):

- `LanguageManagerConfig` (ScriptableObject w `resources.assets`, ładowany z Resources)
  — lista kodów języków: `en fr de es es-419 pt it jp ko zh-hans`.
- Na każdy język cztery banki w `resources.assets`: `StringLanguageBank` (teksty,
  408 wpisów, angielski ~26 KB), `SpriteLanguageBank` (puste), `RawImageMaterialLanguageBank`
  i `ReactionBubbleConfigLanguageBank`.
- `ChangeLanguage(code)` ładuje cztery banki `Resources.Load<…>(<LoadDestination>/<code>)`;
  jeśli któryś jest null, język się nie zmienia.
- `GetLocalisedString(key)` — jedyne wejście do tekstów: `stringBank.Find(key)`,
  potem reguły (`GlobeCharacterReplacer` tylko pilnuje nulla).
- Komponenty `LocalisedText` (UI Text), `LocalisedTextMesh`, `LocalisedMenuItem` itd.
  trzymają klucz i odświeżają się na zdarzeniu `LanguageManager.LanguageChanged`.
  Menu z kodu (`OptionsMenu`, `AudioMenu`, `LevelOverScreen`…) wołają `GetLocalisedString`.
- Menu języków (`LanguageMenu.SetupItems`) buduje pozycje z `Languages`, nazwa pozycji
  to `LANGUAGE_NAME_<kod>`. Wybór zapisuje się w `PlayerOptions.overrideLanguage`.
- Start: `GetSystemLanguage()` mapuje `Application.systemLanguage` na kod (polskiego
  brak → `en`), potem `PlayerOptions.InitializeOptions` nadpisuje zapamiętanym językiem.
- `LanguageFallbackFont[]` (kod języka → font) — gra przełącza całe fonty dla jp/ko/zh.

Tekst spoza banku: prawie nic. W kodzie zostają nazwy bro i napisy z grafik (sprite'y),
a w scenach trochę roboczych napisów bez klucza (edytor, testy). Nazwy bro zostają.

Bank czyta `tools/bank.py` (surowy MonoBehaviour: nagłówek, `m_Name`, lista par klucz/tekst;
pliki gry nie mają drzew typów).

## Fonty

Skan: `work/fonts.py` (pokrycie), `work/text_fonts.py` (który font rysuje który klucz).

| Font | Rodzaj | Polskie litery | Gdzie |
| --- | --- | --- | --- |
| HUDSONNY_BROFORCE | TTF dynamiczny | ma Ł ł Ó ó, brak ąćęńśźż | menu, większość napisów |
| akzidenz-grotesk-* | TTF dynamiczny | ma Ł ł Ó ó, brak reszty | UI Text (kampanie, lobby) |
| HUDSONNY_BROFORCE_ICONS | bitmapa 512×1024 RGBA32 | ma Ł ł Ó ó, `˛ ˙ ´`, É, Ç | przerywniki, THREAT LEVEL, ostrzeżenia |
| K-TYPE - NYC | bitmapa 512×512 Alpha8 | jak wyżej | |
| White_Font_8bitWonder | bitmapa 256×256 RGBA32 | tylko ASCII z pikselami (Latin-1 puste) | czekanie na graczy, przerywniki |
| HudsonOutline | bitmapa, skala ≠ 1 | znaki spoza ASCII zepsute już w oryginale | licznik sekund kampanii |
| 04B_11, 8-BIT WONDER, ArcadeClassic… | TTF | brak polskich | napisy bez klucza |

**Fonty bitmapowe** (`plugin/PolishGlyphs.cs`): dla każdego fontu bez polskich liter plugin
czyta atlas (Blit → ReadPixels), składa literę z bazowej i akcentu tego samego fontu
— kreska wycięta z É nad E (é nad e), kropka z `˙`, ogonek z `˛` przyklejony do prawego
dolnego rogu — kładzie ją w wolnym miejscu atlasu (tablica sum prefiksowych po prostokątach
znaków i pikselach) i dopisuje `CharacterInfo`. Tekstura: `Graphics.CopyTexture` do tej samej
tekstury (formaty RGBA32/Alpha8), inaczej nowa tekstura w materiale fontu. Gdy akcentu
w foncie nie ma (8bitWonder), rysuje go w grubości kreski zmierzonej na „I”.
Orientacja: lewy dolny wierzchołek glifu (vert.x, vert.y+vert.height) ↔ (uv.x, uv.y) —
sprawdzone offline na trzech fontach (`work/compose_proto*.py`, podgląd w `work/fontdump/`).
Znaki obrócone w atlasie (`flipped`: W, w, ´, myślniki…) leżą transponowane: wierzchołek (s, t) ↔
(uv.x + t·uv.w, uv.y + s·uv.h) — sprawdzone offline na W i ´. Składanie idzie w tekselach atlasu,
skala liczona osobno w poziomie i w pionie (HudsonOutline: 2,0 × 1,87).

HudsonOutline ma wpisy spoza ASCII skopiowane z HUDSONNY_BROFORCE_ICONS — wskazują w przypadkowe
miejsca atlasu (stąd „DOŁĄCZ” bez Ł i Ą). Plugin rozpoznaje je po odwróconej orientacji uv względem A–Z
i traktuje jak brak. Akcenty, których font nie ma, rysuje z grubością wypełnienia kreski i obrysem fontu
(geometria dostrojona w `work/compose_proto3.py`, podgląd `work/fontdump/proto3-*.png`). Wolne miejsce:
piksele z alfą + prostokąty znaków ASCII; puste komórki spoza ASCII (8bitWonder) są do wzięcia.

**Fonty dynamiczne** zostają bez zmian: Unity bierze brakujące glify z fontu systemowego.
Test 0.1.0 pokazał, że podstawianie działa (opis regionu na mapie), ale Hudson ma same wersaliki,
więc systemowe ń/ą/ź wyszły jako małe litery. Teksty rysowane dynamicznym Hudsonem piszemy wersalikami
(wyglądają tak samo, podstawione litery są przynajmniej wielkie). Styl podstawionych liter nadal odstaje;
kandydat na poprawę: przełączać takie teksty na HUDSONNY_BROFORCE_ICONS z dopisanymi literami.

## Dostarczanie

Plugin BepInEx 5.4.23.5 (x64), `plugin/Plugin.cs`:

- postfix `LanguageManagerConfig.get_Languages` → dopisuje `pl` (menu języków ma pozycję „Polski”);
- prefiksy `Load{String,Sprite,RawImageMaterial,ReactionBubbleConfig}Bank`: `pl` → `en`;
- postfix `GetLocalisedString`: `LANGUAGE_NAME_pl` → „Polski”; przy języku `pl` tekst z `pl.tsv`,
  brakujące klucze raz w logu („Bez polskiego tekstu: …”);
- postfix `GetSystemLanguage`: polski Windows → `pl`;
- po wczytaniu banku log: ile kluczy gry nie ma polskiego.

Po usunięciu pluginu zapamiętane `pl` jest ignorowane (`ChangeLanguage` sprawdza listę),
gra wraca do języka systemu.

## Budowanie

```powershell
.venv\Scripts\python.exe games\broforce\tools\build_plugin.py --game "C:\Games\Broforce"
```

Kontroluje klucze i placeholdery względem banku gry, odświeża `translations/en-pl-review.json`,
kompiluje plugin, składa `dist/Broforce-PL-<wersja>.zip`.

## Stan

- 0.1.0 vertical: 143/397 wpisów. Test w grze: język „Polski” i teksty działają; brakowało polskich
  liter w menu (JĘZYK, DŹWIĘKU), w „DOŁĄCZ DO GRY” i na mapie. Log: plugin pominął wszystkie fonty
  bitmapowe przez znaki `flipped`, HudsonOutline dodatkowo przez skalę ≠ 1, 8bitWonder przez brak miejsca.
- 0.1.1: poprawki powyżej, opis Wietmanu wersalikami. Test: menu i mapa z polskimi literami;
  „DOŁĄCZ DO GRY” nadal bez Ł i Ą — to nie font, tylko `Text3D` (niżej).
- 0.1.2: `plugin/PolishText3D.cs`. Test: „DOŁĄCZ DO GRY” z Ł i Ą — potwierdzone przez użytkownika;
  log: „Napisy 3D: dołożono 9 liter”, fonty ICONS, K-TYPE, 8bitWonder i HudsonOutline złożone.
- 0.2.0 (pełne): 397/397 wpisów, raport kontrolny czysty. HudsonOutline dostaje Ź — gdy brakuje
  miejsca, a tekstura i tak jest podmieniana (BC7), atlas rośnie dwukrotnie w pionie, a stare uv
  są przeliczane. Paczka w `site/public/pobierz/`, okładka i galeria wygenerowane.
  Zainstalowane do `C:\Games\Broforce`. **Przejście całej gry czeka.** Decyzje:
  `docs/translation-decisions.md`.

## Napisy 3D (Text3D)

Tytuły ekranów („DOŁĄCZ DO GRY”) składa komponent `Text3D` (`LocalisedText3D` podaje tekst):
tekst → `ToUpperInvariant`, każda litera to osobna bryła z listy `characterList`/`meshList`
(charA…charZ w scenesshared, tylko A–Z, odczytywalne), szerokość z `SourceFont` (K-TYPE - NYC,
`GetCharacterInfo(c, 42)`). Znak spoza listy = odstęp. Bryły: wyciągnięte w z (±13,75), wysokość 35,2,
pień „I” 8,7, bez UV (wygląd z oświetlenia). Plugin przed `UpdateText(string)` dopisuje do list
Ą Ć Ę Ł Ń Ó Ś Ź Ż = bryła bazowa + graniastosłup znaku (płaskie ściany, normalne na zewnątrz);
podgląd sylwetek `work/text3d_proto.py` → `work/fontdump/text3d-proto-a.png`.

## Pracownia korekty

`translations/structure.yaml` dzieli teksty na 8 grup po prefiksach kluczy.

## Nota o materiale gry

Paczka niesie wyłącznie BepInEx, plugin i `pl.tsv`. Fonty, atlasy i banki gry zostają
na dysku gracza; polskie litery powstają w pamięci z jego plików.
