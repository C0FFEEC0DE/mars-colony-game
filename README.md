## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-21T00:23:33.825097_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 28 | [SEASON] Early      ║  ║ Mild Solar Activity Boost          ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -77C | [SUN] 69% | [STORM]  ║  ║ 64%, providing a modest boost to   ║
║ NO                                 ║  ║ energy generation across all       ║
║ [EVENT] Meteor Shower Yields       ║  ║ colonies.                          ║
║ Critical Materials Amid Minor      ║  ║ EFFECT solar_boost |               ║
║ Damage                             ║  ║ solar_activity +5                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1060   ║                                        
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Activity Boost |   ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S3202   ║  ║    Adjust and calibrate solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S2891    ║  ║    Install and test water…         ║
║ 3. Irina Vale                      ║  ║ 3. Material Salvage Operation      ║
║    Helios… | P1 B2 | S2326         ║  ║    Collect at least 20 units of…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is favorable…             ║
║ ENERGY    1060                     ║  ║ Helios… -> Marco… | Reports        ║
║ FOOD      700                      ║  ║ indicate potential…                ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 28 of Mars' early spring,   ║  ║ 00:23 | AI directive: Mild Solar…  ║
║ colonies experience a mild solar   ║  ║ 12:22 | During Sol 28's meteor…    ║
║ activity boost enhancing energy    ║  ║ 06:42 | Martian day 28 has begun   ║
║ production. Water conservation     ║  ║ 00:21 | AI directive: Solar…       ║
║ remains a priority due to limited  ║  ║ 00:21 | Sol 27: Subsurface ice…    ║
║ reserves, while material salvage   ║  ╚════════════════════════════════════╝
║ missions offer opportunities to    ║                                        
║ bolster construction resources.    ║                                        
║ Colonists coordinat…               ║                                        
║ During Sol 28's meteor shower,     ║                                        
║ Irina Vale and Marco Quinn         ║                                        
║ salvaged 30 materials combined.    ║                                        
║ Irina also reported structural     ║                                        
║ damage under ongoing -77C          ║                                        
║ conditions with 64% solar          ║                                        
║ activity.                          ║                                        
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
