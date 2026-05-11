## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-11T00:29:19.148754_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 48 | [SEASON] Early      ║  ║ Solar Flare Boosts Energy Output   ║
║ Spring                             ║  ║ Solar activity has surged to 150%, ║
║ [TEMP] -55C | [SUN] 150% | [STORM] ║  ║ increasing potential energy        ║
║ NO                                 ║  ║ generation across all colonies.    ║
║ [EVENT] Meteor Shower Impacts      ║  ║ EFFECT solar_boost |               ║
║ Colony Structures                  ║  ║ solar_activity +0                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║                                        
║ [FOOD] 1200 | [MAT] 450            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Flare Boosts Energy     ║                                        
║ Output | solar_activity +0         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Maximize Solar Array…           ║
║    Dustline Agro | P1 B3 | S4824   ║  ║    Perform maintenance and…        ║
║ 2. Zoya Kade                       ║  ║ 2. Secure Water Reserves from…     ║
║    Ares Systems | P1 B4 | S4493    ║  ║    Deploy excavation equipment to… ║
║ 3. Irina Vale                      ║  ║ 3. Repair Oxygen Recycling…        ║
║    Helios… | P1 B2 | S3641         ║  ║    Inspect and repair oxygen…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity at 150% has…              ║
║ ENERGY    1120                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      1200                     ║  ║ promising…                         ║
║ MATERIALS 450                      ║  ║ Ares Systems -> all… | Reminder:   ║
╚════════════════════════════════════╝  ║ early spring conditions…           ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 48 of early spring, Mars    ║  ║ 00:29 | AI directive: Solar Flare… ║
║ experiences a solar activity surge ║  ║ 00:29 | On Sol 48, a meteor        ║
║ enhancing energy generation        ║  ║ shower…                            ║
║ potential. Colonies are advised to ║  ║ 12:16 | A solar flare has          ║
║ optimize solar arrays and secure   ║  ║ increased…                         ║
║ additional water supplies from     ║  ║ 06:53 | Martian day 48 has begun   ║
║ subsurface ice. Oxygen recycling   ║  ║ 00:28 | AI directive: Solar…       ║
║ system maintenance remains a       ║  ╚════════════════════════════════════╝
║ priority to prevent sho…           ║                                        
║ On Sol 48, a meteor shower caused  ║                                        
║ minor building damage reported by  ║                                        
║ Irina Vale. No dust storm present; ║                                        
║ temperature steady at -55C with    ║                                        
║ elevated solar activity at 150%.   ║                                        
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
