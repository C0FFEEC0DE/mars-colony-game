## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-27T00:27:37.832376_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 70 | [SEASON] Early      ║  ║ Mild Solar Boost Enhances Energy   ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -57C | [SUN] 87% | [STORM]  ║  ║ Solar activity at 82% provides a   ║
║ NO                                 ║  ║ slight increase in solar panel     ║
║ [EVENT] Underground Ice Deposit    ║  ║ efficiency, improving energy       ║
║ Secured on Sol 70                  ║  ║ generation across all colonies.    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1200   ║  ║ solar_activity +5                  ║
║ [FOOD] 2600 | [MAT] 1150           ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Boost Enhances     ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Optimize Solar Arrays           ║
║    Ares Systems | P1 B4 | S8799    ║  ║    Perform maintenance and…        ║
║ 2. Marco Quinn                     ║  ║ 2. Water Recycling System Check    ║
║    Dustline Agro | P1 B3 | S8785   ║  ║    Inspect and repair the water…   ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S7246         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is favorable…             ║
║ ENERGY    1200                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      2600                     ║  ║ stable conditions…                 ║
║ MATERIALS 1150                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 70 in early spring, Mars    ║  ║ 00:27 | AI directive: Mild Solar…  ║
║ colonies experience a mild solar   ║  ║ 00:27 | Exploration teams led by…  ║
║ boost increasing energy            ║  ║ 12:21 | On Sol 70, a trading ship… ║
║ production. Temperature remains    ║  ║ 12:17 | On Sol 70, a meteor        ║
║ cold at -57C, with stable resource ║  ║ shower…                            ║
║ levels. Colonies are advised to    ║  ║ 06:44 | Martian day 70 has begun   ║
║ optimize solar infrastructure and  ║  ╚════════════════════════════════════╝
║ maintain water systems to secure   ║                                        
║ resources for the coming…          ║                                        
║ Exploration teams led by Marco     ║                                        
║ Quinn, Zoya Kade, and Irina Vale   ║                                        
║ have located and extracted         ║                                        
║ underground ice, adding a combined ║                                        
║ 108 units of water to colony       ║                                        
║ reserves amid stable conditions.   ║                                        
╚════════════════════════════════════╝                                        
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

Manual live diagnostics are available through the `AI Health Check` workflow.
GitHub Models run in Actions via the built-in `GITHUB_TOKEN`; deterministic
fallback content is used only when live inference is unavailable.
