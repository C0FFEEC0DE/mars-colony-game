## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-13T00:31:49.753495_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 49 | [SEASON] Early      ║  ║ Solar Activity Peaks               ║
║ Spring                             ║  ║ A surge in solar activity has      ║
║ [TEMP] -48C | [SUN] 100% | [STORM] ║  ║ increased energy availability      ║
║ NO                                 ║  ║ across Mars, improving solar panel ║
║ [EVENT] Subsurface Ice Deposit     ║  ║ efficiency.                        ║
║ Uncovered on Sol 49                ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ╚════════════════════════════════════╝
║ [FOOD] 1200 | [MAT] 450            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks |        ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S5325   ║  ║    Perform maintenance on solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Secure Water Cache              ║
║    Ares Systems | P1 B4 | S4898    ║  ║    Collect and store 50 units of…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S4074         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity has peaked.…              ║
║ ENERGY    1120                     ║  ║ Helios… -> Marco… | Identified     ║
║ FOOD      1200                     ║  ║ water pockets nearby.…             ║
║ MATERIALS 450                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 49 of early spring, Mars    ║  ║ 00:31 | AI directive: Solar…       ║
║ experiences a solar activity peak  ║  ║ 00:31 | Exploration teams Irina…   ║
║ enhancing energy production.       ║  ║ 12:37 | Teams report the           ║
║ Colonies are advised to perform    ║  ║ discovery…                         ║
║ solar array maintenance to take    ║  ║ 06:55 | Martian day 49 has begun   ║
║ advantage of the energy surge.     ║  ║ 00:28 | Teams have confirmed a     ║
║ Additionally, water collection     ║  ║ new…                               ║
║ missions near ice deposits present ║  ╚════════════════════════════════════╝
║ an opportunity to bolst…           ║                                        
║ Exploration teams Irina Vale,      ║                                        
║ Marco Quinn, and Zoya Kade         ║                                        
║ successfully extracted a total of  ║                                        
║ 120 liters of underground water    ║                                        
║ ice today, bolstering colony       ║                                        
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
