## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-13T00:25:39.267245_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 59 | [SEASON] Early      ║  ║ Unexpected Solar Boost Enhances    ║
║ Spring                             ║  ║ Energy Production                  ║
║ [TEMP] -68C | [SUN] 73% | [STORM]  ║  ║ A moderate increase in solar       ║
║ NO                                 ║  ║ activity has led to a temporary    ║
║ [EVENT] Earth Traders Arrive with  ║  ║ surge in available energy across   ║
║ Vital Supplies                     ║  ║ Mars colonies.                     ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ║ solar_activity +5                  ║
║ [FOOD] 2200 | [MAT] 950            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Unexpected Solar Boost        ║                                        
║ Enhances Energy Production |       ║                                        
║ solar_activity +5                  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7414   ║  ║    Increase colony energy…         ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S7331    ║  ║    Perform maintenance to reduce…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6072         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity has increased,…           ║
║ ENERGY    1160                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      2200                     ║  ║ collaboration on…                  ║
║ MATERIALS 950                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 59, Mars colonies benefit   ║  ║ 00:25 | AI directive: Unexpected…  ║
║ from a solar boost enhancing       ║  ║ 00:25 | A trading ship from Earth… ║
║ energy availability during the     ║  ║ 06:51 | Martian day 59 has begun   ║
║ early spring season. Leaders are   ║  ║ 00:25 | AI directive: Solar…       ║
║ advised to optimize energy         ║  ║ 00:25 | A meteor shower was…       ║
║ collection and maintain vital      ║  ╚════════════════════════════════════╝
║ water recycling systems to sustain ║                                        
║ colony operations. Collaborative   ║                                        
║ efforts between factions are…      ║                                        
║ A trading ship from Earth has      ║                                        
║ docked, delivering +100 food units ║                                        
║ and +50 materials to the colony's  ║                                        
║ reserves. Resources boosted as we  ║                                        
║ continue to adapt to Mars' harsh   ║                                        
║ environment.                       ║                                        
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
