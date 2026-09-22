// Nie gęsi — polski dla Neon Abyss, dokładany w czasie działania gry.
//
// Plugin dopisuje jedenasty język do źródła I2 Localization zaraz po jego wczytaniu
// i wypełnia go tekstami z pliku pl.tsv leżącego obok tej biblioteki. Do tego:
// - dopisuje POLSKI do przełącznika języka w opcjach, który gra ma zaszyty w kodzie;
// - daje polskim literom fonty z samej gry: angielskie atlasy są statyczne i nie mają
//   ą, ę, ł, więc dostają zapasowe atlasy z polskimi literami, renderowanymi przy starcie
//   silnikiem fontów z plików TTF gry (dorysowywanie w locie w tej wersji TMP zawodzi).
// Żaden plik gry nie jest zmieniany. Gdy coś się nie zgadza, plugin loguje i odpada,
// a gra zostaje po angielsku.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using I2.Loc;
using TMPro;
using UnityEngine;

namespace NieGesi.NeonAbyss
{
    [BepInPlugin(Id, "Neon Abyss PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.neonabyss";
        public const string Version = "0.3.2";

        internal const string LanguageName = "Polish";
        internal const string LanguageCode = "pl";
        internal const string MenuLabel = "POLSKI";
        internal const string TermsFile = "pl.tsv";

        internal static ManualLogSource Log;
        internal static Dictionary<string, string> Terms;

        private void Awake()
        {
            Log = Logger;

            Terms = ReadTerms();
            if (Terms.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — polski nie zostanie dodany.");
                return;
            }

            Logger.LogInfo(string.Format(
                "Gra {0}, Unity {1}, wczytano {2} wpisów.",
                Application.version, Application.unityVersion, Terms.Count));

            var harmony = new Harmony(Id);
            Patch(harmony, typeof(LocalizationManager), "AddSource", null, "AfterAddSource");
            Patch(harmony, typeof(LocalizationManager), "InitializeIfNeeded", null, "AfterInitialize");

            var valueSource = AccessTools.TypeByName("NEON.UI.Base.UIMenuSwitcherLanguageValueSource");
            var gamePlay = AccessTools.TypeByName("NEON.UI.MainScreen.Options.GamePlay.GamePlaySettingsHandler");
            var settings = AccessTools.TypeByName("NEON.UI.MainScreen.Options.Base.SettingsHandlerBase");
            Patch(harmony, valueSource, "Awake", null, "AfterValuesAwake");
            Patch(harmony, gamePlay, "LanguageReverseMapping", "MapLabel", null);
            Patch(harmony, gamePlay, "LanguageMapping", "MapLabel", null);
            Patch(harmony, settings, "InitWithLanguge", "InitSwitcher", null);
            Patch(harmony, typeof(TMP_Text), "set_font", "BeforeSetFont", null);
            Patch(harmony, typeof(TextMeshProUGUI), "LoadFontAsset", null, "AfterLoadFontAsset");
            Patch(harmony, typeof(TextMeshPro), "LoadFontAsset", null, "AfterLoadFontAsset");
        }

        private void Patch(Harmony harmony, Type type, string method, string prefix, string postfix)
        {
            try
            {
                var original = type == null ? null : AccessTools.Method(type, method);
                if (original == null)
                {
                    Logger.LogWarning("Nie znalazłem " + method + " — ta wersja gry jest inna niż oczekiwana.");
                    return;
                }
                harmony.Patch(original,
                    prefix == null ? null : new HarmonyMethod(typeof(Patches), prefix),
                    postfix == null ? null : new HarmonyMethod(typeof(Patches), postfix));
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w " + method + ": " + error.Message);
            }
        }

        /// Plik obok biblioteki: klucz, tabulator, tekst. Znaki nowej linii zapisane jako \n.
        private Dictionary<string, string> ReadTerms()
        {
            var terms = new Dictionary<string, string>(StringComparer.Ordinal);
            var folder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            var path = Path.Combine(folder, TermsFile);

            if (!File.Exists(path))
            {
                Logger.LogError("Brak pliku " + path);
                return terms;
            }

            foreach (var line in File.ReadAllLines(path, Encoding.UTF8))
            {
                if (line.Length == 0) continue;
                var tab = line.IndexOf('\t');
                if (tab <= 0) continue;
                terms[line.Substring(0, tab)] = line.Substring(tab + 1).Replace("\\n", "\n");
            }

            return terms;
        }
    }

    internal static class Patches
    {
        // --- Źródło I2 -------------------------------------------------------------

        // Globalne źródło przychodzi z Resources, a każde źródło przechodzi
        // przez LocalizationManager.AddSource, zanim gra ustawi zapisany język.
        private static void AfterAddSource(object[] __args)
        {
            Apply(__args.Length > 0 ? __args[0] as LanguageSourceData : null);
        }

        private static void AfterInitialize()
        {
            if (LocalizationManager.Sources == null) return;
            foreach (var source in LocalizationManager.Sources) Apply(source);
        }

        private static void Apply(LanguageSourceData source)
        {
            try
            {
                if (Install(source)) Fonts.Install();
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dołożyć polskiego: " + error);
            }
        }

        private static bool Install(LanguageSourceData source)
        {
            if (source == null || source.mTerms == null || source.mTerms.Count == 0) return false;

            var known = 0;
            foreach (var term in source.mTerms)
            {
                if (Plugin.Terms.ContainsKey(term.Term) && ++known > 4) break;
            }
            if (known == 0) return false;

            // Idempotentnie: to samo źródło może przejść tędy więcej niż raz.
            foreach (var language in source.mLanguages)
            {
                if (string.Equals(language.Code, Plugin.LanguageCode, StringComparison.OrdinalIgnoreCase)) return false;
            }

            var english = source.GetLanguageIndexFromCode("en-US", true, false);
            if (english < 0)
            {
                Plugin.Log.LogError("Źródło nie ma angielskiego — nie mam z czego wziąć brakujących tekstów.");
                return false;
            }

            source.AddLanguage(Plugin.LanguageName, Plugin.LanguageCode);
            var index = source.GetLanguageIndexFromCode(Plugin.LanguageCode, true, false);

            int translated = 0, fallback = 0, other = 0;
            foreach (var term in source.mTerms)
            {
                if (term.Languages == null || index >= term.Languages.Length) continue;
                string value;
                if (Fonts.TermValues.TryGetValue(term.Term, out value))
                {
                    other++;
                }
                else if (term.TermType != eTermType.Text)
                {
                    // Obrazki, materiały, przyciski padów: jak w angielskim.
                    value = term.Languages[english];
                    other++;
                }
                else if (Plugin.Terms.TryGetValue(term.Term, out value))
                {
                    translated++;
                }
                else
                {
                    // Nowe teksty po aktualizacji gry zostają po angielsku.
                    value = term.Languages[english];
                    fallback++;
                }
                term.Languages[index] = value;
            }

            source.UpdateDictionary(true);
            LocalizationManager.LocalizeAll(true);
            Plugin.Log.LogInfo(string.Format(
                "Polski dodany jako język {0}: {1} tekstów po polsku, {2} innych wpisów (fonty, grafiki).",
                index + 1, translated, other));
            if (fallback > 0)
            {
                Plugin.Log.LogWarning(fallback + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            }
            return true;
        }

        // Uszkodzony atlas gry podmieniamy na świeży, zanim trafi do tekstu.
        private static void BeforeSetFont(ref TMP_FontAsset value)
        {
            value = Fonts.Substitute(value);
            Fonts.Ensure(value);
        }

        // Tekst z fontem zapisanym w prefabie nie przechodzi przez setter — łapiemy go tutaj.
        private static void AfterLoadFontAsset(TMP_Text __instance)
        {
            if (__instance != null) Fonts.Ensure(__instance.font);
        }

        // --- Przełącznik języka w opcjach -----------------------------------------
        //
        // Gra trzyma w ustawieniach nazwę języka I2, a w menu pokazuje podpisy
        // („ENGLISH”, „РУССКИЙ”) z listy zaszytej w UIMenuSwitcherLanguageValueSource.
        // Mapowanie w obie strony też jest zaszyte, więc dopisujemy do niego parę
        // POLSKI ↔ Polish.

        private static void AfterValuesAwake(object __instance)
        {
            try
            {
                var values = FindMember(__instance, "Values") as IList;
                if (values == null)
                {
                    Plugin.Log.LogWarning("Lista języków w opcjach ma nieznany kształt — POLSKI nie trafi do menu.");
                    return;
                }
                if (!values.Contains(Plugin.MenuLabel)) values.Add(Plugin.MenuLabel);
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dopisać POLSKI do menu: " + error.Message);
            }
        }

        // LanguageMapping i LanguageReverseMapping: podpis → nazwa języka I2.
        private static bool MapLabel(object[] __args, ref string __result)
        {
            var label = __args.Length > 0 ? __args[0] as string : null;
            if (label != Plugin.MenuLabel && label != Plugin.LanguageName) return true;
            __result = Plugin.LanguageName;
            return false;
        }

        // InitWithLanguge(switcher, nazwa języka): ustawia przełącznik na zapisanym języku.
        private static bool InitSwitcher(object[] __args)
        {
            if (__args.Length < 2 || __args[0] == null || (__args[1] as string) != Plugin.LanguageName) return true;
            try
            {
                var switcher = __args[0];
                var source = Traverse.Create(switcher).Field("DataSource").GetValue();
                var options = Traverse.Create(source).Method("GetOptions").GetValue() as IEnumerable;
                var index = 0;
                foreach (var option in options)
                {
                    if ((option as string) == Plugin.MenuLabel)
                    {
                        Traverse.Create(switcher).Method("SwitchTo", new[] { typeof(int) }).GetValue(index);
                        return false;
                    }
                    index++;
                }
                Plugin.Log.LogWarning("Przełącznik języka nie ma pozycji POLSKI.");
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się ustawić przełącznika na POLSKI: " + error.Message);
            }
            return true;
        }

        private static object FindMember(object instance, string name)
        {
            const BindingFlags all = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic;
            for (var type = instance.GetType(); type != null; type = type.BaseType)
            {
                var field = type.GetField(name, all);
                if (field != null) return field.GetValue(instance);
                var property = type.GetProperty(name, all);
                if (property != null) return property.GetValue(instance, null);
            }
            return null;
        }
    }

    // Fonty. Gra przełącza fonty per język terminami I2 UI/smallFont i UI/BigFont.
    // Angielskie atlasy (PixAntiqua, ModernBrush) są statyczne i bez polskich liter.
    // Mały tekst dostaje pikselowy Zpix, który gra ma jako dynamiczny atlas dla
    // chińskiego tradycyjnego; duże nagłówki zostają przy ModernBrush, któremu
    // dokładamy dynamiczny atlas z jego własnego pliku TTF. Na resztę tekstów
    // z fontem ustawionym na sztywno — globalny zapasowy atlas ze Zpix.
    internal static class Fonts
    {
        private const string Folder = "Fonts & Materials/";

        internal static readonly Dictionary<string, string> TermValues = new Dictionary<string, string>
        {
            { "UI/smallFont", Folder + "CHT_12px_Zpix" },
            { "UI/BigFont", Folder + "EN_70px_ModernBrush" },
        };

        private static bool installed;

        internal static void Install()
        {
            if (installed) return;
            installed = true;

            // Atlasy gry są rastrowe (shader Bitmap), więc zapasowe muszą być takie same:
            // domyślny CreateFontAsset daje SDF, który Bitmap rysuje jako pusty kontur.
            AddFallback(Folder + "EN_70px_ModernBrush", Folder + "_TTF/ModernBrush-Regular", 70, 2);
            AddFallback(Folder + "EN_12px_PixAntiqua", Folder + "_TTF/Zpix", 12, 2);

            var global = Create(Folder + "_TTF/Zpix", 12, 2, Resources.Load<TMP_FontAsset>(Folder + "EN_12px_PixAntiqua"));
            if (global != null && TMP_Settings.instance != null && TMP_Settings.fallbackFontAssets != null)
            {
                Keep(global);
                TMP_Settings.fallbackFontAssets.Add(global);
                Plugin.Log.LogInfo("Globalny zapasowy font: Zpix.");
            }
        }

        // Dynamiczny atlas CHT_12px_Zpix przychodzi z gry z listą wolnych miejsc, która
        // nachodzi na 159 już narysowanych glifów (m.in. „i”). Każda dorysowana polska
        // litera ląduje wtedy na cudzym glifie. Czyszczenie atlasu (ClearFontAssetData)
        // w tej wersji TMP tego nie naprawiło, więc przy polskim podajemy tekstom świeży
        // atlas z tego samego pliku Zpix i z tymi samymi ustawieniami: 12 px, raster
        // z hintingiem, padding 5, shader Bitmap. Chiński dalej dostaje oryginał.
        internal const string BrokenAtlas = "CHT_12px_Zpix";
        private static TMP_FontAsset fresh;
        private static bool freshFailed;

        internal static TMP_FontAsset Substitute(TMP_FontAsset asset)
        {
            if (asset == null || asset.name != BrokenAtlas || freshFailed) return asset;
            if (LocalizationManager.CurrentLanguageCode != Plugin.LanguageCode) return asset;
            if (fresh == null) fresh = CreateFresh(asset);
            return fresh ?? asset;
        }

        private static TMP_FontAsset CreateFresh(TMP_FontAsset original)
        {
            try
            {
                var font = Resources.Load<Font>(Folder + "_TTF/Zpix");
                if (font == null) throw new Exception("brak Fonts & Materials/_TTF/Zpix");
                var asset = TMP_FontAsset.CreateFontAsset(font, 12, 5,
                    UnityEngine.TextCore.LowLevel.GlyphRenderMode.RASTER_HINTED, 1024, 1024,
                    AtlasPopulationMode.Dynamic);
                if (asset == null) throw new Exception("CreateFontAsset zwróciło null");
                asset.name = BrokenAtlas + " (Nie gęsi)";
                Initialize(asset);
                if (original.material != null && asset.material != null)
                {
                    var texture = asset.material.GetTexture(ShaderUtilities.ID_MainTex);
                    asset.material.shader = original.material.shader;
                    asset.material.SetTexture(ShaderUtilities.ID_MainTex, texture);
                }
                if (original.atlasTexture != null && asset.atlasTexture != null)
                    asset.atlasTexture.filterMode = original.atlasTexture.filterMode;
                asset.fallbackFontAssetTable = original.fallbackFontAssetTable;
                Keep(asset);
                Plugin.Log.LogInfo("Polski mały tekst dostaje świeży atlas Zpix zamiast " + BrokenAtlas + ".");
                return asset;
            }
            catch (Exception error)
            {
                freshFailed = true;
                Plugin.Log.LogError("Nie udało się zbudować świeżego atlasu Zpix, zostaje " + BrokenAtlas + ": " + error.Message);
                return null;
            }
        }

        // Zapasowe atlasy z polskimi literami, po nazwie atlasu gry, któremu je doklejamy.
        // Gra między scenami zwalnia nieużywane zasoby (UnloadUnusedAssets), a atlas
        // wczytany ponownie z Resources nie ma już naszego zapasu. Dlatego zapas budujemy
        // raz, chronimy przed zwolnieniem i doklejamy każdemu egzemplarzowi, który trafi
        // do tekstu (Ensure w TMP_Text.font i LoadFontAsset).
        private static readonly Dictionary<string, TMP_FontAsset> polish = new Dictionary<string, TMP_FontAsset>();
        private static readonly HashSet<int> ensured = new HashSet<int>();

        private static void AddFallback(string assetPath, string fontPath, int pointSize, int padding)
        {
            try
            {
                var asset = Resources.Load<TMP_FontAsset>(assetPath);
                var fallback = asset == null ? null : BuildStatic(fontPath, pointSize, padding, asset);
                if (asset == null || fallback == null)
                {
                    Plugin.Log.LogWarning("Brak " + (asset == null ? assetPath : fontPath) + " — polskie litery mogą się nie wyświetlić.");
                    return;
                }
                Keep(fallback);
                polish[asset.name] = fallback;
                Ensure(asset);
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dołożyć fontu do " + assetPath + ": " + error.Message);
            }
        }

        internal static void Ensure(TMP_FontAsset asset)
        {
            TMP_FontAsset fallback;
            if (asset == null || !polish.TryGetValue(asset.name, out fallback)) return;
            if (asset.fallbackFontAssetTable == null) asset.fallbackFontAssetTable = new List<TMP_FontAsset>();
            if (asset.fallbackFontAssetTable.Count > 0 && asset.fallbackFontAssetTable[0] == fallback) return;
            asset.fallbackFontAssetTable.Remove(fallback);
            asset.fallbackFontAssetTable.Insert(0, fallback);
            if (ensured.Add(asset.GetInstanceID()))
                Plugin.Log.LogInfo("Font " + asset.name + " (egzemplarz " + asset.GetInstanceID() + ") dostał polskie litery z " + fallback.name + ".");
        }

        private static void Keep(TMP_FontAsset asset)
        {
            asset.hideFlags |= HideFlags.DontUnloadUnusedAsset;
            if (asset.material != null) asset.material.hideFlags |= HideFlags.DontUnloadUnusedAsset;
            if (asset.atlasTexture != null) asset.atlasTexture.hideFlags |= HideFlags.DontUnloadUnusedAsset;
        }

        // Atlas z CreateFontAsset ma w tej wersji TMP puste (null) listy wolnych i zajętych
        // miejsc, glifów do dodania itd. — w edytorze wypełnia je serializacja. Bez nich
        // FontEngine.TryAddGlyphsToTexture rzuca NullReferenceException, litera nie trafia
        // do atlasu i TMP po cichu bierze ją z kolejnego zapasu. Uzupełniamy je tak jak
        // TMP przy czyszczeniu atlasu: puste kolekcje i jedno wolne pole na cały atlas.
        private static void Initialize(TMP_FontAsset asset)
        {
            const BindingFlags instance = BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public;
            foreach (var field in typeof(TMP_FontAsset).GetFields(instance))
            {
                if (field.GetValue(asset) != null) continue;
                var type = field.FieldType;
                if (type.IsGenericType && type.GetConstructor(Type.EmptyTypes) != null)
                    field.SetValue(asset, Activator.CreateInstance(type));
                else if (type == typeof(TMP_FontFeatureTable))
                    field.SetValue(asset, new TMP_FontFeatureTable());
            }
            var free = AccessTools.Field(typeof(TMP_FontAsset), "m_FreeGlyphRects").GetValue(asset)
                as List<UnityEngine.TextCore.GlyphRect>;
            if (free != null && free.Count == 0)
                free.Add(new UnityEngine.TextCore.GlyphRect(0, 0, asset.atlasWidth, asset.atlasHeight));
            asset.ReadFontAssetDefinition();
        }

        // Dorysowywanie w locie (dynamiczne atlasy) w tej wersji TMP nie działa dla
        // atlasów tworzonych przez CreateFontAsset: TryAddCharacters rzuca wyjątek
        // i litera trafia do kolejnego zapasu, innym krojem. Dlatego zapasowy atlas
        // z polskimi literami składamy sami, silnikiem fontów: każda litera renderowana
        // raz z pliku TTF gry do własnej tekstury, atlas oznaczony jako statyczny.
        internal const string StaticLetters = "ĄĆĘŁŃÓŚŹŻąćęłńóśźż„”–—…";

        private static TMP_FontAsset BuildStatic(string fontPath, int pointSize, int padding, TMP_FontAsset like)
        {
            var font = Resources.Load<Font>(fontPath);
            if (font == null) return null;
            const UnityEngine.TextCore.LowLevel.GlyphRenderMode mode = UnityEngine.TextCore.LowLevel.GlyphRenderMode.RASTER_HINTED;
            var size = pointSize > 32 ? 512 : 128;

            var asset = TMP_FontAsset.CreateFontAsset(font, pointSize, padding, mode, size, size, AtlasPopulationMode.Static);
            if (asset == null) return null;
            asset.name = font.name + " " + pointSize + " PL (Nie gęsi)";
            Initialize(asset);

            var engine = typeof(UnityEngine.TextCore.LowLevel.FontEngine);
            var reset = AccessTools.Method(engine, "ResetAtlasTexture");
            var add = AccessTools.Method(engine, "TryAddGlyphToTexture");
            if (add == null || reset == null) throw new Exception("brak FontEngine.TryAddGlyphToTexture");
            var load = UnityEngine.TextCore.LowLevel.FontEngine.LoadFontFace(font, pointSize);
            if (load != UnityEngine.TextCore.LowLevel.FontEngineError.Success) throw new Exception("LoadFontFace: " + load);

            var texture = new Texture2D(size, size, TextureFormat.Alpha8, false);
            reset.Invoke(null, new object[] { texture });
            var free = new List<UnityEngine.TextCore.GlyphRect> { new UnityEngine.TextCore.GlyphRect(0, 0, size, size) };
            var used = new List<UnityEngine.TextCore.GlyphRect>();

            var added = new StringBuilder();
            var failed = new StringBuilder();
            foreach (var c in StaticLetters)
            {
                uint index;
                if (!UnityEngine.TextCore.LowLevel.FontEngine.TryGetGlyphIndex(c, out index) || index == 0)
                {
                    failed.Append(c);
                    continue;
                }
                var args = new object[] { index, padding, UnityEngine.TextCore.LowLevel.GlyphPackingMode.BestShortSideFit,
                    free, used, mode, texture, null };
                var ok = (bool)add.Invoke(null, args);
                var glyph = args[7] as UnityEngine.TextCore.Glyph;
                if (!ok || glyph == null)
                {
                    failed.Append(c);
                    continue;
                }
                asset.glyphTable.Add(glyph);
                asset.characterTable.Add(new TMP_Character(c, glyph));
                added.Append(c);
            }
            texture.Apply(false, false);
            if (like.atlasTexture != null) texture.filterMode = like.atlasTexture.filterMode;
            texture.name = asset.name + " Atlas";

            AccessTools.Field(typeof(TMP_FontAsset), "m_AtlasTextures").SetValue(asset, new[] { texture });
            if (asset.material != null)
            {
                if (like.material != null) asset.material.shader = like.material.shader;
                asset.material.SetTexture(ShaderUtilities.ID_MainTex, texture);
            }
            asset.ReadFontAssetDefinition();

            Plugin.Log.LogInfo("Atlas " + asset.name + ": wyrenderowane „" + added + "”"
                + (failed.Length > 0 ? ", bez glifu „" + failed + "”" : "") + ".");
            return asset;
        }

        // Dynamiczny atlas rastrowy z pliku TTF gry, z shaderem wziętym z atlasu wzorcowego.
        private static TMP_FontAsset Create(string fontPath, int pointSize, int padding, TMP_FontAsset like)
        {
            var font = Resources.Load<Font>(fontPath);
            if (font == null) return null;
            var asset = TMP_FontAsset.CreateFontAsset(font, pointSize, padding,
                UnityEngine.TextCore.LowLevel.GlyphRenderMode.RASTER_HINTED, 1024, 1024,
                AtlasPopulationMode.Dynamic);
            if (asset == null) return null;
            asset.name = font.name + " " + pointSize + " (Nie gęsi)";
            // Atlas z CreateFontAsset nie ma jeszcze tablic znaków — bez tego TMP
            // wywraca się przy dorysowywaniu i po cichu bierze literę z kolejnego zapasu.
            Initialize(asset);
            if (like != null && like.material != null && asset.material != null)
            {
                var texture = asset.material.GetTexture(ShaderUtilities.ID_MainTex);
                asset.material.shader = like.material.shader;
                asset.material.SetTexture(ShaderUtilities.ID_MainTex, texture);
            }
            // Atlasy gry mają filtr Point (piksel w piksel); domyślny dwuliniowy rozmywa litery.
            if (like != null && like.atlasTexture != null && asset.atlasTexture != null)
                asset.atlasTexture.filterMode = like.atlasTexture.filterMode;
            return asset;
        }
    }
}
