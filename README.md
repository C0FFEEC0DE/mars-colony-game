## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-24T00:48:19.968922_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 89 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 89 opens with thin margins,    ║
║ [TEMP] -31C | [SUN] 79% | [STORM]  ║  ║ nervous operators, and one narrow  ║
║ NO                                 ║  ║ chance to shift the colony balance ║
║ [EVENT] A fresh ice seam opens     ║  ║ before the next weather swing.     ║
║ beneath the regolith               ║  ║ EFFECT energy_surge | energy +52   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 891 | [H2O] 652 | [E] 1327    ║                                        
║ [FOOD] 2929 | [MAT] 1335           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | energy +52                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Recover a silent beacon         ║
║    Dustline Agro | P1 B3 | S11222  ║  ║    Reach the site, recover…        ║
║ 2. Zoya Kade                       ║  ║ 2. Secure ridge ice cores          ║
║    Ares Systems | P1 B4 | S11159   ║  ║    Bring back intact samples…      ║
║ 3. Irina Vale                      ║  ║ 3. Patch the thermal grid          ║
║    Helios… | P1 B2 | S9222         ║  ║    Repair or reinforce one weak…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    891                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1327                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2929                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1335                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 89 begins in Early Spring with ║  ║ 00:48 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:48 | Extraction crews are…      ║
║ holds near -31C, solar activity    ║  ║ 06:26 | Martian day 89 has begun   ║
║ sits at 79%, and the current       ║  ║ 00:51 | AI directive: Operations…  ║
║ leaders are Marco Quinn:11098,     ║  ║ 00:51 | Cargo handlers move fast…  ║
║ Zoya Kade:11057, Irina Vale:9107.  ║  ╚════════════════════════════════════╝
║ Extraction crews are rerouting     ║                                        
║ drills immediately: 💧 UNDERGROUND  ║                                        
║ ICE DISCOVERED!; Irina Vale        ║                                        
║ received +35 water; Zoya Kade      ║                                        
║ received +24 water; Marco Quinn    ║                                        
║ received +44 water.                ║                                        
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
