## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-07T00:19:30.234090_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 14 | [SEASON] Early      ║  ║ Early Spring Solar Boost           ║
║ Spring                             ║  ║ Solar activity has increased to    ║
║ [TEMP] -52C | [SUN] 65% | [STORM]  ║  ║ 60%, providing a moderate energy   ║
║ NO                                 ║  ║ surge for all colonies.            ║
║ [EVENT] Meteor Shower Strikes      ║  ║ EFFECT solar_boost |               ║
║ Colony                             ║  ║ solar_activity +5                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ╚════════════════════════════════════╝
║ [O2] 1000 | [H2O] 545 | [E] 1020   ║                                        
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Early Spring Solar Boost |    ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S2059   ║  ║    Recalibrate and clean solar…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Drill        ║
║    Ares Systems | P1 B4 | S1818    ║  ║    Implement water-saving…         ║
║ 3. Irina Vale                      ║  ║ 3. Spring Crop Planning            ║
║    Helios… | P1 B2 | S1293         ║  ║    Set up hydroponic beds and…     ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is currently…             ║
║ ENERGY    1020                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      400                      ║  ║ stable water…                      ║
║ MATERIALS 50                       ║  ║ Ares Systems -> Zoya Kade | Power  ║
╚════════════════════════════════════╝  ║ levels are sufficient but…         ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Early spring on Mars brings a      ║  ║ 00:19 | AI directive: Early        ║
║ moderate solar boost that benefits ║  ║ Spring…                            ║
║ all colonies with increased energy ║  ║ 12:15 | On Sol 14, a meteor        ║
║ potential. Colonies are advised to ║  ║ shower…                            ║
║ maximize solar panel efficiency,   ║  ║ 06:35 | Martian day 14 has begun   ║
║ conserve water resources, and      ║  ║ 00:19 | AI directive: Unexpected…  ║
║ begin early crop planting to       ║  ║ 06:25 | Martian day 13 has begun   ║
║ improve food stocks.               ║  ╚════════════════════════════════════╝
║ Communications between factions…   ║                                        
║ On Sol 14, a meteor shower         ║                                        
║ resulted in +16 materials salvaged ║                                        
║ by Zoya Kade, who also reported    ║                                        
║ structural damage to habitat       ║                                        
║ modules.                           ║                                        
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
