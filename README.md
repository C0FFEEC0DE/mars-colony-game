## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-01T00:29:38.715857_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 38 | [SEASON] Early      ║  ║ Solar Activity Peaks               ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -76C | [SUN] 150% | [STORM] ║  ║ 150%, providing enhanced energy    ║
║ NO                                 ║  ║ generation potential across Mars   ║
║ [EVENT] Massive Solar Flare        ║  ║ habitats.                          ║
║ Detected                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ╚════════════════════════════════════╝
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks |        ║                                        
║ solar_activity +0                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panels           ║
║    Dustline Agro | P1 B3 | S3777   ║  ║    Adjust and optimize solar…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S3499    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory and Salvage  ║
║    Helios… | P1 B2 | S2819         ║  ║    Send a scout to identify and…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is peaking today;…        ║
║ ENERGY    1100                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      1100                     ║  ║ stable water…                      ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 38 during early spring,     ║  ║ 00:29 | AI directive: Solar…       ║
║ Mars experiences a peak in solar   ║  ║ 12:30 | A powerful solar flare     ║
║ activity enhancing energy          ║  ║ has…                               ║
║ generation capabilities. Colonies  ║  ║ 06:50 | Martian day 38 has begun   ║
║ focus on optimizing solar panel    ║  ║ 00:28 | AI directive: Moderate…    ║
║ arrays and maintaining water       ║  ║ 00:28 | Exploration teams have…    ║
║ recycling systems amid cold        ║  ╚════════════════════════════════════╝
║ temperatures. Material salvage     ║                                        
║ missions are underway to sustain   ║                                        
║ co…                                ║                                        
║ A powerful solar flare has         ║                                        
║ increased radiation levels by 50%  ║                                        
║ for the next cycle. All crew must  ║                                        
║ take immediate shelter to minimize ║                                        
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
