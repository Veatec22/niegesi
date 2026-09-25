// Not Geese — polski dla Laika: Aged Through Blood, podstawiany w czasie działania gry.
//
// Gra używa M2H Localization: arkusz tekstów to TextAsset „Languages/<KOD>_<ARKUSZ>”
// w Resources, a lista języków powstaje z enuma LanguageCode (jest w nim PL) przez
// sprawdzenie, czy dla kodu istnieje pierwszy arkusz. Plugin mówi grze, że arkusze PL
// istnieją, i podaje je z pl.tsv, zbudowane na angielskich: czego nie mamy, zostaje
// po angielsku. W opcjach dopisuje „POLSKI” do listy języków. Wybór zapamiętuje sama
// gra (PlayerPrefs „M2H_lastLanguage”). Żaden plik gry nie jest podmieniany.

using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Security;
using System.Text;
using System.Xml;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using TMPro;
using UnityEngine;
using SettingsViewItem = Laika.UI.Settings.SettingsViewItem;

namespace notgeese.Laika
{
    // Wydanie sprzed zmiany nazwy projektu miało inny GUID. Gdy jego katalog został w plugins,
    // BepInEx pominie ten plugin zamiast ładować dwa spolszczenia naraz.
    [BepInIncompatibility("cc.notgoose.laika")]
    [BepInPlugin(Id, "Laika PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "cc.notgeese.laika";
        public const string Version = "0.2.0";

        internal const string Code = "PL";
        internal const string MenuName = "POLSKI";
        internal const string TermsFile = "pl.tsv";

        internal static ManualLogSource Log;

        /// Klucz gry → polski tekst.
        internal static Dictionary<string, string> Terms;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("PL {0}; gra {1} {2}, Unity {3}.", Version,
                Application.productName, Application.version, Application.unityVersion));

            Terms = ReadTerms();
            if (Terms.Count == 0)
            {
                Logger.LogError("Nie znalazłem tekstów w " + TermsFile + " — polski nie pojawi się na liście języków.");
                return;
            }

            // Zakładanie łatek na klasę Language potrafi uruchomić jej statyczny konstruktor,
            // zanim łatka HasLanguageFile zadziała: gra buduje wtedy listę języków bez PL,
            // nie może przywrócić zapisanego PL i nadpisuje go w PlayerPrefs. Czytamy go więc
            // wcześniej, a po wczytaniu pierwszej sceny przełączamy z powrotem.
            try { saved = PlayerPrefs.GetString(LastLanguageKey, ""); }
            catch (Exception) { saved = ""; }

            try
            {
                var harmony = new Harmony(Id);
                harmony.PatchAll(typeof(LanguagePatch));
                harmony.PatchAll(typeof(MenuPatch));
                UnityEngine.SceneManagement.SceneManager.sceneLoaded += (scene, mode) =>
                {
                    RestoreSaved();
                    Fonts.Refresh();
                };
                var patched = 0;
                foreach (var method in harmony.GetPatchedMethods()) patched++;
                Logger.LogInfo("Wczytano " + Terms.Count + " wpisów, założone łatki: " + patched + ".");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się wpiąć w system języków, polskiego nie będzie: " + error.Message);
            }
        }

        /// Plik obok biblioteki: klucz, tabulator, tekst.
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
                terms[entry.Substring(0, tab)] = entry.Substring(tab + 1);
            }
            return terms;
        }

        internal const string LastLanguageKey = "M2H_lastLanguage";
        private static string saved;

        private static void RestoreSaved()
        {
            if (saved != Code) return;
            saved = null;
            try
            {
                if (Language.CurrentLanguage().ToString() == Code) return;
                Log.LogInfo("Przywracam zapisany język PL.");
                Language.SwitchLanguage(Code);
            }
            catch (Exception error)
            {
                Log.LogWarning("Nie udało się przywrócić polskiego: " + error.Message);
            }
        }

        private static readonly AccessTools.FieldRef<List<string>> Available =
            AccessTools.StaticFieldRefAccess<List<string>>(AccessTools.Field(typeof(Language), "availableLanguages"));

        /// Lista języków M2H musi mieć PL, inaczej Language.SwitchLanguage odmawia.
        internal static void EnsureAvailable()
        {
            var list = Available();
            if (list == null || list.Contains(Code)) return;
            list.Add(Code);
            Log.LogInfo("Lista języków gry powstała bez PL — dopisano.");
        }

        internal static bool PolishActive()
        {
            return Terms != null && Language.CurrentLanguage().ToString() == Code;
        }
    }

    /// Arkusze PL: angielski XML gry z podmienionymi tekstami, które mamy.
    internal static class Sheets
    {
        private static readonly Dictionary<string, string> Cache = new Dictionary<string, string>();
        private static readonly HashSet<string> Reported = new HashSet<string>();

        internal static TextAsset English(string sheet)
        {
            return Resources.Load("Languages/EN_" + sheet, typeof(TextAsset)) as TextAsset;
        }

        internal static string Build(string sheet)
        {
            string xml;
            if (Cache.TryGetValue(sheet, out xml)) return xml;
            var english = English(sheet);
            if (english == null) return "";

            var output = new StringBuilder(english.text.Length + 1024);
            output.Append("<entries>\n");
            int total = 0, missing = 0;
            using (var reader = XmlReader.Create(new StringReader(english.text)))
            {
                while (reader.ReadToFollowing("entry"))
                {
                    var key = reader.GetAttribute("name");
                    var text = reader.ReadElementContentAsString();
                    if (key == null) continue;
                    string polish;
                    if (Plugin.Terms.TryGetValue(key, out polish)) text = polish;
                    else if (text.Trim().Length > 0) missing++;
                    total++;
                    output.Append("<entry name=\"").Append(SecurityElement.Escape(key)).Append("\">")
                        .Append(SecurityElement.Escape(text)).Append("</entry>\n");
                }
            }
            // Opcje zaznaczają bieżący język po nazwie z wpisu UI_SETTINGS_LANGUAGE_<KOD>,
            // którego w angielskim arkuszu dla PL oczywiście nie ma.
            if (sheet == "UI")
                output.Append("<entry name=\"UI_SETTINGS_LANGUAGE_").Append(Plugin.Code).Append("\">")
                    .Append(Plugin.MenuName).Append("</entry>\n");
            output.Append("</entries>\n");
            xml = output.ToString();
            Cache[sheet] = xml;

            if (Reported.Add(sheet))
            {
                if (missing > 0)
                    Plugin.Log.LogWarning(string.Format("Arkusz {0}: {1} z {2} tekstów bez polskiego tłumaczenia — zostaną po angielsku.",
                        sheet, missing, total));
                else
                    Plugin.Log.LogInfo(string.Format("Arkusz {0}: wszystkie {1} teksty po polsku.", sheet, total));
            }
            return xml;
        }
    }

    [HarmonyPatch]
    internal static class LanguagePatch
    {
        // Lista języków gry: PL „istnieje”, jeśli istnieje odpowiedni arkusz angielski.
        [HarmonyPrefix]
        [HarmonyPatch(typeof(Language), "HasLanguageFile")]
        private static bool HasLanguageFile(string lang, string sheetTitle, ref bool __result)
        {
            if (lang != Plugin.Code) return true;
            __result = Sheets.English(sheetTitle) != null;
            return false;
        }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(Language), "SwitchLanguage", new[] { typeof(LanguageCode) })]
        private static void BeforeSwitch()
        {
            try { Plugin.EnsureAvailable(); }
            catch (Exception error) { Plugin.Log.LogWarning("Lista języków: " + error.Message); }
        }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(Language), "GetLanguageFileContents")]
        private static bool GetLanguageFileContents(string sheetTitle, ref string __result)
        {
            if (!Plugin.PolishActive()) return true;
            try
            {
                __result = Sheets.Build(sheetTitle);
                return false;
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Arkusz " + sheetTitle + ": " + error.Message + " — zostaje angielski.");
                var english = Sheets.English(sheetTitle);
                __result = english != null ? english.text : "";
                return false;
            }
        }

        [HarmonyPostfix]
        [HarmonyPatch(typeof(Language), "DoSwitch")]
        private static void Switched()
        {
            Plugin.Log.LogInfo("Język gry: " + Language.CurrentLanguage());
            Fonts.Refresh();
        }

        // Fonty przychodzą ze scen i zasobów w różnych chwilach. Nowy font tylko zaznacza,
        // że jest co robić; litery składamy przed najbliższym pobraniem tekstu.
        [HarmonyPostfix]
        [HarmonyPatch(typeof(TMP_FontAsset), "Awake")]
        private static void FontLoaded()
        {
            Fonts.Pending = true;
        }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(Language), "Get", new[] { typeof(string), typeof(string) })]
        private static void BeforeGet()
        {
            if (Fonts.Pending) Fonts.Refresh();
        }
    }

    /// Opcje → Język: nazwy i kody to dwie równoległe listy zaszyte w kodzie gry.
    [HarmonyPatch]
    internal static class MenuPatch
    {
        private static readonly AccessTools.FieldRef<SettingsViewItem, List<string>> Codes =
            AccessTools.FieldRefAccess<SettingsViewItem, List<string>>("languageCodes");

        [HarmonyPostfix]
        [HarmonyPatch(typeof(SettingsViewItem), "LanguageNamesList", MethodType.Getter)]
        private static void Names(ref List<string> __result)
        {
            if (__result != null && !__result.Contains(Plugin.MenuName)) __result.Add(Plugin.MenuName);
        }

        [HarmonyPrefix]
        [HarmonyPatch(typeof(SettingsViewItem), "SetLayout")]
        private static void SetLayout(SettingsViewItem __instance)
        {
            var codes = Codes(__instance);
            if (codes != null && !codes.Contains(Plugin.Code)) codes.Add(Plugin.Code);
        }
    }

    internal static class Fonts
    {
        internal static bool Pending = true;

        internal static void Refresh()
        {
            try
            {
                if (!Plugin.PolishActive()) return;
                Pending = false;
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
