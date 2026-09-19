"""Turn the disabled Italian language button into a working Polish one.

Every scene that carries the options menu holds ten language buttons. Nine of
them are children of Language_ToggleGroup, which lays them out with a
GridLayoutGroup and holds them in LanguageToggleGroup.filterToggle, the array
the menu indexes by language. The tenth, LanguagePick_ita_03, is a complete
Italian button the developers switched off and moved out to the sibling
Language_Toggle_Panel - which is why simply enabling it puts an unstyled,
half-visible button below the grid instead of in it.

So the button is moved back: reparented under the grid, appended to the array
as index 9, and given the language code and label to match.
"""
import struct
import UnityPy

CODE_FROM, CODE_TO = b'\x03\x00\x00\x00ita\x00', b'\x03\x00\x00\x00pol\x00'
LABEL_FROM, LABEL_TO = b'\x08\x00\x00\x00Italiano', b'\x06\x00\x00\x00Polski\0\0'
TOGGLE_NAME, GRID_NAME = 'LanguagePick_ita_03', 'Language_ToggleGroup'
POLISH_INDEX = 9


def pointer(path_id):
    return struct.pack('<iq', 0, path_id)


class Scene:
    def __init__(self, path):
        self.env = UnityPy.load(str(path))
        self.objects = {o.path_id: o for o in self.env.objects}
        self.raw = {i: o.get_raw_data() for i, o in self.objects.items()}
        self.changed = {}

    # --- reading ---

    def components(self, game_object):
        raw = self.raw[game_object]
        count = struct.unpack_from('<i', raw, 0)[0]
        return [struct.unpack_from('<iq', raw, 4 + 12 * i)[1] for i in range(count)]

    def name(self, game_object):
        raw = self.raw[game_object]
        at = 4 + 12 * struct.unpack_from('<i', raw, 0)[0] + 4
        length = struct.unpack_from('<i', raw, at)[0]
        return raw[at + 4:at + 4 + length].decode('utf-8')

    def find(self, wanted):
        for path_id, obj in self.objects.items():
            if obj.type.name == 'GameObject' and self.name(path_id) == wanted:
                return path_id
        raise AssertionError(f'No GameObject named {wanted}')

    def component(self, game_object, kind):
        found = [c for c in self.components(game_object) if self.objects[c].type.name == kind]
        assert len(found) == 1, (game_object, kind, found)
        return found[0]

    def children_at(self, transform):
        """Offset of the children array inside a RectTransform blob, and the ids in it."""
        at = 12 + 16 + 12 + 12
        count = struct.unpack_from('<i', self.raw[transform], at)[0]
        ids = [struct.unpack_from('<iq', self.raw[transform], at + 4 + 12 * i)[1] for i in range(count)]
        return at, ids

    # --- writing ---

    def write(self, path_id, raw):
        self.changed[path_id] = raw
        self.raw[path_id] = raw

    def reparent(self, transform, old_parent, new_parent):
        at, ids = self.children_at(old_parent)
        assert transform in ids, 'Not a child of the panel it was expected under.'
        keep = [i for i in ids if i != transform]
        raw = self.raw[old_parent]
        self.write(old_parent, raw[:at] + struct.pack('<i', len(keep))
                   + b''.join(pointer(i) for i in keep) + raw[at + 4 + 12 * len(ids):])

        at, ids = self.children_at(new_parent)
        assert transform not in ids
        raw = self.raw[new_parent]
        self.write(new_parent, raw[:at] + struct.pack('<i', len(ids) + 1)
                   + b''.join(pointer(i) for i in ids + [transform]) + raw[at + 4 + 12 * len(ids):])

        at, ids = self.children_at(transform)
        after = at + 4 + 12 * len(ids)
        raw = self.raw[transform]
        assert struct.unpack_from('<iq', raw, after)[1] == old_parent
        # m_Father, then the anchors; reset the stale offset the disabled button carried.
        anchored = after + 12 + 8 + 8
        self.write(transform, raw[:after] + pointer(new_parent) + raw[after + 12:anchored]
                   + struct.pack('<2f', 0.0, 0.0) + raw[anchored + 8:])

    def append_to_array(self, manager, toggle):
        raw = self.raw[manager]
        at = 32                                    # past m_GameObject, m_Enabled, m_Script, empty m_Name
        count = struct.unpack_from('<i', raw, at)[0]
        assert count == 9, count
        ids = [struct.unpack_from('<iq', raw, at + 4 + 12 * i)[1] for i in range(count)]
        assert toggle not in ids
        self.write(manager, raw[:at] + struct.pack('<i', count + 1)
                   + b''.join(pointer(i) for i in ids + [toggle]) + raw[at + 4 + 12 * count:])

    def save(self, destination):
        for path_id, raw in self.changed.items():
            self.objects[path_id].set_raw_data(raw)
        destination.write_bytes(self.env.file.save())


def patch(path, destination):
    scene = Scene(path)
    button = scene.find(TOGGLE_NAME)
    grid = scene.find(GRID_NAME)

    # The button's own pieces.
    transform = scene.component(button, 'RectTransform')
    mapping = next(c for c in scene.components(button)
                   if scene.objects[c].type.name == 'MonoBehaviour' and CODE_FROM in scene.raw[c])
    toggle = struct.unpack_from('<q', scene.raw[mapping], 40)[0]
    assert toggle in scene.components(button), 'The mapping points outside its own button.'

    label = next(c for kid in scene.children_at(transform)[1]
                 for c in scene.components(struct.unpack_from('<q', scene.raw[kid], 4)[0])
                 if scene.objects[c].type.name == 'MonoBehaviour' and LABEL_FROM in scene.raw[c])

    # The grid it belongs in, and the array the menu indexes.
    grid_transform = scene.component(grid, 'RectTransform')
    manager = next(c for c in scene.components(grid)
                   if scene.objects[c].type.name == 'MonoBehaviour' and len(scene.raw[c]) == 152
                   and struct.unpack_from('<i', scene.raw[c], 32)[0] == 9)

    # m_IsActive sits past the name's padding and m_Tag.
    raw = scene.raw[button]
    at = 4 + 12 * struct.unpack_from('<i', raw, 0)[0] + 4
    length = struct.unpack_from('<i', raw, at)[0]
    active = at + 4 + (length + 3 & ~3) + 2
    assert raw[active] == 0, 'The Italian button is already enabled.'
    scene.write(button, raw[:active] + b'\1' + raw[active + 1:])

    # Language code and index.
    raw = scene.raw[mapping]
    assert raw.count(CODE_FROM) == 1 and len(raw) == 60
    scene.write(mapping, raw[:48] + CODE_TO + struct.pack('<i', POLISH_INDEX))

    # The label on the button's text child.
    raw = scene.raw[label]
    assert raw.count(LABEL_FROM) == 1
    scene.write(label, raw.replace(LABEL_FROM, LABEL_TO))

    parent = struct.unpack_from('<q', scene.raw[transform],
                                scene.children_at(transform)[0] + 4
                                + 12 * len(scene.children_at(transform)[1]) + 4)[0]
    assert parent != grid_transform, 'The button is already in the grid.'
    scene.reparent(transform, parent, grid_transform)
    scene.append_to_array(manager, toggle)

    scene.save(destination)
    return {'button': button, 'moved_from': parent, 'into': grid_transform, 'toggle': toggle}
