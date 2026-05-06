## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-06T00:27:34.094397_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 43 | [SEASON] Early      ║  ║ Moderate Solar Activity Boost      ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -35C | [SUN] 64% | [STORM]  ║  ║ 64%, providing a modest energy     ║
║ NO                                 ║  ║ surge across the colony            ║
║ [EVENT] None                       ║  ║ installations.                     ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT energy_surge | energy +20   ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ╚════════════════════════════════════╝
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Moderate Solar Activity Boost ║                                        
║ | energy +20                       ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S4287   ║  ║    Calibrate solar panels to…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S4042    ║  ║    Implement water recycling…      ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3282         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity rising; recommend…        ║
║ ENERGY    1120                     ║  ║ Helios… -> Marco… | Request        ║
║ FOOD      1100                     ║  ║ collaboration on mineral…          ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 43, Mars experiences a      ║  ║ 00:27 | AI directive: Moderate…    ║
║ moderate solar activity boost,     ║  ║ 06:43 | Martian day 43 has begun   ║
║ enhancing energy generation        ║  ║ 00:27 | AI directive: Solar…       ║
║ capabilities across colonies.      ║  ║ 12:31 | On Sol 42, a meteor        ║
║ Temperatures remain low at -35C in ║  ║ shower…                            ║
║ early spring, with no dust storms  ║  ║ 06:59 | Martian day 42 has begun   ║
║ reported. Colonies are focusing on ║  ╚════════════════════════════════════╝
║ optimizing energy use and          ║                                        
║ conserving water to maintain s…    ║                                        
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
