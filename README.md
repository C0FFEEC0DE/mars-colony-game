## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-23T00:26:02.538092_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 67 | [SEASON] Early      ║  ║ Mild Solar Boost Enhances Energy   ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -40C | [SUN] 101% | [STORM] ║  ║ A 96% solar activity level has     ║
║ NO                                 ║  ║ increased available solar energy,  ║
║ [EVENT] Unidentified Structures    ║  ║ providing a modest energy surge    ║
║ Detected Near Equatorial Ridge     ║  ║ for all colonies.                  ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1180   ║  ║ solar_activity +5                  ║
║ [FOOD] 2400 | [MAT] 1050           ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Mild Solar Boost Enhances     ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Optimize Solar Arrays for…      ║
║    Ares Systems | P1 B4 | S8217    ║  ║    Perform maintenance and…        ║
║ 2. Marco Quinn                     ║  ║ 2. Secure Water Reserves Against…  ║
║    Dustline Agro | P1 B3 | S8127   ║  ║    Inspect and reinforce water…    ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6753         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity remains high;…            ║
║ ENERGY    1180                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      2400                     ║  ║ water reserves…                    ║
║ MATERIALS 1050                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars experiences a mild solar      ║  ║ 00:26 | AI directive: Mild Solar…  ║
║ boost on Sol 67 with early spring  ║  ║ 00:25 | Sensors have identified…   ║
║ temperatures around -40C. Colonies ║  ║ 12:31 | On Sol 67, underground     ║
║ are advised to optimize solar      ║  ║ ice…                               ║
║ energy capture and secure water    ║  ║ 06:50 | Martian day 67 has begun   ║
║ storage against seasonal changes.  ║  ║ 00:24 | AI directive: Solar…       ║
║ Resource levels remain stable with ║  ╚════════════════════════════════════╝
║ no active dust storms.             ║                                        
║ Sensors have identified formations ║                                        
║ resembling artificial constructs;  ║                                        
║ analysis ongoing to determine if   ║                                        
║ geological or ancient human        ║                                        
║ activity.                          ║                                        
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
