## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-10T00:19:04.203200_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 17 | [SEASON] Early      ║  ║ Solar Activity Peaks at 150%       ║
║ Spring                             ║  ║ The solar activity on Sol 17 has   ║
║ [TEMP] -80C | [SUN] 150% | [STORM] ║  ║ surged to 150%, increasing energy  ║
║ NO                                 ║  ║ generation potential across all    ║
║ [EVENT] Massive Solar Flare        ║  ║ colonies.                          ║
║ Detected                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks at 150%  ║                                        
║ | solar_activity +0                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2323   ║  ║    Upgrade and calibrate solar…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S2073    ║  ║    Implement water-saving…         ║
║ 3. Irina Vale                      ║  ║ 3. Prospect for Materials in…      ║
║    Helios… | P1 B2 | S1497         ║  ║    Send a scouting party to…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ activity is at an…                 ║
║ ENERGY    1040                     ║  ║ Helios… -> all… | We have located  ║
║ FOOD      400                      ║  ║ promising mineral…                 ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 17 of early spring, Mars    ║  ║ 00:19 | AI directive: Solar…       ║
║ experiences a solar activity surge ║  ║ 00:18 | A massive solar flare is…  ║
║ at 150%, enhancing energy          ║  ║ 12:18 | A massive solar flare is…  ║
║ generation opportunities. Colonies ║  ║ 06:31 | Martian day 17 has begun   ║
║ focus on maximizing solar power    ║  ║ 00:16 | AI directive: Solar…       ║
║ while conserving water amid low    ║  ╚════════════════════════════════════╝
║ temperatures. Exploration for      ║                                        
║ materials in accessible rocky      ║                                        
║ areas is underway to suppor…       ║                                        
║ A massive solar flare is impacting ║                                        
║ Mars with 150% solar activity.     ║                                        
║ Increase radiation shielding       ║                                        
║ protocols and limit EVA exposure   ║                                        
║ during the next cycle.             ║                                        
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
