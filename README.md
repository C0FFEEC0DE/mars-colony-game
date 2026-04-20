## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-20T00:21:54.222518_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 27 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -47C | [SUN] 70% | [STORM]  ║  ║ Solar activity at 65% increases    ║
║ NO                                 ║  ║ solar panel efficiency, enhancing  ║
║ [EVENT] Underground Ice Deposit    ║  ║ energy generation across colonies. ║
║ Secured                            ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1060   ║  ╚════════════════════════════════════╝
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2984   ║  ║    Recalibrate solar arrays to…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S2829    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory and Salvage  ║
║    Helios… | P1 B2 | S2226         ║  ║    Collect at least 20 units of…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently…             ║
║ ENERGY    1060                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      700                      ║  ║ support for water…                 ║
║ MATERIALS 200                      ║  ║ Dustline Agro -> Ares… | Sharing   ║
╚════════════════════════════════════╝  ║ data on energy…                    ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars colonies experience a         ║  ║ 00:21 | AI directive: Solar…       ║
║ beneficial solar boost, enhancing  ║  ║ 00:21 | Sol 27: Subsurface ice…    ║
║ energy production amid early       ║  ║ 06:33 | Martian day 27 has begun   ║
║ spring cold. Stable conditions     ║  ║ 00:21 | AI directive: Increased…   ║
║ allow teams to focus on optimizing ║  ║ 12:09 | A significant solar flare… ║
║ solar arrays, maintaining water    ║  ╚════════════════════════════════════╝
║ recycling systems, and salvaging   ║                                        
║ materials. Coordination between    ║                                        
║ colonies is active to maxi…        ║                                        
║ Sol 27: Subsurface ice located     ║                                        
║ beneath the northern ridge. Water  ║                                        
║ reserves updated—Irina +25L, Marco ║                                        
║ +41L, Zoya +36L.                   ║                                        
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
