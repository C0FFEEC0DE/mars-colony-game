## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-03T00:27:05.177709_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 40 | [SEASON] Early      ║  ║ Moderate Solar Boost Enhances      ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -50C | [SUN] 99% | [STORM]  ║  ║ Solar activity remains high at     ║
║ NO                                 ║  ║ 94%, providing a modest increase   ║
║ [EVENT] None                       ║  ║ in energy generation across all    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ colonies.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 1100 | [MAT] 400            ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Moderate Solar Boost Enhances ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S4060   ║  ║    Adjust and recalibrate solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S3768    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Material Salvage from Old…      ║
║    Helios… | P1 B2 | S3084         ║  ║    Collect and process scrap…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity remains high;…            ║
║ ENERGY    1100                     ║  ║ Helios… -> Irina Vale | Prioritize ║
║ FOOD      1100                     ║  ║ water recycling…                   ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 40 on Mars sees continued high ║  ║ 00:27 | AI directive: Moderate…    ║
║ solar activity boosting energy     ║  ║ 06:37 | Martian day 40 has begun   ║
║ production modestly. Colonies      ║  ║ 00:27 | AI directive: Solar Flare… ║
║ focus on optimizing energy systems ║  ║ 00:27 | Field teams led by Irina…  ║
║ and maintaining water recycling    ║  ║ 12:18 | A powerful solar flare     ║
║ efficiency amid cold early spring  ║  ║ has…                               ║
║ temperatures. Resource management  ║  ╚════════════════════════════════════╝
║ remains critical with limited dust ║                                        
║ storm activit…                     ║                                        
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
