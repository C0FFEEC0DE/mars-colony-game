## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-01T00:20:13.640812_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 8 | [SEASON] Early       ║  ║ Solar Activity Boosts Power Grid   ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -78C | [SUN] 94% | [STORM]  ║  ║ 89%, enhancing energy generation   ║
║ NO                                 ║  ║ capabilities across all colonies.  ║
║ [EVENT] Trading Ship Arrives with  ║  ║ EFFECT solar_boost |               ║
║ Vital Supplies                     ║  ║ solar_activity +5                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1000   ║                                        
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Power   ║                                        
║ Grid | solar_activity +5           ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S1028   ║  ║    Adjust and calibrate solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S922     ║  ║    Implement water-saving…         ║
║ 3. Irina Vale                      ║  ║ 3. Materials Recovery              ║
║    Helios… | P1 B2 | S658          ║  ║    Recover at least 10 units of…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently high;…       ║
║ ENERGY    1000                     ║  ║ Helios… -> all… | Sharing water    ║
║ FOOD      400                      ║  ║ conservation…                      ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 8 of early spring, Mars     ║  ║ 00:20 | AI directive: Solar…       ║
║ experiences a surge in solar       ║  ║ 12:16 | A trading ship from Earth… ║
║ activity, enhancing energy         ║  ║ 06:27 | Martian day 8 has begun    ║
║ production capabilities. Colonies  ║  ║ 00:18 | On Sol 7, analysis         ║
║ focus on optimizing their solar    ║  ║ revealed…                          ║
║ arrays and conserving vital water  ║  ║ 12:45 | AI directive: Solar…       ║
║ resources. Efforts to recover      ║  ╚════════════════════════════════════╝
║ materials continue to support      ║                                        
║ sustainable operations amid chal…  ║                                        
║ A trading ship from Earth has      ║                                        
║ docked, delivering 100 units of    ║                                        
║ food and 50 units of materials to  ║                                        
║ the colony's reserves. This        ║                                        
║ shipment bolsters our survival     ║                                        
║ resources as Sol 8 unfolds under   ║                                        
║ stable conditions.                 ║                                        
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
