## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-02T00:17:05.132851_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 9 | [SEASON] Early       ║  ║ Solar Activity Surge Powers Up     ║
║ Spring                             ║  ║ Systems                            ║
║ [TEMP] -55C | [SUN] 150% | [STORM] ║  ║ Solar activity has peaked at 150%, ║
║ NO                                 ║  ║ boosting energy generation across  ║
║ [EVENT] Underground Ice Deposit    ║  ║ the colony. Systems relying on     ║
║ Found on Sol 9                     ║  ║ solar panels are operating at      ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ enhanced capacity today.           ║
║ [O2] 1000 | [H2O] 545 | [E] 1000   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 400 | [MAT] 50              ║  ║ solar_activity +0                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Solar Activity Surge Powers   ║                                        
║ Up Systems | solar_activity +0     ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Array Alignment  ║
║    Dustline Agro | P1 B3 | S1189   ║  ║    Recalibrate solar arrays to…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S1121    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Prospect for Local Materials    ║
║    Helios… | P1 B2 | S835          ║  ║    Collect at least 10 units of…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity has increased,…           ║
║ ENERGY    1000                     ║  ║ Helios… -> Irina Vale | Report     ║
║ FOOD      400                      ║  ║ from field teams indicate…         ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 9 of Early Spring, Mars     ║  ║ 00:17 | AI directive: Solar…       ║
║ experiences a solar activity surge ║  ║ 00:16 | Team members Irina Vale,…  ║
║ enhancing energy generation.       ║  ║ 12:16 | A powerful solar flare is… ║
║ Colonies are encouraged to         ║  ║ 06:33 | Martian day 9 has begun    ║
║ optimize their solar arrays to     ║  ║ 00:20 | AI directive: Solar…       ║
║ capitalize on this boost. Water    ║  ╚════════════════════════════════════╝
║ systems require routine            ║                                        
║ maintenance while conditions       ║                                        
║ permit safe material prospecting   ║                                        
║ near set…                          ║                                        
║ Team members Irina Vale, Marco     ║                                        
║ Quinn, and Zoya Kade have secured  ║                                        
║ vital water reserves, gaining 42,  ║                                        
║ 20, and 47 units respectively,     ║                                        
║ boosting colony sustainability.    ║                                        
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
