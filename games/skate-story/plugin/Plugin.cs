// Not Geese — polski dla Skate Story, włączany w czasie działania gry.
//
// Gra ma polski slot I2 pod indeksem 15, ale wyłączony i pusty. Plugin go włącza,
// wypełnia 2305 tekstami z pl.tsv i przestawia dziewięć referencji do czcionek
// na kroje, które umieją polskie znaki. Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using BepInEx.Unity.Mono;
using HarmonyLib;
using I2.Loc;
using UnityEngine;

namespace notgeese.SkateStory
{
    // Wydanie sprzed zmiany nazwy projektu miało inny GUID. Gdy jego katalog został w plugins,
    // BepInEx pominie ten plugin zamiast ładować dwa spolszczenia naraz.
    [BepInIncompatibility("cc.notgoose.skatestory")]
    [BepInPlugin(Id, "Skate Story PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgeese.skatestory";
        public const string Version = "0.3";

        internal const string LanguageCode = "pl";
        internal const string TermsFile = "pl.tsv";
        internal const string FontsFile = "fonts.tsv";

        internal static ManualLogSource Log;
        internal static Dictionary<string, string> Terms;
        internal static Dictionary<string, string> Fonts;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("Gra {0} {1}, Unity {2}.",
                Application.productName, GameVersion(), Application.unityVersion));

            Terms = ReadTable(TermsFile);
            Fonts = ReadTable(FontsFile);
            if (Terms.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — polski nie zostanie włączony.");
                return;
            }
            Logger.LogInfo("Wczytano " + Terms.Count + " wpisów i " + Fonts.Count + " referencji czcionek.");

            // Gdyby przyszła wersja gry przestawiła I2, plugin ma odpaść po cichu.
            try
            {
                var harmony = new Harmony(Id);
                harmony.PatchAll(typeof(SourcePatch));
                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                if (patched == 0)
                {
                    Logger.LogError("Nie znalazłem miejsc do wpięcia w I2 — ta wersja gry jest inna niż oczekiwana.");
                    return;
                }
                Logger.LogInfo("Założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w I2, gra zostaje po angielsku: " + error.Message);
            }
        }

        /// Numer wersji gry przez refleksję — różne wydania Unity trzymają go inaczej,
        /// a to tylko informacja do logu i nie ma prawa wywrócić pluginu.
        private static string GameVersion()
        {
            try
            {
                var property = typeof(Application).GetProperty("version", BindingFlags.Public | BindingFlags.Static);
                var value = property == null ? null : property.GetValue(null, null) as string;
                return string.IsNullOrEmpty(value) ? "(bez numeru)" : value;
            }
            catch
            {
                return "(bez numeru)";
            }
        }

        /// Plik obok biblioteki: klucz, tabulator, wartość. Nowe linie zapisane jako \n.
        private Dictionary<string, string> ReadTable(string name)
        {
            var table = new Dictionary<string, string>(StringComparer.Ordinal);
            var folder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            var path = Path.Combine(folder, name);

            if (!File.Exists(path))
            {
                Logger.LogError("Brak pliku " + path);
                return table;
            }

            foreach (var line in File.ReadAllText(path, Encoding.UTF8).Split('\n'))
            {
                if (line.Length == 0) continue;
                var tab = line.IndexOf('\t');
                if (tab <= 0) continue;
                table[line.Substring(0, tab)] = line.Substring(tab + 1).Replace("\\n", "\n");
            }

            return table;
        }
    }

    [HarmonyPatch]
    internal static class SourcePatch
    {
        private static readonly HashSet<LanguageSourceData> Done = new HashSet<LanguageSourceData>();

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LocalizationManager), "AddSource")]
        private static void AfterAddSource(LanguageSourceData __0)
        {
            Apply(__0);
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LocalizationManager), "InitializeIfNeeded")]
        private static void AfterInitialize()
        {
            if (LocalizationManager.Sources == null) return;
            foreach (var source in LocalizationManager.Sources) Apply(source);
        }

        private static void Apply(LanguageSourceData source)
        {
            if (source == null || Done.Contains(source)) return;
            try
            {
                Install(source);
            }
            catch (Exception error)
            {
                Done.Add(source);
                Plugin.Log.LogError("Nie udało się włączyć polskiego: " + error);
            }
        }

        private static void Install(LanguageSourceData source)
        {
            if (source.mTerms == null || source.mTerms.Count == 0) return;

            var index = source.GetLanguageIndexFromCode(Plugin.LanguageCode, false, false);
            if (index < 0)
            {
                Plugin.Log.LogInfo("Źródło bez polskiego slotu — pomijam.");
                return;
            }
            Done.Add(source);

            // Slot jest w grze wyłączony; zerowa flaga znaczy „dostępny w selektorze".
            source.mLanguages[index].Flags = 0;

            var texts = 0;
            var fonts = 0;
            var missing = 0;
            foreach (var term in source.mTerms)
            {
                if (term.Languages == null || index >= term.Languages.Length) continue;

                string value;
                var isText = (int)term.TermType == 0;
                if (isText ? Plugin.Terms.TryGetValue(term.Term, out value)
                           : Plugin.Fonts.TryGetValue(term.Term, out value))
                {
                    term.Languages[index] = value;
                    if (term.Flags != null && index < term.Flags.Length) term.Flags[index] = 0;
                    if (isText) texts++; else fonts++;
                }
                else if (isText)
                {
                    missing++;
                }
            }

            RegisterFontAssets(source);
            LocalizationManager.LocalizeAll(true);

            Plugin.Log.LogInfo(string.Format(
                "Polski włączony jako język {0} z {1}: {2} tekstów, {3} czcionek, bez tłumaczenia {4}.",
                index + 1, source.mLanguages.Count, texts, fonts, missing));

            if (missing > 0)
            {
                Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            }
        }

        /// I2 szuka czcionek po nazwie w swojej liście zasobów. Dwa kroje, na które
        /// przestawiamy interfejs, nie są w niej zarejestrowane — dokładamy je z tych,
        /// które gra i tak ma już wczytane. Bez nich reszta tłumaczenia i tak działa.
        private static void RegisterFontAssets(LanguageSourceData source)
        {
            var wanted = new HashSet<string>(StringComparer.Ordinal);
            foreach (var name in Plugin.Fonts.Values) wanted.Add(name);

            var have = new HashSet<string>(StringComparer.Ordinal);
            if (source.Assets != null)
            {
                foreach (var asset in source.Assets)
                {
                    if (asset != null) have.Add(asset.name);
                }
            }

            var added = new List<UnityEngine.Object>();
            foreach (var name in wanted)
            {
                if (have.Contains(name)) continue;
                var found = FindLoaded(name);
                if (found != null)
                {
                    added.Add(found);
                    have.Add(name);
                }
                else
                {
                    Plugin.Log.LogWarning("Nie znalazłem kroju \"" + name + "\" — ten element zostanie w oryginalnej czcionce.");
                }
            }

            if (added.Count == 0) return;

            source.Assets.AddRange(added);
            source.UpdateAssetDictionary();
            Plugin.Log.LogInfo("Dołożone kroje: " + added.Count + ".");
        }

        private static UnityEngine.Object FindLoaded(string name)
        {
            foreach (var type in new[] { TmpFontAssetType(), typeof(Font) })
            {
                if (type == null) continue;
                foreach (var candidate in Resources.FindObjectsOfTypeAll(type))
                {
                    if (candidate != null && string.Equals(candidate.name, name, StringComparison.Ordinal))
                    {
                        return candidate;
                    }
                }
            }
            return null;
        }

        /// TextMeshPro bez referencji w czasie kompilacji — nazwa typu wystarczy.
        private static Type TmpFontAssetType()
        {
            return Type.GetType("TMPro.TMP_FontAsset, Unity.TextMeshPro", false);
        }
    }
}
