## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-31T00:26:58.427327_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 73 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 73 opens with thin margins,    ║
║ [TEMP] -43C | [SUN] 0% | [STORM]   ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] A wall of dust is crossing ║  ║ before the next weather swing.     ║
║ the grid                           ║  ║ EFFECT oxygen_leak | oxygen -52    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 948 | [H2O] 545 | [E] 1200    ║                                        
║ [FOOD] 2600 | [MAT] 1150           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | oxygen -52                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Patch the thermal grid          ║
║    Dustline Agro | P1 B3 | S9483   ║  ║    Repair or reinforce one weak…   ║
║ 2. Zoya Kade                       ║  ║ 2. Secure ridge ice cores          ║
║    Ares Systems | P1 B4 | S9228    ║  ║    Bring back intact samples…      ║
║ 3. Irina Vale                      ║  ║ 3. Recover a silent beacon         ║
║    Helios… | P1 B2 | S7587         ║  ║    Reach the site, recover…        ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     545                      ║  ║ reports short and your…            ║
║ ENERGY    1200                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2600                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1150                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 73 begins in Early Spring with ║  ║ 00:26 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:26 | Operations shift to storm… ║
║ holds near -43C, solar activity    ║  ║ 12:32 | A significant solar flare… ║
║ sits at 0%, and the current        ║  ║ 06:50 | Martian day 73 has begun   ║
║ leaders are Marco Quinn:9353, Zoya ║  ║ 00:24 | AI directive: Solar…       ║
║ Kade:9140, Irina Vale:7508.        ║  ╚════════════════════════════════════╝
║ Operations shift to storm posture  ║                                        
║ until visibility returns: 🌪️       ║                                        
║ MASSIVE SANDSTORM!; All solar      ║                                        
║ panels offline for 6 hours.        ║                                        
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
