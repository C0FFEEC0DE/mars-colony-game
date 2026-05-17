## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-17T00:30:03.146905_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 52 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ A surge in solar activity has      ║
║ [TEMP] -67C | [SUN] 150% | [STORM] ║  ║ increased energy generation by 20% ║
║ NO                                 ║  ║ across all solar panels, improving ║
║ [EVENT] Massive Solar Flare        ║  ║ power reserves on Mars.            ║
║ Detected on Sol 52                 ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ╚════════════════════════════════════╝
║ [FOOD] 1200 | [MAT] 450            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +0         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Alignment  ║
║    Dustline Agro | P1 B3 | S5878   ║  ║    Recalibrate solar arrays for…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S5227    ║  ║    Reduce water consumption by…    ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S4455         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is heightened;…           ║
║ ENERGY    1120                     ║  ║ Helios… -> all… | Sharing recent   ║
║ FOOD      1200                     ║  ║ findings on…                       ║
║ MATERIALS 450                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Solar activity has increased to    ║  ║ 00:30 | AI directive: Solar Flare… ║
║ 150%, providing an energy boost    ║  ║ 00:29 | A massive solar flare has… ║
║ for all colonies on Sol 52 during  ║  ║ 06:44 | Martian day 52 has begun   ║
║ early spring. Colonies are         ║  ║ 00:28 | A massive solar flare has… ║
║ encouraged to optimize their solar ║  ║ 00:30 | AI directive: Mild Solar…  ║
║ arrays to capitalize on this       ║  ╚════════════════════════════════════╝
║ surge. Water remains a critical    ║                                        
║ resource, with conservation        ║                                        
║ efforts recommended as tempera…    ║                                        
║ A massive solar flare has          ║                                        
║ increased energy levels by 50% for ║                                        
║ the next turn. All personnel must  ║                                        
║ take cover to minimize radiation   ║                                        
║ exposure.                          ║                                        
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
