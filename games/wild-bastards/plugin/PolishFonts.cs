// Polskie litery w fontach TextMeshPro Wild Bastards.
//
// Atlasy SDF gry są statyczne i nie mają ąćęłńśźż, ale gra ma w folderze Resources pliki TTF
// tych samych krojów (Southbank Spurs, Grindstone Display, Josefin Sans). Dla każdego atlasu
// bez polskich liter tworzymy dynamiczny TMP_FontAsset z TTF tej samej rodziny i wpinamy go
// jako pierwszy font zapasowy — brakujące glify dorysowują się w locie tym samym krojem.
// Do paczki nie trafia żaden font.

using System;
using System.Collections.Generic;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.TextCore.LowLevel;

namespace NieGesi.WildBastards
{
    internal static class PolishFonts
    {
        private static readonly HashSet<int> Done = new HashSet<int>();
        private static Dictionary<string, Font> fonts;

        internal static void PatchLoadedFonts()
        {
            LoadFonts();
            foreach (var asset in Resources.FindObjectsOfTypeAll<TMP_FontAsset>())
            {
                if (asset == null || Done.Contains(asset.GetInstanceID())) continue;
                Done.Add(asset.GetInstanceID());
                try
                {
                    Patch(asset);
                }
                catch (Exception error)
                {
                    Plugin.Log.LogWarning("Font „" + asset.name + "”: " + error.Message);
                }
            }
        }

        private static void LoadFonts()
        {
            if (fonts != null) return;
            fonts = new Dictionary<string, Font>();
            // Najpierw nazwy plików, potem nazwy rodzin — i tylko jeśli klucz jest wolny, bo
            // SouthbankSpurs-Italic też deklaruje rodzinę „Southbank Spurs” i nadpisywał prostą.
            var all = new List<Font>(Resources.LoadAll<Font>("Fonts"));
            all.AddRange(Resources.FindObjectsOfTypeAll<Font>());
            foreach (var font in all)
                if (font != null && !fonts.ContainsKey(Key(font.name))) fonts[Key(font.name)] = font;
            foreach (var font in all) Remember(font);
            Plugin.Log.LogInfo("Pliki TTF gry dostępne dla polskich liter: " + string.Join(", ", new List<string>(fonts.Keys).ToArray()));
        }

        private static void Remember(Font font)
        {
            if (font == null || font.fontNames == null) return;
            if (font.name.IndexOf("italic", StringComparison.OrdinalIgnoreCase) >= 0) return;
            foreach (var name in font.fontNames)
                if (!fonts.ContainsKey(Key(name))) fonts[Key(name)] = font;
        }

        private static string Key(string name)
        {
            var key = new StringBuilder();
            foreach (var c in name ?? "")
                if (char.IsLetterOrDigit(c)) key.Append(char.ToLowerInvariant(c));
            var text = key.ToString();
            return text.EndsWith("regular", StringComparison.Ordinal) ? text.Substring(0, text.Length - 7) : text;
        }

        private static Font FindFont(string family)
        {
            var key = Key(family);
            Font font;
            if (fonts.TryGetValue(key, out font)) return font;
            foreach (var pair in fonts)
                if (pair.Key.StartsWith(key, StringComparison.Ordinal) && !pair.Key.Contains("italic")) return pair.Value;
            return null;
        }

        private static void Patch(TMP_FontAsset asset)
        {
            if (asset.name.StartsWith("NieGesi", StringComparison.Ordinal)) return;
            var family = asset.faceInfo.familyName ?? "";
            if (family.IndexOf("Noto Sans JP", StringComparison.OrdinalIgnoreCase) >= 0) return;

            var missing = Missing(asset);
            if (missing.Length == 0) return;

            if (asset.atlasPopulationMode == AtlasPopulationMode.Dynamic)
            {
                string left;
                asset.TryAddCharacters(missing, out left);
                Plugin.Log.LogInfo(string.Format("Font TMP „{0}” (dynamiczny): dodano polskie litery, braki: {1}.",
                    asset.name, string.IsNullOrEmpty(left) ? "-" : left));
                return;
            }

            var source = FindFont(family);
            if (source == null)
            {
                Plugin.Log.LogInfo(string.Format("Font TMP „{0}” ({1}): brak {2}, nie ma TTF tej rodziny — zostaje zapasowy font gry.",
                    asset.name, family, missing));
                return;
            }

            var fallback = TMP_FontAsset.CreateFontAsset(source, Mathf.Max(24, asset.faceInfo.pointSize),
                Mathf.Max(5, asset.atlasPadding), GlyphRenderMode.SDFAA, 512, 512, AtlasPopulationMode.Dynamic, true);
            if (fallback == null)
            {
                Plugin.Log.LogWarning("Nie udało się utworzyć fontu z " + source.name + ".");
                return;
            }
            fallback.name = "NieGesi PL " + asset.name;
            string notAdded;
            fallback.TryAddCharacters(missing, out notAdded);
            UnityEngine.Object.DontDestroyOnLoad(fallback);

            if (asset.fallbackFontAssetTable == null) asset.fallbackFontAssetTable = new List<TMP_FontAsset>();
            asset.fallbackFontAssetTable.Insert(0, fallback);
            Plugin.Log.LogInfo(string.Format("Font TMP „{0}” ({1}): brak {2} → zapasowy z {3}{4}.",
                asset.name, family, missing, source.name,
                string.IsNullOrEmpty(notAdded) ? "" : " (TTF też nie ma: " + notAdded + ")"));
        }

        private static string Missing(TMP_FontAsset asset)
        {
            var missing = new StringBuilder();
            foreach (var c in Plugin.PolishLetters)
                if (!asset.HasCharacter(c, false, false)) missing.Append(c);
            return missing.ToString();
        }
    }
}
