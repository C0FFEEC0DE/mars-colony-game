## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-30T00:24:16.582502_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 72 | [SEASON] Early      ║  ║ Solar Activity Spike Boosts Energy ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -39C | [SUN] 150% | [STORM] ║  ║ Solar activity has surged to 150%, ║
║ NO                                 ║  ║ increasing energy generation       ║
║ [EVENT] Massive Solar Flare        ║  ║ efficiency across all colonies.    ║
║ Detected                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1200   ║  ╚════════════════════════════════════╝
║ [FOOD] 2600 | [MAT] 1150           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Spike Boosts   ║                                        
║ Energy Output | solar_activity +0  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Array Alignment  ║
║    Dustline Agro | P1 B3 | S9306   ║  ║    Adjust solar panels to…         ║
║ 2. Zoya Kade                       ║  ║ 2. Inspect Oxygen Storage Tanks    ║
║    Ares Systems | P1 B4 | S9107    ║  ║    Perform maintenance checks on…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S7478         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is high today;…           ║
║ ENERGY    1200                     ║  ║ Helios… -> Marco… | We have        ║
║ FOOD      2600                     ║  ║ detected promising…                ║
║ MATERIALS 1150                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 72, Mars experiences a      ║  ║ 00:24 | AI directive: Solar…       ║
║ spike in solar activity boosting   ║  ║ 00:24 | A powerful solar flare     ║
║ energy generation. Colonies are    ║  ║ has…                               ║
║ advised to optimize solar arrays   ║  ║ 12:38 | A massive solar flare is…  ║
║ to take advantage. Oxygen supply   ║  ║ 06:52 | Martian day 72 has begun   ║
║ maintenance remains critical amid  ║  ║ 00:23 | AI directive: Mild Solar…  ║
║ cold early spring conditions.      ║  ╚════════════════════════════════════╝
║ A powerful solar flare has         ║                                        
║ increased radiation levels by 50%  ║                                        
║ for the next cycle. All personnel  ║                                        
║ must seek radiation shelter        ║                                        
║ immediately.                       ║                                        
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
