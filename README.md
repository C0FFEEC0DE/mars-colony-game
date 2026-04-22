## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-22T00:20:50.577388_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 29 | [SEASON] Early      ║  ║ Mild Solar Boost Enhances Energy   ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -47C | [SUN] 77% | [STORM]  ║  ║ Solar activity remains steady at   ║
║ NO                                 ║  ║ 72%, providing a slight increase   ║
║ [EVENT] None                       ║  ║ in energy generation across all    ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar arrays.                      ║
║ [O2] 1000 | [H2O] 545 | [E] 1060   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 700 | [MAT] 200             ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Mild Solar Boost Enhances     ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panels           ║
║    Dustline Agro | P1 B3 | S3325   ║  ║    Adjust and calibrate solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S2958    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ║ 3. Material Inventory and…         ║
║    Helios… | P1 B2 | S2381         ║  ║    Conduct a materials audit and…  ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity stable with a mild…       ║
║ ENERGY    1060                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      700                      ║  ║ additional oxygen…                 ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 29 of early spring, Mars    ║  ║ 00:20 | AI directive: Mild Solar…  ║
║ experiences a mild solar boost     ║  ║ 06:35 | Martian day 29 has begun   ║
║ enhancing energy production.       ║  ║ 00:23 | AI directive: Mild Solar…  ║
║ Colonies focus on optimizing solar ║  ║ 12:22 | During Sol 28's meteor…    ║
║ panels and maintaining water       ║  ║ 06:42 | Martian day 28 has begun   ║
║ recycling systems to conserve      ║  ╚════════════════════════════════════╝
║ resources. Oxygen shortages are    ║                                        
║ reported at Helios Prospecting,    ║                                        
║ highlighting the ongoing chal…     ║                                        
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
