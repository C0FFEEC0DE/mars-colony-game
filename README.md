## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-22T00:24:21.446712_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 66 | [SEASON] Early      ║  ║ Solar Activity Peaks               ║
║ Spring                             ║  ║ Solar radiation levels have surged ║
║ [TEMP] -41C | [SUN] 150% | [STORM] ║  ║ to 150%, enhancing energy          ║
║ NO                                 ║  ║ generation potential across Mars   ║
║ [EVENT] Underground Ice Deposit    ║  ║ colonies.                          ║
║ Secured                            ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +0                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1180   ║  ╚════════════════════════════════════╝
║ [FOOD] 2400 | [MAT] 1050           ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Peaks |        ║                                        
║ solar_activity +0                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Zoya Kade                       ║  ║ 1. Optimize Solar Arrays           ║
║    Ares Systems | P1 B4 | S8020    ║  ║    Adjust and optimize solar…      ║
║ 2. Marco Quinn                     ║  ║ 2. Water Reserve Maintenance       ║
║    Dustline Agro | P1 B3 | S7908   ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6614         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar flare ║
║ WATER     545                      ║  ║ alert: Take advantage…             ║
║ ENERGY    1180                     ║  ║ Helios… -> Marco… | Helios         ║
║ FOOD      2400                     ║  ║ suggests coordinating…             ║
║ MATERIALS 1050                     ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 66, Mars experiences a      ║  ║ 00:24 | AI directive: Solar…       ║
║ significant solar activity         ║  ║ 00:24 | On Sol 66, the team…       ║
║ increase, providing colonies with  ║  ║ 12:31 | A massive solar flare has… ║
║ an opportunity to enhance energy   ║  ║ 06:49 | Martian day 66 has begun   ║
║ production. Temperatures remain    ║  ║ 12:41 | On Sol 65, a trading ship… ║
║ harsh at -41C in early spring,     ║  ╚════════════════════════════════════╝
║ requiring careful maintenance of   ║                                        
║ water reserves. Collaboration      ║                                        
║ among colonies is encouraged…      ║                                        
║ On Sol 66, the team confirmed a    ║                                        
║ new underground ice layer,         ║                                        
║ boosting water reserves by 95      ║                                        
║ units distributed among Kade,      ║                                        
║ Vale, and Quinn.                   ║                                        
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
