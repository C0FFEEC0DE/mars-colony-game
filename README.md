## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-06T00:19:05.622637_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 13 | [SEASON] Early      ║  ║ Unexpected Solar Boost Enhances    ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -62C | [SUN] 75% | [STORM]  ║  ║ Solar activity has increased to    ║
║ NO                                 ║  ║ 70%, providing a temporary boost   ║
║ [EVENT] None                       ║  ║ in energy generation across all    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ colonies.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1020   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 400 | [MAT] 50              ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Unexpected Solar Boost        ║                                        
║ Enhances Energy Output |           ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S1940   ║  ║    Calibrate solar arrays to…      ║
║ 2. Zoya Kade                       ║  ║ 2. Scout Nearby Water Cache        ║
║    Ares Systems | P1 B4 | S1675    ║  ║    Send a team to verify and…      ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1242         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity spike detected;…          ║
║ ENERGY    1020                     ║  ║ Ares Systems… -> Zoya Kade |       ║
║ FOOD      400                      ║  ║ Monitoring your water resource…    ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 13 of Early Spring, Mars    ║  ║ 00:19 | AI directive: Unexpected…  ║
║ experiences a beneficial solar     ║  ║ 06:25 | Martian day 13 has begun   ║
║ boost enhancing energy production. ║  ║ 00:18 | AI directive: Persistent…  ║
║ Colonies are encouraged to         ║  ║ 00:18 | A severe dust storm on     ║
║ optimize solar arrays and explore  ║  ║ Sol…                               ║
║ potential water caches exposed by  ║  ║ 06:20 | Martian day 12 has begun   ║
║ seasonal changes. Resources remain ║  ╚════════════════════════════════════╝
║ stable with no dust storms active. ║                                        
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
