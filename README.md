## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-29T00:23:38.509621_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 71 | [SEASON] Early      ║  ║ Mild Solar Boost Increases Energy  ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -50C | [SUN] 94% | [STORM]  ║  ║ Solar activity is at 89%,          ║
║ NO                                 ║  ║ providing a modest increase in     ║
║ [EVENT] Unidentified Signal        ║  ║ solar panel efficiency across      ║
║ Detected on 1420 MHz               ║  ║ colonies.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1200   ║  ║ solar_activity +5                  ║
║ [FOOD] 2600 | [MAT] 1150           ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Boost Increases    ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S9142   ║  ║    Adjust and recalibrate solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S8999    ║  ║    Reduce daily water consumption… ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S7382         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity remains high;…            ║
║ ENERGY    1200                     ║  ║ Helios… -> Irina Vale | Request    ║
║ FOOD      2600                     ║  ║ status update on resource…         ║
║ MATERIALS 1150                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 71 of early spring, Mars    ║  ║ 00:23 | AI directive: Mild Solar…  ║
║ colonies experience a mild solar   ║  ║ 12:34 | Mission control confirms…  ║
║ boost increasing energy            ║  ║ 06:50 | Martian day 71 has begun   ║
║ efficiency. Water resources remain ║  ║ 00:24 | On Sol 70, a meteor        ║
║ stable but require conservation    ║  ║ shower…                            ║
║ efforts. Colonies prepare to       ║  ║ 00:27 | AI directive: Mild Solar…  ║
║ optimize energy systems and        ║  ╚════════════════════════════════════╝
║ preserve vital resources amid cold ║                                        
║ temperatures averaging -50C.       ║                                        
║ Mission control confirms reception ║                                        
║ of a strange signal at 1420 MHz.   ║                                        
║ Analysis underway to determine     ║                                        
║ source and significance.           ║                                        
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
