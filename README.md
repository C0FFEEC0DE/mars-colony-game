## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-16T00:49:20.763737_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 81 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 81 opens with thin margins,    ║
║ [TEMP] -62C | [SUN] 150% | [STORM] ║  ║ nervous operators, and one narrow  ║
║ NO                                 ║  ║ chance to shift the colony balance ║
║ [EVENT] Radiation monitors spike   ║  ║ before the next weather swing.     ║
║ as the sun lashes the colony       ║  ║ EFFECT water_cache | water +107    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 948 | [H2O] 652 | [E] 1248    ║                                        
║ [FOOD] 2729 | [MAT] 1211           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | water +107                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Patch the thermal grid          ║
║    Dustline Agro | P1 B3 | S10564  ║  ║    Repair or reinforce one weak…   ║
║ 2. Zoya Kade                       ║  ║ 2. Recover a silent beacon         ║
║    Ares Systems | P1 B4 | S10483   ║  ║    Reach the site, recover…        ║
║ 3. Irina Vale                      ║  ║ 3. Secure ridge ice cores          ║
║    Helios… | P1 B2 | S8606         ║  ║    Bring back intact samples…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    948                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1248                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2729                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1211                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 81 begins in Early Spring with ║  ║ 00:49 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 12:20 | Power teams are balancing… ║
║ holds near -62C, solar activity    ║  ║ 06:22 | Martian day 81 has begun   ║
║ sits at 150%, and the current      ║  ║ 00:46 | AI directive: Operations…  ║
║ leaders are Marco Quinn:10494,     ║  ║ 12:45 | Power teams are balancing… ║
║ Zoya Kade:10395, Irina Vale:8527.  ║  ╚════════════════════════════════════╝
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
