// Not Geese — polski dla Shotgun Cop Man, dokładany w czasie działania gry.
//
// Gra ma dziesięć języków w tabeli I2 Localization wkompilowanej w kod.
// Plugin dokłada jedenasty i wypełnia go tekstami z pl.tsv. Menu wylicza języki
// z tabeli, więc polski pojawia się w ustawieniach sam.
// Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using I2.Loc;

namespace notgeese.ShotgunCopMan
{
    // Wydanie sprzed zmiany nazwy projektu miało inny GUID. Gdy jego katalog został w plugins,
    // BepInEx pominie ten plugin zamiast ładować dwa spolszczenia naraz.
    [BepInIncompatibility("cc.notgoose.shotguncopman")]
    [BepInPlugin(Id, "Shotgun Cop Man PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgeese.shotguncopman";
        public const string Version = "0.3.1";

        internal const string LanguageName = "Polski";
        internal const string LanguageCode = "pl";
        internal const string TermsFile = "pl.tsv";

        internal static ManualLogSource Log;
        internal static Dictionary<string, string> Terms;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("Gra {0}, Unity {1}.",
                UnityEngine.Application.productName, UnityEngine.Application.unityVersion));

            Terms = ReadTerms();
            if (Terms.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — polski nie zostanie dodany.");
                return;
            }

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
                Logger.LogInfo("Wczytano " + Terms.Count + " wpisów, założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w I2, gra zostaje po angielsku: " + error.Message);
            }
        }

        /// Plik obok biblioteki: klucz wpisu, tabulator, tekst. Nowe linie jako \n.
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

            foreach (var line in File.ReadAllText(path, Encoding.UTF8).Split('\n'))
            {
                // Plik z końcami CRLF zostawiłby \r w tekście, a TextMeshPro cofa po nim pióro.
                var entry = line.TrimEnd('\r');
                if (entry.Length == 0) continue;
                var tab = entry.IndexOf('\t');
                if (tab <= 0) continue;
                terms[entry.Substring(0, tab)] = entry.Substring(tab + 1).Replace("\\n", "\n");
            }

            return terms;
        }
    }

    // Źródło tłumaczeń bywa zasobem, nie obiektem sceny, więc jego Awake może nigdy
    // nie polecieć. Pewnym punktem jest rejestracja źródła w menedżerze.
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
                Plugin.Log.LogError("Nie udało się dołożyć polskiego: " + error);
            }
        }

        private static void Install(LanguageSourceData source)
        {
            if (source.mTerms == null || source.mTerms.Count == 0) return;

            var known = 0;
            foreach (var term in source.mTerms)
            {
                if (Plugin.Terms.ContainsKey(term.Term) && ++known > 4) break;
            }
            if (known == 0)
            {
                Plugin.Log.LogInfo("Pomijam źródło bez naszych kluczy (" + source.mTerms.Count + " wpisów).");
                return;
            }
            Done.Add(source);

            if (source.GetLanguageIndexFromCode(Plugin.LanguageCode, false, false) >= 0)
            {
                Plugin.Log.LogInfo("Polski jest już w tabeli — nie dokładam drugi raz.");
                return;
            }

            var before = source.mLanguages.Count;
            source.AddLanguage(Plugin.LanguageName, Plugin.LanguageCode);
            var index = source.mLanguages.Count - 1;

            var filled = 0;
            var missing = 0;
            foreach (var term in source.mTerms)
            {
                if (term.Languages == null || index >= term.Languages.Length) continue;

                string polish;
                if (Plugin.Terms.TryGetValue(term.Term, out polish))
                {
                    term.Languages[index] = polish;
                    if (term.Flags != null && index < term.Flags.Length) term.Flags[index] = 0;
                    filled++;
                }
                else
                {
                    missing++;
                }
            }

            LocalizationManager.LocalizeAll(true);
            Plugin.Log.LogInfo(string.Format(
                "Polski dodany jako język {0} z {1}: {2} tekstów, bez tłumaczenia {3}.",
                index + 1, before + 1, filled, missing));

            if (missing > 0)
            {
                Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            }
        }
    }
}
