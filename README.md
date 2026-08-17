## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-17T00:46:30.050396_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 82 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 82 opens with thin margins,    ║
║ [TEMP] -43C | [SUN] 0% | [STORM]   ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] Research teams report a    ║  ║ before the next weather swing.     ║
║ discovery worth a second look      ║  ║ EFFECT cold_snap | temperature -3  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 948 | [H2O] 652 | [E] 1248    ║                                        
║ [FOOD] 2729 | [MAT] 1211           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | temperature -3            ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Secure ridge ice cores          ║
║    Dustline Agro | P1 B3 | S10595  ║  ║    Bring back intact samples…      ║
║ 2. Zoya Kade                       ║  ║ 2. Recover a silent beacon         ║
║    Ares Systems | P1 B4 | S10538   ║  ║    Reach the site, recover…        ║
║ 3. Irina Vale                      ║  ║ 3. Patch the thermal grid          ║
║    Helios… | P1 B2 | S8649         ║  ║    Repair or reinforce one weak…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1248                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2729                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1211                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 82 begins in Early Spring with ║  ║ 00:46 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:46 | Science crews are locking… ║
║ holds near -40C, solar activity    ║  ║ 12:21 | Operations shift to storm… ║
║ sits at 0%, and the current        ║  ║ 06:25 | Martian day 82 has begun   ║
║ leaders are Marco Quinn:10591,     ║  ║ 00:49 | AI directive: Operations…  ║
║ Zoya Kade:10516, Irina Vale:8636.  ║  ╚════════════════════════════════════╝
║ Science crews are locking the site ║                                        
║ down for analysis: 🛸 Ancient       ║                                        
║ ruins... or just rocks?.           ║                                        
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
