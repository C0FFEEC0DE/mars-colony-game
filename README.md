## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-17T00:25:53.836741_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 62 | [SEASON] Early      ║  ║ Unexpected Solar Boost             ║
║ Spring                             ║  ║ Solar activity surges to 80%,      ║
║ [TEMP] -33C | [SUN] 85% | [STORM]  ║  ║ providing a temporary increase in  ║
║ NO                                 ║  ║ solar energy input across Mars.    ║
║ [EVENT] Underground Ice Deposit    ║  ║ EFFECT solar_boost |               ║
║ Located Near Colony                ║  ║ solar_activity +5                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║                                        
║ [FOOD] 2200 | [MAT] 950            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Unexpected Solar Boost |      ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7661   ║  ║    Adjust panel angles and clear…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S7648    ║  ║    Implement water recycling…      ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6349         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity has increased;…           ║
║ ENERGY    1160                     ║  ║ Helios… -> all… | Sharing water    ║
║ FOOD      2200                     ║  ║ conservation…                      ║
║ MATERIALS 950                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 62 of early spring, Mars    ║  ║ 00:25 | AI directive: Unexpected…  ║
║ experiences a notable solar        ║  ║ 12:30 | On Sol 62, team members…   ║
║ activity surge, enhancing energy   ║  ║ 06:46 | Martian day 62 has begun   ║
║ availability. Colonies are advised ║  ║ 00:24 | AI directive: Enhanced…    ║
║ to optimize solar infrastructure   ║  ║ 00:24 | A massive solar flare has… ║
║ and conserve water amid low        ║  ╚════════════════════════════════════╝
║ temperatures. Cooperation in       ║                                        
║ resource management remains vital  ║                                        
║ for survival in the harsh M…       ║                                        
║ On Sol 62, team members Zoya Kade, ║                                        
║ Irina Vale, and Marco Quinn        ║                                        
║ successfully extracted underground ║                                        
║ ice, adding a combined total of 87 ║                                        
║ units of water to the colony       ║                                        
║ reserves amid stable conditions.   ║                                        
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
