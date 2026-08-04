## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-03T00:27:04.152136_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 76 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 76 opens with thin margins,    ║
║ [TEMP] -57C | [SUN] 150% | [STORM] ║  ║ nervous operators, and one narrow  ║
║ YES                                ║  ║ chance to shift the colony balance ║
║ [EVENT] Radiation monitors spike   ║  ║ before the next weather swing.     ║
║ as the sun lashes the colony       ║  ║ EFFECT energy_surge | energy +48   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 948 | [H2O] 545 | [E] 1248    ║                                        
║ [FOOD] 2600 | [MAT] 1161           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | energy +48                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Recover a silent beacon         ║
║    Dustline Agro | P1 B3 | S9704   ║  ║    Reach the site, recover…        ║
║ 2. Zoya Kade                       ║  ║ 2. Patch the thermal grid          ║
║    Ares Systems | P1 B4 | S9429    ║  ║    Repair or reinforce one weak…   ║
║ 3. Irina Vale                      ║  ║ 3. Secure ridge ice cores          ║
║    Helios… | P1 B2 | S7736         ║  ║    Bring back intact samples…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     545                      ║  ║ reports short and your…            ║
║ ENERGY    1248                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2600                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1161                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 76 begins in Early Spring with ║  ║ 00:26 | Power teams are balancing… ║
║ 3 active colonies. Temperature     ║  ║ 00:27 | AI directive: Operations…  ║
║ holds near -57C, solar activity    ║  ║ 12:20 | Operations shift to storm… ║
║ sits at 0%, and the current        ║  ║ 06:51 | Martian day 76 has begun   ║
║ leaders are Marco Quinn:9686, Zoya ║  ║ 00:27 | AI directive: Operations…  ║
║ Kade:9389, Irina Vale:7717.        ║  ╚════════════════════════════════════╝
║ Power teams are balancing the      ║                                        
║ surge while shelters stay sealed:  ║                                        
║ ⚡ MASSIVE SOLAR FLARE!; Energy     ║                                        
║ +50% for next turn; Take cover     ║                                        
║ from radiation.                    ║                                        
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
