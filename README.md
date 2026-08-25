## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-25T00:47:37.013166_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 90 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 90 opens with thin margins,    ║
║ [TEMP] -51C | [SUN] 150% | [STORM] ║  ║ nervous operators, and one narrow  ║
║ NO                                 ║  ║ chance to shift the colony balance ║
║ [EVENT] Radiation monitors spike   ║  ║ before the next weather swing.     ║
║ as the sun lashes the colony       ║  ║ EFFECT energy_surge | energy +62   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 891 | [H2O] 652 | [E] 1389    ║                                        
║ [FOOD] 3029 | [MAT] 1385           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | energy +62                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Secure ridge ice cores          ║
║    Dustline Agro | P1 B3 | S11347  ║  ║    Bring back intact samples…      ║
║ 2. Zoya Kade                       ║  ║ 2. Patch the thermal grid          ║
║    Ares Systems | P1 B4 | S11228   ║  ║    Repair or reinforce one weak…   ║
║ 3. Irina Vale                      ║  ║ 3. Recover a silent beacon         ║
║    Helios… | P1 B2 | S9279         ║  ║    Reach the site, recover…        ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    891                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1389                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      3029                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1385                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 90 begins in Early Spring with ║  ║ 00:47 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:47 | Power teams are balancing… ║
║ holds near -51C, solar activity    ║  ║ 12:31 | Cargo handlers move fast…  ║
║ sits at 150%, and the current      ║  ║ 06:39 | Martian day 90 has begun   ║
║ leaders are Marco Quinn:11254,     ║  ║ 00:48 | AI directive: Operations…  ║
║ Zoya Kade:11177, Irina Vale:9237.  ║  ╚════════════════════════════════════╝
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
