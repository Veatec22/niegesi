# Laika — manifest pokrycia review po fullu (2026-09-24)

Wejście: `translations/en-pl-review.json` (SHA-256 7b16b51b…6ea7338), `translations/pl.json`
(SHA-256 de0fcdcc…9333921). Zgodność: 3470 = 3470 kluczy, 0 rozjazdów PL, 0 rozjazdów EN
względem `work/source/en.json` (4209 wpisów, 739 pustych — poza zakresem).

Dialogi czytane scenami w kolejności skryptów `D_*` z tabel gry (scratchpad `ta/`);
49 kluczy bez skryptu (HideAndSeek, część Pillars/CatacombsFail/Antennas/FixingHarpoon)
dołączone do sceny z klucza, w kolejności numerów.

| Partia | Zakres | Wpisy | Stan |
| --- | --- | ---: | --- |
| UI_1 | AC_* (86), UI_BLACKJACK…UI_TUT_CHECKPOINT | ~320 | przeczytane |
| UI_2 | UI_TUT_DASH…UI_WEAPONS_HELP, `task` | ~58 | przeczytane |
| CHARACTERS | CH_* | 79 | przeczytane |
| ZONES | ZN_* | 83 | przeczytane |
| ITEMS_1–2 | I_* (236), R_* (28) | 264 | przeczytane |
| QUESTS_1–2 | Q_D_* | 218 | przeczytane |
| d01 | D_0_* (prolog), D_1_Mines_*, D_2_Lighthouse_Antennas…Borderpoints_Undone8C | ~330 | przeczytane |
| d02 | D_2_Lighthouse_Borderpoints_Undone8D…Wastelands, D_3_TheBigTree_AfterBoss…Prima_Meeting | ~300 | przeczytane |
| d03 | D_3_Prima_Undone…Wastelands_1, D_4_FloatingCity_*, D_6_*, D_A_Blackjack, D_A_Dictionary, D_A_GiftsPuppy_Bike | ~290 | przeczytane |
| d04 | D_A_GiftsPuppy_BookMother…Ukulele, D_A_MapGuy, D_A_MayasHouse, D_A_Musicians, D_A_Statues, D_A_Tapes, D_B_Alfredo (część) | ~290 | przeczytane |
| d05 | D_B_Alfredo…D_B_Maya_A1 (Anarchist, Anthropologist, Blacksmith, Borden, Bustender, Camilla, Carey, Chief, Cook, Dalia, DyingBird, Entomologist, Gunlady, Herman, Hilda, Kidgutter, Laika, Leatherworker, Lewis) | ~245 | przeczytane |
| d06 | D_B_Maya_A2…D_B_Tapeguy_Tapes1 (Maya, Merchant, Miner, Molly, Pebble, Petey, Primo, Puppy, Rapist, Shaza, Shopkeeper*) | ~285 | przeczytane |
| d07 | D_B_Tapeguy_Tapes2…D_M_Bags1 (Tressie, Undertaker, D_F_* retrospekcje, D_K_* porwanie) | ~320 | przeczytane |
| d08 | D_M_*, D_S_BoneFlour…D_S_NewSheriff_Briefing | ~335 | przeczytane |
| d09 | D_S_NewSheriff_Complete…D_S_TutorialDash_Briefing | ~300 | przeczytane |
| d10 | D_S_TutorialDash_*, D_S_TutorialHook_*, D_S_YoungLaika_*, D_TutorialDash_* | ~115 | przeczytane |

Razem: DIALOGUES 2448 (716 scen), UI 378, ITEMS 264, QUESTS 218, ZONES 83, CHARACTERS 79 = 3470.
Luki: brak nieprzeczytanych partii. Wpisy bez rozstrzygnięcia (brak kontekstu) wymienione
w raporcie `docs/localization-review.md`.

Kontrole pomocnicze (skrypty jednorazowe, bez zmian w repo): formy 1. os. czasu przeszłego
względem płci mówiącego (tylko 3 znane fałszywe alarmy Primo), formy 2. os. męskie
(wszystkie do postaci męskich), odmiana żeńskich imion na spółgłoskę/-o, spójność
terminów (wieniec/wianek, pogrzebowa przyjaciółka, dwuskrzydłowy, „Język!”, „zamknięcie”),
limity pól UI (PL dłuższe od EN i od limitu: tylko UI_TUT_CANDLES_DESC).
Fakty z RU/ES/FR: sklepikarze W02/W04/W06, Antropolog, sierżant, dzieci, Unae, kwestie sporne.
