## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-29T00:28:30.965253_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 36 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ A surge in solar activity has      ║
║ [TEMP] -54C | [SUN] 150% | [STORM] ║  ║ increased solar panel efficiency   ║
║ NO                                 ║  ║ across Mars, providing a temporary ║
║ [EVENT] Massive Solar Flare        ║  ║ energy boost for all colonies.     ║
║ Detected, Radiation Risk Up        ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ╚════════════════════════════════════╝
║ [FOOD] 1000 | [MAT] 350            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +0         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Array Output     ║
║    Dustline Agro | P1 B3 | S3645   ║  ║    Reconfigure solar panels and…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S3319    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Prospect for Material Deposits  ║
║    Helios… | P1 B2 | S2663         ║  ║    Survey designated sectors and…  ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ activity detected;…                ║
║ ENERGY    1100                     ║  ║ Helios… -> all… | Sharing data on  ║
║ FOOD      1000                     ║  ║ promising new…                     ║
║ MATERIALS 350                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 36, Mars experiences a      ║  ║ 00:28 | AI directive: Solar Flare… ║
║ solar flare that temporarily       ║  ║ 00:28 | A massive solar flare has… ║
║ boosts energy production, aiding   ║  ║ 06:52 | Martian day 36 has begun   ║
║ all colonies. Early Spring         ║  ║ 00:27 | AI directive: Ongoing      ║
║ conditions remain cold but stable, ║  ║ Dust…                              ║
║ allowing maintenance and           ║  ║ 00:27 | On Sol 35, despite active… ║
║ exploration missions. Colonies are ║  ╚════════════════════════════════════╝
║ focusing on maximizing energy      ║                                        
║ efficiency and scouting material   ║                                        
║ re…                                ║                                        
║ A massive solar flare has          ║                                        
║ increased energy output by 50% for ║                                        
║ the next cycle. All crew advised   ║                                        
║ to take shelter to minimize        ║                                        
║ radiation exposure.                ║                                        
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
