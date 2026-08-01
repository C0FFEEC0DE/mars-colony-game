## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-01T00:25:48.697986_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 74 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 74 opens with thin margins,    ║
║ [TEMP] -36C | [SUN] 0% | [STORM]   ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] A fresh ice seam opens     ║  ║ before the next weather swing.     ║
║ beneath the regolith               ║  ║ EFFECT materials_find | materials  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ +11                                ║
║ [O2] 948 | [H2O] 545 | [E] 1200    ║  ╚════════════════════════════════════╝
║ [FOOD] 2600 | [MAT] 1161           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | materials +11             ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Secure ridge ice cores          ║
║    Dustline Agro | P1 B3 | S9565   ║  ║    Bring back intact samples…      ║
║ 2. Zoya Kade                       ║  ║ 2. Recover a silent beacon         ║
║    Ares Systems | P1 B4 | S9338    ║  ║    Reach the site, recover…        ║
║ 3. Irina Vale                      ║  ║ 3. Patch the thermal grid          ║
║    Helios… | P1 B2 | S7681         ║  ║    Repair or reinforce one weak…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     545                      ║  ║ reports short and your…            ║
║ ENERGY    1200                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2600                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1161                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 74 begins in Early Spring with ║  ║ 00:25 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:25 | Extraction crews are…      ║
║ holds near -36C, solar activity    ║  ║ 12:36 | Operations shift to storm… ║
║ sits at 0%, and the current        ║  ║ 06:56 | Martian day 74 has begun   ║
║ leaders are Marco Quinn:9500, Zoya ║  ║ 00:26 | AI directive: Operations…  ║
║ Kade:9231, Irina Vale:7587.        ║  ╚════════════════════════════════════╝
║ Extraction crews are rerouting     ║                                        
║ drills immediately: 💧 UNDERGROUND  ║                                        
║ ICE DISCOVERED!; Marco Quinn       ║                                        
║ received +31 water; Zoya Kade      ║                                        
║ received +43 water; Irina Vale     ║                                        
║ received +41 water.                ║                                        
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
