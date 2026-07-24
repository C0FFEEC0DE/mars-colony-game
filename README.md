## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-24T00:23:51.243921_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 68 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ A moderate solar flare has         ║
║ [TEMP] -79C | [SUN] 73% | [STORM]  ║  ║ increased solar panel efficiency   ║
║ NO                                 ║  ║ across Mars, providing a temporary ║
║ [EVENT] Earth Traders Deliver      ║  ║ energy surge.                      ║
║ Vital Supplies                     ║  ║ EFFECT energy_surge | energy +20   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1200   ║                                        
║ [FOOD] 2500 | [MAT] 1100           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | energy +20                ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Optimize Solar Arrays           ║
║    Ares Systems | P1 B4 | S8291    ║  ║    Adjust and fine-tune solar…     ║
║ 2. Marco Quinn                     ║  ║ 2. Water System Maintenance        ║
║    Dustline Agro | P1 B3 | S8257   ║  ║    Conduct routine checks and…     ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6815         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ detected increasing…               ║
║ ENERGY    1200                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      2500                     ║  ║ additional materials…              ║
║ MATERIALS 1100                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 68, Mars experiences a      ║  ║ 00:23 | AI directive: Solar Flare… ║
║ beneficial solar flare enhancing   ║  ║ 12:31 | A trading ship from Earth… ║
║ energy production. Colonies are    ║  ║ 06:48 | Martian day 68 has begun   ║
║ advised to optimize solar arrays   ║  ║ 00:26 | AI directive: Mild Solar…  ║
║ to capitalize on the surge.        ║  ║ 00:25 | Sensors have identified…   ║
║ Meanwhile, early spring's cold     ║  ╚════════════════════════════════════╝
║ temperatures necessitate careful   ║                                        
║ maintenance of water systems to    ║                                        
║ ensure stable supplies.            ║                                        
║ A trading ship from Earth has      ║                                        
║ docked, boosting our global food   ║                                        
║ reserves by 100 units and          ║                                        
║ materials by 50 units. This influx ║                                        
║ supports ongoing colony            ║                                        
║ sustainability efforts.            ║                                        
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
