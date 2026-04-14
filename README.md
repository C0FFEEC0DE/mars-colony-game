## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-14T00:24:10.586016_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 21 | [SEASON] Early      ║  ║ Persistent Dust Storm Limits Solar ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -59C | [SUN] 0% | [STORM]   ║  ║ A continuing dust storm on Sol 21  ║
║ YES                                ║  ║ severely reduces solar energy      ║
║ [EVENT] Microbial Signature Found  ║  ║ generation, straining colony power ║
║ in Soil Sample                     ║  ║ reserves.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT cold_snap | temperature -3  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 500 | [MAT] 100             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Limits  ║                                        
║ Solar Output | temperature -3      ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Emergency Power Conservation    ║
║    Dustline Agro | P1 B3 | S2533   ║  ║    Implement energy-saving…        ║
║ 2. Zoya Kade                       ║  ║ 2. Dust Storm Sensor Maintenance   ║
║    Ares Systems | P1 B4 | S2339    ║  ║    Perform exterior sensor…        ║
║ 3. Irina Vale                      ║  ║ 3. Water Recycling System Check    ║
║    Helios… | P1 B2 | S1715         ║  ║    Inspect and repair water…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ conditions persist.…               ║
║ ENERGY    1040                     ║  ║ Helios… -> all… | Sharing sensor   ║
║ FOOD      500                      ║  ║ maintenance…                       ║
║ MATERIALS 100                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 21, a persistent dust storm ║  ║ 00:24 | AI directive: Persistent…  ║
║ has severely reduced solar energy  ║  ║ 00:24 | On Sol 21, analysis…       ║
║ production, forcing colonies to    ║  ║ 12:20 | A severe sandstorm is…     ║
║ implement strict power             ║  ║ 06:41 | Martian day 21 has begun   ║
║ conservation measures. Sensor      ║  ║ 00:21 | AI directive: Early        ║
║ maintenance and water recycling    ║  ║ Spring…                            ║
║ system checks are critical to      ║  ╚════════════════════════════════════╝
║ maintaining operational stability  ║                                        
║ in early spring's harsh condi…     ║                                        
║ On Sol 21, analysis detected       ║                                        
║ unknown bacterial presence in      ║                                        
║ Martian soil amid ongoing dust     ║                                        
║ storm. Sample integrity            ║                                        
║ maintained; further study          ║                                        
║ required.                          ║                                        
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
