## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-18T00:31:51.585127_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 53 | [SEASON] Early      ║  ║ Dust Storm Disrupts Solar Panels   ║
║ Spring                             ║  ║ A persistent dust storm reduces    ║
║ [TEMP] -66C | [SUN] 0% | [STORM]   ║  ║ solar energy generation efficiency ║
║ YES                                ║  ║ across Mars colonies.              ║
║ [EVENT] New Subsurface Caverns     ║  ║ EFFECT energy_surge | energy +20   ║
║ Mapped Amid Dust Storm             ║  ╚════════════════════════════════════╝
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║                                        
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║                                        
║ [FOOD] 1400 | [MAT] 550            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Dust Storm Disrupts Solar     ║                                        
║ Panels | energy +20                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Panel Maintenance    ║
║    Dustline Agro | P1 B3 | S5936   ║  ║    Clean and inspect solar panels… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Optimization    ║
║    Ares Systems | P1 B4 | S5315    ║  ║    Upgrade water recycling…        ║
║ 3. Irina Vale                      ║  ║ 3. Emergency Oxygen…               ║
║    Helios… | P1 B2 | S4524         ║  ║    Transfer at least 150 units of… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ ongoing. Prioritize…               ║
║ ENERGY    1140                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      1400                     ║  ║ additional oxygen…                 ║
║ MATERIALS 550                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is currently experiencing a   ║  ║ 12:45 | On Sol 53, despite         ║
║ strong dust storm reducing solar   ║  ║ ongoing…                           ║
║ energy production and complicating ║  ║ 00:32 | On Sol 53, a meteor        ║
║ resource management. Colonies are  ║  ║ shower…                            ║
║ focusing on maintaining solar      ║  ║ 00:34 | On Sol 53, a trading       ║
║ arrays, optimizing water           ║  ║ vessel…                            ║
║ recycling, and balancing oxygen    ║  ║ 12:48 | A severe sandstorm is…     ║
║ supplies to sustain life during    ║  ║ 00:33 | A severe dust storm is…    ║
║ these harsh conditions.            ║  ╚════════════════════════════════════╝
║ On Sol 53, despite ongoing dust    ║                                        
║ storm conditions and -66°C         ║                                        
║ temperatures, rover sensors have   ║                                        
║ confirmed the presence of          ║                                        
║ underground caverns, offering      ║                                        
║ potential new sites for habitat    ║                                        
║ expansion.                         ║                                        
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
