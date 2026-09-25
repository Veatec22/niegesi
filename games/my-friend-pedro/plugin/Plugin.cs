// Not Geese — polski dla My Friend Pedro, dokładany w czasie działania gry.
//
// Zamiast podmieniać resources.assets (205 MB), plugin dopisuje jedenasty język
// do źródła I2 Localization zaraz po jego wczytaniu i wypełnia go tekstami
// z pliku pl.tsv leżącego obok tej biblioteki. Oryginalne dziesięć języków
// zostaje nietknięte, a gra nie wie, że coś się zmieniło.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using I2.Loc;

namespace notgeese.Pedro
{
    // Wydanie sprzed zmiany nazwy projektu miało inny GUID. Gdy jego katalog został w plugins,
    // BepInEx pominie ten plugin zamiast ładować dwa spolszczenia naraz.
    [BepInIncompatibility("cc.notgoose.myfriendpedro")]
    [BepInPlugin(Id, "My Friend Pedro PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgeese.myfriendpedro";
        public const string Version = "0.3.1";

        internal const string LanguageName = "Polski";
        internal const string LanguageCode = "pl";
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
                UnityEngine.Application.version, UnityEngine.Application.unityVersion, Terms.Count));

            // Gdyby przyszła wersja gry przestawiła I2, plugin ma odpaść po cichu,
            // a nie wywrócić uruchomienie. Gra zostaje wtedy po angielsku.
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

    // I2 bierze globalne źródło prosto z prefabu w Resources, więc Awake na nim
    // nigdy nie leci. Każde źródło — z prefabu i ze sceny — przechodzi natomiast
    // przez LocalizationManager.AddSource i dopiero to jest pewny punkt zaczepienia.
    [HarmonyPatch]
    internal static class SourcePatch
    {
        [HarmonyPostfix]
        [HarmonyPatch(typeof(LocalizationManager), "AddSource")]
        private static void AfterAddSource(LanguageSource __0)
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

        private static void Apply(LanguageSource source)
        {
            try
            {
                Install(source);
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dołożyć polskiego: " + error);
            }
        }

        private static void Install(LanguageSource source)
        {
            if (source == null || source.mTerms == null || source.mTerms.Count == 0) return;

            // Gra może mieć kilka źródeł; interesuje nas to z naszymi kluczami.
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

            // Idempotentnie: źródło może się obudzić więcej niż raz.
            foreach (var language in source.mLanguages)
            {
                if (string.Equals(language.Code, Plugin.LanguageCode, StringComparison.OrdinalIgnoreCase)) return;
            }

            var before = source.mLanguages.Count;
            source.AddLanguage(Plugin.LanguageName, Plugin.LanguageCode);
            var index = source.mLanguages.Count - 1;

            var filled = 0;
            var missing = 0;
            foreach (var term in source.mTerms)
            {
                string polish;
                if (!Plugin.Terms.TryGetValue(term.Term, out polish))
                {
                    missing++;
                    continue;
                }
                if (term.Languages != null && index < term.Languages.Length)
                {
                    term.Languages[index] = polish;
                    filled++;
                }
            }

            LocalizationManager.LocalizeAll(true);
            Plugin.Log.LogInfo(string.Format(
                "Polski dodany jako język {0} z {1}: {2} tekstów, bez tłumaczenia {3}.",
                index + 1, before + 1, filled, missing));

            // Nowe teksty po aktualizacji gry zostają po angielsku — to nie błąd,
            // tylko sygnał, że warto je dotłumaczyć.
            if (missing > 0)
            {
                Plugin.Log.LogWarning(missing + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            }
        }
    }
}
