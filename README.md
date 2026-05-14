## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-14T00:32:55.420868_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 50 | [SEASON] Early      ║  ║ Moderate Solar Boost Enhances      ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -39C | [SUN] 96% | [STORM]  ║  ║ Solar activity has increased to    ║
║ NO                                 ║  ║ 91%, providing a mild boost to     ║
║ [EVENT] Microbial Discovery in     ║  ║ solar panel efficiency across the  ║
║ Martian Soil                       ║  ║ colony.                            ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ║ solar_activity +5                  ║
║ [FOOD] 1200 | [MAT] 450            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Moderate Solar Boost Enhances ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S5467   ║  ║    Adjust and fine-tune solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S4984    ║  ║    Perform maintenance and…        ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S4148         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is elevated;…             ║
║ ENERGY    1120                     ║  ║ Ares Systems -> Zoya Kade |        ║
║ FOOD      1200                     ║  ║ Requesting status update on…       ║
║ MATERIALS 450                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 50 of early spring, Mars    ║  ║ 00:32 | AI directive: Moderate…    ║
║ experiences a mild solar activity  ║  ║ 12:40 | On Sol 50, analysis        ║
║ boost enhancing energy generation  ║  ║ reveals…                           ║
║ potential. Colonies focus on       ║  ║ 06:59 | Martian day 50 has begun   ║
║ optimizing solar panels and        ║  ║ 00:31 | AI directive: Solar…       ║
║ maintaining critical water         ║  ║ 00:31 | Exploration teams Irina…   ║
║ recycling systems amid cold        ║  ╚════════════════════════════════════╝
║ temperatures. Resource management  ║                                        
║ remains key for survival as dust…  ║                                        
║ On Sol 50, analysis reveals        ║                                        
║ presence of unknown bacteria in    ║                                        
║ soil sample. Further study         ║                                        
║ scheduled to assess implications   ║                                        
║ for planetary protection.          ║                                        
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
