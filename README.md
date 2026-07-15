## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-15T00:21:17.778148_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 60 | [SEASON] Early      ║  ║ Early Spring Solar Boost           ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -49C | [SUN] 82% | [STORM]  ║  ║ 77%, providing a mild boost to     ║
║ NO                                 ║  ║ energy generation across all       ║
║ [EVENT] None                       ║  ║ colonies.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ║ solar_activity +5                  ║
║ [FOOD] 2200 | [MAT] 950            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Early Spring Solar Boost |    ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Solar Panel Maintenance         ║
║    Dustline Agro | P1 B3 | S7463   ║  ║    Inspect and clean solar panels… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S7428    ║  ║    Perform diagnostics and…        ║
║ 3. Irina Vale                      ║  ║ 3. Early Spring Crop Assessment    ║
║    Helios… | P1 B2 | S6145         ║  ║    Evaluate and report on current… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity stable at 77%.…           ║
║ ENERGY    1160                     ║  ║ Helios… -> all… | Sharing data on  ║
║ FOOD      2200                     ║  ║ water recycling…                   ║
║ MATERIALS 950                      ║  ║ Ares Systems -> Mars… | Requesting ║
╚════════════════════════════════════╝  ║ technical support for…             ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars enters early spring on Sol 60 ║  ║ 00:21 | AI directive: Early        ║
║ with temperatures holding steady   ║  ║ Spring…                            ║
║ at -49C and solar activity at 77%, ║  ║ 06:42 | Martian day 60 has begun   ║
║ boosting energy availability.      ║  ║ 12:47 | A severe sandstorm is…     ║
║ Colonies focus on maintenance      ║  ║ 00:25 | AI directive: Unexpected…  ║
║ tasks to optimize water recycling  ║  ║ 00:25 | A trading ship from Earth… ║
║ and solar energy capture.          ║  ╚════════════════════════════════════╝
║ Collaboration among factions is    ║                                        
║ increasing to overcome s…          ║                                        
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
