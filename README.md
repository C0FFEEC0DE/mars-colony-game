## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-04T00:17:29.593831_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 11 | [SEASON] Early      ║  ║ Solar Flare Boosts Power Systems   ║
║ Spring                             ║  ║ A moderate solar flare has         ║
║ [TEMP] -50C | [SUN] 88% | [STORM]  ║  ║ increased solar panel efficiency,  ║
║ NO                                 ║  ║ providing a temporary energy surge ║
║ [EVENT] Underground Ice Deposits   ║  ║ across Mars colonies.              ║
║ Confirmed on Sol 11                ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1020   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Power      ║                                        
║ Systems | solar_activity +5        ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S1709   ║  ║    Recalibrate solar panels to…    ║
║ 2. Zoya Kade                       ║  ║ 2. Secure Water Reserves           ║
║    Ares Systems | P1 B4 | S1556    ║  ║    Inspect and reinforce water…    ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1147         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ detected. Take…                    ║
║ ENERGY    1020                     ║  ║ Helios… -> Irina Vale | Resource   ║
║ FOOD      400                      ║  ║ analysis shows stable…             ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 11 during early spring,     ║  ║ 00:17 | AI directive: Solar Flare… ║
║ Mars colonies experience a solar   ║  ║ 00:17 | Excavation teams led by…   ║
║ flare increasing solar energy      ║  ║ 12:11 | Underground ice was…       ║
║ output by 83%, providing a         ║  ║ 06:24 | Martian day 11 has begun   ║
║ temporary energy boost.            ║  ║ 00:19 | AI directive: Solar Flare… ║
║ Temperatures remain cold at -50C   ║  ╚════════════════════════════════════╝
║ but stable, and no dust storms are ║                                        
║ present. Colonies are advised to   ║                                        
║ optimize solar arrays and secure…  ║                                        
║ Excavation teams led by Irina,     ║                                        
║ Marco, and Zoya have successfully  ║                                        
║ extracted significant underground  ║                                        
║ ice, boosting water reserves by    ║                                        
║ 114 units total.                   ║                                        
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
