// Nie gęsi — polski dla Cyber Hook, podstawiany w czasie działania gry.
//
// Gra trzyma każdy język jako CSV (klucz → tekst) w Language_SO, a język wybiera się
// wartością enuma zapisaną w ustawieniach. Enuma nie da się rozszerzyć bez podmiany
// kodu gry, więc polski zajmuje miejsce angielskiego: gdy aktywny jest język „en”,
// Language_SO odpowiada tekstami z pl.tsv. Pozostałe języki działają jak dotąd.
// Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using TMPro;
using UnityEngine;

namespace NieGesi.CyberHook
{
    [BepInPlugin(Id, "Cyber Hook PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgoose.cyberhook";
        public const string Version = "0.2.0";

        // Klucz języka, który zastępujemy. W menu podpisany jest wpisem option_en.
        internal const string LanguageKey = "en";
        internal const string TermsFile = "pl.tsv";

        internal static ManualLogSource Log;

        /// Klucz gry (małe litery, bez spacji z brzegów — tak jak w Language_SO) → polski tekst.
        internal static Dictionary<string, string> Terms;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("PL {0}; gra {1} {2}, Unity {3}.", Version,
                Application.productName, Application.version, Application.unityVersion));

            Terms = ReadTerms();
            if (Terms.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — gra zostaje po angielsku.");
                return;
            }

            try
            {
                var harmony = new Harmony(Id);
                harmony.PatchAll(typeof(LanguagePatch));
                harmony.PatchAll(typeof(FontPatch));
                harmony.PatchAll(typeof(DialogPatch));
                UnityEngine.SceneManagement.SceneManager.sceneLoaded += (scene, mode) => FontPatch.Refresh();
                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                Logger.LogInfo("Wczytano " + Terms.Count + " wpisów, założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w system języków, gra zostaje po angielsku: " + error.Message);
            }
        }

        /// Plik obok biblioteki: klucz, tabulator, tekst. Nowe linie jako \n.
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
                terms[Normalize(entry.Substring(0, tab))] = entry.Substring(tab + 1).Replace("\\n", "\n");
            }
            return terms;
        }

        internal static string Normalize(string key)
        {
            return key.ToLowerInvariant().Trim();
        }

        /// Czy tłumaczymy: pytany jest angielski Language_SO i to on jest aktywnym językiem.
        /// Inne języki pytają angielski jako zapasowy — wtedy zostaje angielski.
        internal static bool Active(Language_SO language)
        {
            if (Terms == null || language == null || language.LanguageKey != LanguageKey) return false;
            if (!GenericSingleton<LanguageManager>.IsInstantiated) return true;
            return GenericSingleton<LanguageManager>.Instance.LanguageKey == LanguageKey;
        }

        internal static bool TryGet(string key, out string text)
        {
            text = null;
            return key != null && Terms.TryGetValue(Normalize(key), out text);
        }
    }

    [HarmonyPatch]
    internal static class LanguagePatch
    {
        private static bool reported;

        [HarmonyPrefix]
        [HarmonyPatch(typeof(Language_SO), nameof(Language_SO.GetTranslatedKey))]
        private static bool GetTranslatedKey(Language_SO __instance, string key, ref string __result)
        {
            if (!Plugin.Active(__instance)) return true;
            FontPatch.RefreshIfPending();
            string text;
            if (!Plugin.TryGet(key, out text)) return true;
            __result = text;
            return false;
        }

        // Część kwestii ma zamiast klucza sam angielski tekst; gra uznaje je za brak klucza
        // i pokazuje tekst jak jest. Dla tych, które mamy przetłumaczone, klucz „istnieje”.
        [HarmonyPostfix]
        [HarmonyPatch(typeof(Language_SO), nameof(Language_SO.KeyExists))]
        private static void KeyExists(Language_SO __instance, string key, ref bool __result)
        {
            string text;
            if (!__result && Plugin.Active(__instance) && Plugin.TryGet(key, out text)) __result = true;
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(Language_SO), "ParseLanguageFile")]
        private static void Parsed(Language_SO __instance, Dictionary<string, string> __result)
        {
            if (reported || __result == null || __instance.LanguageKey != Plugin.LanguageKey) return;
            reported = true;
            var missing = 0;
            foreach (var key in __result.Keys)
                if (!Plugin.Terms.ContainsKey(key)) missing++;
            if (missing > 0)
                Plugin.Log.LogWarning(missing + " z " + __result.Count + " tekstów tej wersji gry nie ma w spolszczeniu — zostaną po angielsku.");
            else
                Plugin.Log.LogInfo("Wszystkie " + __result.Count + " teksty gry mają polskie tłumaczenie.");
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(LanguageManager), nameof(LanguageManager.LanguageKey), MethodType.Setter)]
        private static void LanguageChanged()
        {
            FontPatch.Refresh();
        }
    }

    // Okno dialogu (Dron, Numero) jest przycięte maską tuż nad pierwszą linią tekstu.
    // Angielskie wersaliki się mieszczą, ale kreska i kropka nad Ś, Ć, Ż wystają ponad nie
    // i maska by je ucinała. Odsuwamy tekst od górnej krawędzi o ćwierć wysokości fontu.
    [HarmonyPatch]
    internal static class DialogPatch
    {
        private static readonly HashSet<int> Done = new HashSet<int>();

        [HarmonyPostfix]
        [HarmonyPatch(typeof(DialogTextDisplay), nameof(DialogTextDisplay.Init))]
        private static void Init(DialogTextDisplay __instance)
        {
            try
            {
                var text = Traverse.Create(__instance).Field("_text").GetValue<TMPro.TextMeshProUGUI>();
                if (text == null || !Done.Add(text.GetInstanceID())) return;
                var margin = text.margin;
                margin.y += text.fontSize * 0.25f;
                text.margin = margin;
            }
            catch (Exception error)
            {
                Plugin.Log.LogWarning("Nie udało się odsunąć tekstu dialogu: " + error.Message);
            }
        }
    }

    // Fonty przychodzą z paczek zasobów w różnych chwilach. Nowy font tylko zaznacza,
    // że jest co robić; litery składamy przed najbliższym tłumaczeniem tekstu.
    [HarmonyPatch]
    internal static class FontPatch
    {
        private static bool pending = true;

        [HarmonyPostfix]
        [HarmonyPatch(typeof(TMP_FontAsset), "Awake")]
        private static void FontLoaded()
        {
            pending = true;
        }

        internal static void RefreshIfPending()
        {
            if (pending) Refresh();
        }

        internal static void Refresh()
        {
            try
            {
                if (!GenericSingleton<LanguageManager>.IsInstantiated
                    || GenericSingleton<LanguageManager>.Instance.LanguageKey != Plugin.LanguageKey) return;
                pending = false;
                if (PolishGlyphs.PatchLoadedFonts() == 0) return;
                // Teksty złożone przed łatką pokazałyby dalej kwadraty zamiast liter.
                foreach (var text in Resources.FindObjectsOfTypeAll<TMP_Text>())
                {
                    if (text == null || !text.isActiveAndEnabled) continue;
                    text.havePropertiesChanged = true;
                    text.SetAllDirty();
                }
            }
            catch (Exception error)
            {
                Plugin.Log.LogWarning("Uzupełnianie fontów nie powiodło się: " + error.Message);
            }
        }
    }
}
