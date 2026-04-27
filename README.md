## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-27T00:24:08.013780_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 34 | [SEASON] Early      ║  ║ Solar Activity Boosts Power Output ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -78C | [SUN] 72% | [STORM]  ║  ║ 67%, providing a modest boost in   ║
║ NO                                 ║  ║ energy generation across all       ║
║ [EVENT] Trading Ship Arrives with  ║  ║ colonies.                          ║
║ Vital Supplies                     ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1080   ║  ╚════════════════════════════════════╝
║ [FOOD] 800 | [MAT] 250             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Power   ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Alignment  ║
║    Dustline Agro | P1 B3 | S3645   ║  ║    Calibrate and realign solar…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Pipe Inspection           ║
║    Ares Systems | P1 B4 | S3275    ║  ║    Inspect and repair any leaks…   ║
║ 3. Irina Vale                      ║  ║ 3. Prospect for Construction…      ║
║    Helios… | P1 B2 | S2658         ║  ║    Survey local terrain and…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently…             ║
║ ENERGY    1080                     ║  ║ Helios… -> Marco… | Offering       ║
║ FOOD      800                      ║  ║ trade: surplus materials…          ║
║ MATERIALS 250                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is experiencing early spring  ║  ║ 00:24 | AI directive: Solar…       ║
║ conditions with temperatures       ║  ║ 00:24 | A trading vessel from      ║
║ averaging -78C. Solar activity has ║  ║ Earth…                             ║
║ increased, benefiting energy       ║  ║ 06:36 | Martian day 34 has begun   ║
║ production across all colonies.    ║  ║ 00:23 | AI directive: Moderate…    ║
║ Resource management remains        ║  ║ 06:29 | Martian day 33 has begun   ║
║ critical as colonies prepare for   ║  ╚════════════════════════════════════╝
║ the seasonal transition.           ║                                        
║ A trading vessel from Earth has    ║                                        
║ docked, delivering 100 units of    ║                                        
║ food and 50 units of materials to  ║                                        
║ the colony's global reserves. This ║                                        
║ influx bolsters our resource pool  ║                                        
║ as Mars Sol 34 progresses under    ║                                        
║ stable conditions.                 ║                                        
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
