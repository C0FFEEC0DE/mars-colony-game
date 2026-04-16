## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-16T00:24:41.109681_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 23 | [SEASON] Early      ║  ║ Mild Solar Activity Increase       ║
║ Spring                             ║  ║ Solar activity has risen to 64%,   ║
║ [TEMP] -54C | [SUN] 69% | [STORM]  ║  ║ providing a modest boost to solar  ║
║ NO                                 ║  ║ power generation across the        ║
║ [EVENT] Meteor Shower Boosts       ║  ║ colonies.                          ║
║ Resource Salvage                   ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 600 | [MAT] 150             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Activity Increase  ║                                        
║ | solar_activity +5                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S2701   ║  ║    Adjust and optimize solar…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S2460    ║  ║    Perform diagnostics and…        ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1927         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels rising…            ║
║ ENERGY    1040                     ║  ║ Helios… -> Marco… | Sharing recent ║
║ FOOD      600                      ║  ║ findings on…                       ║
║ MATERIALS 150                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 23 of early spring, Mars    ║  ║ 00:24 | AI directive: Mild Solar…  ║
║ colonies experience a mild         ║  ║ 12:18 | On Sol 23, a meteor        ║
║ increase in solar activity         ║  ║ shower…                            ║
║ enhancing power generation. Water  ║  ║ 06:35 | Martian day 23 has begun   ║
║ reserves remain stable, prompting  ║  ║ 00:24 | AI directive: Mild Solar…  ║
║ maintenance missions to sustain    ║  ║ 00:24 | On Sol 22, a meteor        ║
║ supply. Cooperation between Helios ║  ║ shower…                            ║
║ Prospecting and Dustline Agro      ║  ╚════════════════════════════════════╝
║ suggests potential resource…       ║                                        
║ On Sol 23, a meteor shower         ║                                        
║ provided unexpected salvage        ║                                        
║ opportunities. Irina Vale          ║                                        
║ recovered 15 additional materials  ║                                        
║ under stable conditions with -54C  ║                                        
║ temperature and 64% solar          ║                                        
║ activity.                          ║                                        
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
