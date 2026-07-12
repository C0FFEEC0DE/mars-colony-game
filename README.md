## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-12T00:25:39.236780_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 58 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -74C | [SUN] 85% | [STORM]  ║  ║ A surge in solar activity          ║
║ NO                                 ║  ║ increases energy generation        ║
║ [EVENT] Sol 58 Meteor Shower       ║  ║ efficiency across all colonies.    ║
║ Enhances Material Stockpile        ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ╚════════════════════════════════════╝
║ [FOOD] 2100 | [MAT] 900            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7370   ║  ║    Upgrade and recalibrate solar…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S7263    ║  ║    Reduce water consumption…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6016         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is favorable…             ║
║ ENERGY    1160                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      2100                     ║  ║ data on your agro…                 ║
║ MATERIALS 900                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 58 brings a welcome solar      ║  ║ 00:25 | AI directive: Solar…       ║
║ activity increase, enhancing       ║  ║ 00:25 | A meteor shower was…       ║
║ energy production across Mars      ║  ║ 12:16 | During Sol 58's meteor…    ║
║ colonies. Colonies are focusing    ║  ║ 06:43 | Martian day 58 has begun   ║
║ efforts on optimizing solar arrays ║  ║ 00:24 | A severe sandstorm is…     ║
║ and conserving water as early      ║  ╚════════════════════════════════════╝
║ spring conditions persist.         ║                                        
║ Collaboration between factions     ║                                        
║ remains steady to maximize         ║                                        
║ resource…                          ║                                        
║ A meteor shower was recorded today ║                                        
║ with no adverse effects. Zoya Kade ║                                        
║ successfully salvaged 11 extra     ║                                        
║ materials from debris.             ║                                        
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
