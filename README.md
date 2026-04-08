## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-08T00:20:10.568475_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 15 | [SEASON] Early      ║  ║ Dust Storm Disrupts Solar Arrays   ║
║ Spring                             ║  ║ The ongoing dust storm reduces     ║
║ [TEMP] -57C | [SUN] 79% | [STORM]  ║  ║ solar panel efficiency, impacting  ║
║ YES                                ║  ║ energy generation across all       ║
║ [EVENT] None                       ║  ║ colonies.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT energy_surge | energy +20   ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Dust Storm Disrupts Solar     ║                                        
║ Arrays | energy +20                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Removal from Solar Panels  ║
║    Dustline Agro | P1 B3 | S2056   ║  ║    Deploy rover or crew to clear…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S1822    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Emergency Oxygen Supply…        ║
║    Helios… | P1 B2 | S1278         ║  ║    Test and calibrate oxygen…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ alert: prioritize…                 ║
║ ENERGY    1040                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      400                      ║  ║ additional filters and…            ║
║ MATERIALS 50                       ║  ║ Dustline Agro -> Mars… | Energy    ║
╚════════════════════════════════════╝  ║ reserves critically low;…          ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 15 features a persistent dust  ║  ║ 00:20 | AI directive: Dust Storm…  ║
║ storm disrupting solar power       ║  ║ 06:29 | 🌪️ Dust storm damaged…     ║
║ generation and threatening         ║  ║ 06:29 | Martian day 15 has begun   ║
║ resource stability. Colonies focus ║  ║ 00:19 | AI directive: Early        ║
║ on critical maintenance missions   ║  ║ Spring…                            ║
║ to secure energy, water, and       ║  ║ 12:15 | On Sol 14, a meteor        ║
║ oxygen supplies. Communication     ║  ║ shower…                            ║
║ remains active to coordinate       ║  ╚════════════════════════════════════╝
║ responses and minimize impact on…  ║                                        
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
