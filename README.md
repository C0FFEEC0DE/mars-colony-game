## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-08-23T00:51:08.669218_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 88 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 88 opens with thin margins,    ║
║ [TEMP] -43C | [SUN] 92% | [STORM]  ║  ║ nervous operators, and one narrow  ║
║ NO                                 ║  ║ chance to shift the colony balance ║
║ [EVENT] An orbital trader opens an ║  ║ before the next weather swing.     ║
║ unexpected supply window           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +8                  ║
║ [O2] 891 | [H2O] 652 | [E] 1275    ║  ╚════════════════════════════════════╝
║ [FOOD] 2929 | [MAT] 1335           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | solar_activity +8         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Patch the thermal grid          ║
║    Dustline Agro | P1 B3 | S11083  ║  ║    Repair or reinforce one weak…   ║
║ 2. Zoya Kade                       ║  ║ 2. Secure ridge ice cores          ║
║    Ares Systems | P1 B4 | S11036   ║  ║    Bring back intact samples…      ║
║ 3. Irina Vale                      ║  ║ 3. Recover a silent beacon         ║
║    Helios… | P1 B2 | S9089         ║  ║    Reach the site, recover…        ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    891                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1275                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      2929                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1335                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 88 begins in Early Spring with ║  ║ 00:51 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:51 | Cargo handlers move fast…  ║
║ holds near -43C, solar activity    ║  ║ 06:24 | Martian day 88 has begun   ║
║ sits at 84%, and the current       ║  ║ 00:45 | AI directive: Operations…  ║
║ leaders are Marco Quinn:11044,     ║  ║ 12:29 | Cargo handlers move fast…  ║
║ Zoya Kade:10979, Irina Vale:9041.  ║  ╚════════════════════════════════════╝
║ Cargo handlers move fast before    ║                                        
║ the burn window closes: 🛸 TRADING  ║                                        
║ SHIP FROM EARTH!; Food +100 to     ║                                        
║ global pool; Materials +50 to      ║                                        
║ global pool.                       ║                                        
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
