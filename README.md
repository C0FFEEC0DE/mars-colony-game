## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-11-03T00:13:57.492429_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 94 | [SEASON] Early      ║  ║ Operations drift into a new rhythm ║
║ Spring                             ║  ║ Sol 94 opens with thin margins,    ║
║ [TEMP] -57C | [SUN] 64% | [STORM]  ║  ║ nervous operators, and one narrow  ║
║ NO                                 ║  ║ chance to shift the colony balance ║
║ [EVENT] An orbital trader opens an ║  ║ before the next weather swing.     ║
║ unexpected supply window           ║  ║ EFFECT food_relief | food +45      ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 891 | [H2O] 652 | [E] 1389    ║                                        
║ [FOOD] 3174 | [MAT] 1435           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Operations drift into a new   ║                                        
║ rhythm | food +45                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Recover a silent beacon         ║
║    Ares Systems | P1 B4 | S12675   ║  ║    Reach the site, recover…        ║
║ 2. Marco Quinn                     ║  ║ 2. Secure ridge ice cores          ║
║    Dustline Agro | P1 B3 | S11874  ║  ║    Bring back intact samples…      ║
║ 3. Irina Vale                      ║  ║ 3. Patch the thermal grid          ║
║    Helios… | P1 B2 | S10258        ║  ║    Repair or reinforce one weak…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    891                      ║  ║ Mars Control -> All… | Keep your   ║
║ WATER     652                      ║  ║ reports short and your…            ║
║ ENERGY    1389                     ║  ║ Orbital Relay -> Irina Vale | Your ║
║ FOOD      3174                     ║  ║ telemetry is the cleanest on…      ║
║ MATERIALS 1435                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 94 begins in Early Spring with ║  ║ 00:13 | AI directive: Operations…  ║
║ 3 active colonies. Temperature     ║  ║ 00:13 | Cargo handlers move fast…  ║
║ holds near -57C, solar activity    ║  ║ 12:01 | Salvage teams report a…    ║
║ sits at 64%, and the current       ║  ║ 06:08 | Martian day 94 has begun   ║
║ leaders are Zoya Kade:11435, Marco ║  ║ 12:20 | Extraction crews are…      ║
║ Quinn:11190, Irina Vale:9346.      ║  ╚════════════════════════════════════╝
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
