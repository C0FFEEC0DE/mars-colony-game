## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-20T00:45:26.313579_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 85 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 85 opens with thin margins,    ║
║ [TEMP] -67C | [SUN] 0% | [STORM]   ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] A wall of dust is crossing ║  ║ before the next weather swing.     ║
║ the grid                           ║  ║ EFFECT oxygen_leak | oxygen -57    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 891 | [H2O] 652 | [E] 1275    ║                                        
║ [FOOD] 2729 | [MAT] 1211           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | oxygen -57                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Recover a silent beacon         ║
║    Dustline Agro | P1 B3 | S10925  ║  ║    Reach the site, recover…        ║
║ 2. Zoya Kade                       ║  ║ 2. Patch the thermal grid          ║
║    Ares Systems | P1 B4 | S10806   ║  ║    Repair or reinforce one weak…   ║
║ 3. Irina Vale                      ║  ║ 3. Secure ridge ice cores          ║
║    Helios… | P1 B2 | S8895         ║  ║    Bring back intact samples…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    891                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1275                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2729                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1211                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 85 begins in Early Spring with ║  ║ 00:45 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 12:28 | Operations shift to storm… ║
║ holds near -67C, solar activity    ║  ║ 06:29 | Martian day 85 has begun   ║
║ sits at 0%, and the current        ║  ║ 00:45 | AI directive: Operations…  ║
║ leaders are Marco Quinn:10897,     ║  ║ 00:45 | Science crews are locking… ║
║ Zoya Kade:10780, Irina Vale:8878.  ║  ╚════════════════════════════════════╝
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
