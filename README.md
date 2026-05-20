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
║ [EVENT] Sol 53: Massive Sandstorm  ║  ║ EFFECT energy_surge | energy +20   ║
║ Disables Solar Arrays              ║  ╚════════════════════════════════════╝
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║                                        
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║                                        
║ [FOOD] 1300 | [MAT] 500            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Dust Storm Disrupts Solar     ║                                        
║ Panels | energy +20                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Panel Maintenance    ║
║    Dustline Agro | P1 B3 | S5907   ║  ║    Clean and inspect solar panels… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Optimization    ║
║    Ares Systems | P1 B4 | S5254    ║  ║    Upgrade water recycling…        ║
║ 3. Irina Vale                      ║  ║ 3. Emergency Oxygen…               ║
║    Helios… | P1 B2 | S4454         ║  ║    Transfer at least 150 units of… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ ongoing. Prioritize…               ║
║ ENERGY    1140                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      1300                     ║  ║ additional oxygen…                 ║
║ MATERIALS 500                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars is currently experiencing a   ║  ║ 00:33 | A severe dust storm is…    ║
║ strong dust storm reducing solar   ║  ║ 00:31 | AI directive: Dust Storm…  ║
║ energy production and complicating ║  ║ 12:18 | On Sol 53, despite active… ║
║ resource management. Colonies are  ║  ║ 06:55 | 🌪️ Dust storm damaged…     ║
║ focusing on maintaining solar      ║  ║ 06:55 | Martian day 53 has begun   ║
║ arrays, optimizing water           ║  ╚════════════════════════════════════╝
║ recycling, and balancing oxygen    ║                                        
║ supplies to sustain life during    ║                                        
║ these harsh conditions.            ║                                        
║ A severe dust storm is currently   ║                                        
║ active, causing all solar panels   ║                                        
║ to be offline for the next 6       ║                                        
║ hours. Expect reduced power        ║                                        
║ availability until conditions      ║                                        
║ improve.                           ║                                        
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
