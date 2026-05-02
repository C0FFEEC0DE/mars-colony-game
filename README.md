## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-02T00:27:12.834401_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 39 | [SEASON] Early      ║  ║ Solar Flare Boost Increases Energy ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -52C | [SUN] 150% | [STORM] ║  ║ A surge in solar activity has      ║
║ NO                                 ║  ║ temporarily increased solar panel  ║
║ [EVENT] Underground Ice Deposit    ║  ║ efficiency across all colonies,    ║
║ Secured on Sol 39                  ║  ║ boosting energy generation by 15%. ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ║ solar_activity +0                  ║
║ [FOOD] 1100 | [MAT] 400            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boost Increases   ║                                        
║ Energy Output | solar_activity +0  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S3908   ║  ║    Recalibrate solar panel angles… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Purification Maintenance  ║
║    Ares Systems | P1 B4 | S3672    ║  ║    Inspect and repair filtration…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S3000         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ event detected. Take…              ║
║ ENERGY    1100                     ║  ║ Helios… -> Marco… | Considering a  ║
║ FOOD      1100                     ║  ║ resource exchange…                 ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars colonies experience a boost   ║  ║ 00:27 | AI directive: Solar Flare… ║
║ in energy production thanks to a   ║  ║ 00:27 | Field teams led by Irina…  ║
║ solar flare increasing solar panel ║  ║ 12:18 | A powerful solar flare     ║
║ efficiency. Colonies are advised   ║  ║ has…                               ║
║ to optimize energy capture and     ║  ║ 06:52 | Martian day 39 has begun   ║
║ maintain water systems to conserve ║  ║ 00:29 | AI directive: Solar…       ║
║ resources during early spring.     ║  ╚════════════════════════════════════╝
║ Collaborative resource exchanges   ║                                        
║ are being propo…                   ║                                        
║ Field teams led by Irina Vale have ║                                        
║ confirmed a significant            ║                                        
║ underground ice source, adding 88  ║                                        
║ units of water to colony reserves. ║                                        
║ Marco Quinn and Zoya Kade          ║                                        
║ contributed to extraction efforts, ║                                        
║ ensuring improved hydration su…    ║                                        
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
