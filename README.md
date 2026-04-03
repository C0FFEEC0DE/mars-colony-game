## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-03T00:19:49.705594_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 10 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ Increased solar activity has       ║
║ [TEMP] -66C | [SUN] 150% | [STORM] ║  ║ temporarily enhanced solar panel   ║
║ NO                                 ║  ║ efficiency, providing a modest     ║
║ [EVENT] Massive Solar Flare Boosts ║  ║ energy surge across all colonies.  ║
║ Energy Output                      ║  ║ EFFECT energy_surge | energy +20   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1020   ║                                        
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | energy +20                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S1441   ║  ║    Adjust and recalibrate solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S1292    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S919          ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is elevated;…             ║
║ ENERGY    1020                     ║  ║ Helios… -> Irina Vale | Coordinate ║
║ FOOD      400                      ║  ║ with local teams to…               ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 10 marks a boost in solar      ║  ║ 00:19 | AI directive: Solar Flare… ║
║ energy due to heightened solar     ║  ║ 00:19 | A powerful solar flare     ║
║ activity, allowing colonies to     ║  ║ has…                               ║
║ improve energy production. Early   ║  ║ 12:16 | A meteor shower passed     ║
║ spring conditions remain harsh at  ║  ║ Mars…                              ║
║ -66C but stable with no dust       ║  ║ 06:24 | Martian day 10 has begun   ║
║ storms. Colonies focus on          ║  ║ 00:17 | AI directive: Solar…       ║
║ optimizing energy and water        ║  ╚════════════════════════════════════╝
║ systems to sustain growth and      ║                                        
║ resourc…                           ║                                        
║ A powerful solar flare has         ║                                        
║ increased energy levels by 50% for ║                                        
║ the next cycle. Ensure all crew    ║                                        
║ take appropriate radiation         ║                                        
║ shielding measures immediately.    ║                                        
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
