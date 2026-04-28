## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-28T00:27:13.721844_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 35 | [SEASON] Early      ║  ║ Ongoing Dust Storm Limits Solar    ║
║ Spring                             ║  ║ Efficiency                         ║
║ [TEMP] -31C | [SUN] 100% | [STORM] ║  ║ The persistent dust storm          ║
║ YES                                ║  ║ continues to reduce solar panel    ║
║ [EVENT] Trading Ship Arrives Amid  ║  ║ output despite peak solar          ║
║ Dust Storm                         ║  ║ activity, straining energy         ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ reserves.                          ║
║ [O2] 1000 | [H2O] 545 | [E] 1100   ║  ║ EFFECT energy_surge | energy +20   ║
║ [FOOD] 1000 | [MAT] 350            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Ongoing Dust Storm Limits     ║                                        
║ Solar Efficiency | energy +20      ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Energy Optimization  ║
║    Dustline Agro | P1 B3 | S3621   ║  ║    Reduce nonessential energy use… ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recovery from…            ║
║    Ares Systems | P1 B4 | S3271    ║  ║    Deploy and maintain…            ║
║ 3. Irina Vale                      ║  ║ 3. Oxygen Recycling System…        ║
║    Helios… | P1 B2 | S2627         ║  ║    Inspect and repair oxygen…      ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ expected to persist…               ║
║ ENERGY    1100                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      1000                     ║  ║ assistance with oxygen…            ║
║ MATERIALS 350                      ║  ║ Ares Systems -> all… | Sharing     ║
╚════════════════════════════════════╝  ║ updated protocols for…             ║
                                        ╚════════════════════════════════════╝

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 35 on Mars sees a persistent   ║  ║ 00:27 | AI directive: Ongoing      ║
║ dust storm continuing to hamper    ║  ║ Dust…                              ║
║ solar energy production despite    ║  ║ 00:27 | On Sol 35, despite active… ║
║ peak solar activity. Colonies face ║  ║ 12:29 | Despite the ongoing dust…  ║
║ challenges in maintaining energy   ║  ║ 06:50 | 🌪️ Dust storm damaged…     ║
║ and water supplies, prompting      ║  ║ 06:50 | Martian day 35 has begun   ║
║ urgent missions focused on         ║  ╚════════════════════════════════════╝
║ optimization and resource          ║                                        
║ harvesting. Communication betwe…   ║                                        
║ On Sol 35, despite active dust     ║                                        
║ storm and -31C temperatures, the   ║                                        
║ Earth trading ship docked          ║                                        
║ successfully, delivering +100 food ║                                        
║ and +50 materials to the colony    ║                                        
║ reserves.                          ║                                        
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
