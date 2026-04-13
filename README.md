## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-13T00:21:11.986297_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 20 | [SEASON] Early      ║  ║ Early Spring Solar Boost           ║
║ Spring                             ║  ║ Solar activity is at 74%,          ║
║ [TEMP] -63C | [SUN] 79% | [STORM]  ║  ║ providing a moderate boost to      ║
║ NO                                 ║  ║ energy generation across all       ║
║ [EVENT] Earth Trading Vessel       ║  ║ colonies.                          ║
║ Arrives at Mars Base               ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 500 | [MAT] 100             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Early Spring Solar Boost |    ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panels           ║
║    Dustline Agro | P1 B3 | S2518   ║  ║    Calibrate solar arrays to…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Check           ║
║    Ares Systems | P1 B4 | S2300    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory and…         ║
║    Helios… | P1 B2 | S1688         ║  ║    Complete materials audit and…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity increased;…               ║
║ ENERGY    1040                     ║  ║ Helios… -> Irina Vale | Report any ║
║ FOOD      500                      ║  ║ anomalies in water…                ║
║ MATERIALS 100                      ║  ║ Dustline Agro -> Marco… | Crop     ║
╚════════════════════════════════════╝  ║ growth expected to improve;…       ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 20 brings a moderate solar     ║  ║ 00:21 | AI directive: Early        ║
║ boost enhancing energy production  ║  ║ Spring…                            ║
║ across Mars colonies. Water and    ║  ║ 12:10 | A trading ship from Earth… ║
║ materials remain critical          ║  ║ 06:31 | Martian day 20 has begun   ║
║ priorities with ongoing efforts to ║  ║ 00:20 | AI directive: Unexpected…  ║
║ optimize recycling and resource    ║  ║ 12:08 | Solar activity spiked to…  ║
║ allocation. Colonists prepare for  ║  ╚════════════════════════════════════╝
║ improved agricultural yields as    ║                                        
║ early spring progresses.           ║                                        
║ A trading ship from Earth has      ║                                        
║ docked, delivering 100 units of    ║                                        
║ food and 50 units of materials to  ║                                        
║ the colony's global reserves.      ║                                        
║ Operations proceed smoothly under  ║                                        
║ stable conditions on Sol 20.       ║                                        
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
