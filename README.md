## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-09T00:29:08.501314_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 46 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -41C | [SUN] 103% | [STORM] ║  ║ High solar activity today          ║
║ NO                                 ║  ║ increases solar panel efficiency,  ║
║ [EVENT] None                       ║  ║ providing a temporary boost in     ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ energy generation across all       ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ║ colonies.                          ║
║ [FOOD] 1100 | [MAT] 400            ║  ║ EFFECT solar_boost |               ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ║ solar_activity +5                  ║
║ [AI] Solar Activity Boosts Energy  ║  ╚════════════════════════════════════╝
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panels           ║
║    Dustline Agro | P1 B3 | S4658   ║  ║    Increase colony energy…         ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S4319    ║  ║    Implement water recycling…      ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3491         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels are at 98%,…       ║
║ ENERGY    1120                     ║  ║ Helios… -> Irina Vale | Increased  ║
║ FOOD      1100                     ║  ║ solar flux today;…                 ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is experiencing early spring  ║  ║ 00:29 | AI directive: Solar…       ║
║ with temperatures averaging -41C   ║  ║ 06:34 | Martian day 46 has begun   ║
║ and high solar activity at 98%. No ║  ║ 00:27 | AI directive: Solar        ║
║ dust storms are reported, allowing ║  ║ Output…                            ║
║ colonies to optimize solar energy  ║  ║ 00:27 | A significant solar flare… ║
║ production. Water conservation     ║  ║ 12:35 | Geological survey reports… ║
║ remains critical as melting ice    ║  ╚════════════════════════════════════╝
║ begins to augment water            ║                                        
║ availability.                      ║                                        
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
