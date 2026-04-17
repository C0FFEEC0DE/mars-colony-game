## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-17T00:23:11.070206_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 24 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -31C | [SUN] 78% | [STORM]  ║  ║ Solar activity has increased to    ║
║ NO                                 ║  ║ 73%, enhancing solar panel         ║
║ [EVENT] Unidentified Bacteria      ║  ║ efficiency across the colony.      ║
║ Detected in Soil Sample            ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 600 | [MAT] 150             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2744   ║  ║    Adjust and recalibrate solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Maintenance     ║
║    Ares Systems | P1 B4 | S2527    ║  ║    Perform maintenance on water…   ║
║ 3. Irina Vale                      ║  ║ 3. Scout Nearby Materials Cache    ║
║    Helios… | P1 B2 | S1982         ║  ║    Send a scout mission to locate… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity increased, expect…        ║
║ ENERGY    1040                     ║  ║ Helios… -> all… | Offering trade   ║
║ FOOD      600                      ║  ║ in materials for…                  ║
║ MATERIALS 150                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 24 of early spring on Mars     ║  ║ 00:23 | AI directive: Solar…       ║
║ sees a solar activity rise to 73%, ║  ║ 12:20 | On Sol 24, analysis…       ║
║ boosting energy production across  ║  ║ 06:36 | Martian day 24 has begun   ║
║ colonies. Water remains limited,   ║  ║ 00:24 | AI directive: Mild Solar…  ║
║ prompting maintenance efforts.     ║  ║ 12:18 | On Sol 23, a meteor        ║
║ Scouts prepare to explore newly    ║  ║ shower…                            ║
║ accessible materials as the thaw   ║  ╚════════════════════════════════════╝
║ progresses.                        ║                                        
║ On Sol 24, analysis revealed       ║                                        
║ unknown bacterial presence in      ║                                        
║ Martian soil. Further study        ║                                        
║ underway to assess biological and  ║                                        
║ environmental implications.        ║                                        
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
