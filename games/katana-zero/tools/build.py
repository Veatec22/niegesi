"""Buduje spolszczone Katana ZERO.exe i data.win z oryginałów GOG 1.0.5.

    .venv\\Scripts\\python.exe games\\katana-zero\\tools\\build.py --game "C:\\Games\\Katana ZERO"

Polski zajmuje miejsce rosyjskiego: gra ma dziesięć języków w sztywnej tablicy
(język * 32000 + numer), więc nowego nie da się dopisać bez przepisywania kodu.
Wybór „Русский” w menu staje się „Polski”, a rosyjska ścieżka rysowania tekstu
(fonty ze sprite'ów z pełną łaciną) niesie polskie litery.

Exe: polskie napisy lądują w nowej sekcji `.ngpl` na końcu pliku, a instrukcje, które
podawały adres rosyjskiego napisu, dostają adres polskiego. Wpisy bez tłumaczenia
wskazują napis angielski. Adresy są objęte istniejącymi relokacjami (sprawdzamy każdy),
więc ASLR działa bez zmian. Mapy znaków fontów dostają polskie litery na końcu.

data.win: polskie litery (tools/fonts.py) na nowych stronach tekstur (po jednej na grupę
tekstur fontu, dopisanej do tej grupy), nowe pozycje TPAG, drugi chunk TPAG z pełną listą
i nowe kopie struktur sześciu sprite'ów fontów z dłuższą listą klatek. Przesuwają się
tylko dane tekstur i dźwięków — ich wskaźniki poprawiamy o długość wstawek.

Wynik trafia do dist/build/. Build nie dotyka katalogu gry.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import struct
import sys
from pathlib import Path

import pefile
from PIL import Image

from exe import Exe, LANGS
from fonts import FONT_SPRITES, LOWER, UPPER, glyphs_for
from gmdata import DataWin, TPAG_SIZE, u32

ROOT = Path(__file__).resolve().parents[1]
EXE_NAME = 'Katana ZERO.exe'
EXE_SHA256 = '291c552e7aa4640a5a40b320863fe13747ac431133a834c8532a2cdfa574bb93'
WIN_SHA256 = '8353b7da345f8c72ecafdc0a523d7b627091ff88a17cd56c8350cf15bdba509e'
SECTION = b'.ngpl\0\0\0'
SLOT = 'ru'
LANGUAGE_NAME_KEY = 'init_misc_text:1790'   # nazwa języka w jego własnym brzmieniu


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def align(v: int, a: int) -> int:
    return (v + a - 1) // a * a


# ---------------------------------------------------------------- exe

def reloc_rvas(pe: pefile.PE) -> set[int]:
    pe.parse_data_directories(directories=[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_BASERELOC']])
    out = set()
    for block in pe.DIRECTORY_ENTRY_BASERELOC:
        for e in block.entries:
            if e.type == pefile.RELOCATION_TYPE['IMAGE_REL_BASED_HIGHLOW']:
                out.add(e.rva)
    return out


def build_exe(src: Path, pl: dict[str, str], new_maps: dict[str, str], out: Path) -> dict:
    exe = Exe(src)
    pe = exe.pe
    data = bytearray(exe.data)
    entries = exe.entries() + exe.menu_entries()
    relocs = reloc_rvas(pefile.PE(data=exe.data, fast_load=True))

    last = pe.sections[-1]
    sec_rva = align(last.VirtualAddress + last.Misc_VirtualSize, pe.OPTIONAL_HEADER.SectionAlignment)
    sec_va = exe.base + sec_rva
    blob = bytearray()
    placed: dict[str, int] = {}

    def put(s: str) -> int:
        if s not in placed:
            placed[s] = sec_va + len(blob)
            blob.extend(s.encode('utf-8') + b'\0')
        return placed[s]

    def repoint(site: int, va: int):
        rva = pe.get_rva_from_offset(site)
        if rva not in relocs:
            raise SystemExit(f'miejsce {site:#x} nie ma relokacji — adres nie przetrwałby ASLR')
        struct.pack_into('<I', data, site, va)

    known = {e.key for e in entries}
    unknown = sorted(set(pl) - known)
    if unknown:
        raise SystemExit(f'pl.json ma klucze, których nie ma w grze: {unknown[:10]}')
    stats = {'entries': len(entries), 'translated': 0, 'english': 0}
    for e in entries:
        if e.key in pl:
            va = put(pl[e.key])
            stats['translated'] += 1
        else:
            va = struct.unpack_from('<I', exe.data, e.sites['en'])[0]
            stats['english'] += 1
        repoint(e.sites[SLOT], va)

    for old, new in new_maps.items():
        if old == new:
            continue
        refs = exe.references(exe.find_string(old))
        if not refs:
            raise SystemExit('mapa fontu bez odwołań w kodzie')
        va = put(new)
        for site in refs:
            repoint(site, va)

    # nowa sekcja: nagłówek za ostatnim, dane na końcu pliku
    hdr = last.get_file_offset() + 40
    if hdr + 40 > pe.OPTIONAL_HEADER.SizeOfHeaders or any(data[hdr:hdr + 40]):
        raise SystemExit('brak miejsca na nagłówek nowej sekcji')
    fa = pe.OPTIONAL_HEADER.FileAlignment
    raw_at = align(len(data), fa)
    data.extend(b'\0' * (raw_at - len(data)))
    raw_size = align(len(blob), fa)
    data.extend(blob + b'\0' * (raw_size - len(blob)))
    struct.pack_into('<8sIIIIIIHHI', data, hdr, SECTION, len(blob), sec_rva, raw_size, raw_at,
                     0, 0, 0, 0, 0x40000040)   # dane zainicjowane, tylko do odczytu
    nt = pe.DOS_HEADER.e_lfanew
    struct.pack_into('<H', data, nt + 6, pe.FILE_HEADER.NumberOfSections + 1)
    opt = nt + 24
    struct.pack_into('<I', data, opt + 56, sec_rva + align(len(blob), pe.OPTIONAL_HEADER.SectionAlignment))
    fixed = pefile.PE(data=bytes(data), fast_load=True)
    struct.pack_into('<I', data, opt + 64, fixed.generate_checksum())
    out.write_bytes(data)
    stats['section_bytes'] = len(blob)
    return stats


def verify_exe(src: Path, built: Path, pl: dict[str, str], new_maps: dict[str, str]):
    a, b = Exe(src), Exe(built)
    ea = {e.key: e for e in a.entries() + a.menu_entries()}
    for e in ea.values():
        for lang in LANGS:
            got = b.cstr(struct.unpack_from('<I', b.data, e.sites[lang])[0])
            want = (pl.get(e.key, e.text['en'])) if lang == SLOT else e.text[lang]
            if got != want:
                raise SystemExit(f'weryfikacja exe: {e.key} [{lang}] = {got!r}, oczekiwano {want!r}')
    for old, new in new_maps.items():
        if old != new:
            for site in a.references(a.find_string(old)):
                if b.cstr(struct.unpack_from('<I', b.data, site)[0]) != new:
                    raise SystemExit('weryfikacja exe: mapa fontu nie podmieniona')
    # poza podmienionymi adresami i nagłówkiem plik ma być identyczny
    changed = [i for i in range(0x400, len(a.data)) if a.data[i] != b.data[i]]
    sites = {s + k for e in ea.values() for s in [e.sites[SLOT]] for k in range(4)}
    sites |= {s + k for old in new_maps for s in a.references(a.find_string(old)) for k in range(4)}
    stray = [i for i in changed if i not in sites]
    if stray:
        raise SystemExit(f'weryfikacja exe: {len(stray)} bajtów zmienionych poza adresami, np. {stray[0]:#x}')


# ---------------------------------------------------------------- data.win

def pack_glyphs(items: list[tuple[str, str, Image.Image]]):
    """Półkowe pakowanie przyciętych liter na jedną stronę; zwraca stronę i pozycje."""
    trimmed = []
    for sprite, ch, img in items:
        b = img.getchannel('A').getbbox()
        # jak gra: margines jednego piksela wokół rysunku, w granicach klatki
        x0, y0 = max(0, b[0] - 1), max(0, b[1] - 1)
        x1, y1 = min(img.width, b[2] + 1), min(img.height, b[3] + 1)
        trimmed.append((sprite, ch, img, (x0, y0, x1, y1)))
    width = 512
    x = y = shelf = 0
    pos = []
    for sprite, ch, img, (x0, y0, x1, y1) in trimmed:
        w, h = x1 - x0, y1 - y0
        if x + w > width:
            x, y, shelf = 0, y + shelf + 1, 0
        pos.append((x, y))
        x += w + 1
        shelf = max(shelf, h)
    height = 1
    while height < y + shelf:
        height *= 2
    page = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    out = []
    for (sprite, ch, img, box), (px, py) in zip(trimmed, pos):
        page.paste(img.crop(box), (px, py))
        out.append((sprite, ch, box, (px, py)))
    return page, out


def texture_groups(dw: DataWin) -> list[dict]:
    """Grupy tekstur (TGIN): nazwa, wskaźnik listy stron i numery stron oraz sprite'ów.

    Gra wczytuje strony tekstur grupami. Strona spoza wszystkich grup nigdy nie trafia
    do pamięci karty, więc litery na niej są niewidoczne (sprawdzone w grze w 0.1).
    """
    d = dw.data
    start, _ = dw.chunks['TGIN']
    out = []
    for i in range(u32(d, start + 4)):
        g = u32(d, start + 8 + 4 * i)
        lists = []
        for k in range(5):                 # strony, sprite'y, spine, fonty, tilesety
            p = u32(d, g + 4 + 4 * k)
            lists.append([u32(d, p + 4 + 4 * j) for j in range(u32(d, p))])
        out.append({'name': dw.string(u32(d, g)), 'at': g, 'textures': lists[0], 'sprites': lists[1]})
    return out


def build_win(src: Path, glyphs: dict[str, dict[str, Image.Image]], out: Path) -> dict:
    """Trzy wstawki: nowy chunk TPAG przed TXTR, wskaźniki stron za listą TXTR, obrazki na końcu TXTR.

    Runner zamienia numer strony w każdej pozycji TPAG na identyfikator tekstury w karcie,
    ale tylko w pozycjach z listy chunku TPAG (sprawdzone w kodzie ładowania TXTR, 0.1.1
    wyszło w grze bez polskich liter). Listy nie da się wydłużyć w miejscu, więc dokładamy
    drugi chunk TPAG z pełną listą — stare pozycje w tej samej kolejności plus nasze —
    zaraz przed TXTR. Handler TPAG tylko zapamiętuje położenie listy, więc wygrywa ten
    późniejszy, a pierwszy zostaje na swoim miejscu.
    """
    dw = DataWin(src)
    d = dw.data
    sprites = dw.sprites()
    tex_start, tex_ptrs = dw.pointer_list('TXTR')
    tpag_start, tpag_ptrs = dw.pointer_list('TPAG')
    n_tex = len(tex_ptrs)
    C = tex_start - 8                      # nowy chunk TPAG: przed nagłówkiem TXTR
    P = tex_start + 4 + 4 * n_tex          # nowe wskaźniki stron: za listą TXTR
    Q = sum(dw.chunks['TXTR'])             # obrazki: na końcu danych tekstur

    # jedna nowa strona na grupę tekstur, w której siedzi font
    groups = texture_groups(dw)
    by_group: dict[int, list[str]] = {}
    for name in FONT_SPRITES:
        gi = [i for i, g in enumerate(groups) if sprites[name].index in g['sprites']]
        if len(gi) != 1:
            raise SystemExit(f'{name}: sprite w {len(gi)} grupach tekstur')
        by_group.setdefault(gi[0], []).append(name)
    pages = []                             # (grupa, numer strony, png, rozmieszczenie, rozmiar)
    for k, (gi, names) in enumerate(by_group.items()):
        items = [(name, ch, img) for name in names for ch, img in glyphs[name].items()]
        page, placed = pack_glyphs(items)
        buf = io.BytesIO()
        page.save(buf, 'PNG', optimize=True)
        pages.append((gi, n_tex + k, buf.getvalue(), placed, page.size))
    n_new = sum(len(p[3]) for p in pages)

    # --- chunk C: lista TPAG, pozycje TPAG, sprite'y, listy grup, pozycje stron
    c = bytearray(b'TPAG\0\0\0\0')
    c += struct.pack('<I', len(tpag_ptrs) + n_new)
    c += b''.join(struct.pack('<I', p) for p in tpag_ptrs)
    new_list_at = len(c)
    c += b'\0' * (4 * n_new)
    tpag_off = {}
    for gi, tex, png, placed, size in pages:
        for sprite, ch, box, (px, py) in placed:
            x0, y0, x1, y1 = box
            s = sprites[sprite]
            tpag_off[(sprite, ch)] = len(c)
            c += struct.pack('<11H', px, py, x1 - x0, y1 - y0, x0, y0, x1 - x0, y1 - y0,
                             s.width, s.height, tex)
            c += b'\0\0'                   # wyrównanie do 4
    for i, key in enumerate(tpag_off):
        struct.pack_into('<I', c, new_list_at + 4 * i, C + tpag_off[key])
    sprite_off = {}
    for name in FONT_SPRITES:
        s = sprites[name]
        new = [C + tpag_off[(name, ch)] for ch in glyphs[name]]
        sprite_off[name] = len(c)
        c += d[s.offset:s.frames_at] + struct.pack('<I', len(s.frames) + len(new))
        c += b''.join(struct.pack('<I', f) for f in s.frames + new) + s.tail
        while len(c) % 4:
            c += b'\0'
    list_off = {}
    for gi, tex, *_ in pages:
        old = groups[gi]['textures']
        list_off[gi] = len(c)
        c += struct.pack(f'<{len(old) + 2}I', len(old) + 1, *old, tex)
    template = tex_ptrs[dw.tpag(sprites['spr_vcr_font'].frames[0]).texture]
    entry_off = []
    for _ in pages:
        entry_off.append(len(c))
        c += d[template:template + 8] + b'\0\0\0\0'
    LC = align(len(c), 0x80)               # dane TXTR za nim zachowują wyrównanie
    c += b'\0' * (LC - len(c))
    struct.pack_into('<I', c, 4, LC - 8)

    # --- blok P: nowe wskaźniki na liście stron TXTR
    LA = align(4 * len(pages), 0x80)
    a = bytearray(LA)
    for k in range(len(pages)):
        struct.pack_into('<I', a, 4 * k, C + entry_off[k])

    # --- blok Q: obrazki stron, każdy wyrównany do 0x80
    b = bytearray()
    png_off = []
    for gi, tex, png, *_ in pages:
        b += b'\0' * (align(Q + len(b), 0x80) - Q - len(b))
        png_off.append(len(b))
        b += png
    LB = align(len(b), 0x80)
    b += b'\0' * (LB - len(b))
    for k in range(len(pages)):
        struct.pack_into('<I', c, entry_off[k] + 8, Q + LC + LA + png_off[k])

    # wskaźniki za punktami wstawienia przesuwają się o długość wstawek przed nimi
    w = bytearray(d)
    def bump(at):
        v = u32(w, at)
        if v >= Q:
            struct.pack_into('<I', w, at, v + LC + LA + LB)
        elif v >= P:
            struct.pack_into('<I', w, at, v + LC + LA)
        elif v >= C:
            struct.pack_into('<I', w, at, v + LC)
    for i in range(n_tex):
        bump(tex_start + 4 + 4 * i)
        bump(tex_ptrs[i] + 8)              # adres PNG w pozycji strony
    audo_start, audo_ptrs = dw.pointer_list('AUDO')
    for i in range(len(audo_ptrs)):
        bump(audo_start + 4 + 4 * i)
    struct.pack_into('<I', w, tex_start, n_tex + len(pages))
    struct.pack_into('<I', w, tex_start - 4, dw.chunks['TXTR'][1] + LA + LB)
    struct.pack_into('<I', w, 4, u32(w, 4) + LC + LA + LB)
    for name in FONT_SPRITES:
        struct.pack_into('<I', w, sprites[name].list_slot, C + sprite_off[name])
    for gi in list_off:
        struct.pack_into('<I', w, groups[gi]['at'] + 4, C + list_off[gi])
    w[Q:Q] = b
    w[P:P] = a
    w[C:C] = c
    out.write_bytes(w)
    return {'glyphs': n_new,
            'pages': [(groups[gi]['name'], tex, size) for gi, tex, png, placed, size in pages],
            'block': LC + LA + LB}


def verify_win(src: Path, built: Path, glyphs: dict[str, dict[str, Image.Image]]):
    a, b = DataWin(src), DataWin(built)
    want = list(a.order)
    want.insert(want.index('TXTR'), 'TPAG')
    if b.order != want:
        raise SystemExit(f'weryfikacja data.win: chunki {b.order}, oczekiwano {want}')
    sa, sb = a.sprites(), b.sprites()
    new_tpag = []
    for name in sa:
        fa, fb = sa[name].frames, sb[name].frames
        extra = list(glyphs.get(name, {}).values())
        if fb[:len(fa)] != fa or len(fb) != len(fa) + len(extra):
            raise SystemExit(f'weryfikacja data.win: klatki {name}')
        for img, ptr in zip(extra, fb[len(fa):]):
            if b.frame_image(ptr).tobytes() != img.tobytes():
                raise SystemExit(f'weryfikacja data.win: litera w {name} nie zgadza się z wzorem')
            new_tpag.append(ptr)
    # runner czyta ostatni chunk TPAG: stara lista w tej samej kolejności plus nasze pozycje
    old_list = a.pointer_list('TPAG')[1]
    got = b.pointer_list('TPAG')[1]        # DataWin pamięta ostatni chunk o danej nazwie
    if got[:len(old_list)] != old_list or sorted(got[len(old_list):]) != sorted(new_tpag):
        raise SystemExit('weryfikacja data.win: nowa lista TPAG nie jest starą plus nasze pozycje')
    ta, tb = a.texture_entries(), b.texture_entries()
    for i in range(len(ta)):
        pa, pb = u32(a.data, ta[i] + 8), u32(b.data, tb[i] + 8)
        if a.data[pa:pa + 64] != b.data[pb:pb + 64]:
            raise SystemExit(f'weryfikacja data.win: strona tekstury {i}')
    pngs = [u32(b.data, t + 8) for t in tb]
    if pngs != sorted(pngs) or any(p % 0x80 for p in pngs):
        raise SystemExit('weryfikacja data.win: obrazki stron poza kolejnością albo niewyrównane')
    for p in new_tpag:
        if b.tpag(p).texture >= len(tb):
            raise SystemExit('weryfikacja data.win: pozycja TPAG wskazuje nieistniejącą stronę')
    # każda strona z literami należy do grupy tekstur swojego fontu
    ga, gb = texture_groups(a), texture_groups(b)
    for name in glyphs:
        idx = sb[name].index
        pages = {b.tpag(p).texture for p in sb[name].frames[len(sa[name].frames):]}
        group = next(g for g in gb if idx in g['sprites'])
        if not pages <= set(group['textures']):
            raise SystemExit(f'weryfikacja data.win: strona liter {name} poza grupą {group["name"]}')
    for g0, g1 in zip(ga, gb):
        if g1['textures'][:len(g0['textures'])] != g0['textures'] or g0['sprites'] != g1['sprites']:
            raise SystemExit(f'weryfikacja data.win: grupa {g0["name"]} zmieniona poza nowymi stronami')
    aa, ab = a.pointer_list('AUDO')[1], b.pointer_list('AUDO')[1]
    for pa, pb in zip(aa, ab):
        n = u32(a.data, pa)
        if u32(b.data, pb) != n or a.data[pa:pa + 4 + min(n, 4096)] != b.data[pb:pb + 4 + min(n, 4096)]:
            raise SystemExit('weryfikacja data.win: dźwięk przesunięty źle')


# ---------------------------------------------------------------- całość

def font_glyphs(dw: DataWin, maps: dict[str, str]):
    sprites = dw.sprites()
    glyphs = {name: glyphs_for(dw, sprites[name], maps[name]) for name in FONT_SPRITES}
    new_maps = {}
    for name in FONT_SPRITES:
        old = maps[name]
        new = old + ''.join(glyphs[name])
        if old in new_maps and new_maps[old] != new:
            raise SystemExit(f'{name}: wspólna mapa znaków dostała różne litery')
        new_maps[old] = new
    return glyphs, new_maps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--game', required=True, type=Path)
    ap.add_argument('--out', type=Path, default=ROOT / 'dist' / 'build')
    a = ap.parse_args()
    src_exe, src_win = a.game / EXE_NAME, a.game / 'data.win'
    for p, want in ((src_exe, EXE_SHA256), (src_win, WIN_SHA256)):
        got = sha256(p)
        if got != want:
            sys.exit(f'{p.name}: SHA-256 {got}, oczekiwano {want} (GOG 1.0.5). Nic nie zapisano.')
    pl = json.loads((ROOT / 'translations' / 'pl.json').read_text(encoding='utf-8'))
    maps = json.loads((ROOT / 'work' / 'fontmaps.json').read_text(encoding='utf-8'))
    dw = DataWin(src_win)
    glyphs, new_maps = font_glyphs(dw, maps)
    a.out.mkdir(parents=True, exist_ok=True)
    out_exe, out_win = a.out / EXE_NAME, a.out / 'data.win'
    se = build_exe(src_exe, pl, new_maps, out_exe)
    verify_exe(src_exe, out_exe, pl, new_maps)
    sw = build_win(src_win, glyphs, out_win)
    verify_win(src_win, out_win, glyphs)
    print(f'exe: {se["translated"]} wpisów po polsku, {se["english"]} po angielsku '
          f'(z {se["entries"]}), sekcja {se["section_bytes"]} B')
    pages = ', '.join(f'{t} ({g}, {w}x{h})' for g, t, (w, h) in sw['pages'])
    print(f'data.win: {sw["glyphs"]} liter na stronach {pages}, bloki {sw["block"]} B')
    print(f'wynik: {a.out}')


if __name__ == '__main__':
    main()
