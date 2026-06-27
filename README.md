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
║ [EVENT] Massive Sandstorm Disables ║  ║ improving power availability for   ║
║ Solar Arrays                       ║  ║ critical systems.                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║  ║ solar_activity +5                  ║
║ [FOOD] 1900 | [MAT] 800            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7043   ║  ║    Adjust and optimize solar…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S6841    ║  ║    Perform diagnostics and minor…  ║
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
║ Sol 55 on Mars brings a            ║  ║ 12:40 | A severe dust storm is…    ║
║ significant solar boost,           ║  ║ 12:41 | On Sol 55, amid a…         ║
║ increasing energy availability     ║  ║ 00:30 | During Sol 55, analysis    ║
║ across all colonies. Colonists are ║  ║ of…                                ║
║ tasked with optimizing solar       ║  ║ 12:54 | On Sol 55, a meteor        ║
║ arrays and maintaining critical    ║  ║ shower…                            ║
║ life support systems to take       ║  ║ 00:35 | Despite ongoing dust       ║
║ advantage of favorable conditions. ║  ║ storm…                             ║
║ Resource management remains a      ║  ╚════════════════════════════════════╝
║ priority…                          ║                                        
║ A severe dust storm is currently   ║                                        
║ active on Sol 55, causing all      ║                                        
║ solar panels to be offline for the ║                                        
║ next 6 hours. Power management     ║                                        
║ protocols are in effect.           ║                                        
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
