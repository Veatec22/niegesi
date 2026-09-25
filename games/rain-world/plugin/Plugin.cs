// Nie gęsi — polski dla Rain World jako osobny język gry.
//
// Rain World ma własnego BepInEksa i system modów (Remix). Języki są rozszerzalnym
// ExtEnumem, a teksty gra czyta z text/text_<trzy litery nazwy>/ — także z folderów
// modów. Wystarczy więc zarejestrować język „Polish” (folder text_pol leży obok,
// w tym samym modzie) i dopisać go do listy języków w menu opcji, która jest w kodzie
// sztywną tablicą. Żaden plik gry nie jest podmieniany; pozostałe języki działają jak dotąd.

using System;
using System.Collections.Generic;
using System.Reflection;
using System.Reflection.Emit;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using UnityEngine;

namespace NieGesi.RainWorldPL
{
    [BepInPlugin(Id, "Rain World PL", Version)]
    public class Plugin : BaseUnityPlugin
    {
        public const string Id = "niegesi.rainworld.polski";
        public const string Version = "0.2.0";

        // Nazwa wartości ExtEnuma. Pierwsze trzy litery wyznaczają folder tekstów: text_pol.
        internal const string LanguageName = "Polish";

        internal static ManualLogSource Log;
        internal static InGameTranslator.LanguageID Polish;

        private void Awake()
        {
            Log = Logger;
            Logger.LogInfo(string.Format("PL {0}; gra {1}, Unity {2}.", Version, GameVersion(), Application.unityVersion));

            try
            {
                Polish = new InGameTranslator.LanguageID(LanguageName, true);
                Logger.LogInfo("Zarejestrowano język " + LanguageName + " (indeks " + Polish.Index + ").");
            }
            catch (Exception error)
            {
                Logger.LogError("Nie udało się dodać języka, gra zostaje bez polskiego: " + error);
                return;
            }

            var harmony = new Harmony(Id);
            Patch(harmony, typeof(OptionsMenuPatch), "lista języków w opcjach");
            Patch(harmony, typeof(ShortStringsPatch), "polskie teksty interfejsu");
            Patch(harmony, typeof(DecryptPatch), "czatlogi i komentarz twórców");
            Patch(harmony, typeof(MissingPatch), "log brakujących tekstów");
        }

        // Każda łatka osobno: jeśli aktualizacja gry zmieni jedno miejsce, reszta działa dalej.
        private void Patch(Harmony harmony, Type patch, string what)
        {
            try
            {
                harmony.PatchAll(patch);
            }
            catch (Exception error)
            {
                Logger.LogWarning("Nie założono łatki (" + what + "): " + error.Message);
            }
        }

        private void OnApplicationQuit()
        {
            if (MissingPatch.Seen.Count > 0)
                Logger.LogInfo("Teksty bez polskiego tłumaczenia w tej sesji: " + MissingPatch.Seen.Count + ".");
        }

        // Po nazwie, nie po typie: brak pola w innej wersji gry nie może wywrócić pluginu.
        private static string GameVersion()
        {
            try
            {
                var field = AccessTools.Field(typeof(global::RainWorld), "GAME_VERSION_STRING");
                return field != null ? (string)field.GetValue(null) : "?";
            }
            catch (Exception)
            {
                return "?";
            }
        }

        internal static bool PolishActive()
        {
            var world = RWCustom.Custom.rainWorld;
            return Polish != null && world != null && world.inGameTranslator != null
                && world.inGameTranslator.currentLanguage == Polish;
        }
    }

    /// Menu opcji buduje przyciski z tablicy languageOrder (dziesięć języków wpisanych
    /// w kod). Dopisujemy polski tuż przed zapisem tablicy do pola.
    [HarmonyPatch(typeof(Menu.OptionsMenu), MethodType.Constructor, new[] { typeof(ProcessManager) })]
    internal static class OptionsMenuPatch
    {
        private static IEnumerable<CodeInstruction> Transpiler(IEnumerable<CodeInstruction> instructions)
        {
            var field = AccessTools.Field(typeof(Menu.OptionsMenu), "languageOrder");
            var add = AccessTools.Method(typeof(OptionsMenuPatch), nameof(AddPolish));
            var done = false;
            foreach (var instruction in instructions)
            {
                if (!done && field != null && instruction.opcode == OpCodes.Stfld && Equals(instruction.operand, field))
                {
                    yield return new CodeInstruction(OpCodes.Call, add);
                    done = true;
                }
                yield return instruction;
            }
            if (!done)
                Plugin.Log.LogWarning("Nie znalazłem listy języków w menu opcji — polski wybierzesz tylko, jeśli był już ustawiony.");
        }

        private static InGameTranslator.LanguageID[] AddPolish(InGameTranslator.LanguageID[] order)
        {
            if (Plugin.Polish == null || Array.IndexOf(order, Plugin.Polish) >= 0) return order;
            var extended = new InGameTranslator.LanguageID[order.Length + 1];
            order.CopyTo(extended, 0);
            extended[order.Length] = Plugin.Polish;
            return extended;
        }
    }

    /// Gra wczytuje najpierw angielski strings.txt, a potem tabelę bieżącego języka — ale tylko
    /// wtedy, gdy ta leży w katalogu podstawki (StreamingAssets/text/text_pol). Nasza leży
    /// w folderze moda, więc doczytujemy ją sami, tym samym formatem co gra. Angielski
    /// zostaje pod spodem: czego nie ma po polsku, pokaże się po angielsku.
    [HarmonyPatch(typeof(InGameTranslator), "LoadShortStrings")]
    internal static class ShortStringsPatch
    {
        internal const string File = "text/text_pol/strings.txt";
        internal static readonly HashSet<string> Keys = new HashSet<string>(StringComparer.Ordinal);
        private static int logged = -1;

        private static void Postfix(InGameTranslator __instance)
        {
            try
            {
                if (!Plugin.PolishActive()) return;
                var path = AssetManager.ResolveFilePath(File);
                if (!System.IO.File.Exists(path))
                {
                    Plugin.Log.LogWarning("Brak " + File + " w modzie — teksty zostają po angielsku.");
                    return;
                }
                var text = System.IO.File.ReadAllText(path, System.Text.Encoding.UTF8);
                if (text.Length > 0 && text[0] == '0') text = text.Substring(1);
                var table = MissingPatch.ShortStrings(__instance);
                var count = 0;
                foreach (var raw in text.Split(new[] { "\r\n", "\n" }, StringSplitOptions.None))
                {
                    var line = raw.Contains("///") ? raw.Split('/')[0].TrimEnd() : raw;
                    var bar = line.IndexOf('|');
                    if (bar <= 0 || bar == line.Length - 1) continue;
                    var key = line.Substring(0, bar);
                    table[key] = line.Substring(bar + 1);
                    Keys.Add(key);
                    count++;
                }
                if (count != logged)
                {
                    Plugin.Log.LogInfo("Wczytano " + count + " polskich tekstów z " + path + ".");
                    logged = count;
                }
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się wczytać polskich tekstów: " + error.Message);
            }
        }
    }

    /// Czatlogi, transmisje i komentarz twórców z Downpour gra deszyfruje bezwarunkowo
    /// (ChatlogData.DecryptResult). Nasze pliki są otwartym tekstem ze znacznikiem 0 na początku
    /// — takie przepuszczamy bez zmian. Zaszyfrowane oryginały zaczynają się od 1 i idą jak dotąd.
    [HarmonyPatch(typeof(MoreSlugcats.ChatlogData), "DecryptResult")]
    internal static class DecryptPatch
    {
        private static bool Prefix(string __0, ref string __result)
        {
            var text = __0 == null ? null : __0.TrimStart('﻿');
            if (string.IsNullOrEmpty(text) || text[0] != '0') return true;
            __result = text;
            return false;
        }
    }

    /// Brak polskiego wpisu gra i tak obsługuje: pokazuje angielski. Zapisujemy w logu
    /// każdy taki tekst raz, żeby zgłoszenie od gracza mówiło, czego brakuje.
    [HarmonyPatch(typeof(InGameTranslator), nameof(InGameTranslator.Translate))]
    internal static class MissingPatch
    {
        internal static readonly HashSet<string> Seen = new HashSet<string>(StringComparer.Ordinal);
        internal static readonly AccessTools.FieldRef<InGameTranslator, Dictionary<string, string>> ShortStrings =
            AccessTools.FieldRefAccess<InGameTranslator, Dictionary<string, string>>("shortStrings");

        private static void Postfix(InGameTranslator __instance, string s)
        {
            try
            {
                if (string.IsNullOrEmpty(s) || !Plugin.PolishActive()) return;
                if (ShortStringsPatch.Keys.Count > 0 && !ShortStringsPatch.Keys.Contains(s) && Seen.Add(s))
                    Plugin.Log.LogInfo("Brak tłumaczenia: " + s.Replace("\n", "\\n"));
            }
            catch (Exception)
            {
                // Tylko diagnostyka — nigdy nie przeszkadza grze.
            }
        }
    }
}
