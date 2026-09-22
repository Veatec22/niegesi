// Nie gęsi — polski dla Void Bastards, dokładany w czasie działania gry.
//
// Gra ma dziewięć języków w tabeli I2 Localization wkompilowanej w kod. Plugin dokłada
// dziesiąty („Polish”) i wypełnia go tekstami z pl.tsv. Ekran języków wylicza języki
// z tabeli i podpisuje je terminem „Language/<nazwa>”, więc polski pojawia się sam.
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
using UnityEngine;

namespace NieGesi.VoidBastards
{
    [BepInPlugin(Id, "Void Bastards PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.voidbastards";
        public const string Version = "0.2.1";

        // Nazwa języka jest też kluczem podpisu w menu: „Language/Polish”.
        internal const string LanguageName = "Polish";
        internal const string LanguageCode = "pl";
        internal const string TermsFile = "pl.tsv";
        internal const string PolishLetters = "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ";

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
                UnityEngine.SceneManagement.SceneManager.sceneLoaded += (scene, mode) => LanguagePatch.RefreshFonts();
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

    // Obiekt BepInEksa bywa niszczony przy zmianie sceny, więc zamiast Update wpinamy się
    // w samo ustawienie języka i wczytanie sceny.
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
                PolishGlyphs.PatchLoadedFonts();
                FontReport.Write();
            }
            catch (Exception error)
            {
                Plugin.Log.LogWarning("Uzupełnianie fontów nie powiodło się: " + error.Message);
            }
        }
    }

    internal static class FontReport
    {
        private static readonly HashSet<string> Reported = new HashSet<string>();

        internal static void Write()
        {
            try
            {
                foreach (var font in Resources.FindObjectsOfTypeAll<Font>())
                    Report("Font", font.name, font.dynamic, c => font.HasCharacter(c));
                foreach (var font in Resources.FindObjectsOfTypeAll<TMPro.TMP_FontAsset>())
                {
                    if (font.name.StartsWith("NieGesi", StringComparison.Ordinal)) continue;
                    var asset = font;
                    Report("TMP", font.name, false, c => HasWithFallback(asset, c));
                }
            }
            catch (Exception error)
            {
                Plugin.Log.LogWarning("Raport fontów nie powiódł się: " + error.Message);
            }
        }

        private static bool HasWithFallback(TMPro.TMP_FontAsset font, char c)
        {
            if (font.HasCharacter(c)) return true;
            if (font.fallbackFontAssets == null) return false;
            foreach (var fallback in font.fallbackFontAssets)
                if (fallback != null && fallback.HasCharacter(c)) return true;
            return false;
        }

        private static void Report(string kind, string name, bool dynamic, Func<char, bool> has)
        {
            if (!Reported.Add(kind + "/" + name)) return;
            var missing = new StringBuilder();
            foreach (var c in Plugin.PolishLetters)
                if (!has(c)) missing.Append(c);
            Plugin.Log.LogInfo(string.Format("Font {0} „{1}”{2}: {3}", kind, name,
                dynamic ? " (dynamiczny)" : "", missing.Length == 0 ? "wszystkie polskie litery" : "brak " + missing));
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

            // Terminy, których gra nie ma, a są potrzebne polskiemu (podpis w menu języków).
            var added = 0;
            foreach (var pair in Plugin.Terms)
            {
                if (source.GetTermData(pair.Key, false) != null) continue;
                if (!pair.Key.StartsWith("Language/", StringComparison.Ordinal)) continue;
                var created = source.AddTerm(pair.Key);
                if (created != null) added++;
            }

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
                "Polski dodany jako język {0} z {1}: {2} tekstów, nowe terminy {3}, bez tłumaczenia {4}.",
                index + 1, before + 1, filled, added, missing));
            if (missing > 0)
                Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
        }
    }
}
