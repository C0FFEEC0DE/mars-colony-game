## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-15T00:24:27.553456_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 22 | [SEASON] Early      ║  ║ Mild Solar Boost Increases Power   ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -66C | [SUN] 81% | [STORM]  ║  ║ Solar activity reaches 76%,        ║
║ NO                                 ║  ║ enhancing energy generation        ║
║ [EVENT] Meteor Shower Boosts       ║  ║ efficiency for all colonies today. ║
║ Resource Recovery                  ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 600 | [MAT] 150             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Boost Increases    ║                                        
║ Power Output | solar_activity +5   ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2661   ║  ║    Recalibrate solar arrays to…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S2396    ║  ║    Implement stricter water usage… ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1800         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is expected to…           ║
║ ENERGY    1040                     ║  ║ Helios… -> Irina Vale | New        ║
║ FOOD      600                      ║  ║ prospecting data suggests…         ║
║ MATERIALS 150                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 22 on Mars enters early spring ║  ║ 00:24 | AI directive: Mild Solar…  ║
║ with temperatures at -66C and no   ║  ║ 00:24 | On Sol 22, a meteor        ║
║ dust storms active. Solar activity ║  ║ shower…                            ║
║ increases energy availability      ║  ║ 12:19 | A trading vessel from      ║
║ across colonies, prompting         ║  ║ Earth…                             ║
║ missions to optimize solar arrays  ║  ║ 06:35 | Martian day 22 has begun   ║
║ and conserve water. Colonists      ║  ║ 00:24 | AI directive: Persistent…  ║
║ remain vigilant as resources       ║  ╚════════════════════════════════════╝
║ balance remains stable.            ║                                        
║ On Sol 22, a meteor shower enabled ║                                        
║ Irina Vale and Marco Quinn to      ║                                        
║ salvage 8 and 19 additional        ║                                        
║ materials respectively, enhancing  ║                                        
║ our resource stockpile amid stable ║                                        
║ conditions.                        ║                                        
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
