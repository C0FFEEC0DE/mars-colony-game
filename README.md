## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-09T00:16:26.524042_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 16 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -46C | [SUN] 95% | [STORM]  ║  ║ Solar activity has surged to 90%,  ║
║ NO                                 ║  ║ enhancing energy capture           ║
║ [EVENT] Underground Ice Deposit    ║  ║ efficiency across colonies.        ║
║ Located on Sol 16                  ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panels           ║
║    Dustline Agro | P1 B3 | S2158   ║  ║    Calibrate all solar panels to…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Drill        ║
║    Ares Systems | P1 B4 | S1964    ║  ║    Reduce water usage colony-wide… ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory Assessment   ║
║    Helios… | P1 B2 | S1400         ║  ║    Complete a materials audit and… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels are…               ║
║ ENERGY    1040                     ║  ║ Helios… -> Mars… | Request         ║
║ FOOD      400                      ║  ║ guidance on improving…             ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ The Mars colonies benefit from a   ║  ║ 00:16 | AI directive: Solar…       ║
║ surge in solar activity boosting   ║  ║ 00:16 | Teams led by Irina Vale,…  ║
║ energy efficiency. Water           ║  ║ 06:30 | Martian day 16 has begun   ║
║ conservation remains critical due  ║  ║ 00:20 | AI directive: Dust Storm…  ║
║ to limited reserves, while         ║  ║ 06:29 | 🌪️ Dust storm damaged…     ║
║ materials supplies require careful ║  ╚════════════════════════════════════╝
║ management. Colonies are advised   ║                                        
║ to optimize resource use to        ║                                        
║ maintain stability during the e…   ║                                        
║ Teams led by Irina Vale, Marco     ║                                        
║ Quinn, and Zoya Kade have          ║                                        
║ extracted a combined total of 102  ║                                        
║ units of water from subsurface ice ║                                        
║ deposits, bolstering colony        ║                                        
║ reserves.                          ║                                        
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
