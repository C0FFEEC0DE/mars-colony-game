## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-20T00:26:29.673937_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 65 | [SEASON] Early      ║  ║ Dust Storm Reduces Solar           ║
║ Spring                             ║  ║ Efficiency                         ║
║ [TEMP] -69C | [SUN] 87% | [STORM]  ║  ║ A persistent dust storm is         ║
║ YES                                ║  ║ limiting solar panel output,       ║
║ [EVENT] Trading Vessel Arrives     ║  ║ reducing energy generation across  ║
║ Amid Dust Storm                    ║  ║ all colonies despite high solar    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ activity.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1180   ║  ║ EFFECT energy_surge | energy +20   ║
║ [FOOD] 2400 | [MAT] 1050           ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Dust Storm Reduces Solar      ║                                        
║ Efficiency | energy +20            ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Dust Storm Panel Maintenance    ║
║    Ares Systems | P1 B4 | S7839    ║  ║    Clear dust from solar panels…   ║
║ 2. Marco Quinn                     ║  ║ 2. Emergency Oxygen Conservation   ║
║    Dustline Agro | P1 B3 | S7791   ║  ║    Implement oxygen-saving…        ║
║ 3. Irina Vale                      ║  ║ 3. Water Recycling Optimization    ║
║    Helios… | P1 B2 | S6485         ║  ║    Optimize water recycling…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ ongoing, expect…                   ║
║ ENERGY    1180                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      2400                     ║  ║ assistance in sharing…             ║
║ MATERIALS 1050                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 65 on Mars continues under a   ║  ║ 12:41 | On Sol 65, a trading ship… ║
║ challenging early spring dust      ║  ║ 00:26 | AI directive: Dust Storm…  ║
║ storm, significantly impacting     ║  ║ 06:49 | 🌪️ Dust storm damaged…     ║
║ solar energy production. Colonies  ║  ║ 06:49 | Martian day 65 has begun   ║
║ are focusing on maintenance and    ║  ║ 00:24 | AI directive: Seasonal…    ║
║ conservation efforts to maintain   ║  ╚════════════════════════════════════╝
║ vital systems. Collaboration       ║                                        
║ between colonies is encouraged to  ║                                        
║ optimize resource manag…           ║                                        
║ On Sol 65, a trading ship from     ║                                        
║ Earth has docked despite an active ║                                        
║ dust storm. Supplies boosted: Food ║                                        
║ +100, Materials +50 to global      ║                                        
║ reserves.                          ║                                        
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
