## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-30T00:28:16.833176_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 37 | [SEASON] Early      ║  ║ Moderate Solar Boost Enhances      ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -62C | [SUN] 66% | [STORM]  ║  ║ Solar activity has increased to    ║
║ NO                                 ║  ║ 61%, providing a mild boost to     ║
║ [EVENT] New subterranean caverns   ║  ║ solar panel efficiency across Mars ║
║ mapped beneath the colony          ║  ║ colonies.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ║ solar_activity +5                  ║
║ [FOOD] 1100 | [MAT] 400            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Moderate Solar Boost Enhances ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S3699   ║  ║    Adjust and calibrate solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S3397    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S2729         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is trending…              ║
║ ENERGY    1100                     ║  ║ Helios… -> all… | Sharing data on  ║
║ FOOD      1100                     ║  ║ effective water…                   ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 37, Mars colonies           ║  ║ 00:28 | AI directive: Moderate…    ║
║ experience a moderate solar boost  ║  ║ 00:28 | Exploration teams have…    ║
║ amid early spring's cold           ║  ║ 12:30 | A trading vessel from      ║
║ temperatures. Energy systems are   ║  ║ Earth…                             ║
║ primed for optimization while      ║  ║ 06:47 | Martian day 37 has begun   ║
║ water recycling remains essential  ║  ║ 00:28 | AI directive: Solar Flare… ║
║ due to ongoing scarcity. Colonists ║  ╚════════════════════════════════════╝
║ focus on maintaining critical      ║                                        
║ infrastructure to sustain their r… ║                                        
║ Exploration teams have located     ║                                        
║ underground caverns near the       ║                                        
║ habitat perimeter. These           ║                                        
║ formations may provide stable      ║                                        
║ thermal conditions for future      ║                                        
║ expansion.                         ║                                        
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
