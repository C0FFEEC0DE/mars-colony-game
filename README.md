## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-25T00:27:19.504664_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 69 | [SEASON] Early      ║  ║ Unexpected Solar Boost Enhances    ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -46C | [SUN] 99% | [STORM]  ║  ║ Solar activity has risen to 94%,   ║
║ NO                                 ║  ║ increasing energy generation       ║
║ [EVENT] Subsurface Ice Deposit     ║  ║ efficiency across all colonies     ║
║ Secured on Sol 69                  ║  ║ today.                             ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1200   ║  ║ solar_activity +5                  ║
║ [FOOD] 2500 | [MAT] 1100           ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Unexpected Solar Boost        ║                                        
║ Enhances Energy Output |           ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S8577   ║  ║    Perform maintenance and…        ║
║ 2. Zoya Kade                       ║  ║ 2. Water Reservoir Inspection      ║
║    Ares Systems | P1 B4 | S8525    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Materials Recycling Initiative  ║
║    Helios… | P1 B2 | S7003         ║  ║    Process at least 100 units of…  ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently high;…       ║
║ ENERGY    1200                     ║  ║ Helios… -> Irina Vale | Irina,     ║
║ FOOD      2500                     ║  ║ your water reserves look…          ║
║ MATERIALS 1100                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 69 of early spring on Mars, ║  ║ 00:27 | AI directive: Unexpected…  ║
║ a significant solar boost has      ║  ║ 00:27 | Underground ice was        ║
║ enhanced energy production         ║  ║ located…                           ║
║ potential across all colonies.     ║  ║ 12:28 | Exploration team           ║
║ Despite cold temperatures of -46C, ║  ║ confirmed…                         ║
║ the absence of dust storms allows  ║  ║ 06:48 | Martian day 69 has begun   ║
║ for uninterrupted solar array      ║  ║ 00:23 | AI directive: Solar Flare… ║
║ operations. Colonies are focusing  ║  ╚════════════════════════════════════╝
║ on optimizing energy co…           ║                                        
║ Underground ice was located today, ║                                        
║ boosting water reserves: Marco     ║                                        
║ Quinn +50 units, Zoya Kade +45,    ║                                        
║ Irina Vale +21. This extends our   ║                                        
║ sustainability margin amid stable  ║                                        
║ conditions.                        ║                                        
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
