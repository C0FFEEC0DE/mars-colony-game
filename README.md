## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-11T00:18:01.024695_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 18 | [SEASON] Early      ║  ║ Persistent Dust Storm Limits Solar ║
║ Spring                             ║  ║ Power                              ║
║ [TEMP] -35C | [SUN] 0% | [STORM]   ║  ║ A severe dust storm continues to   ║
║ YES                                ║  ║ blanket the colony, reducing solar ║
║ [EVENT] Massive Sandstorm Shuts    ║  ║ energy generation and straining    ║
║ Down Solar Arrays                  ║  ║ resource management.               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT cold_snap | temperature -3  ║
║ [O2] 1000 | [H2O] 545 | [E] 1040   ║  ╚════════════════════════════════════╝
║ [FOOD] 400 | [MAT] 50              ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Limits  ║                                        
║ Solar Power | temperature -3       ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Deploy Dust Shields             ║
║    Dustline Agro | P1 B3 | S2395   ║  ║    Install dust shields on solar…  ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling Optimization    ║
║    Ares Systems | P1 B4 | S2129    ║  ║    Upgrade water recycling…        ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S1541         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ persists; prioritize…              ║
║ ENERGY    1040                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      400                      ║  ║ assistance with dust…              ║
║ MATERIALS 50                       ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Sol 18 on Mars is marked by a      ║  ║ 00:18 | AI directive: Persistent…  ║
║ relentless dust storm severely     ║  ║ 12:15 | Sol 18: A severe dust      ║
║ impacting solar energy production. ║  ║ storm…                             ║
║ Colonies are focusing on           ║  ║ 06:35 | Martian day 18 has begun   ║
║ protective measures and optimizing ║  ║ 00:19 | AI directive: Solar…       ║
║ water recycling to sustain their   ║  ║ 00:18 | A massive solar flare is…  ║
║ operations. Resource management    ║  ╚════════════════════════════════════╝
║ remains critical as temperatures   ║                                        
║ remain low during early s…         ║                                        
║ Sol 18: A severe dust storm is     ║                                        
║ active, forcing all solar panels   ║                                        
║ offline for the next 6 hours.      ║                                        
║ Expect reduced power availability  ║                                        
║ during this period.                ║                                        
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
