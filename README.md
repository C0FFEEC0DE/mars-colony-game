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
║ [EVENT] None                       ║  ║ in energy generation across all    ║
║ [POP] 18 | [BLD] 9 | [PLY] 3       ║  ║ colonies.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1000   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 300 | [MAT] 0               ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Solar Activity Boosts Power   ║                                        
║ Systems | solar_activity +5        ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Expand Water Extraction         ║
║    Dustline Agro | P7 B3 | S1476   ║  ║    Deploy and activate additional… ║
║ 2. Zoya Kade                       ║  ║ 2. Optimize Energy Storage         ║
║    Ares Systems | P5 B4 | S1300    ║  ║    Install enhanced battery…       ║
║ 3. Irina Vale                      ║  ║ 3. Food Supply Recon               ║
║    Helios… | P6 B2 | S1203         ║  ║    Survey and report viable…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity elevated; optimize…       ║
║ ENERGY    1000                     ║  ║ Helios… -> Mars… | Request         ║
║ FOOD      300                      ║  ║ assistance for additional…         ║
║ MATERIALS 0                        ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 7 of early spring, Mars     ║  ║ 12:45 | AI directive: Solar…       ║
║ experiences a significant solar    ║  ║ 12:45 | Martian day 7 has begun    ║
║ activity boost enhancing energy    ║  ║ 12:39 | AI directive: Operations…  ║
║ production. Colonies are advised   ║  ║ 12:39 | Martian day 6 has begun    ║
║ to optimize resource extraction    ║  ║ 12:39 | Science crews are locking… ║
║ and storage to maximize benefits.  ║  ╚════════════════════════════════════╝
║ Conditions remain stable with no   ║                                        
║ dust storms reported.              ║                                        
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
