// Przycisk „Polski” w panelu języków menu głównego.
//
// Panel języków to gotowy prefab z przyciskami, które przez trwałe wywołanie
// UIMGMainMenu.OnSetLanguage(string) ustawiają język, zapisują opcje i przeładowują scenę.
// Klonujemy ostatni taki przycisk, podpisujemy „Polski” i podpinamy OnSetLanguage("Polish").
// Budowę panelu wypisujemy do logu, żeby test w grze dał fakty o układzie.

using System;
using System.Collections.Generic;
using HarmonyLib;
using TMPro;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

namespace notgeese.WildBastards
{
    [HarmonyPatch]
    internal static class LanguageButton
    {
        private const string CloneName = "notgeese Polski";
        private static Sprite flag;

        [HarmonyPostfix]
        [HarmonyPatch(typeof(UIMGMainMenu), "Start")]
        private static void AfterStart(UIMGMainMenu __instance)
        {
            try
            {
                Add(__instance);
            }
            catch (Exception error)
            {
                Plugin.Log.LogError("Nie udało się dodać przycisku Polski: " + error);
            }
        }

        private static void Add(UIMGMainMenu menu)
        {
            var panel = Traverse.Create(menu).Field("languagePanel").GetValue<GameObject>();
            if (panel == null)
            {
                Plugin.Log.LogWarning("Brak panelu języków w menu głównym.");
                return;
            }
            if (FindChild(panel.transform, CloneName) != null) return;

            var buttons = new List<Button>();
            foreach (var button in panel.GetComponentsInChildren<Button>(true))
            {
                var calls = button.onClick.GetPersistentEventCount();
                for (var i = 0; i < calls; i++)
                {
                    if (button.onClick.GetPersistentMethodName(i) != "OnSetLanguage") continue;
                    buttons.Add(button);
                    Plugin.Log.LogInfo(string.Format("Przycisk języka „{0}” → OnSetLanguage(\"{1}\"), tekst: {2}",
                        button.name, PersistentArgument(button.onClick, i), Texts(button.gameObject)));
                    break;
                }
            }
            if (buttons.Count == 0)
            {
                Plugin.Log.LogWarning("Panel języków nie ma przycisków OnSetLanguage — nie dodaję Polskiego.");
                return;
            }

            // Gra ukrywa część języków (w prefabie są wyłączone przyciski), więc wzorem jest
            // ostatni aktywny przycisk, a klon ląduje tuż za nim i jest jawnie włączony.
            var template = buttons[buttons.Count - 1];
            for (var i = buttons.Count - 1; i >= 0; i--)
            {
                if (!buttons[i].gameObject.activeSelf) continue;
                template = buttons[i];
                break;
            }
            var clone = UnityEngine.Object.Instantiate(template.gameObject, template.transform.parent, false);
            clone.name = CloneName;
            clone.SetActive(true);
            clone.transform.SetSiblingIndex(template.transform.GetSiblingIndex() + 1);

            foreach (var localize in clone.GetComponentsInChildren<I2.Loc.Localize>(true))
                UnityEngine.Object.DestroyImmediate(localize);
            foreach (var text in clone.GetComponentsInChildren<TMP_Text>(true))
                text.text = Plugin.ButtonLabel;
            foreach (var text in clone.GetComponentsInChildren<Text>(true))
                text.text = Plugin.ButtonLabel;
            foreach (var image in clone.GetComponentsInChildren<Image>(true))
            {
                var spriteName = image.sprite != null ? image.sprite.name : "";
                if ((image.name + spriteName).IndexOf("flag", StringComparison.OrdinalIgnoreCase) >= 0)
                    image.sprite = Flag();
            }

            var cloneButton = clone.GetComponent<Button>();
            cloneButton.onClick = new Button.ButtonClickedEvent();
            var setLanguage = AccessTools.Method(typeof(UIMGMainMenu), "OnSetLanguage");
            cloneButton.onClick.AddListener(() => setLanguage.Invoke(menu, new object[] { Plugin.LanguageName }));

            var parent = template.transform.parent;
            if (parent.GetComponent<LayoutGroup>() == null && buttons.Count >= 2)
            {
                var previous = buttons[buttons.Count - 2].transform as RectTransform;
                var last = template.transform as RectTransform;
                var rect = clone.transform as RectTransform;
                if (previous != null && last != null && rect != null)
                    rect.anchoredPosition = last.anchoredPosition + (last.anchoredPosition - previous.anchoredPosition);
            }

            Plugin.Log.LogInfo(string.Format("Dodano przycisk Polski (wzór: „{0}”, rodzic: „{1}”, układ: {2}, przycisków: {3}).",
                template.name, parent.name, parent.GetComponent<LayoutGroup>() != null ? parent.GetComponent<LayoutGroup>().GetType().Name : "brak",
                buttons.Count + 1));
        }

        private static string PersistentArgument(UnityEventBase evt, int index)
        {
            try
            {
                var calls = Traverse.Create(evt).Field("m_PersistentCalls").Field("m_Calls").GetValue<System.Collections.IList>();
                return Traverse.Create(calls[index]).Field("m_Arguments").Field("m_StringArgument").GetValue<string>();
            }
            catch (Exception)
            {
                return "?";
            }
        }

        private static string Texts(GameObject target)
        {
            var parts = new List<string>();
            foreach (var text in target.GetComponentsInChildren<TMP_Text>(true))
                parts.Add("„" + text.text + "” (" + (text.font != null ? text.font.name : "?") + ")");
            foreach (var image in target.GetComponentsInChildren<Image>(true))
                parts.Add("obraz " + image.name + (image.sprite != null ? ":" + image.sprite.name : ""));
            return string.Join(", ", parts.ToArray());
        }

        private static Transform FindChild(Transform root, string name)
        {
            foreach (var child in root.GetComponentsInChildren<Transform>(true))
                if (child.name == name) return child;
            return null;
        }

        private static Sprite Flag()
        {
            if (flag != null) return flag;
            var texture = new Texture2D(32, 20, TextureFormat.RGBA32, false);
            var white = new Color32(255, 255, 255, 255);
            var red = new Color32(220, 20, 60, 255);
            for (var y = 0; y < 20; y++)
                for (var x = 0; x < 32; x++)
                    texture.SetPixel(x, y, y >= 10 ? white : red);
            texture.Apply();
            flag = Sprite.Create(texture, new Rect(0, 0, 32, 20), new Vector2(0.5f, 0.5f));
            flag.name = "notgeese flaga PL";
            UnityEngine.Object.DontDestroyOnLoad(texture);
            return flag;
        }
    }
}
