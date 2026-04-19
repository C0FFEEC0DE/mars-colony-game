## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-19T00:21:26.965652_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 26 | [SEASON] Early      ║  ║ Increased Solar Activity Boosts    ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -65C | [SUN] 150% | [STORM] ║  ║ Solar activity has risen to 150%,  ║
║ NO                                 ║  ║ providing a natural energy surge   ║
║ [EVENT] Massive Solar Flare        ║  ║ across Mars colonies today.        ║
║ Detected                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1060   ║  ╚════════════════════════════════════╝
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Increased Solar Activity      ║                                        
║ Boosts Energy Output |             ║                                        
║ solar_activity +0                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2845   ║  ║    Recalibrate and realign solar…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Efficiency…     ║
║    Ares Systems | P1 B4 | S2676    ║  ║    Inspect and enhance the water…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S2107         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ activity has…                      ║
║ ENERGY    1060                     ║  ║ Helios… -> Irina Vale | Resource   ║
║ FOOD      700                      ║  ║ survey indicates…                  ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars experiences a surge in solar  ║  ║ 00:21 | AI directive: Increased…   ║
║ activity, increasing energy        ║  ║ 12:09 | A significant solar flare… ║
║ availability for all colonies.     ║  ║ 06:24 | Martian day 26 has begun   ║
║ Colonies focus on optimizing solar ║  ║ 00:20 | AI directive: Persistent…  ║
║ arrays and improving water         ║  ║ 00:20 | A severe sandstorm is…     ║
║ recycling to capitalize on the     ║  ╚════════════════════════════════════╝
║ conditions. Resource exploration   ║                                        
║ remains a priority to bolster      ║                                        
║ materials stockpiles.              ║                                        
║ A significant solar flare has      ║                                        
║ increased radiation levels by 50%  ║                                        
║ for the next cycle. All personnel  ║                                        
║ are advised to seek shelter        ║                                        
║ immediately to minimize exposure.  ║                                        
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
