## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-15T00:30:18.542802_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 51 | [SEASON] Early      ║  ║ Mild Solar Boost Enhances Energy   ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -58C | [SUN] 86% | [STORM]  ║  ║ Solar activity remains high at     ║
║ NO                                 ║  ║ 81%, providing a modest increase   ║
║ [EVENT] Sol 51 Meteor Shower       ║  ║ in energy generation across        ║
║ Yields Critical Salvage            ║  ║ colonies.                          ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ║ solar_activity +5                  ║
║ [FOOD] 1200 | [MAT] 450            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Boost Enhances     ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S5602   ║  ║    Adjust and clean solar panels…  ║
║ 2. Zoya Kade                       ║  ║ 2. Check Oxygen Recycling Systems  ║
║    Ares Systems | P1 B4 | S5063    ║  ║    Inspect and repair oxygen…      ║
║ 3. Irina Vale                      ║  ║ 3. Water Conservation Protocol     ║
║    Helios… | P1 B2 | S4315         ║  ║    Deploy water-saving technology… ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is favorable;…            ║
║ ENERGY    1120                     ║  ║ Helios… -> Irina Vale | Urgent:    ║
║ FOOD      1200                     ║  ║ Oxygen reserves…                   ║
║ MATERIALS 450                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 51, Mars colonies benefit   ║  ║ 00:30 | AI directive: Mild Solar…  ║
║ from a mild solar boost, improving ║  ║ 12:34 | A meteor shower passed…    ║
║ energy generation. Early spring    ║  ║ 06:58 | Martian day 51 has begun   ║
║ temperatures remain frigid at      ║  ║ 00:32 | AI directive: Moderate…    ║
║ -58C, but no dust storms are       ║  ║ 12:40 | On Sol 50, analysis        ║
║ present. Attention focuses on      ║  ║ reveals…                           ║
║ oxygen recycling and water         ║  ╚════════════════════════════════════╝
║ conservation as resource levels    ║                                        
║ vary across colonies.              ║                                        
║ A meteor shower passed overhead    ║                                        
║ with solar activity at 81%. Irina  ║                                        
║ Vale successfully salvaged 20      ║                                        
║ units of materials during the      ║                                        
║ event. Temperature steady at -58C; ║                                        
║ no dust storm detected.            ║                                        
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
