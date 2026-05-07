## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-07T00:27:46.925622_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 44 | [SEASON] Early      ║  ║ Persistent Dust Storm Reduces      ║
║ Spring                             ║  ║ Solar Efficiency                   ║
║ [TEMP] -49C | [SUN] 0% | [STORM]   ║  ║ A continuing dust storm is         ║
║ YES                                ║  ║ limiting solar energy generation,  ║
║ [EVENT] Underground Ice Deposit    ║  ║ impacting colony power reserves.   ║
║ Found Amid Dust Storm              ║  ║ EFFECT cold_snap | temperature -3  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║                                        
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Reduces ║                                        
║ Solar Efficiency | temperature -3  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Repair Solar Panel Arrays       ║
║    Dustline Agro | P1 B3 | S4399   ║  ║    Clear dust and repair 3 solar…  ║
║ 2. Zoya Kade                       ║  ║ 2. Emergency Oxygen Recycling…     ║
║    Ares Systems | P1 B4 | S4172    ║  ║    Upgrade oxygen recycling unit…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3368         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ is forecasted to…                  ║
║ ENERGY    1120                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      1100                     ║  ║ additional oxygen…                 ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is enduring a persistent dust ║  ║ 00:27 | AI directive: Persistent…  ║
║ storm during early spring on Sol   ║  ║ 00:27 | Sol 44: Despite active     ║
║ 44, significantly reducing solar   ║  ║ dust…                              ║
║ power generation. Colonies are     ║  ║ 12:34 | A severe sandstorm is…     ║
║ adapting by conducting urgent      ║  ║ 06:52 | Martian day 44 has begun   ║
║ repairs and optimizing life        ║  ║ 00:27 | AI directive: Moderate…    ║
║ support systems to maintain        ║  ╚════════════════════════════════════╝
║ essential supplies. Mars Control   ║                                        
║ has issued warnings to conse…      ║                                        
║ Sol 44: Despite active dust        ║                                        
║ storms, the crew located           ║                                        
║ significant underground ice. Irina ║                                        
║ Vale, Marco Quinn, and Zoya Kade   ║                                        
║ secured a combined 128 units of    ║                                        
║ water to support ongoing           ║                                        
║ operations.                        ║                                        
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
