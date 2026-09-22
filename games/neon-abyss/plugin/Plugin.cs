// Nie gęsi — polski dla Neon Abyss, dokładany w czasie działania gry.
//
// Plugin dopisuje jedenasty język do źródła I2 Localization zaraz po jego wczytaniu
// i wypełnia go tekstami z pliku pl.tsv leżącego obok tej biblioteki. Do tego:
// - dopisuje POLSKI do przełącznika języka w opcjach, który gra ma zaszyty w kodzie;
// - daje polskim literom fonty z samej gry: angielskie atlasy są statyczne i nie mają
//   ą, ę, ł, więc dostają dynamiczne atlasy zapasowe budowane z plików TTF gry.
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
        public const string Version = "0.2.0";

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

            AddFallback(Folder + "EN_70px_ModernBrush", Folder + "_TTF/ModernBrush-Regular");
            AddFallback(Folder + "EN_12px_PixAntiqua", Folder + "_TTF/Zpix");

            var global = Create(Folder + "_TTF/Zpix");
            if (global != null && TMP_Settings.instance != null && TMP_Settings.fallbackFontAssets != null)
            {
                TMP_Settings.fallbackFontAssets.Add(global);
                Plugin.Log.LogInfo("Globalny zapasowy font: Zpix.");
            }
        }

        private static void AddFallback(string assetPath, string fontPath)
        {
            try
            {
                var asset = Resources.Load<TMP_FontAsset>(assetPath);
                var fallback = Create(fontPath);
                if (asset == null || fallback == null)
                {
                    Plugin.Log.LogWarning("Brak " + (asset == null ? assetPath : fontPath) + " — polskie litery mogą się nie wyświetlić.");
                    return;
                }
                if (asset.fallbackFontAssetTable == null) asset.fallbackFontAssetTable = new List<TMP_FontAsset>();
                asset.fallbackFontAssetTable.Insert(0, fallback);
                Plugin.Log.LogInfo("Font " + asset.name + " dostał zapasowy atlas z " + fontPath + ".");
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dołożyć fontu do " + assetPath + ": " + error.Message);
            }
        }

        private static TMP_FontAsset Create(string fontPath)
        {
            var font = Resources.Load<Font>(fontPath);
            if (font == null) return null;
            var asset = TMP_FontAsset.CreateFontAsset(font);
            if (asset != null) asset.name = font.name + " (Nie gęsi)";
            return asset;
        }
    }
}
