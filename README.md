## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-05T00:30:09.673783_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 56 | [SEASON] Early      ║  ║ Severe Dust Storm Suppresses Solar ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -54C | [SUN] 0% | [STORM]   ║  ║ A persistent dust storm is         ║
║ YES                                ║  ║ blocking sunlight, causing a 0%    ║
║ [EVENT] Sol 56: Sandstorm Disrupts ║  ║ solar activity and reducing energy ║
║ Solar Operations                   ║  ║ generation across Mars.            ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT cold_snap | temperature -3  ║
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║  ╚════════════════════════════════════╝
║ [FOOD] 2000 | [MAT] 850            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Severe Dust Storm Suppresses  ║                                        
║ Solar Output | temperature -3      ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Resource…            ║
║    Dustline Agro | P1 B3 | S7377   ║  ║    Coordinate resource transfers…  ║
║ 2. Zoya Kade                       ║  ║ 2. Stormproof Habitat Maintenance  ║
║    Ares Systems | P1 B4 | S7009    ║  ║    Deploy maintenance drones to…   ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S5962         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ ongoing. Prioritize…               ║
║ ENERGY    1140                     ║  ║ Helios… -> Dustline… | Requesting  ║
║ FOOD      2000                     ║  ║ oxygen transfer to…                ║
║ MATERIALS 850                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is experiencing a severe dust ║  ║ 00:30 | AI directive: Severe Dust… ║
║ storm during early spring, causing ║  ║ 00:30 | A massive dust storm is…   ║
║ solar activity to drop to zero and ║  ║ 06:58 | 🌪️ Dust storm damaged…     ║
║ energy shortages across colonies.  ║  ║ 06:58 | Martian day 56 has begun   ║
║ Critical resource sharing and      ║  ║ 12:36 | Despite ongoing dust       ║
║ habitat maintenance missions are   ║  ║ storm…                             ║
║ underway to mitigate the impacts.  ║  ╚════════════════════════════════════╝
║ Leaders Marco Quinn, Zoya Kade,    ║                                        
║ and Irina V…                       ║                                        
║ A massive dust storm is active,    ║                                        
║ forcing all solar panels offline   ║                                        
║ for the next 6 hours. Expect power ║                                        
║ constraints until the storm        ║                                        
║ subsides.                          ║                                        
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
