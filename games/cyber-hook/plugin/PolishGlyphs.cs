// Polskie litery dla statycznych atlasów TextMeshPro, składane w czasie działania gry.
//
// Fonty Cyber Hook to atlasy SDF bez ąćęłńśźż (część ma ó). Dla każdego fontu, któremu
// ich brakuje, budujemy mały atlas zapasowy: bazowa litera jest kopiowana z atlasu tego
// samego fontu (ten sam krój i grubość), a znak diakrytyczny (kreska, kropka, ogonek,
// przekreślenie) dorysowujemy jako pole odległości. Zapasowy font trafia na początek
// fallbackFontAssetTable oryginału. Do paczki nie trafia żaden font ani fragment atlasu —
// wszystko powstaje z plików gry na komputerze gracza.
//
// Przeniesione z Void Bastards (stary TMP) na TMP 2.x: glify to Glyph/GlyphRect,
// prostokąty w atlasie liczone od dołu, metryki w GlyphMetrics.

using System;
using System.Collections.Generic;
using HarmonyLib;
using TMPro;
using UnityEngine;
using UnityEngine.TextCore;
using UnityEngine.TextCore.LowLevel;

namespace notgeese.CyberHook
{
    internal static class PolishGlyphs
    {
        private enum Mark { Acute, Dot, Ogonek, Stroke, Low, Copy }

        private struct Recipe
        {
            public char Letter;
            public string Bases; // pierwsza litera bazowa, którą font ma
            public Mark Mark;
            public Recipe(char letter, string bases, Mark mark) { Letter = letter; Bases = bases; Mark = mark; }
        }

        private static readonly Recipe[] Recipes =
        {
            new Recipe('ą', "a", Mark.Ogonek), new Recipe('ć', "c", Mark.Acute), new Recipe('ę', "e", Mark.Ogonek),
            new Recipe('ł', "l", Mark.Stroke), new Recipe('ń', "n", Mark.Acute), new Recipe('ó', "o", Mark.Acute),
            new Recipe('ś', "s", Mark.Acute), new Recipe('ź', "z", Mark.Acute), new Recipe('ż', "z", Mark.Dot),
            new Recipe('Ą', "A", Mark.Ogonek), new Recipe('Ć', "C", Mark.Acute), new Recipe('Ę', "E", Mark.Ogonek),
            new Recipe('Ł', "L", Mark.Stroke), new Recipe('Ń', "N", Mark.Acute), new Recipe('Ó', "O", Mark.Acute),
            new Recipe('Ś', "S", Mark.Acute), new Recipe('Ź', "Z", Mark.Acute), new Recipe('Ż', "Z", Mark.Dot),
            // Polskie cudzysłowy: zamykający to prosty cudzysłów fontu, otwierający ten sam kształt na linii bazowej.
            new Recipe('”', "\"", Mark.Copy), new Recipe('„', "”\"", Mark.Low),
        };

        private static readonly HashSet<int> Done = new HashSet<int>();

        /// Uzupełnij wszystkie załadowane fonty TMP. Zwraca liczbę uzupełnionych fontów.
        internal static int PatchLoadedFonts()
        {
            var patched = 0;
            foreach (var font in Resources.FindObjectsOfTypeAll<TMP_FontAsset>())
            {
                if (font == null || Done.Contains(font.GetInstanceID())) continue;
                try
                {
                    bool final;
                    if (Patch(font, out final)) patched++;
                    if (final) Done.Add(font.GetInstanceID());
                }
                catch (Exception error)
                {
                    Done.Add(font.GetInstanceID());
                    Plugin.Log.LogWarning("Font „" + font.name + "”: nie udało się złożyć polskich liter: " + error.Message);
                }
            }
            return patched;
        }

        /// final = nie ma sensu próbować ponownie (gotowe albo font nie ma z czego składać).
        private static bool Patch(TMP_FontAsset font, out bool final)
        {
            final = true;
            if (font.name.StartsWith("notgeese", StringComparison.Ordinal)) return false;
            if (font.material == null || font.atlasTextures == null || font.atlasTextures.Length == 0)
            {
                final = false; // font jeszcze się ładuje
                return false;
            }

            // Font, którego gra jeszcze nie użyła, ma w tabeli znaków puste glify; getter je wypełnia.
            if (font.characterLookupTable == null) { final = false; return false; }
            var own = OwnCharacters(font);

            // Font dynamiczny dorysowuje litery w locie: najpierw niech dorysuje bazowe.
            if (font.atlasPopulationMode == AtlasPopulationMode.Dynamic && font.sourceFontFile != null)
            {
                var bases = "IlLE";
                foreach (var recipe in Recipes)
                    if (!own.ContainsKey(recipe.Letter) && recipe.Mark != Mark.Copy && recipe.Mark != Mark.Low)
                        bases += recipe.Bases;
                string missing;
                font.TryAddCharacters(bases, out missing);
                own = OwnCharacters(font);
            }

            var wanted = new List<KeyValuePair<Recipe, Glyph>>();
            foreach (var recipe in Recipes)
            {
                if (own.ContainsKey(recipe.Letter)) continue;
                var glyph = BaseGlyph(recipe, own, wanted);
                if (glyph != null) wanted.Add(new KeyValuePair<Recipe, Glyph>(recipe, glyph));
            }
            if (wanted.Count == 0) return false;

            var padding = Mathf.Max(1, font.atlasPadding);
            var gradient = font.material.HasProperty("_GradientScale") ? font.material.GetFloat("_GradientScale") : padding + 1f;
            var atlases = new Dictionary<int, byte[]>();

            var stroke = MeasureStroke(font, own, atlases);
            var cells = new List<Cell>();
            foreach (var pair in wanted)
                cells.Add(Compose(pair.Key, pair.Value, Alpha(font, pair.Value.atlasIndex, atlases),
                    font.atlasTextures[pair.Value.atlasIndex], padding, gradient, stroke, font.faceInfo.ascentLine));

            var fallback = Build(font, cells, padding);
            if (font.fallbackFontAssetTable == null) font.fallbackFontAssetTable = new List<TMP_FontAsset>();
            font.fallbackFontAssetTable.Insert(0, fallback);

            var letters = "";
            foreach (var pair in wanted) letters += pair.Key.Letter;
            Plugin.Log.LogInfo(string.Format("Font TMP „{0}”: złożono {1} ({2} px kreski, atlas {3}×{4}).",
                font.name, letters, stroke.ToString("0.0"), fallback.atlasTexture.width, fallback.atlasTexture.height));
            return true;
        }

        /// Tylko własne znaki fontu: słownik wyszukiwania trzyma też znaki znalezione w fontach zapasowych.
        private static Dictionary<uint, TMP_Character> OwnCharacters(TMP_FontAsset font)
        {
            var own = new Dictionary<uint, TMP_Character>();
            foreach (var character in font.characterTable)
                if (character != null && character.glyph != null && !own.ContainsKey(character.unicode))
                    own[character.unicode] = character;
            return own;
        }

        /// Litera bazowa z własnego atlasu fontu; dla „„” może nią być świeżo złożony „””.
        private static Glyph BaseGlyph(Recipe recipe, Dictionary<uint, TMP_Character> own, List<KeyValuePair<Recipe, Glyph>> wanted)
        {
            foreach (var b in recipe.Bases)
            {
                TMP_Character character;
                if (own.TryGetValue(b, out character) && character.glyph.glyphRect.width > 0) return character.glyph;
                foreach (var pair in wanted)
                    if (pair.Key.Letter == b && pair.Key.Mark == Mark.Copy) return pair.Value;
            }
            return null;
        }

        // ---------- atlas ----------

        private static byte[] Alpha(TMP_FontAsset font, int index, Dictionary<int, byte[]> cache)
        {
            byte[] alpha;
            if (!cache.TryGetValue(index, out alpha))
            {
                alpha = ReadAlpha(font.atlasTextures[index]);
                cache[index] = alpha;
            }
            return alpha;
        }

        private static byte[] ReadAlpha(Texture2D texture)
        {
            var target = RenderTexture.GetTemporary(texture.width, texture.height, 0, RenderTextureFormat.ARGB32, RenderTextureReadWrite.Linear);
            var previous = RenderTexture.active;
            try
            {
                Graphics.Blit(texture, target);
                RenderTexture.active = target;
                var copy = new Texture2D(texture.width, texture.height, TextureFormat.RGBA32, false, true);
                copy.ReadPixels(new Rect(0, 0, texture.width, texture.height), 0, 0);
                copy.Apply();
                var pixels = copy.GetPixels32(); // wiersze od dołu, tak jak GlyphRect
                UnityEngine.Object.Destroy(copy);
                var alpha = new byte[pixels.Length];
                for (var i = 0; i < pixels.Length; i++) alpha[i] = pixels[i].a;
                return alpha;
            }
            finally
            {
                RenderTexture.active = previous;
                RenderTexture.ReleaseTemporary(target);
            }
        }

        /// Grubość kreski fontu: najdłuższy poziomy odcinek „wnętrza” w połowie wysokości „I” albo „l”.
        private static float MeasureStroke(TMP_FontAsset font, Dictionary<uint, TMP_Character> own, Dictionary<int, byte[]> atlases)
        {
            foreach (var probe in new[] { 'I', 'l', 'i', 'L', 'E' })
            {
                TMP_Character character;
                if (!own.TryGetValue(probe, out character)) continue;
                var rect = character.glyph.glyphRect;
                var texture = font.atlasTextures[character.glyph.atlasIndex];
                var alpha = Alpha(font, character.glyph.atlasIndex, atlases);
                var row = rect.y + rect.height / 2;
                if (row < 0 || row >= texture.height) continue;
                int best = 0, run = 0;
                for (var x = rect.x; x < rect.x + rect.width && x < texture.width; x++)
                {
                    run = alpha[row * texture.width + x] >= 128 ? run + 1 : 0;
                    best = Math.Max(best, run);
                }
                if (best > 0) return Mathf.Clamp(best, rect.height * 0.08f, rect.height * 0.3f);
            }
            TMP_Character e;
            return own.TryGetValue('E', out e) ? e.glyph.glyphRect.height * 0.15f : 4f;
        }

        // ---------- składanie litery ----------

        private sealed class Cell
        {
            public uint Id;
            public int Width, Height;
            public byte[] Alpha;
            public float BoxWidth, BoxHeight;
            public GlyphMetrics Metrics;
            public float Scale;
        }

        private struct Capsule
        {
            public Vector2 A, B;
            public float Radius;
            public bool Square;
            public Capsule(Vector2 a, Vector2 b, float radius, bool square = false) { A = a; B = b; Radius = radius; Square = square; }
        }

        private static Cell Compose(Recipe recipe, Glyph glyph, byte[] source, Texture2D atlas, int padding, float gradient,
            float stroke, float ascent)
        {
            var rect = glyph.glyphRect;
            float w = rect.width, h = rect.height;
            var m = glyph.metrics;
            // Metryki są w jednostkach fontu; zwykle równe pikselom atlasu, ale nie zakładamy tego.
            var kx = w > 0 ? m.width / w : 1f;
            var ky = h > 0 ? m.height / h : 1f;

            // Znak nie grubszy niż piąta część litery — w grubych krojach kreska pnia bywa szersza.
            var t = Mathf.Min(stroke, h * 0.2f);
            // Miejsce nad literą do linii wydłużeń górnych fontu. W krojach samych wersalików jest go
            // mało, a okna gry (np. dialog Drona) ucinają wszystko ponad nią maską. Znak nad literą
            // mieści się w tym miejscu, a gdy go brak — jest zwarty, ale nie cieńszy niż 1,3 kreski.
            var room = Mathf.Max((ascent - m.horizontalBearingY) / ky, t * 1.3f);
            var gap = Mathf.Min(t * 0.6f, room * 0.2f);
            var shapes = new List<Capsule>();
            switch (recipe.Mark)
            {
                case Mark.Acute:
                    {
                        var cx = w * 0.5f;
                        var r = Mathf.Min(t * 0.42f, (room - gap) * 0.3f);
                        var rise = Mathf.Clamp(room - gap - 2f * r, t * 0.2f, t);
                        shapes.Add(new Capsule(new Vector2(cx - t * 0.35f, h + gap + r),
                            new Vector2(cx + t * 0.75f, h + gap + r + rise), r));
                        break;
                    }
                case Mark.Dot:
                    {
                        var r = Mathf.Min(t * 0.5f, (room - gap) * 0.5f);
                        var c = new Vector2(w * 0.5f, h + gap + r);
                        shapes.Add(new Capsule(c, c, r, true));
                        break;
                    }
                case Mark.Ogonek:
                    {
                        var x = w - t * 0.55f;
                        shapes.Add(new Capsule(new Vector2(x, t * 0.3f), new Vector2(x - t * 0.45f, -t * 0.85f), t * 0.38f));
                        shapes.Add(new Capsule(new Vector2(x - t * 0.45f, -t * 0.85f), new Vector2(x + t * 0.35f, -t * 1.35f), t * 0.34f));
                        break;
                    }
                case Mark.Stroke:
                    {
                        // „L” ma pień z lewej, „l” pośrodku.
                        var stem = char.IsUpper(recipe.Letter) ? t * 0.5f : w * 0.5f;
                        shapes.Add(new Capsule(new Vector2(stem - t * 0.95f, h * 0.36f), new Vector2(stem + t * 1.25f, h * 0.62f), t * 0.4f));
                        break;
                    }
            }

            float minX = 0, minY = 0, maxX = w, maxY = h;
            foreach (var s in shapes)
            {
                minX = Mathf.Min(minX, Mathf.Min(s.A.x, s.B.x) - s.Radius);
                minY = Mathf.Min(minY, Mathf.Min(s.A.y, s.B.y) - s.Radius);
                maxX = Mathf.Max(maxX, Mathf.Max(s.A.x, s.B.x) + s.Radius);
                maxY = Mathf.Max(maxY, Mathf.Max(s.A.y, s.B.y) + s.Radius);
            }
            minX = Mathf.Floor(minX);
            minY = Mathf.Floor(minY);
            maxX = Mathf.Ceil(maxX);
            maxY = Mathf.Ceil(maxY);

            var bearingY = m.horizontalBearingY + (maxY - h) * ky;
            // Cudzysłów dolny: ten sam kształt, dół tuż pod linią bazową.
            if (recipe.Mark == Mark.Low) bearingY = m.height * 0.15f;

            var cell = new Cell
            {
                Id = recipe.Letter,
                BoxWidth = maxX - minX,
                BoxHeight = maxY - minY,
                Scale = glyph.scale,
            };
            cell.Metrics = new GlyphMetrics(cell.BoxWidth * kx, cell.BoxHeight * ky,
                m.horizontalBearingX + minX * kx, bearingY,
                Mathf.Max(m.horizontalAdvance, m.horizontalBearingX + maxX * kx));
            cell.Width = (int)cell.BoxWidth + padding * 2;
            cell.Height = (int)cell.BoxHeight + padding * 2;
            cell.Alpha = new byte[cell.Width * cell.Height];

            for (var cy = 0; cy < cell.Height; cy++)
            {
                for (var cx = 0; cx < cell.Width; cx++)
                {
                    // Współrzędne w układzie litery bazowej (0,0 = lewy dolny róg jej prostokąta).
                    var bu = cx - padding + (int)minX;
                    var bv = cy - padding + (int)minY;
                    var baseAlpha = 0;
                    var sx = rect.x + bu;
                    var sy = rect.y + bv;
                    if (bu >= -padding && bu < w + padding && bv >= -padding && bv < h + padding
                        && sx >= 0 && sx < atlas.width && sy >= 0 && sy < atlas.height)
                        baseAlpha = source[sy * atlas.width + sx];

                    var point = new Vector2(bu + 0.5f, bv + 0.5f);
                    var distance = float.MaxValue;
                    foreach (var s in shapes) distance = Mathf.Min(distance, Distance(point, s));
                    var markAlpha = Mathf.Clamp01(0.5f - distance / (2f * gradient));
                    cell.Alpha[cy * cell.Width + cx] = (byte)Mathf.Max(baseAlpha, Mathf.RoundToInt(markAlpha * 255f));
                }
            }
            return cell;
        }

        private static float Distance(Vector2 p, Capsule s)
        {
            if (s.Square)
            {
                var d = new Vector2(Mathf.Abs(p.x - s.A.x) - s.Radius, Mathf.Abs(p.y - s.A.y) - s.Radius);
                var outside = new Vector2(Mathf.Max(d.x, 0), Mathf.Max(d.y, 0)).magnitude;
                return outside + Mathf.Min(Mathf.Max(d.x, d.y), 0);
            }
            var ab = s.B - s.A;
            var along = ab.sqrMagnitude < 1e-6f ? 0f : Mathf.Clamp01(Vector2.Dot(p - s.A, ab) / ab.sqrMagnitude);
            return (p - (s.A + ab * along)).magnitude - s.Radius;
        }

        // ---------- font zapasowy ----------

        private static TMP_FontAsset Build(TMP_FontAsset font, List<Cell> cells, int padding)
        {
            var size = 64;
            List<Vector2Int> places;
            while (!TryPack(cells, size, out places)) size *= 2;

            var alpha = new byte[size * size];
            var fallback = ScriptableObject.CreateInstance<TMP_FontAsset>();
            fallback.name = "notgeese PL " + font.name;
            for (var i = 0; i < cells.Count; i++)
            {
                var cell = cells[i];
                var place = places[i]; // lewy dolny róg komórki, liczony od dołu atlasu
                for (var y = 0; y < cell.Height; y++)
                    Array.Copy(cell.Alpha, y * cell.Width, alpha, (place.y + y) * size + place.x, cell.Width);
                var rect = new GlyphRect(place.x + padding, place.y + padding, (int)cell.BoxWidth, (int)cell.BoxHeight);
                var glyph = new Glyph(cell.Id, cell.Metrics, rect, cell.Scale, 0);
                fallback.glyphTable.Add(glyph);
                fallback.characterTable.Add(new TMP_Character(cell.Id, glyph));
            }

            var atlas = new Texture2D(size, size, TextureFormat.Alpha8, false, true);
            atlas.name = "notgeese PL atlas";
            atlas.filterMode = FilterMode.Bilinear;
            atlas.wrapMode = TextureWrapMode.Clamp;
            var pixels = new Color32[alpha.Length];
            for (var i = 0; i < alpha.Length; i++) pixels[i] = new Color32(255, 255, 255, alpha[i]);
            atlas.SetPixels32(pixels);
            atlas.Apply(false, false);

            var material = new Material(font.material);
            material.name = fallback.name + " Material";
            material.SetTexture("_MainTex", atlas);
            material.SetFloat("_TextureWidth", size);
            material.SetFloat("_TextureHeight", size);

            // Pola z wewnętrznymi setterami; nazwy sprawdzone w TMP z Unity 2019.4.
            var traverse = Traverse.Create(fallback);
            traverse.Field("m_Version").SetValue("1.1.0");
            traverse.Field("m_AtlasWidth").SetValue(size);
            traverse.Field("m_AtlasHeight").SetValue(size);
            traverse.Field("m_AtlasPadding").SetValue(padding);
            traverse.Field("m_AtlasRenderMode").SetValue(font.atlasRenderMode);
            fallback.faceInfo = font.faceInfo;
            fallback.atlasPopulationMode = AtlasPopulationMode.Static;
            fallback.atlasTextures = new[] { atlas };
            fallback.material = material;
            fallback.ReadFontAssetDefinition();

            UnityEngine.Object.DontDestroyOnLoad(atlas);
            UnityEngine.Object.DontDestroyOnLoad(material);
            UnityEngine.Object.DontDestroyOnLoad(fallback);
            return fallback;
        }

        private static bool TryPack(List<Cell> cells, int size, out List<Vector2Int> places)
        {
            places = new List<Vector2Int>();
            int x = 0, y = 0, shelf = 0;
            foreach (var cell in cells)
            {
                if (cell.Width > size || cell.Height > size) return false;
                if (x + cell.Width > size)
                {
                    x = 0;
                    y += shelf;
                    shelf = 0;
                }
                if (y + cell.Height > size) return false;
                places.Add(new Vector2Int(x, y));
                x += cell.Width + 1;
                shelf = Math.Max(shelf, cell.Height + 1);
            }
            return true;
        }
    }
}
