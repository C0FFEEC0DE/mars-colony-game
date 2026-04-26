## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-26T00:23:11.541982_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 33 | [SEASON] Early      ║  ║ Moderate Solar Boost Enhances      ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -37C | [SUN] 78% | [STORM]  ║  ║ Solar activity has risen to 73%,   ║
║ NO                                 ║  ║ providing a modest increase in     ║
║ [EVENT] None                       ║  ║ solar panel efficiency across all  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ colonies.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1080   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 700 | [MAT] 200             ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Moderate Solar Boost Enhances ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S3603   ║  ║    Adjust and clean solar panels…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S3209    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Spring Crop Planning            ║
║    Helios… | P1 B2 | S2604         ║  ║    Design and plant new crops…     ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels are…               ║
║ ENERGY    1080                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      700                      ║  ║ collaboration on water…            ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars enters early spring with a    ║  ║ 00:23 | AI directive: Moderate…    ║
║ moderate solar boost improving     ║  ║ 06:29 | Martian day 33 has begun   ║
║ energy collection. Colonies focus  ║  ║ 00:22 | AI directive: Solar Flare… ║
║ on optimizing resources with       ║  ║ 12:19 | Exploration team located   ║
║ missions targeting solar panel     ║  ║ a…                                 ║
║ efficiency and water recycling.    ║  ║ 06:37 | Martian day 32 has begun   ║
║ Collaborative efforts begin        ║  ╚════════════════════════════════════╝
║ between key factions to enhance    ║                                        
║ sustainability.                    ║                                        
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
