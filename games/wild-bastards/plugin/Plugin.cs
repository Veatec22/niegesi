// Nie gęsi — polski dla Wild Bastards, dokładany w czasie działania gry.
//
// Gra ma dziesięć języków w tabeli I2 Localization wkompilowanej w kod. Plugin dokłada
// jedenasty („Polish”) i wypełnia go tekstami z pl.tsv, dodaje przycisk „Polski” do panelu
// języków w menu głównym (LanguageButton.cs) i uzupełnia fonty o polskie litery z plików
// TTF gry (PolishFonts.cs). Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using I2.Loc;
using UnityEngine;

namespace NieGesi.WildBastards
{
    [BepInPlugin(Id, "Wild Bastards PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.wildbastards";
        public const string Version = "0.2.0";

        internal const string LanguageName = "Polish";
        internal const string LanguageCode = "pl";
        internal const string ButtonLabel = "Polski";
        internal const string TermsFile = "pl.tsv";
        internal const string PolishLetters = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ„”";

        internal static ManualLogSource Log;
        internal static Dictionary<string, string> Terms;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("PL {0}; gra {1} {2}, Unity {3}.", Version,
                Application.productName, Application.version, Application.unityVersion));

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
                harmony.PatchAll(typeof(LanguagePatch));
                harmony.PatchAll(typeof(LanguageButton));
                UnityEngine.SceneManagement.SceneManager.sceneLoaded += (scene, mode) => LanguagePatch.RefreshFonts();
                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                Logger.LogInfo("Wczytano " + Terms.Count + " wpisów, założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w grę, zostaje po angielsku: " + error);
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
                if (line.Length == 0) continue;
                var tab = line.IndexOf('\t');
                if (tab <= 0) continue;
                terms[line.Substring(0, tab)] = line.Substring(tab + 1).Replace("\\n", "\n");
            }
            return terms;
        }
    }

    // Obiekt BepInEksa bywa niszczony przy zmianie sceny, więc zamiast Update wpinamy się
    // w samo ustawienie języka i wczytanie sceny (ta gra przeładowuje scenę po zmianie języka).
    [HarmonyPatch]
    internal static class LanguagePatch
    {
        [HarmonyPostfix]
        [HarmonyPatch(typeof(LocalizationManager), "CurrentLanguage", MethodType.Setter)]
        private static void AfterSetLanguage()
        {
            RefreshFonts();
        }

        internal static void RefreshFonts()
        {
            try
            {
                if (LocalizationManager.CurrentLanguage != Plugin.LanguageName) return;
                PolishFonts.PatchLoadedFonts();
            }
            catch (Exception error)
            {
                Plugin.Log.LogWarning("Uzupełnianie fontów nie powiodło się: " + error.Message);
            }
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
                if (Plugin.Terms.ContainsKey(term.Term) && ++known > 4) break;
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
                else if (!string.IsNullOrEmpty(term.Languages[0]))
                {
                    missing++;
                }
            }

            source.UpdateDictionary(true);
            LanguagePatch.RefreshFonts();
            LocalizationManager.LocalizeAll(true);
            Plugin.Log.LogInfo(string.Format(
                "Polski dodany jako język {0} z {1}: {2} tekstów, bez tłumaczenia {3}.",
                index + 1, before + 1, filled, missing));
            if (missing > 0)
                Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
        }
    }
}
