## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-05T00:18:39.728217_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 12 | [SEASON] Early      ║  ║ Persistent Dust Storm Limits Solar ║
║ Spring                             ║  ║ Power                              ║
║ [TEMP] -40C | [SUN] 0% | [STORM]   ║  ║ A strong dust storm continues to   ║
║ YES                                ║  ║ blanket the colony regions,        ║
║ [EVENT] Massive Sandstorm Shuts    ║  ║ severely reducing solar energy     ║
║ Down Solar Arrays                  ║  ║ generation and visibility.         ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT cold_snap | temperature -3  ║
║ [O2] 1000 | [H2O] 545 | [E] 1020   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Limits  ║                                        
║ Solar Power | temperature -3       ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Reinforce Solar Panel Shields   ║
║    Dustline Agro | P1 B3 | S1830   ║  ║    Deploy protective shields on…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Optimization    ║
║    Ares Systems | P1 B4 | S1621    ║  ║    Upgrade water filtration and…   ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1200         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ forecast extended for…             ║
║ ENERGY    1020                     ║  ║ Helios… -> Marco… | Offer to share ║
║ FOOD      400                      ║  ║ materials for…                     ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 12 sees a persistent dust      ║  ║ 00:18 | AI directive: Persistent…  ║
║ storm severely limiting solar      ║  ║ 00:18 | A severe dust storm on     ║
║ energy production and visibility   ║  ║ Sol…                               ║
║ across Mars colonies. Water        ║  ║ 06:20 | Martian day 12 has begun   ║
║ recycling and solar panel          ║  ║ 00:17 | AI directive: Solar Flare… ║
║ maintenance missions are           ║  ║ 00:17 | Excavation teams led by…   ║
║ prioritized to mitigate resource   ║  ╚════════════════════════════════════╝
║ strain. Mars Control urges all     ║                                        
║ settlements to conserve energy and ║                                        
║ minimize…                          ║                                        
║ A severe dust storm on Sol 12 has  ║                                        
║ forced all solar panels offline    ║                                        
║ for the next 6 hours. Power        ║                                        
║ conservation protocols are now in  ║                                        
║ effect.                            ║                                        
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
