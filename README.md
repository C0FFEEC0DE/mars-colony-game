## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-09T00:29:16.937257_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 57 | [SEASON] Early      ║  ║ Dust Storm Reduces Solar           ║
║ Spring                             ║  ║ Efficiency                         ║
║ [TEMP] -42C | [SUN] 75% | [STORM]  ║  ║ A persistent dust storm has        ║
║ YES                                ║  ║ lowered solar panel output,        ║
║ [EVENT] None                       ║  ║ reducing energy availability       ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ across all colonies.               ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ║ EFFECT energy_surge | energy +20   ║
║ [FOOD] 2100 | [MAT] 900            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Dust Storm Reduces Solar      ║                                        
║ Efficiency | energy +20            ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Shield…              ║
║    Dustline Agro | P1 B3 | S7358   ║  ║    Use materials to strengthen…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Optimization    ║
║    Ares Systems | P1 B4 | S7004    ║  ║    Adjust and repair water…        ║
║ 3. Irina Vale                      ║  ║ 3. Oxygen Reserve Transfer         ║
║    Helios… | P1 B2 | S5938         ║  ║    Organize and execute oxygen…    ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storms ║
║ WATER     545                      ║  ║ expected to persist…               ║
║ ENERGY    1160                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      2100                     ║  ║ additional materials…              ║
║ MATERIALS 900                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 57 marks a challenging period  ║  ║ 00:29 | AI directive: Dust Storm…  ║
║ for all Mars colonies as an        ║  ║ 06:48 | 🌪️ Dust storm damaged…     ║
║ ongoing dust storm decreases solar ║  ║ 06:48 | Martian day 57 has begun   ║
║ energy production and complicates  ║  ║ 00:31 | Sol 56 report: Rover…      ║
║ resource management. Colonies are  ║  ║ 12:27 | Despite the ongoing dust…  ║
║ focusing on reinforcing            ║  ╚════════════════════════════════════╝
║ infrastructure and optimizing      ║                                        
║ water recycling to mitigate        ║                                        
║ environmental impacts. Coordinat…  ║                                        
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
