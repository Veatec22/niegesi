"""Keyarty i metadane gier ze Steama.

Dla każdej gry z `games/<gra>/game.yaml` szuka wpisu w sklepie Steam, pobiera
zrzut ekranu i przycina go do 1600x900 (WebP + JPG) w `site/public/keyart/`.
Przy okazji uzupełnia w game.yaml `steam_appid`, `year` i link do sklepu.

    .venv\\Scripts\\python.exe tools\\keyart.py                 wszystkie gry
    .venv\\Scripts\\python.exe tools\\keyart.py --game otxo     jedna gra
    .venv\\Scripts\\python.exe tools\\keyart.py --game otxo --shot 3   inny zrzut
    .venv\\Scripts\\python.exe tools\\keyart.py --list-shots otxo      podgląd listy

Zrzuty i grafiki promocyjne należą do autorów gier — używamy ich jako ilustracji
przy opisie spolszczenia, nie jako własnych materiałów.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
GAMES = ROOT / 'games'
KEYART = ROOT / 'site' / 'public' / 'keyart'

WIDTH, HEIGHT = 1600, 900
SEARCH = 'https://steamcommunity.com/actions/SearchApps/{}'
DETAILS = 'https://store.steampowered.com/api/appdetails?appids={}&l=english'
STORE = 'https://store.steampowered.com/app/{}/'
USER_AGENT = 'niegesi-keyart/1.0 (+https://github.com/Veatec22/niegesi)'


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def normalise(name: str) -> str:
    return re.sub(r'[^a-z0-9]', '', name.lower())


def find_appid(title: str) -> int | None:
    """Steam zwraca też sequele i dema, więc dokładna nazwa ma pierwszeństwo."""
    results = json.loads(fetch(SEARCH.format(urllib.parse.quote(title))))
    if not results:
        return None

    wanted = normalise(title)
    for entry in results:
        if normalise(entry['name']) == wanted:
            return int(entry['appid'])
    return int(results[0]['appid'])


def app_details(appid: int) -> dict:
    payload = json.loads(fetch(DETAILS.format(appid)))
    entry = payload.get(str(appid), {})
    if not entry.get('success'):
        raise RuntimeError(f'Steam nie zwrócił danych dla appid {appid}')
    return entry['data']


def to_keyart(raw: bytes, slug: str) -> None:
    """Kadr 16:9 ze środka, bez zniekształceń. Zrzuty są zwykle 1920x1080."""
    image = Image.open(io.BytesIO(raw)).convert('RGB')
    target = WIDTH / HEIGHT
    width, height = image.size

    if width / height > target:
        crop = int(height * target)
        left = (width - crop) // 2
        image = image.crop((left, 0, left + crop, height))
    else:
        crop = int(width / target)
        top = (height - crop) // 2
        image = image.crop((0, top, width, top + crop))

    image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)
    KEYART.mkdir(parents=True, exist_ok=True)
    image.save(KEYART / f'{slug}.webp', 'WEBP', quality=82, method=6)
    image.save(KEYART / f'{slug}.jpg', 'JPEG', quality=86, optimize=True, progressive=True)


def set_scalar(text: str, key: str, value: str) -> str:
    """Podmienia wartość klucza najwyższego poziomu, zachowując resztę pliku."""
    pattern = re.compile(rf'^{re.escape(key)}:.*$', re.MULTILINE)
    line = f'{key}: {value}'
    return pattern.sub(line, text) if pattern.search(text) else f'{text.rstrip()}\n{line}\n'


def set_store(text: str, url: str) -> str:
    block = f'stores:\n  steam: {url}'
    if re.search(r'^stores:\s*\{\s*\}\s*$', text, re.MULTILINE):
        return re.sub(r'^stores:\s*\{\s*\}\s*$', block, text, flags=re.MULTILINE)
    if re.search(r'^stores:\s*$', text, re.MULTILINE):
        return re.sub(r'^stores:\s*$\n(?:  .*\n)*', block + '\n', text, flags=re.MULTILINE)
    return f'{text.rstrip()}\n{block}\n'


def process(path: Path, shot: int | None, force: bool) -> None:
    text = path.read_text(encoding='utf-8')
    data = yaml.safe_load(text)
    slug = data['slug']

    appid = data.get('steam_appid') or find_appid(data['title'])
    if not appid:
        print(f'{slug}: nie znalazłem gry na Steamie — uzupełnij steam_appid ręcznie')
        return

    details = app_details(appid)
    screenshots = [item['path_full'] for item in details.get('screenshots', [])]
    if not screenshots:
        print(f'{slug}: appid {appid} nie ma zrzutów — potrzebny własny keyart')
        return

    index = shot if shot is not None else int(data.get('keyart_shot') or 1)
    index = max(1, min(index, len(screenshots)))

    has_art = (KEYART / f'{slug}.webp').exists()
    if has_art and shot is None and not force:
        print(f'{slug}: keyart już jest (appid {appid}) — pomijam, użyj --force')
    else:
        to_keyart(fetch(screenshots[index - 1]), slug)
        print(f'{slug}: keyart ze zrzutu {index}/{len(screenshots)} (appid {appid})')

    text = set_scalar(text, 'steam_appid', str(appid))
    text = set_scalar(text, 'keyart_shot', str(index))
    released = re.search(r'\b(19|20)\d{2}\b', (details.get('release_date') or {}).get('date', ''))
    if released:
        text = set_scalar(text, 'year', released.group(0))
    text = set_store(text, STORE.format(appid))
    path.write_text(text, encoding='utf-8')


def list_shots(path: Path) -> None:
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    appid = data.get('steam_appid') or find_appid(data['title'])
    if not appid:
        print('nie znalazłem gry na Steamie')
        return
    for number, item in enumerate(app_details(appid).get('screenshots', []), start=1):
        print(f'{number:2}  {item["path_full"]}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--game', help='slug jednej gry; domyślnie wszystkie')
    parser.add_argument('--shot', type=int, help='numer zrzutu użytego jako keyart')
    parser.add_argument('--force', action='store_true', help='nadpisz istniejący keyart')
    parser.add_argument('--list-shots', metavar='SLUG', help='wypisz dostępne zrzuty i zakończ')
    args = parser.parse_args()

    if args.list_shots:
        list_shots(GAMES / args.list_shots / 'game.yaml')
        return 0

    paths = sorted(GAMES.glob('*/game.yaml'))
    if args.game:
        paths = [path for path in paths if path.parent.name == args.game]
        if not paths:
            print(f'nie ma gry {args.game}')
            return 1

    for number, path in enumerate(paths):
        if number:
            time.sleep(1)  # Steam nie lubi serii zapytań bez oddechu.
        try:
            process(path, args.shot, args.force)
        except Exception as error:  # jedna gra nie może wywrócić całej serii
            print(f'{path.parent.name}: {error}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
