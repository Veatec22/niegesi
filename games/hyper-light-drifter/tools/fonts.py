"""Polskie litery fontu `f_uni` („Visitor TT2 BRK”, piksele 5×7).

Font ma wpisy dla wszystkich polskich liter, ale ich pola w atlasie są puste: GameMaker
wyrenderował zakres znaków, których krój nie zawierał. Litery składamy z liter samej
gry: kreska to akcent z „Ó” (dwa piksele po skosie w rzędach 0–1), kropka to jeden
piksel w rzędzie 1, ogonek to haczyk w rzędach 7–8 pod prawą stroną litery — jak cedylla
„Ç”, która też sięga dwa rzędy pod linię (wysokość glifu 9 zamiast 7).

Małe litery fontu to wersaliki, ale nie zawsze te same („n” ma inny kształt niż „N”),
więc każda polska litera powstaje ze swojej bazy o tej samej wielkości.

Wszystkie 16 liter dostaje nowe pola w pustym pasie na dole strony tekstur (od rzędu
1424; zawartość strony kończy się na 1418). Współrzędne glifu liczą się od początku
prostokąta fontu, ale mogą wskazywać dowolne miejsce tej samej strony. Dzięki temu
zmienia się tylko koniec PNG i łatka nie niesie pikseli gry (pngsplice.py). Struktury
glifów zmieniamy w miejscu: x, y i wysokość.
"""
from __future__ import annotations

from PIL import Image

from hld import Font

FONT = 'f_uni'
WHITE = (255, 255, 255, 255)

ACUTE = [(3, 0), (2, 1)]
DOT = [(2, 1)]
OGONEK = [(3, 7), (4, 8)]
# Ł: pień przesunięty do kolumny 1, kreska po skosie przez pień (0,4)–(2,3).
L_STROKE = {
    2: '.#...',
    3: '.##..',
    4: '##...',
    5: '.#...',
    6: '.####',
}

DESIGN = {
    'Ą': ('A', OGONEK), 'ą': ('a', OGONEK),
    'Ć': ('C', ACUTE), 'ć': ('c', ACUTE),
    'Ę': ('E', OGONEK), 'ę': ('e', OGONEK),
    'Ł': ('L', None), 'ł': ('l', None),
    'Ń': ('N', ACUTE), 'ń': ('n', ACUTE),
    'Ś': ('S', ACUTE), 'ś': ('s', ACUTE),
    'Ź': ('Z', ACUTE), 'ź': ('z', ACUTE),
    'Ż': ('Z', DOT), 'ż': ('z', DOT),
}
POLISH = ''.join(DESIGN)
PAGE_ROW = 1424     # pierwszy rząd pasa na litery, na stronie tekstur


def cell(page: Image.Image, font: Font, char: str) -> Image.Image:
    g = font.glyphs[char]
    ax, ay = font.atlas[:2]
    return page.crop((ax + g.x, ay + g.y, ax + g.x + g.w, ay + g.y + g.h))


def pixels(img: Image.Image) -> set[tuple[int, int]]:
    return {(x, y) for x in range(img.width) for y in range(img.height) if img.getpixel((x, y))[3]}


def design(page: Image.Image, font: Font) -> dict[str, Image.Image]:
    """Obrazy 5×7 albo 5×9 polskich liter."""
    # Akcent z samej gry: „Ó” minus „O”, żeby kreska była dokładnie taka jak w fontcie.
    acute = pixels(cell(page, font, 'Ó')) - pixels(cell(page, font, 'O'))
    assert acute == set(ACUTE), acute
    cedilla = pixels(cell(page, font, 'Ç')) - pixels(cell(page, font, 'C'))
    assert {y for _, y in cedilla} == {7, 8}, cedilla   # ogonek w tych samych rzędach
    out = {}
    for char, (base, mark) in DESIGN.items():
        b = cell(page, font, base)
        assert b.size == (5, 7), (base, b.size)
        if mark is None:
            assert pixels(b) == {(0, y) for y in range(2, 7)} | {(x, 6) for x in range(5)}, base
            points = {(x, y) for y, row in L_STROKE.items() for x, c in enumerate(row) if c == '#'}
        else:
            points = pixels(b) | set(mark)
        h = 9 if mark is OGONEK else 7
        img = Image.new('RGBA', (5, h), (0, 0, 0, 0))
        for p in points:
            img.putpixel(p, WHITE)
        out[char] = img
    return out


def placement(font: Font) -> dict[str, tuple[int, int]]:
    """Nowe (x, y) glifów, względem początku prostokąta fontu."""
    ax, ay = font.atlas[:2]
    return {c: (2 + 7 * i - ax, PAGE_ROW - ay) for i, c in enumerate(DESIGN)}
