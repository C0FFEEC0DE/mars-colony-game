## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-08T00:27:51.651470_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 45 | [SEASON] Early      ║  ║ Solar Output Peaks Early Spring    ║
║ Spring                             ║  ║ Solar activity has surged to 150%, ║
║ [TEMP] -64C | [SUN] 150% | [STORM] ║  ║ increasing energy availability     ║
║ NO                                 ║  ║ across the colony network.         ║
║ [EVENT] Massive Solar Flare        ║  ║ EFFECT solar_boost |               ║
║ Detected                           ║  ║ solar_activity +0                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║                                        
║ [FOOD] 1100 | [MAT] 400            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Output Peaks Early      ║                                        
║ Spring | solar_activity +0         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Expand Solar Array Capacity     ║
║    Dustline Agro | P1 B3 | S4503   ║  ║    Construct additional solar…     ║
║ 2. Zoya Kade                       ║  ║ 2. Inspect Water Reservoir…        ║
║    Ares Systems | P1 B4 | S4220    ║  ║    Perform a full inspection and…  ║
║ 3. Irina Vale                      ║  ║ 3. Optimize Oxygen Recycling…      ║
║    Helios… | P1 B2 | S3404         ║  ║    Upgrade oxygen recycling…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is at a seasonal…         ║
║ ENERGY    1120                     ║  ║ Ares Systems -> Zoya Kade |        ║
║ FOOD      1100                     ║  ║ Support available for upgrading…   ║
║ MATERIALS 400                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 45 in early Martian spring, ║  ║ 00:27 | AI directive: Solar        ║
║ solar activity reached 150%,       ║  ║ Output…                            ║
║ providing a natural energy boost   ║  ║ 00:27 | A significant solar flare… ║
║ to all colonies. Temperatures      ║  ║ 12:35 | Geological survey reports… ║
║ remain low at -64C, requiring      ║  ║ 06:57 | Martian day 45 has begun   ║
║ careful resource management.       ║  ║ 00:27 | AI directive: Persistent…  ║
║ Colonies are focusing on expanding ║  ╚════════════════════════════════════╝
║ energy infrastructure and securing ║                                        
║ water and oxygen suppli…           ║                                        
║ A significant solar flare has been ║                                        
║ recorded, increasing energy levels ║                                        
║ by 50% for the next cycle. All     ║                                        
║ personnel should take necessary    ║                                        
║ radiation shielding precautions.   ║                                        
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
