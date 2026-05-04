## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-04T00:27:02.649537_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 41 | [SEASON] Early      ║  ║ Solar Activity Peaks               ║
║ Spring                             ║  ║ Solar activity has surged to 150%, ║
║ [TEMP] -59C | [SUN] 150% | [STORM] ║  ║ boosting solar panel efficiency    ║
║ NO                                 ║  ║ across the planet.                 ║
║ [EVENT] Massive Solar Flare        ║  ║ EFFECT solar_boost |               ║
║ Increases Radiation Levels         ║  ║ solar_activity +0                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║                                        
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks |        ║                                        
║ solar_activity +0                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S4103   ║  ║    Upgrade and recalibrate solar…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Maintenance     ║
║    Ares Systems | P1 B4 | S3835    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3139         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is at a high.…            ║
║ ENERGY    1100                     ║  ║ Helios… -> Marco… | We are low on  ║
║ FOOD      1100                     ║  ║ oxygen resources;…                 ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 41 of early spring, Mars    ║  ║ 00:27 | AI directive: Solar…       ║
║ experiences a significant solar    ║  ║ 00:26 | A powerful solar flare     ║
║ activity surge, enhancing energy   ║  ║ has…                               ║
║ production capabilities. Colonies  ║  ║ 06:49 | Martian day 41 has begun   ║
║ are advised to capitalize on the   ║  ║ 00:27 | AI directive: Moderate…    ║
║ increased solar input by           ║  ║ 06:37 | Martian day 40 has begun   ║
║ optimizing their solar arrays.     ║  ╚════════════════════════════════════╝
║ Water reserves remain a critical   ║                                        
║ resource, with ongoing mai…        ║                                        
║ A powerful solar flare has         ║                                        
║ increased energy output by 50% for ║                                        
║ the next cycle. All personnel must ║                                        
║ take cover to minimize radiation   ║                                        
║ exposure.                          ║                                        
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
