## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-05T00:27:57.185943_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 42 | [SEASON] Early      ║  ║ Solar Activity Peaks               ║
║ Spring                             ║  ║ Solar activity has reached 95%,    ║
║ [TEMP] -69C | [SUN] 100% | [STORM] ║  ║ providing increased energy input   ║
║ NO                                 ║  ║ across the colony's solar arrays.  ║
║ [EVENT] Meteor Shower Strikes      ║  ║ EFFECT solar_boost |               ║
║ Colony Infrastructure              ║  ║ solar_activity +5                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║                                        
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks |        ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Upgrade Solar Panels            ║
║    Dustline Agro | P1 B3 | S4243   ║  ║    Install enhanced solar capture… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S3974    ║  ║    Inspect and repair any leaks…   ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3226         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is peaking today;…        ║
║ ENERGY    1100                     ║  ║ Helios… -> Irina Vale | Keep       ║
║ FOOD      1100                     ║  ║ monitoring oxygen levels…          ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 42 of early spring, Mars    ║  ║ 00:27 | AI directive: Solar…       ║
║ colonies experience a solar energy ║  ║ 12:31 | On Sol 42, a meteor        ║
║ surge boosting power availability. ║  ║ shower…                            ║
║ Water supplies remain stable but   ║  ║ 06:59 | Martian day 42 has begun   ║
║ require maintenance to prevent     ║  ║ 00:27 | AI directive: Solar…       ║
║ loss. Colonies are advised to      ║  ║ 00:26 | A powerful solar flare     ║
║ optimize energy infrastructure and ║  ║ has…                               ║
║ maintain critical life support     ║  ╚════════════════════════════════════╝
║ systems to ensure…                 ║                                        
║ On Sol 42, a meteor shower caused  ║                                        
║ minor building damage reported by  ║                                        
║ Irina Vale. Salvage operations by  ║                                        
║ Marco Quinn and Zoya Kade          ║                                        
║ recovered 21 materials total.      ║                                        
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
