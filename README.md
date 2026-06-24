## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-31T00:35:03.857859_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 55 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ A surge in solar activity has      ║
║ [TEMP] -48C | [SUN] 0% | [STORM]   ║  ║ increased energy generation        ║
║ YES                                ║  ║ capacity across all colonies,      ║
║ [EVENT] Microbial Discovery Amid   ║  ║ improving power availability for   ║
║ Martian Dust Storm                 ║  ║ critical systems.                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║  ║ solar_activity +5                  ║
║ [FOOD] 1900 | [MAT] 800            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7079   ║  ║    Adjust and optimize solar…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S6805    ║  ║    Perform diagnostics and minor…  ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory and Salvage  ║
║    Helios… | P1 B2 | S5861         ║  ║    Survey storage and salvage…     ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ activity is currently…             ║
║ ENERGY    1140                     ║  ║ Ares Systems -> Zoya Kade |        ║
║ FOOD      1900                     ║  ║ Requesting status update on water… ║
║ MATERIALS 800                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 55 on Mars brings a            ║  ║ 00:30 | During Sol 55, analysis    ║
║ significant solar boost,           ║  ║ of…                                ║
║ increasing energy availability     ║  ║ 12:54 | On Sol 55, a meteor        ║
║ across all colonies. Colonists are ║  ║ shower…                            ║
║ tasked with optimizing solar       ║  ║ 00:35 | Despite ongoing dust       ║
║ arrays and maintaining critical    ║  ║ storm…                             ║
║ life support systems to take       ║  ║ 00:38 | A massive sandstorm is…    ║
║ advantage of favorable conditions. ║  ║ 12:34 | A massive solar flare is…  ║
║ Resource management remains a      ║  ╚════════════════════════════════════╝
║ priority…                          ║                                        
║ During Sol 55, analysis of soil    ║                                        
║ samples revealed unknown bacterial ║                                        
║ presence despite ongoing dust      ║                                        
║ storm and zero solar activity,     ║                                        
║ signaling potential bio-signatures ║                                        
║ beneath Mars' surface.             ║                                        
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
