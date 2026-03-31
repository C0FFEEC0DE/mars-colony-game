## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-03-30T12:45:35.810976_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 7 | [SEASON] Early       ║  ║ Solar Activity Boosts Power        ║
║ Spring                             ║  ║ Systems                            ║
║ [TEMP] -31C | [SUN] 89% | [STORM]  ║  ║ Solar activity has increased to    ║
║ NO                                 ║  ║ 84%, providing a temporary surge   ║
║ [EVENT] Unexpected Microbial Life  ║  ║ in energy generation across all    ║
║ Detected in Soil                   ║  ║ colonies.                          ║
║ [POP] 14 | [BLD] 9 | [PLY] 3       ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1000   ║  ║ solar_activity +5                  ║
║ [FOOD] 300 | [MAT] 0               ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Power   ║                                        
║ Systems | solar_activity +5        ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Expand Water Extraction         ║
║    Ares Systems | P5 B4 | S1286    ║  ║    Deploy and activate additional… ║
║ 2. Irina Vale                      ║  ║ 2. Optimize Energy Storage         ║
║    Helios… | P6 B2 | S1165         ║  ║    Install enhanced battery…       ║
║ 3. Marco Quinn                     ║  ║ 3. Food Supply Recon               ║
║    Dustline Agro | P3 B3 | S1100   ║  ║    Survey and report viable…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity elevated; optimize…       ║
║ ENERGY    1000                     ║  ║ Helios… -> Mars… | Request         ║
║ FOOD      300                      ║  ║ assistance for additional…         ║
║ MATERIALS 0                        ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 7 of early spring, Mars     ║  ║ 00:18 | On Sol 7, analysis         ║
║ experiences a significant solar    ║  ║ revealed…                          ║
║ activity boost enhancing energy    ║  ║ 12:45 | AI directive: Solar…       ║
║ production. Colonies are advised   ║  ║ 12:45 | Martian day 7 has begun    ║
║ to optimize resource extraction    ║  ║ 12:39 | AI directive: Operations…  ║
║ and storage to maximize benefits.  ║  ║ 12:39 | Martian day 6 has begun    ║
║ Conditions remain stable with no   ║  ╚════════════════════════════════════╝
║ dust storms reported.              ║                                        
║ On Sol 7, analysis revealed        ║                                        
║ unknown bacteria in the Martian    ║                                        
║ soil sample. This discovery may    ║                                        
║ provide new insights into Mars'    ║                                        
║ past habitability.                 ║                                        
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
