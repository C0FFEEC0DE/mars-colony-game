## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-02T00:27:08.880833_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 75 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 75 opens with thin margins,    ║
║ [TEMP] -34C | [SUN] 26% | [STORM]  ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] A wall of dust is crossing ║  ║ before the next weather swing.     ║
║ the grid                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +26                 ║
║ [O2] 948 | [H2O] 545 | [E] 1200    ║  ╚════════════════════════════════════╝
║ [FOOD] 2600 | [MAT] 1161           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | solar_activity +26        ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Recover a silent beacon         ║
║    Dustline Agro | P1 B3 | S9669   ║  ║    Reach the site, recover…        ║
║ 2. Zoya Kade                       ║  ║ 2. Secure ridge ice cores          ║
║    Ares Systems | P1 B4 | S9386    ║  ║    Bring back intact samples…      ║
║ 3. Irina Vale                      ║  ║ 3. Patch the thermal grid          ║
║    Helios… | P1 B2 | S7717         ║  ║    Repair or reinforce one weak…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     545                      ║  ║ reports short and your…            ║
║ ENERGY    1200                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2600                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1161                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 75 begins in Early Spring with ║  ║ 00:27 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:27 | Operations shift to storm… ║
║ holds near -34C, solar activity    ║  ║ 06:48 | Martian day 75 has begun   ║
║ sits at 0%, and the current        ║  ║ 00:25 | AI directive: Operations…  ║
║ leaders are Marco Quinn:9582, Zoya ║  ║ 00:25 | Extraction crews are…      ║
║ Kade:9341, Irina Vale:7681.        ║  ╚════════════════════════════════════╝
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
