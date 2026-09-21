// Nie gęsi — polski dla Anger Foot, dokładany w czasie działania gry.
//
// Gra ma dwanaście slotów tłumaczeń, z czego włoski jest pusty i niedostępny
// w menu. Plugin przemianowuje ten rekord na polski i włącza go, a teksty
// podstawia w locie, przechwytując LocalizedString.GetTranslation.
// Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;

namespace NieGesi.AngerFoot
{
    [BepInPlugin(Id, "Anger Foot PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.angerfoot";
        public const string Version = "0.2";

        internal const string TermsFile = "pl.tsv";
        internal const string LanguageName = "Polski";
        internal const string LanguageTag = "pl";

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
                harmony.PatchAll(typeof(LanguagePatch));
                harmony.PatchAll(typeof(TranslationPatch));

                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                if (patched == 0)
                {
                    Logger.LogError("Nie znalazłem miejsc do wpięcia — ta wersja gry jest inna niż oczekiwana.");
                    return;
                }
                Logger.LogInfo("Wczytano " + Terms.Count + " wpisów, założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w lokalizację, gra zostaje po angielsku: " + error.Message);
            }
        }

        /// Plik obok biblioteki: GUID wpisu, tabulator, tekst. Nowe linie jako \n.
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
                if (line.Length == 0) continue;
                var tab = line.IndexOf('\t');
                if (tab <= 0) continue;
                terms[line.Substring(0, tab)] = line.Substring(tab + 1).Replace("\\n", "\n");
            }

            return terms;
        }
    }

    /// Pusty slot włoski staje się polskim. Klucz arkusza zostaje „ITALIAN",
    /// bo to po nim gra wylicza pozycję tłumaczenia w każdym wpisie.
    [HarmonyPatch(typeof(LocalizationManager), "Initialize")]
    internal static class LanguagePatch
    {
        private static void Prefix()
        {
            try
            {
                var italian = LocalizationLanguage.Italian;
                if (italian == null)
                {
                    Plugin.Log.LogError("Nie ma rekordu języka włoskiego — nie mam czego przemianować.");
                    return;
                }
                if (italian.NativeName == Plugin.LanguageName) return;

                italian.NativeName = Plugin.LanguageName;
                italian.LanguageTag = Plugin.LanguageTag;
                italian.Supported = true;
                Plugin.Log.LogInfo("Slot włoski przemianowany na polski i włączony w menu.");
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się włączyć polskiego: " + error);
            }
        }
    }

    /// Podmiana tekstu w locie: rozpoznajemy wpis po GUID-zie, bo terminy
    /// powtarzają się między kategoriami (1518 unikalnych na 1776 wpisów).
    [HarmonyPatch(typeof(LocalizedString), "GetTranslation")]
    internal static class TranslationPatch
    {
        private static int _served;
        private static int _missing;

        private static void Postfix(LocalizedString __instance, ref string __result)
        {
            try
            {
                if (__instance == null) return;
                if (LocalizationManager.CurrentLanguage != LocalizationLanguage.Italian) return;

                string polish;
                if (Plugin.Terms.TryGetValue(__instance.GUID, out polish))
                {
                    __result = polish;
                    if (++_served == 1) Plugin.Log.LogInfo("Pierwszy polski tekst podany grze.");
                }
                else if (++_missing <= 5)
                {
                    Plugin.Log.LogWarning("Bez tłumaczenia: " + __instance.Term + " (" + __instance.GUID + ")");
                }
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Błąd przy podmianie tekstu: " + error.Message);
            }
        }
    }
}
