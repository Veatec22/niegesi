# Okładki na kafelkach i karuzela w panelu gry — plan

21 września 2026. Plan do osobnej sesji. Decyzje podjęte z użytkownikiem:
okładka zamiast zrzutu na kafelku, karuzela tylko w panelu gry, grafiki
trzymane w repo (bez linkowania do serwerów Steama), mocniejsza kompresja.

## Stan dziś

- `tools/keyart.py` bierze z API Steam (`appdetails`) zrzut ekranu nr `keyart_shot`
  z `game.yaml`, przycina go do 16:9 i zapisuje `site/public/keyart/<slug>.webp`
  (jakość 82) oraz `.jpg` (jakość 86) w 1600×900. Razem 4,8 MB dla 13 gier;
  około 60% to zapasowe JPG.
- `site/src/lib/keyart.ts` (`keyartFor`) szuka tych plików, a `site/src/components/Keyart.astro`
  wstawia `<picture>` w wariancie `card` (kafelek, lazy) i `panel` (panel gry, eager).
  Style: `.ng-card-art` i `.ng-panel-art` w `site/src/styles/global.css`
  (`object-fit: cover`).
- Zrzuty często nie mówią, co to za gra (połowa to broń FPP w korytarzu).

## Co daje Steam (sprawdzone na wszystkich 13 grach ze `steam_appid`)

Stały adres, bez konta:
`https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/<appid>/<plik>`

| Plik | Wymiary | Uwagi |
| --- | --- | --- |
| `capsule_616x353.jpg` | 616×353 | logo + grafika; **brak w Shotgun Cop Man** (appid 2966850) — tam `header.jpg` |
| `header.jpg` | 460×215 | zapas dla kafelka |
| `library_600x900_2x.jpg` | 600×900 | pionowa okładka (na razie nieużywana) |
| `library_hero.jpg` | 1920×620 | szerokie tło bez logo, `logo.png` osobno |
| zrzuty (`appdetails` → `screenshots[].path_full`) | 1920×1080 | zwykle 8–10 |

`appdetails` podaje też `header_image` z hashem w ścieżce — zwykła ścieżka
bez hasha i tak odpowiada 200, ale kod ma na wszelki wypadek brać adres z API,
a dopiero przy braku składać go ręcznie.

## Do zrobienia

### 1. `tools/keyart.py`

- **Kafelek:** `capsule_616x353` (zapas: `header`) zamiast zrzutu. Proporcje 616:353
  ≈ 1,745 — albo zmienić proporcję kafelka na tę samą, albo lekko przyciąć do 16:9
  (wybrać po obejrzeniu; logo nie może zostać ucięte, więc raczej zmiana proporcji
  `.ng-card-art` niż crop).
- **Karuzela:** kapsuła jako pierwszy slajd + 4–6 zrzutów. Pole w `game.yaml`
  zamiast `keyart_shot`: np. `gallery: [1, 3, 4, 6]` (numery zrzutów z `--list-shots`);
  domyślnie pierwsze 5. `keyart_shot` usunąć z wszystkich `game.yaml` po migracji.
- **Formaty i rozmiary:** bez JPG. AVIF (Pillow ≥ 11 zapisuje AVIF; sprawdzić
  `features.check('avif')` w `.venv`, inaczej `pillow-avif-plugin`) + WebP jako zapas.
  - kafelek: 800 px szerokości (1× i 2× na ekranach do ~400 px), cel ~30–50 KB AVIF;
  - slajdy panelu: 1600 px, cel ~60–100 KB AVIF;
  - jakość dobrać na 2–3 grach z porównaniem na oko (np. AVIF q50–60, WebP q75–80).
- Nazwy plików np. `keyart/<slug>/cover-800.avif`, `cover-800.webp`,
  `shot-1-1600.avif`… — jeden katalog na grę, łatwe czyszczenie.
- Opcja `--all` odświeża wszystkie gry; stare pliki `keyart/<slug>.webp/.jpg` usunąć.
- Szacunek: 0,4–0,6 MB na grę, ~6–8 MB łącznie.

### 2. Strona (`site/`)

- `keyart.ts`: zwraca okładkę (`avif`/`webp`, 800 i 1600) i listę slajdów.
- `Keyart.astro` wariant `card`: `<picture>` z `<source type="image/avif">`,
  `<source type="image/webp">`, `srcset` 800w/1600w, `sizes` pod szerokość kafelka.
- Panel gry: karuzela bez biblioteki — lista slajdów z `scroll-snap-type: x mandatory`,
  strzałki i kropki w małym skrypcie, obsługa klawiatury (←/→), `alt` z tytułem gry
  i numerem slajdu, `loading="lazy"` dla slajdów poza pierwszym, działa na telefonie
  (przewijanie palcem) i bez JS (zwykłe przewijanie w poziomie).
- Zasady wyglądu: `docs/DESIGN.md`. Bez karuzeli na kafelkach.
- Gra bez `steam_appid` / bez grafik: dotychczasowy zastępczy kafelek `[keyart]`.

### 3. Dokumentacja i standard

- `docs/dodawanie-gry.md` i `AGENTS.md` (punkt 7, domykanie gry): wygenerowanie
  okładki i galerii `tools/keyart.py --game <slug>` jako część oddania — w ostatniej
  sesji keyart dla Void/Wild Bastards został zapomniany.
- Zaktualizować docstring `tools/keyart.py` (skąd grafiki, prawa: materiały
  promocyjne twórców jako ilustracja przy opisie spolszczenia).

### 4. Sprawdzenie

- `npm run build` w `site/`; obejrzeć kafelki i panel (desktop i ~375 px),
  karuzelę klawiaturą i palcem. Zgodnie z pamięcią użytkownika: **nie otwierać
  strony w przeglądarce agenta** — użytkownik ogląda sam; podać mu, co sprawdzić.
- Porównać rozmiar `site/public/keyart/` przed/po.
- Commit i push na prośbę użytkownika; deploy robi workflow `.github/workflows/pages.yml`
  po pushu na `main`.
