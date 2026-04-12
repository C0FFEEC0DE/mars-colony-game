## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-12T00:20:18.865288_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 19 | [SEASON] Early      ║  ║ Unexpected Solar Boost Increases   ║
║ Spring                             ║  ║ Energy Yield                       ║
║ [TEMP] -68C | [SUN] 150% | [STORM] ║  ║ Solar activity has surged to 150%, ║
║ NO                                 ║  ║ providing a significant energy     ║
║ [EVENT] Massive Solar Flare        ║  ║ bonus for all colonies today.      ║
║ Detected                           ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Unexpected Solar Boost        ║                                        
║ Increases Energy Yield |           ║                                        
║ solar_activity +0                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S2458   ║  ║    Adjust and recalibrate solar…   ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S2216    ║  ║    Perform diagnostics and…        ║
║ 3. Irina Vale                      ║  ║ 3. Scout Nearby Material Deposits  ║
║    Helios… | P1 B2 | S1616         ║  ║    Explore designated zones to…    ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently…             ║
║ ENERGY    1040                     ║  ║ Helios… -> all… | We recommend     ║
║ FOOD      400                      ║  ║ scouting expeditions…              ║
║ MATERIALS 50                       ║  ║ Ares Systems -> all… | Reminder:   ║
╚════════════════════════════════════╝  ║ maintain water…                    ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Early spring on Mars brings a      ║  ║ 00:20 | AI directive: Unexpected…  ║
║ solar energy surge, boosting power ║  ║ 12:08 | Solar activity spiked to…  ║
║ generation across all colonies.    ║  ║ 06:21 | Martian day 19 has begun   ║
║ With temperatures remaining low,   ║  ║ 00:18 | AI directive: Persistent…  ║
║ maintaining water recycling        ║  ║ 12:15 | Sol 18: A severe dust      ║
║ systems is critical to resource    ║  ║ storm…                             ║
║ management. Several colonies       ║  ╚════════════════════════════════════╝
║ prepare scouting missions to       ║                                        
║ locate additional material depo…   ║                                        
║ Solar activity spiked to 150%,     ║                                        
║ triggering a massive flare. All    ║                                        
║ personnel must take immediate      ║                                        
║ radiation shelter; energy output   ║                                        
║ increased by 50% for the next      ║                                        
║ cycle.                             ║                                        
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
