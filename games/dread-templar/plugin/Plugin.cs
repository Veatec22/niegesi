// Not Geese — polski dla Dread Templar, dokładany w czasie działania gry.
//
// Gra ma w swoich danych pusty blok „pol", zostawiony przez twórców, oraz
// wyłączony przycisk włoski zaparkowany obok siatki języków w menu opcji.
// Plugin wypełnia pierwszy tekstami z pl.tsv, a drugi ożywia i przemianowuje.
// Zamiast podmieniać 35 plików gry o łącznej wadze 789 MB.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using UnityEngine;

namespace notgeese.DreadTemplar
{
    // Wydanie sprzed zmiany nazwy projektu miało inny GUID. Gdy jego katalog został w plugins,
    // BepInEx pominie ten plugin zamiast ładować dwa spolszczenia naraz.
    [BepInIncompatibility("cc.notgoose.dreadtemplar")]
    [BepInPlugin(Id, "Dread Templar PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgeese.dreadtemplar";
        public const string Version = "0.2";

        internal const string LanguageCode = "pol";
        internal const string LanguageLabel = "Polski";
        internal const string TermsFile = "pl.tsv";

        /// Nazwy z hierarchii sceny — te same, których szukała metoda z podmianą plików.
        internal const string ParkedButton = "LanguagePick_ita_03";
        internal const string ToggleGrid = "Language_ToggleGroup";

        internal static ManualLogSource Log;
        internal static Dictionary<string, string> Texts;
        internal static Dictionary<string, string> Names;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("Gra {0}, Unity {1}.",
                Application.productName, Application.unityVersion));

            Texts = new Dictionary<string, string>(StringComparer.Ordinal);
            Names = new Dictionary<string, string>(StringComparer.Ordinal);
            ReadTerms();
            if (Texts.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — polski nie zostanie dodany.");
                return;
            }

            try
            {
                var harmony = new Harmony(Id);
                harmony.PatchAll(typeof(TextPatch));
                harmony.PatchAll(typeof(NamePatch));
                harmony.PatchAll(typeof(MenuPatch));

                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                if (patched == 0)
                {
                    Logger.LogError("Nie znalazłem miejsc do wpięcia — ta wersja gry jest inna niż oczekiwana.");
                    return;
                }
                Logger.LogInfo(string.Format("Wczytano {0} tekstów i {1} imion, założone łatki: {2}.",
                    Texts.Count, Names.Count, patched));
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w teksty, gra zostaje po angielsku: " + error.Message);
            }
        }

        /// Plik obok biblioteki: rodzaj wpisu, kategoria/klucz, tekst.
        /// Rodzaj to „t" dla treści albo „n" dla imienia mówiącego.
        private void ReadTerms()
        {
            var folder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            var path = Path.Combine(folder, TermsFile);
            if (!File.Exists(path))
            {
                Logger.LogError("Brak pliku " + path);
                return;
            }

            foreach (var line in File.ReadAllText(path).Split('\n'))
            {
                var parts = line.Split('\t');
                if (parts.Length < 3 || parts[1].Length == 0) continue;
                var value = Unescape(parts[2]);
                if (parts[0] == "n") Names[parts[1]] = value;
                else Texts[parts[1]] = value;
            }
        }

        /// Odwrotność escape() z build_plugin.py.
        private static string Unescape(string value)
        {
            if (value.IndexOf('\\') < 0) return value;

            var text = new StringBuilder(value.Length);
            for (var i = 0; i < value.Length; i++)
            {
                if (value[i] != '\\' || i + 1 >= value.Length)
                {
                    text.Append(value[i]);
                    continue;
                }
                i++;
                if (value[i] == 'n') text.Append('\n');
                else if (value[i] == 't') text.Append('\t');
                else text.Append(value[i]);
            }
            return text.ToString();
        }

        internal static bool PolishActive()
        {
            try
            {
                var vars = GlobalVars.instance;
                return vars != null && vars.curLanguage == LanguageCode;
            }
            catch
            {
                return false;
            }
        }
    }

    [HarmonyPatch(typeof(GlobalTextCtrl), "GetText")]
    internal static class TextPatch
    {
        private static int _served;
        private static int _missing;

        private static void Postfix(string type, string id, ref string __result)
        {
            if (!Plugin.PolishActive()) return;

            string polish;
            if (Plugin.Texts.TryGetValue(type + "/" + id, out polish))
            {
                __result = polish;
                if (++_served == 1) Plugin.Log.LogInfo("Pierwszy polski tekst podany grze.");
            }
            else if (++_missing <= 5)
            {
                Plugin.Log.LogWarning("Bez tłumaczenia: " + type + "/" + id);
            }
        }
    }

    [HarmonyPatch(typeof(GlobalTextCtrl), "GetTextName")]
    internal static class NamePatch
    {
        private static void Postfix(string type, string id, ref string __result)
        {
            if (!Plugin.PolishActive()) return;

            string polish;
            if (Plugin.Names.TryGetValue(type + "/" + id, out polish)) __result = polish;
        }
    }

    /// Przycisk włoski stoi w każdej scenie obok siatki języków, wyłączony.
    /// Ożywiamy go, przemianowujemy na polski i wstawiamy do siatki.
    [HarmonyPatch(typeof(LanguageToggleGroup), "OnEnable")]
    internal static class MenuPatch
    {
        private static void Postfix(LanguageToggleGroup __instance)
        {
            try
            {
                Install(__instance);
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się ożywić przycisku polskiego: " + error);
            }
        }

        private static void Install(LanguageToggleGroup group)
        {
            var button = FindInactive(Plugin.ParkedButton);
            if (button == null)
            {
                Plugin.Log.LogWarning("Nie znalazłem zaparkowanego przycisku " + Plugin.ParkedButton + ".");
                return;
            }

            var mapping = button.GetComponent<LanguageMapToggle>();
            if (mapping == null)
            {
                Plugin.Log.LogWarning("Przycisk nie ma komponentu wyboru języka.");
                return;
            }

            var languageField = typeof(LanguageMapToggle).GetField("_language",
                BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
            if (languageField == null)
            {
                Plugin.Log.LogWarning("Komponent wyboru języka nie ma pola z kodem języka.");
                return;
            }

            var already = Plugin.LanguageCode.Equals(languageField.GetValue(mapping) as string, StringComparison.Ordinal);
            if (already && button.activeSelf) return;

            languageField.SetValue(mapping, Plugin.LanguageCode);
            SetLabel(button);

            var grid = group.transform;
            if (button.transform.parent != grid) button.transform.SetParent(grid, false);
            button.SetActive(true);

            Plugin.Log.LogInfo("Polski przycisk ożywiony i wstawiony do siatki języków.");
        }

        /// Podpis siedzi w potomnym obiekcie tekstowym; sięgamy po niego bez wiązania
        /// się z TextMeshPro, bo wystarczy właściwość „text".
        private static void SetLabel(GameObject button)
        {
            foreach (var component in button.GetComponentsInChildren<Component>(true))
            {
                if (component == null) continue;
                var property = component.GetType().GetProperty("text", typeof(string));
                if (property == null || !property.CanWrite) continue;

                var current = property.GetValue(component, null) as string;
                if (string.IsNullOrEmpty(current)) continue;
                if (current == Plugin.LanguageLabel) return;

                property.SetValue(component, Plugin.LanguageLabel, null);
                return;
            }
            Plugin.Log.LogWarning("Nie znalazłem podpisu na przycisku — zostanie włoski.");
        }

        /// GameObject.Find nie widzi obiektów wyłączonych, a nasz właśnie taki jest.
        private static GameObject FindInactive(string name)
        {
            foreach (var transform in Resources.FindObjectsOfTypeAll<Transform>())
            {
                if (transform != null && transform.name == name && transform.hideFlags == HideFlags.None)
                {
                    return transform.gameObject;
                }
            }
            return null;
        }
    }
}
