// Nie gęsi — polski dla Broforce, dokładany w czasie działania gry.
//
// Gra ma własny system języków (Localisation.LanguageManager): lista kodów
// w LanguageManagerConfig i po jednym banku tekstów na język w resources.assets.
// Plugin dopisuje do listy kod „pl”, pod „pl” wczytuje banki angielskie,
// a GetLocalisedString oddaje tekst z pl.tsv. Pliki gry zostają nietknięte.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Localisation;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace NieGesi.Broforce
{
    [BepInPlugin(Id, "Broforce PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.broforce";
        public const string Version = "0.2.0";

        internal const string LanguageCode = "pl";
        internal const string LanguageName = "Polski";
        internal const string SourceLanguage = "en";
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

            // Gdyby przyszła wersja gry przebudowała system języków, plugin ma odpaść
            // po cichu, a nie wywrócić uruchomienie. Gra zostaje wtedy po angielsku.
            try
            {
                var harmony = new Harmony(Id);
                harmony.PatchAll(typeof(LanguagePatch));
                try
                {
                    harmony.PatchAll(typeof(PolishText3D));
                }
                catch (Exception error)
                {
                    Logger.LogWarning("Napisy 3D zostaną bez polskich liter: " + error.Message);
                }

                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                Logger.LogInfo("Założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w system języków, gra zostaje po angielsku: " + error);
                return;
            }

            SceneManager.sceneLoaded += (scene, mode) => PolishGlyphs.PatchLoadedFonts();
            PolishGlyphs.PatchLoadedFonts();
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

    [HarmonyPatch]
    internal static class LanguagePatch
    {
        private static readonly HashSet<string> Missing = new HashSet<string>(StringComparer.Ordinal);
        private static bool bankChecked;

        // Lista języków z konfiguracji gry; menu języków buduje się prosto z niej.
        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManagerConfig), "get_Languages")]
        private static void AddLanguage(List<string> __result)
        {
            if (__result != null && !__result.Contains(Plugin.LanguageCode)) __result.Add(Plugin.LanguageCode);
        }

        // Banków „pl” w grze nie ma: tekstów, grafik, materiałów i dymków używamy angielskich.
        [HarmonyPrefix]
        [HarmonyPatch(typeof(LanguageManager), "LoadStringBank")]
        private static void StringBank(ref string __0) { UseSourceBank(ref __0); }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(LanguageManager), "LoadSpriteBank")]
        private static void SpriteBank(ref string __0) { UseSourceBank(ref __0); }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(LanguageManager), "LoadRawImageMaterialBank")]
        private static void RawImageMaterialBank(ref string __0) { UseSourceBank(ref __0); }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(LanguageManager), "LoadReactionBubbleConfigBank")]
        private static void ReactionBubbleConfigBank(ref string __0) { UseSourceBank(ref __0); }

        private static void UseSourceBank(ref string language)
        {
            if (language == Plugin.LanguageCode) language = Plugin.SourceLanguage;
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManager), "LoadStringBank")]
        private static void CheckBank(LanguageManager __instance, bool __result)
        {
            if (bankChecked || !__result || Plugin.Terms == null) return;
            try
            {
                var bank = Traverse.Create(__instance).Field("stringBank").Field("languageValues").GetValue() as System.Collections.IList;
                if (bank == null) return;
                bankChecked = true;
                var missing = 0;
                foreach (var pair in bank)
                {
                    var key = Traverse.Create(pair).Field("key").GetValue<string>();
                    if (key != null && !Plugin.Terms.ContainsKey(key) && !key.StartsWith("LANGUAGE_", StringComparison.Ordinal)) missing++;
                }
                Plugin.Log.LogInfo(string.Format("Bank tekstów gry: {0} wpisów, bez polskiego {1}.", bank.Count, missing));
                // Nowe teksty po aktualizacji gry zostają po angielsku — to nie błąd,
                // tylko sygnał, że warto je dotłumaczyć.
                if (missing > 0) Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            }
            catch (Exception error)
            {
                bankChecked = true;
                Plugin.Log.LogWarning("Nie udało się policzyć tekstów gry: " + error.Message);
            }
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManager), "GetLocalisedString")]
        private static void Translate(LanguageManager __instance, string __0, ref string __result)
        {
            if (string.IsNullOrEmpty(__0)) return;
            if (__0 == "LANGUAGE_NAME_" + Plugin.LanguageCode)
            {
                __result = Plugin.LanguageName;
                return;
            }
            if (Plugin.Terms == null || __instance == null || __instance.CurrentLanguage != Plugin.LanguageCode) return;

            string polish;
            if (Plugin.Terms.TryGetValue(__0, out polish))
            {
                __result = polish;
                PolishGlyphs.PatchLoadedFonts();
            }
            else if (!__0.StartsWith("LANGUAGE_", StringComparison.Ordinal) && Missing.Add(__0))
            {
                Plugin.Log.LogInfo("Bez polskiego tekstu: " + __0);
            }
        }

        // Polski system → polski na starcie, jak gra robi to dla swoich języków.
        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManager), "GetSystemLanguage")]
        private static void SystemLanguage(ref string __result)
        {
            if (Application.systemLanguage == UnityEngine.SystemLanguage.Polish) __result = Plugin.LanguageCode;
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManager), "ChangeLanguage")]
        private static void Changed(string __0)
        {
            if (__0 != null && __0.ToLowerInvariant() == Plugin.LanguageCode)
                Plugin.Log.LogInfo("Język gry: polski.");
        }
    }
}
