## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-18T00:23:55.270522_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 63 | [SEASON] Early      ║  ║ Solar Activity Peaks at 150%       ║
║ Spring                             ║  ║ Mars experiences a significant     ║
║ [TEMP] -36C | [SUN] 150% | [STORM] ║  ║ surge in solar radiation, boosting ║
║ NO                                 ║  ║ energy generation across colonies. ║
║ [EVENT] Solar Flare Surge on Sol   ║  ║ EFFECT solar_boost |               ║
║ 63                                 ║  ║ solar_activity +0                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║                                        
║ [FOOD] 2200 | [MAT] 950            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks at 150%  ║                                        
║ | solar_activity +0                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Solar Panel Optimization        ║
║    Dustline Agro | P1 B3 | S7774   ║  ║    Inspect and adjust solar…       ║
║ 2. Zoya Kade                       ║  ║ 2. Spring Water Collection         ║
║    Ares Systems | P1 B4 | S7725    ║  ║    Deploy portable drills and…     ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6414         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is at a peak; all…        ║
║ ENERGY    1160                     ║  ║ Helios… -> Marco… | Potential      ║
║ FOOD      2200                     ║  ║ water pockets spotted…             ║
║ MATERIALS 950                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 63, Mars experiences a      ║  ║ 00:23 | AI directive: Solar…       ║
║ notable solar energy surge,        ║  ║ 00:23 | A massive solar flare…     ║
║ increasing energy generation       ║  ║ 06:45 | Martian day 63 has begun   ║
║ potential across colonies. Early   ║  ║ 00:25 | AI directive: Unexpected…  ║
║ spring conditions offer            ║  ║ 12:30 | On Sol 62, team members…   ║
║ opportunities for water extraction ║  ╚════════════════════════════════════╝
║ from subsurface ice pockets.       ║                                        
║ Colonies are encouraged to         ║                                        
║ optimize solar infrastructure and  ║                                        
║ prepare fo…                        ║                                        
║ A massive solar flare increases    ║                                        
║ energy levels by 50% for the next  ║                                        
║ cycle. All personnel must seek     ║                                        
║ radiation shelter immediately.     ║                                        
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
