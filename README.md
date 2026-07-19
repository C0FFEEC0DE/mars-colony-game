## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-19T00:24:49.148879_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 64 | [SEASON] Early      ║  ║ Seasonal Solar Boost               ║
║ Spring                             ║  ║ Early spring brings increased      ║
║ [TEMP] -53C | [SUN] 94% | [STORM]  ║  ║ solar activity, enhancing solar    ║
║ NO                                 ║  ║ panel efficiency across all        ║
║ [EVENT] Trading Ship Arrives,      ║  ║ colonies.                          ║
║ Boosting Supplies                  ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ╚════════════════════════════════════╝
║ [FOOD] 2300 | [MAT] 1000           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Seasonal Solar Boost |        ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7843   ║  ║    Recalibrate and clean solar…    ║
║ 2. Zoya Kade                       ║  ║ 2. Early Spring Water Survey       ║
║    Ares Systems | P1 B4 | S7818    ║  ║    Conduct a survey to identify…   ║
║ 3. Irina Vale                      ║  ║ 3. Material Salvage Operation      ║
║    Helios… | P1 B2 | S6495         ║  ║    Collect and process 50 units…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels are high;…         ║
║ ENERGY    1160                     ║  ║ Helios… -> Marco… | Irina requests ║
║ FOOD      2300                     ║  ║ coordination for…                  ║
║ MATERIALS 1000                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 64 during early spring,     ║  ║ 00:24 | AI directive: Seasonal…    ║
║ Mars colonies experience a solar   ║  ║ 00:24 | A trading ship from Earth… ║
║ boost increasing energy production ║  ║ 06:37 | Martian day 64 has begun   ║
║ capabilities. With no dust storms  ║  ║ 00:23 | AI directive: Solar…       ║
║ active, conditions allow for       ║  ║ 00:23 | A massive solar flare…     ║
║ resource surveys and salvage       ║  ╚════════════════════════════════════╝
║ operations. Colonies are advised   ║                                        
║ to optimize solar arrays and       ║                                        
║ explore new water and mate…        ║                                        
║ A trading ship from Earth has      ║                                        
║ docked, delivering +100 food units ║                                        
║ and +50 materials to the global    ║                                        
║ pool. Operations anticipate        ║                                        
║ improved resource stability.       ║                                        
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
