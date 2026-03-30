## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-03-30T12:45:35.810976_

```text
╔═══════════════════ LIVE WORLD SNAPSHOT ════════════════════╗
║ [SOL] Sol 7   [SEASON] Early Spring                        ║
║ [TEMP] -31C   [SUN] 89%   [STORM] NO                       ║
║ [EVENT] None                                               ║
║ [POP] 18   [BLD] 9   [PLY] 3                               ║
║ [O2] 1000   [H2O] 545   [E] 1000                           ║
║ [FOOD] 300   [MAT] 0                                       ║
║ [AI] Solar Activity Boosts Power Systems | solar_activity  ║
║ +5                                                         ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ RESOURCE RESERVES ═════════════════════╗
║ OXYGEN    1000                                             ║
║ WATER     545                                              ║
║ ENERGY    1000                                             ║
║ FOOD      300                                              ║
║ MATERIALS 0                                                ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ MARKET PRICES ═══════════════════════╗
║ [O2] 0   [H2O] 0                                           ║
║ [FOOD] 0   [MAT] 0                                         ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ AI DAILY DIRECTIVE ════════════════════╗
║ Solar Activity Boosts Power Systems                        ║
║ Solar activity has increased to 84%, providing a temporary ║
║ surge in energy generation across all colonies.            ║
║ EFFECT solar_boost | solar_activity +5                     ║
╚════════════════════════════════════════════════════════════╝

╔═════════════════════ COLONY STANDINGS ═════════════════════╗
║ RK NAME             CORP                 POP BLD SCORE     ║
║  1 Marco Quinn      Dustline Agro          7   3  1476     ║
║  2 Zoya Kade        Ares Systems           5   4  1300     ║
║  3 Irina Vale       Helios Prospecting     6   2  1203     ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ MISSION BOARD ═══════════════════════╗
║ 1. Expand Water Extraction | REWARD Gain increased water   ║
║ reserves for your colony.                                  ║
║    OBJ Deploy and activate additional water extraction     ║
║ units near Helios Prospecting.                             ║
║    RISK Potential mechanical failure due to harsh terrain. ║
║ 2. Optimize Energy Storage | REWARD Improved energy        ║
║ storage capacity.                                          ║
║    OBJ Install enhanced battery modules at Dustline Agro   ║
║ facilities.                                                ║
║    RISK Installation delays may cause missed energy gains. ║
║ 3. Food Supply Recon | REWARD Potential increase in food   ║
║ resources.                                                 ║
║    OBJ Survey and report viable agricultural sites near    ║
║ Ares Systems.                                              ║
║    RISK Exposure to cold may impact scouting team health.  ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ NPC TRANSMISSIONS ═════════════════════╗
║ Mars Control -> all colonies | Solar activity elevated;    ║
║ optimize energy harvesting to capitalize on increased      ║
║ power.                                                     ║
║ Helios Prospecting -> Mars Control | Request assistance    ║
║ for additional water extraction units to support expanding ║
║ operations.                                                ║
╚════════════════════════════════════════════════════════════╝

╔═════════════════════ COLONY NEWS FEED ═════════════════════╗
║ On Sol 7 of early spring, Mars experiences a significant   ║
║ solar activity boost enhancing energy production. Colonies ║
║ are advised to optimize resource extraction and storage to ║
║ maximize benefits. Conditions remain stable with no dust   ║
║ storms reported.                                           ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ RECENT EVENTS ═══════════════════════╗
║ 2026-03-30T12:45:35.810976 | AI directive: Solar Activity  ║
║ Boosts Power Systems                                       ║
║ 2026-03-30T12:45:27.759588 | Martian day 7 has begun       ║
║ 2026-03-30T12:39:58.394061 | AI directive: Operations      ║
║ drift into a new rhythm                                    ║
║ 2026-03-30T12:39:57.598851 | Martian day 6 has begun       ║
║ 2026-03-30T12:39:56.762403 | Science crews are locking the ║
║ site down for analysis: 📡 Strange signal on 1420 MHz       ║
║ detected.                                                  ║
╚════════════════════════════════════════════════════════════╝
```

<!-- WORLD_SUMMARY:END -->



















```text
┌──────────────────────────────────────────────────────────────┐
│ MARS COLONY REPO                                            │
│ git + GitHub Actions drive the concept loop                 │
│ use the links below as the entrypoint into the repo         │
└──────────────────────────────────────────────────────────────┘
```

## QUICK LINKS

- [Player Instructions](PLAYER_INSTRUCTIONS.md)
- [CI/CD Setup](CI_CD_SETUP.md)
- [Game Client](mars_client.py)
- [World State](world_state.json)
- [Workflows](.github/workflows/)

The scheduled game loop runs through one orchestrator workflow and executes the
economy, random events, Mars day, daily AI content, and README summary stages in
sequence.
