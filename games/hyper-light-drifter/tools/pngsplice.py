"""Zmiana dolnych rzędów PNG bez przekodowania reszty obrazu.

Strona tekstur to PNG 1024×2048, którego dół jest pusty. Polskie litery rysujemy
w tym pustym pasie, a nowy PNG składamy tak, żeby niósł tylko to, co nasze:

1. strumień deflate oryginału kopiujemy bit w bit do granicy symbolu tuż przed
   pierwszym zmienionym rzędem;
2. w tym miejscu zamykamy bieżący blok jego własnym kodem końca bloku (256) i zerujemy
   w jego nagłówku bit „ostatni blok”, jeśli był ustawiony;
3. resztę danych (nasze rzędy, filtr 0) kompresujemy od nowa i doklejamy bitowo;
4. na końcu nowa suma Adler-32, a IDAT dzielimy tak jak oryginał, więc pierwsze
   fragmenty pliku są identyczne bajt w bajt.

Łatka różnicowa kopiuje wtedy prawie cały PNG z pliku gracza, a nowe bajty to
nagłówek ostatniego IDAT, kilkaset bajtów naszych rzędów i sumy kontrolne.
"""
from __future__ import annotations

import struct
import zlib

from PIL import Image

SIGNATURE = b'\x89PNG\r\n\x1a\n'
ORDER = [16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15]
LBASE = [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 23, 27, 31, 35, 43, 51, 59, 67, 83, 99,
         115, 131, 163, 195, 227, 258]
LEXT = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 0]
DEXT = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12,
        12, 13, 13]


def chunks(png: bytes) -> list[tuple[bytes, bytes]]:
    assert png[:8] == SIGNATURE
    out, o = [], 8
    while True:
        n = struct.unpack_from('>I', png, o)[0]
        kind = png[o + 4:o + 8]
        out.append((kind, png[o + 8:o + 8 + n]))
        o += 12 + n
        if kind == b'IEND':
            return out


def chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))


class Bits:
    def __init__(self, data: bytes):
        self.data, self.pos = data, 0

    def read(self, n: int) -> int:
        v = 0
        for i in range(n):
            v |= ((self.data[self.pos >> 3] >> (self.pos & 7)) & 1) << i
            self.pos += 1
        return v


def huffman(lengths: list[int]) -> dict:
    """Kanoniczny kod deflate: {(długość, kod): symbol}."""
    top = max(lengths)
    counts = [0] * (top + 1)
    for n in lengths:
        if n:
            counts[n] += 1
    code, nxt = 0, [0] * (top + 2)
    for n in range(1, top + 1):
        code = (code + counts[n - 1]) << 1
        nxt[n] = code
    table = {}
    for sym, n in enumerate(lengths):
        if n:
            table[(n, nxt[n])] = sym
            nxt[n] += 1
    return table


def symbol(bits: Bits, table: dict) -> int:
    code = 0
    for n in range(1, 16):
        code = (code << 1) | bits.read(1)
        if (n, code) in table:
            return table[(n, code)]
    raise ValueError('zły kod Huffmana')


FIXED_L = huffman([8] * 144 + [9] * 112 + [7] * 24 + [8] * 8)
FIXED_D = huffman([5] * 30)


def cut_point(stream: bytes, target: int) -> tuple[int, int, int, tuple[int, int]]:
    """Ostatnia granica symbolu przed bajtem `target` danych po dekompresji.

    Zwraca (bit, bajt danych, bit nagłówka bloku, kod końca bloku jako (długość, kod)).
    """
    bits = Bits(stream)
    out = 0
    while True:
        header = bits.pos
        final, kind = bits.read(1), bits.read(2)
        if kind == 0:
            bits.pos = (bits.pos + 7) & ~7
            n = bits.read(16)
            bits.read(16)
            assert out + n <= target, 'blok bez kompresji w miejscu cięcia'
            bits.pos += 8 * n
            out += n
        else:
            if kind == 1:
                lit, dist = FIXED_L, FIXED_D
            else:
                hlit, hdist, hclen = bits.read(5) + 257, bits.read(5) + 1, bits.read(4) + 4
                cl = [0] * 19
                for i in range(hclen):
                    cl[ORDER[i]] = bits.read(3)
                ct, lengths = huffman(cl), []
                while len(lengths) < hlit + hdist:
                    s = symbol(bits, ct)
                    if s < 16:
                        lengths.append(s)
                    elif s == 16:
                        lengths += [lengths[-1]] * (3 + bits.read(2))
                    elif s == 17:
                        lengths += [0] * (3 + bits.read(3))
                    else:
                        lengths += [0] * (11 + bits.read(7))
                lit, dist = huffman(lengths[:hlit]), huffman(lengths[hlit:])
            eob = next(k for k, v in lit.items() if v == 256)
            while True:
                at, before = bits.pos, out
                s = symbol(bits, lit)
                if s == 256:
                    break
                if s < 256:
                    out += 1
                else:
                    s -= 257
                    out += LBASE[s] + bits.read(LEXT[s])
                    d = symbol(bits, dist)
                    bits.read(DEXT[d])
                if out > target:
                    return at, before, header, eob
            if out == target:
                return bits.pos - eob[0], out, header, eob   # przed kodem końca bloku
        assert not final, 'cięcie za końcem strumienia'


def append_bits(buf: list[int], value: int, n: int, msb_first: bool = False):
    for i in range(n):
        buf.append((value >> (n - 1 - i)) & 1 if msb_first else (value >> i) & 1)


def pack(bits: list[int]) -> bytes:
    out = bytearray((len(bits) + 7) // 8)
    for i, b in enumerate(bits):
        out[i >> 3] |= b << (i & 7)
    return bytes(out)


def rows_raw(img: Image.Image, start: int) -> bytes:
    """Rzędy od `start` z filtrem 0 (None)."""
    raw = img.tobytes()
    stride = img.width * 4
    return b''.join(b'\x00' + raw[y * stride:(y + 1) * stride] for y in range(start, img.height))


def splice(png: bytes, image: Image.Image, first_row: int) -> bytes:
    """Nowy PNG: oryginał do rzędu `first_row`, dalej rzędy z `image`."""
    parts = chunks(png)
    idat = b''.join(data for kind, data in parts if kind == b'IDAT')
    header, stream = idat[:2], idat[2:]
    assert header[0] & 0x0f == 8 and not header[1] & 0x20, 'zlib bez słownika'
    ihdr = parts[0][1]
    width, height, depth, color, _, _, interlace = struct.unpack('>IIBBBBB', ihdr)
    assert (width, height, depth, color, interlace) == (image.width, image.height, 8, 6, 0)
    stride = 1 + width * 4
    original = zlib.decompress(idat)
    assert len(original) == stride * height

    bit, out, block, eob = cut_point(stream, first_row * stride)
    bits = []
    head = stream[:(bit + 7) // 8]
    for i in range(bit):
        bits.append((head[i >> 3] >> (i & 7)) & 1)
    bits[block] = 0                                   # blok przestaje być ostatnim
    append_bits(bits, eob[1], eob[0], msb_first=True)
    data = original[:out] + original[out:first_row * stride] + rows_raw(image, first_row)
    tail = zlib.compressobj(9, zlib.DEFLATED, -15, 9)
    rest = tail.compress(data[out:]) + tail.flush()
    for byte in rest:
        append_bits(bits, byte, 8)
    new_stream = header + pack(bits) + struct.pack('>I', zlib.adler32(data))
    assert zlib.decompress(new_stream) == data

    # IDAT w tych samych kawałkach co oryginał, ostatni bierze resztę.
    sizes = [len(d) for kind, d in parts if kind == b'IDAT']
    pieces, o = [], 0
    for n in sizes[:-1]:
        if o + n >= len(new_stream):
            break
        pieces.append(new_stream[o:o + n])
        o += n
    pieces.append(new_stream[o:])
    result = SIGNATURE
    written = False
    for kind, d in parts:
        if kind == b'IDAT':
            if not written:
                result += b''.join(chunk(b'IDAT', p) for p in pieces)
                written = True
        else:
            result += chunk(kind, d)
    return result
