## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-18T00:20:39.151182_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 25 | [SEASON] Early      ║  ║ Persistent Dust Storm Hampers      ║
║ Spring                             ║  ║ Solar Output                       ║
║ [TEMP] -56C | [SUN] 0% | [STORM]   ║  ║ A severe dust storm continues to   ║
║ YES                                ║  ║ blanket the colony, reducing solar ║
║ [EVENT] Massive Sandstorm Forces   ║  ║ energy generation and visibility   ║
║ Solar Shutdown                     ║  ║ across all sectors.                ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT energy_surge | energy +20   ║
║ [O2] 1000 | [H2O] 545 | [E] 1060   ║  ╚════════════════════════════════════╝
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Hampers ║                                        
║ Solar Output | energy +20          ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Shield…              ║
║    Dustline Agro | P1 B3 | S2783   ║  ║    Use materials to strengthen…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S2590    ║  ║    Perform diagnostics and minor…  ║
║ 3. Irina Vale                      ║  ║ 3. Oxygen Conservation Protocol    ║
║    Helios… | P1 B2 | S2033         ║  ║    Coordinate with colony members… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ severity remains high;…            ║
║ ENERGY    1060                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      700                      ║  ║ materials resupply due…            ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 25 on Mars brings continuing   ║  ║ 00:20 | AI directive: Persistent…  ║
║ challenges as a severe dust storm  ║  ║ 00:20 | A severe sandstorm is…     ║
║ reduces solar energy generation    ║  ║ 12:17 | A trading ship from Earth… ║
║ and visibility. Colonies focus on  ║  ║ 06:35 | Martian day 25 has begun   ║
║ reinforcing dust shields,          ║  ║ 00:23 | AI directive: Solar…       ║
║ maintaining water recycling, and   ║  ╚════════════════════════════════════╝
║ conserving oxygen to mitigate the  ║                                        
║ impacts. Resource management       ║                                        
║ remains critical as Mars…          ║                                        
║ A severe sandstorm is underway on  ║                                        
║ Sol 25, knocking all solar panels  ║                                        
║ offline for the next 6 hours.      ║                                        
║ Prepare for reduced power          ║                                        
║ availability.                      ║                                        
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
