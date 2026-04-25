## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-25T00:22:04.485093_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 32 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ A moderate solar flare increases   ║
║ [TEMP] -48C | [SUN] 83% | [STORM]  ║  ║ solar panel efficiency by 15%,     ║
║ NO                                 ║  ║ temporarily boosting energy        ║
║ [EVENT] Underground Ice Deposit    ║  ║ generation across all colonies.    ║
║ Confirmed on Sol 32                ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1080   ║  ╚════════════════════════════════════╝
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S3477   ║  ║    Perform system diagnostics and… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S3139    ║  ║    Inspect and repair any leaks…   ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S2546         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ detected. Recommended…             ║
║ ENERGY    1080                     ║  ║ Helios… -> all… | Early spring     ║
║ FOOD      700                      ║  ║ conditions stable.…                ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 32, Mars colonies benefit   ║  ║ 00:22 | AI directive: Solar Flare… ║
║ from a moderate solar flare        ║  ║ 12:19 | Exploration team located   ║
║ increasing energy generation.      ║  ║ a…                                 ║
║ Early spring weather remains       ║  ║ 06:37 | Martian day 32 has begun   ║
║ stable with no dust storms.        ║  ║ 00:25 | AI directive: Solar…       ║
║ Colonies focus on optimizing solar ║  ║ 12:20 | Exploration teams have…    ║
║ arrays and maintaining essential   ║  ╚════════════════════════════════════╝
║ water recycling systems to sustain ║                                        
║ operations.                        ║                                        
║ Exploration team located a viable  ║                                        
║ underground ice source. Irina Vale ║                                        
║ extracted 34 units, Marco Quinn    ║                                        
║ 32, and Zoya Kade 27 units of      ║                                        
║ water for colony reserves.         ║                                        
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
