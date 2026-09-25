"""Polskie napisy na grafikach DEADBOLT (menu główne, samouczek, wybór misji) — projekt i podgląd.

Plugin nie dostaje żadnych pikseli gry. Dla każdej etykiety przepis (`notgeese/labels.txt`) mówi:
  erase — w prostokącie klatki zamaluj kolorem tła piksele w kolorach napisu
          (faktura etykiety — plamy, zabrudzenia — zostaje, bo ma inne kolory);
  fill  — wypełnij prostokąt kolorem (klawisz „SPACE” z wyciętymi literami);
  mask  — narysuj naszą maskę (polski napis) podanym kolorem; AA=00 oznacza przezroczystość.
Współrzędne liczone od lewego górnego rogu prostokąta źródłowego klatki (TPAG) na stronie tekstur.
Maski renderujemy 1-bitowo z krojów o podobnym charakterze (Courier New Bold, Ink Free,
Bahnschrift, Georgia Bold, Lucida Console) i obrabiamy (pogrubienie, cień, przetarcie).
Paczka niesie tylko te maski konkretnych napisów, nie pliki fontów.

    .venv\\Scripts\\python.exe games\\deadbolt\\tools\\labels.py --game "C:\\SteamLibrary\\steamapps\\common\\DEADBOLT"

zapisuje podglądy work/labels-preview-*.png (złożone z grafik gry — tylko do oglądania).
"""
from __future__ import annotations

import argparse
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
FONTS = Path(r'C:\Windows\Fonts')

TYPEWRITER = dict(font='courbd.ttf')
MARKER = dict(font='Inkfree.ttf', bold=1)
STENCIL = dict(font='bahnschrift.ttf')
CHALK = dict(font='Inkfree.ttf')
HAND = dict(font='Inkfree.ttf')
SERIF = dict(font='georgiab.ttf')
MONO = dict(font='lucon.ttf')
PIXEL = dict(font=None)   # własny krój, patrz PIXEL_GLYPHS


def rgba(h: str):
    """RRGGBB albo RRGGBBAA (AA=00: przezroczystość)."""
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + ((int(h[6:8], 16),) if len(h) == 8 else (255,))


# Każda etykieta: sprite, klatka, prostokąt do czyszczenia (x0, y0, x1, y1 włącznie) z tłem i kolorami
# napisu (albo `fill`), obszar, w którym może stanąć nowy napis, tekst PL, styl, wysokość wersalików,
# środek napisu (albo `left`), rozstrzelenie, kolor.
LABELS = [
    # Menu główne — jedna grafika 960×540, każdy przycisk w innym stylu.
    dict(sprite='sMain', frame=0, rect=(146, 108, 277, 125), bg='dcd2b4', inks=['5b4444', '9e7c7c', 'baa69e'],
         area=(120, 106, 298, 127), text='NOWA GRA', style=TYPEWRITER, cap=12, center=(211, 116.5), spacing=5,
         color='5b4444', mottle='9e7c7c'),
    dict(sprite='sMain', frame=0, rect=(142, 164, 279, 181), bg='dcd2b4', inks=['5b4444', '9e7c7c', 'baa69e'],
         area=(120, 162, 298, 184), text='WCZYTAJ GRĘ', style=TYPEWRITER, cap=12, center=(210, 172.5), spacing=2,
         color='5b4444', mottle='9e7c7c'),
    dict(sprite='sMain', frame=0, rect=(145, 219, 276, 239), bg='cccb95', inks=['201d1c', 'baa985'],
         area=(131, 217, 298, 241), text='WŁASNE MAPY', style=MARKER, cap=15, center=(213, 229), spacing=1,
         color='201d1c'),
    dict(sprite='sMain', frame=0, rect=(143, 276, 277, 296), bg='201d1c', inks=['e1e1d7', '777573', '101014', '222626'],
         area=(120, 274, 298, 298), text='OPCJE', style=STENCIL, cap=15, center=(210, 285.5), spacing=10,
         color='e1e1d7', shadow=[('101014', 1, 2), ('777573', 0, 1)]),
    dict(sprite='sMain', frame=0, rect=(147, 330, 273, 355), bg='222626', inks=['777573', '33302f'],
         area=(120, 329, 298, 356), text='TWÓRCY', style=CHALK, cap=19, center=(211, 344), spacing=7,
         color='777573'),
    dict(sprite='sMain', frame=0, rect=(150, 381, 282, 411), bg='e1e1d7', inks=['201d1c', '33302f', '777573'],
         area=(131, 381, 285, 411), text='WYJDŹ', style=MARKER, cap=22, center=(210, 398), spacing=6,
         color='201d1c', bold=1),
    # Samouczek: żółte odręczne napisy na przezroczystym tle; „SPACE” wycięte w żółtym klawiszu.
    dict(sprite='sTutorial', frame=4, rect=(21, 0, 54, 15), bg='00000000', inks=['e2ed5c'],
         area=(21, 0, 54, 41), text='KLIK', style=PIXEL, cap=9, center=(38, 7.5), spacing=1, color='e2ed5c'),
    dict(sprite='sTutorial', frame=5, rect=(0, 12, 34, 30), bg='00000000', inks=['e2ed5c'],
         area=(0, 2, 35, 38), text='TRZYMAJ', style=PIXEL, cap=9, center=(17.5, 21), spacing=1, color='e2ed5c'),
    dict(sprite='sTutorial', frame=5, rect=(57, 12, 89, 30), bg='00000000', inks=['e2ed5c'],
         area=(57, 2, 90, 38), text='POTEM', style=PIXEL, cap=9, center=(73.5, 21), spacing=2, color='e2ed5c'),
    dict(sprite='sTutorial', frame=6, rect=(24, 11, 45, 25), bg='00000000', inks=['e2ed5c'],
         area=(22, 4, 46, 32), text='LUB', style=PIXEL, cap=9, center=(34, 18), spacing=1, color='e2ed5c'),
    dict(sprite='sTutorial', frame=6, fill=(55, 15, 96, 24), fillcolor='e2ed5c',
         area=(52, 13, 99, 26), text='SPACJA', style=PIXEL, cap=9, center=(76, 19.5), spacing=2, color='00000000'),
    # Wybór misji: przycisk „Back” (klatka 1 podświetlona) i teczka.
    dict(sprite='sMissionBack', frame=0, rect=(3, 3, 36, 14), bg='9a8a74', inks=['635845'],
         area=(3, 2, 68, 16), text='Wstecz', style=SERIF, cap=9, left=4, center=(0, 8.5), spacing=0, color='635845'),
    dict(sprite='sMissionBack', frame=1, rect=(3, 3, 36, 14), bg='9a8a74', inks=['ffffff'],
         area=(3, 2, 70, 16), text='Wstecz', style=SERIF, cap=9, left=4, center=(0, 8.5), spacing=0, color='ffffff'),
    dict(sprite='sMissionFolder', frame=0, rect=(13, 10, 41, 20), bg='9a8a74', inks=['635845'],
         area=(13, 9, 90, 20), text='Nazwa:', style=MONO, cap=8, left=14, center=(0, 15), spacing=0, color='635845'),
    dict(sprite='sMissionFolder', frame=0, rect=(13, 25, 48, 35), bg='9a8a74', inks=['635845'],
         area=(13, 24, 62, 35), text='Nr akt:', style=MONO, cap=8, left=14, center=(0, 30), spacing=0, color='635845'),
]


# Własny krój pikselowy do samouczka (kreska 1 px, wersaliki 7 wierszy, rozciągane do 9).
PIXEL_GLYPHS = {
    'A': ['.##.', '#..#', '#..#', '####', '#..#', '#..#', '#..#'],
    'B': ['###.', '#..#', '#..#', '###.', '#..#', '#..#', '###.'],
    'C': ['.###', '#...', '#...', '#...', '#...', '#...', '.###'],
    'E': ['####', '#...', '#...', '###.', '#...', '#...', '####'],
    'I': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '###'],
    'J': ['.###', '...#', '...#', '...#', '...#', '#..#', '.##.'],
    'K': ['#..#', '#.#.', '##..', '##..', '#.#.', '#..#', '#..#'],
    'L': ['#...', '#...', '#...', '#...', '#...', '#...', '####'],
    'M': ['#...#', '##.##', '#.#.#', '#.#.#', '#...#', '#...#', '#...#'],
    'O': ['.##.', '#..#', '#..#', '#..#', '#..#', '#..#', '.##.'],
    'P': ['###.', '#..#', '#..#', '###.', '#...', '#...', '#...'],
    'R': ['###.', '#..#', '#..#', '###.', '#.#.', '#..#', '#..#'],
    'S': ['.###', '#...', '#...', '.##.', '...#', '...#', '###.'],
    'T': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '.#.'],
    'U': ['#..#', '#..#', '#..#', '#..#', '#..#', '#..#', '.##.'],
    'Y': ['#.#', '#.#', '#.#', '.#.', '.#.', '.#.', '.#.'],
    'Z': ['####', '...#', '...#', '..#.', '.#..', '#...', '####'],
}


def render_pixel(text, spacing=1, seed=3):
    """Maska z własnego kroju: wiersze 1 i 5 zdublowane (9 px), litery podskakują o ±1 px jak pismo odręczne."""
    rnd = random.Random(seed)
    glyphs = [PIXEL_GLYPHS[c] for c in text]
    width = sum(len(g[0]) for g in glyphs) + spacing * (len(glyphs) - 1)
    img = Image.new('L', (width, 11), 0)
    x = 0
    for g in glyphs:
        rows = g[:2] + g[1:2] + g[2:6] + g[5:6] + g[6:]
        dy = 1 + rnd.choice((-1, 0, 0, 1))
        for y, row in enumerate(rows):
            for xx, ch in enumerate(row):
                if ch == '#':
                    img.putpixel((x + xx, y + dy), 255)
        x += len(g[0]) + spacing
    return img.crop(img.getbbox())


def render(text, style, cap, spacing, bold=None):
    """Maska napisu (Image 'L', 0/255) o wysokości wersalików `cap`."""
    if style is PIXEL:
        return render_pixel(text, spacing)
    path = str(FONTS / style['font'])
    size = cap
    for _ in range(60):   # dobór rozmiaru: wysokość „H”
        font = ImageFont.truetype(path, size)
        box = font.getbbox('H')
        if box[3] - box[1] >= cap:
            break
        size += 1
    top = font.getbbox('H')[1]
    widths = [font.getlength(c) for c in text]
    img = Image.new('L', (int(sum(widths) + spacing * len(text) + cap * 2), cap * 3), 0)
    d = ImageDraw.Draw(img)
    d.fontmode = '1'
    x = cap // 2
    for c, w in zip(text, widths):
        d.text((x, cap - top), c, font=font, fill=255)
        x += w + spacing
    thick = bold if bold is not None else style.get('bold', 0)
    for _ in range(thick):
        img = img.filter(ImageFilter.MaxFilter(3)) if thick > 1 else _thicken(img)
    return img.crop(img.getbbox())


def _thicken(img):
    """Pogrubienie o 1 px w prawo i w dół (jak marker), bez puchnięcia na boki."""
    out = img.copy()
    out.paste(255, mask=img.transform(img.size, Image.AFFINE, (1, 0, -1, 0, 1, 0)))
    out.paste(255, mask=img.transform(img.size, Image.AFFINE, (1, 0, 0, 0, 1, -1)))
    return out


def build():
    """Operacje dla pluginu, w kolejności wykonania."""
    ops = []
    rnd = random.Random(7)
    for lab in LABELS:
        s, f = lab['sprite'], lab['frame']
        if 'fill' in lab:
            ops.append(('fill', s, f, *lab['fill'], lab['fillcolor']))
        else:
            ops.append(('erase', s, f, *lab['rect'], lab['bg'], lab['inks'], 12))
        mask = render(lab['text'], lab['style'], lab['cap'], lab['spacing'], lab.get('bold'))
        cx, cy = lab['center']
        mx, my = round(cx - mask.width / 2), round(cy - mask.height / 2)
        if 'left' in lab:
            mx = lab['left']
        ax0, ay0, ax1, ay1 = lab['area']   # wnętrze etykiety, w którym może stanąć nowy napis
        if mx < ax0 or my < ay0 or mx + mask.width - 1 > ax1 or my + mask.height - 1 > ay1:
            raise SystemExit(f"{lab['text']}: maska {mask.size} w ({mx}, {my}) nie mieści się w {lab['area']}")
        for color, dx, dy in lab.get('shadow', []):
            ops.append(('mask', s, f, mx + dx, my + dy, mask, color))
        ops.append(('mask', s, f, mx, my, mask, lab['color']))
        if lab.get('mottle'):   # przetarcie tuszu jak w oryginale
            mot = Image.new('L', mask.size, 0)
            src, dst = mask.load(), mot.load()
            for y in range(mask.height):
                for x in range(mask.width):
                    if src[x, y] and (x + 2 * y) % 5 == 0 and rnd.random() < 0.8:
                        dst[x, y] = 255
            ops.append(('mask', s, f, mx, my, mot, lab['mottle']))
    return ops


def count(img: Image.Image, op) -> int:
    """Ile pikseli starego napisu zamaluje erase / ile przezroczystych wypełni fill — jak plugin."""
    px = img.load()
    kind, _, _, x0, y0, x1, y1 = op[:7]
    n = 0
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            p = px[x, y]
            if kind == 'fill':
                n += p[3] == 0
            elif p[3] and any(sum(abs(a - b) for a, b in zip(p[:3], rgba(i)[:3])) <= op[9] for i in op[8]):
                n += 1
    return n


def write_recipe(path: Path, game: Path) -> int:
    """labels.txt dla pluginu; oczekiwane liczby pikseli z grafik gry (plugin porównuje ±10%)."""
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from inspect_game import DataWin
    ops = build()
    frames = {(n, k): img.copy() for n, k, img in DataWin(game / 'data.win').sprite_frames({lab['sprite'] for lab in LABELS})}
    lines = []
    for op in ops:
        kind, sprite, frame = op[:3]
        work = frames[(sprite, frame)]
        if kind == 'erase':
            x0, y0, x1, y1, bg, inks, tol = op[3:]
            lines.append(f'erase\t{sprite}\t{frame}\t{x0}\t{y0}\t{x1}\t{y1}\t{bg}\t{",".join(inks)}\t{tol}\t{count(work, op)}\n')
            apply(work, [op], sprite, frame)
        elif kind == 'fill':
            x0, y0, x1, y1, color = op[3:]
            lines.append(f'fill\t{sprite}\t{frame}\t{x0}\t{y0}\t{x1}\t{y1}\t{color}\t{count(work, op)}\n')
            apply(work, [op], sprite, frame)
        else:
            x, y, mask, color = op[3:]
            rows = ['' .join('1' if mask.getpixel((xx, yy)) else '0' for xx in range(mask.width))
                    for yy in range(mask.height)]
            lines.append(f'mask\t{sprite}\t{frame}\t{x}\t{y}\t{mask.width}\t{mask.height}\t{color}\t{"/".join(rows)}\n')
            apply(work, [op], sprite, frame)
    path.write_text(''.join(lines), encoding='ascii', newline='\n')
    return len(lines)


def apply(img: Image.Image, ops, sprite, frame):
    """To samo, co zrobi plugin — na kopii klatki (podgląd)."""
    px = img.load()
    for op in ops:
        kind, s, f = op[:3]
        if (s, f) != (sprite, frame):
            continue
        if kind == 'erase':
            x0, y0, x1, y1, bg, inks, tol = op[3:]
            inks = [rgba(i) for i in inks]
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1):
                    p = px[x, y]
                    if p[3] and any(sum(abs(a - b) for a, b in zip(p[:3], ink[:3])) <= tol for ink in inks):
                        px[x, y] = rgba(bg)
        elif kind == 'fill':
            x0, y0, x1, y1, color = op[3:]
            for y in range(y0, y1 + 1):
                for x in range(x0, x1 + 1):
                    px[x, y] = rgba(color)
        else:
            x, y, mask, color = op[3:]
            c = rgba(color)
            for yy in range(mask.height):
                for xx in range(mask.width):
                    if mask.getpixel((xx, yy)):
                        px[x + xx, y + yy] = c
    return img


def preview(game: Path):
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from inspect_game import DataWin
    ops = build()
    dw = DataWin(game / 'data.win')
    frames = {(n, k): img for n, k, img in dw.sprite_frames({lab['sprite'] for lab in LABELS})}
    out = []
    for (name, k), img in frames.items():
        if not any(op[1] == name and op[2] == k for op in ops):
            continue
        after = apply(img.copy(), ops, name, k)
        if name == 'sMain':
            img, after = img.crop((100, 90, 320, 420)), after.crop((100, 90, 320, 420))
        if name == 'sMissionFolder':
            img, after = img.crop((0, 0, 100, 45)), after.crop((0, 0, 100, 45))
        pair = Image.new('RGBA', (img.width * 2 + 8, img.height), (40, 40, 40, 255))
        pair.alpha_composite(img, (0, 0))
        pair.alpha_composite(after, (img.width + 8, 0))
        scale = 3 if name == 'sMain' else 6
        out.append((f'{name}-{k}', pair.resize((pair.width * scale, pair.height * scale), Image.NEAREST)))
    for name, im in out:
        im.save(ROOT / f'work/labels-preview-{name}.png')
    return [n for n, _ in out]


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--game', type=Path, required=True)
    print(preview(ap.parse_args().game))
