"""Teach LanguageToggleGroup.LoadCurLanguage about Polish.

Four methods in Assembly-CSharp map a saved language code to something. Three of
them - GlobalVars.SetLanguage, GlobalVars.SaveLanguageStr and
GlobalVars.InitialGameLanguage - already handle 'pol'; the game is Polish-ready
below the surface, which is why it picks Polish up from a Polish Windows on its
own. The one that does not is LanguageToggleGroup.LoadCurLanguage, the menu's
own lookup: it turns the saved string into an index into the array of language
buttons, and an unknown string falls through to 0. That is why the menu ticks
English while the game runs in Polish, and why reopening the menu can write
'eng' back over the saved language.

The method's body is replaced in place with an equivalent that also maps 'pol'.
The original is a compiler-generated hash switch over nine strings, 447 bytes;
the replacement is a plain if-chain over ten, 234 bytes, padded with nops back
to the same length so no offset in the assembly moves. Nothing else in the file
changes - not the header, not the local signature, not one other method.
"""
import struct
import dnfile

# Every three-letter language code has exactly one entry in the user string heap.
CODE_TOKENS = {
    'eng': 0x700092A4, 'fre': 0x700092AC, 'ger': 0x700092B4, 'por': 0x700092BC,
    'rus': 0x700092C4, 'spa': 0x700092CC, 'chn': 0x700092D4, 'cht': 0x700092DC,
    'jan': 0x700092E4, 'pol': 0x7002BCA0,
}
# Index order the rest of the game already uses; eng is index 0 and the fallback.
INDEXED = [('fre', 1), ('ger', 2), ('por', 3), ('rus', 4), ('spa', 5),
           ('chn', 6), ('cht', 7), ('jan', 8), ('pol', 9)]

PROLOGUE = bytes.fromhex('72 88 92 00 70 7e b3 11 00 04 6f f5 0e 00 06 72 9a 92 00 70 28 4d 00 00 2b 0a')
EPILOGUE = bytes.fromhex('02 7b a1 0c 00 04 02 7b a2 0c 00 04 9a 17 6f 51 01 00 0a 2a')
STORE_INDEX = bytes.fromhex('7d a2 0c 00 04')      # stfld curInt
STRING_EQUALS = bytes.fromhex('28 3a 01 00 0a')    # call String::op_Equality
LOAD_SAVED, LOAD_THIS, NOP = b'\x06', b'\x02', b'\x00'


def constant(value):
    return bytes([0x16 + value]) if value <= 8 else b'\x1f' + bytes([value])


def compiled():
    """The replacement method body, before padding."""
    code = bytearray(PROLOGUE)
    code += LOAD_THIS + constant(0) + STORE_INDEX          # curInt = 0, the fallback
    for name, index in INDEXED:
        assign = LOAD_THIS + constant(index) + STORE_INDEX
        code += LOAD_SAVED
        code += b'\x72' + struct.pack('<I', CODE_TOKENS[name])
        code += STRING_EQUALS
        code += b'\x2c' + bytes([len(assign)])             # brfalse.s past the assignment
        code += assign
    return bytes(code), EPILOGUE


def locate(path):
    """(file offset, size) of LoadCurLanguage's body, and a sanity check on its header."""
    pe = dnfile.dnPE(str(path))
    data = pe.__data__
    for row in pe.net.mdtables.TypeDef.rows:
        if row.TypeName != 'LanguageToggleGroup':
            continue
        for member in row.MethodList:
            method = member.row
            if method is None or method.Name != 'LoadCurLanguage':
                continue
            at = pe.get_offset_from_rva(method.Rva)
            flags = struct.unpack_from('<H', data, at)[0]
            assert flags & 3 == 3, 'Expected a fat method header.'
            assert not flags & 8, 'The method carries extra sections.'
            assert struct.unpack_from('<H', data, at + 2)[0] >= 3, 'Max stack too small.'
            size = struct.unpack_from('<I', data, at + 4)[0]
            return at + (flags >> 12) * 4, size
    raise AssertionError('LanguageToggleGroup.LoadCurLanguage not found.')


def patch(path):
    """The assembly's bytes with the method replaced. Refuses anything unexpected."""
    original = path.read_bytes()
    start, size = locate(path)
    body = original[start:start + size]
    assert body.startswith(PROLOGUE), 'The method does not start as expected.'
    assert body.endswith(EPILOGUE), 'The method does not end as expected.'
    assert body.count(STORE_INDEX) == 11, body.count(STORE_INDEX)   # nine languages, two fallbacks
    assert struct.pack('<I', CODE_TOKENS['pol']) not in body, 'Polish is already handled.'

    head, tail = compiled()
    padding = size - len(head) - len(tail)
    assert padding >= 0, f'Replacement is {-padding} bytes too long.'
    replacement = head + NOP * padding + tail
    assert len(replacement) == size
    return original[:start] + replacement + original[start + size:], {
        'method_at': start, 'body_size': size, 'written': len(head) + len(tail), 'nops': padding,
    }
