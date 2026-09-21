// Nie gęsi — polski dla Boomerang X, dokładany w czasie działania gry.
//
// Gra trzyma teksty w tabeli wkompilowanej w kod i ma dziesięć języków bez miejsca
// na jedenasty. Plugin dokłada go w pamięci: przechwytuje pobieranie tłumaczenia,
// podstawia krój rosyjski (jedyny z ogonkami) i dopisuje pozycję do listy języków.
// Żaden plik gry nie jest podmieniany.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;

namespace NieGesi.BoomerangX
{
    [BepInPlugin(Id, "Boomerang X PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.boomerangx";
        public const string Version = "0.2";

        /// Nasz język siada tuż za ostatnim istniejącym (language.LENGTH).
        internal const int PolishIndex = 10;
        internal const string LanguageLabel = "Polski";
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
                harmony.PatchAll(typeof(TranslationPatch));
                harmony.PatchAll(typeof(FontPatch));
                harmony.PatchAll(typeof(DropdownPatch));

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

            foreach (var line in File.ReadAllText(path).Split('\n'))
            {
                if (line.Length == 0) continue;
                var tab = line.IndexOf('\t');
                if (tab <= 0) continue;
                terms[line.Substring(0, tab)] = line.Substring(tab + 1).Replace("\\n", "\n");
            }

            return terms;
        }
    }

    /// Gra dla nieznanego języka zwraca „LOCALIZATION ERROR". Podajemy swój tekst,
    /// a dla wpisów jeszcze nieprzetłumaczonych cofamy się do angielskiego.
    [HarmonyPatch(typeof(localization_manager), "get_translation")]
    internal static class TranslationPatch
    {
        private static int _served;
        private static int _missing;

        private static void Postfix(localization_manager __instance, Localization_tableTypes.Data phrase,
                                    language lang, ref string __result)
        {
            if ((int)lang != Plugin.PolishIndex) return;

            try
            {
                string polish;
                if (phrase != null && Plugin.Terms.TryGetValue(phrase.id, out polish))
                {
                    __result = polish;
                    if (++_served == 1) Plugin.Log.LogInfo("Pierwszy polski tekst podany grze.");
                    return;
                }

                __result = __instance.get_translation(phrase, language.english);
                if (++_missing <= 5) Plugin.Log.LogWarning("Bez tłumaczenia, zostaje angielski: " + (phrase == null ? "?" : phrase.id));
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Błąd przy podmianie tekstu: " + error.Message);
            }
        }
    }

    /// Kroje wypalone w grze nie mają ogonków poza rosyjskim, więc polski rysujemy nim.
    [HarmonyPatch(typeof(font_manager), "get_font")]
    internal static class FontPatch
    {
        private static void Prefix(ref language lang)
        {
            if ((int)lang == Plugin.PolishIndex) lang = language.russian;
        }
    }

    /// Lista języków w opcjach powstaje z dziesięciu pozycji; dopisujemy jedenastą.
    [HarmonyPatch(typeof(options_screen), "on_reading_save_complete")]
    internal static class DropdownPatch
    {
        private static void Postfix(options_screen __instance)
        {
            try
            {
                var field = typeof(options_screen).GetField("language_dropdown",
                    BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                var dropdown = field == null ? null : field.GetValue(__instance);
                if (dropdown == null)
                {
                    Plugin.Log.LogWarning("Nie znalazłem listy języków w opcjach.");
                    return;
                }

                // TMP_Dropdown i zwykły Dropdown mają to samo AddOptions(List<string>),
                // więc sięgamy po nie przez refleksję i nie wiążemy się z żadnym z nich.
                var add = dropdown.GetType().GetMethod("AddOptions", new[] { typeof(List<string>) });
                if (add == null)
                {
                    Plugin.Log.LogWarning("Lista języków nie przyjmuje nowych pozycji (" + dropdown.GetType().Name + ").");
                    return;
                }

                var options = dropdown.GetType().GetProperty("options");
                var count = -1;
                if (options != null)
                {
                    var value = options.GetValue(dropdown, null) as IList;
                    if (value != null)
                    {
                        count = value.Count;
                        // Po powrocie do ekranu opcji lista jest budowana od nowa,
                        // ale nie zaszkodzi upewnić się, że nie dopisujemy dwa razy.
                        if (count > Plugin.PolishIndex) return;
                    }
                }

                add.Invoke(dropdown, new object[] { new List<string> { Plugin.LanguageLabel } });
                Plugin.Log.LogInfo("Dopisano polski do listy języków (było " + count + " pozycji).");
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dopisać polskiego do listy: " + error.Message);
            }
        }
    }
}
