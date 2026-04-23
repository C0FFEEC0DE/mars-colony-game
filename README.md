## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-23T00:25:59.774022_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 30 | [SEASON] Early      ║  ║ Persistent Dust Storm Reduces      ║
║ Spring                             ║  ║ Solar Efficiency                   ║
║ [TEMP] -76C | [SUN] 85% | [STORM]  ║  ║ A dust storm continues across      ║
║ YES                                ║  ║ Mars, reducing solar panel output  ║
║ [EVENT] None                       ║  ║ despite high solar activity.       ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT energy_surge | energy +20   ║
║ [O2] 1000 | [H2O] 545 | [E] 1080   ║  ╚════════════════════════════════════╝
║ [FOOD] 700 | [MAT] 200             ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Persistent Dust Storm Reduces ║                                        
║ Solar Efficiency | energy +20      ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Dust Storm Shield…              ║
║    Dustline Agro | P1 B3 | S3287   ║  ║    Deploy and reinforce dust…      ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System Check    ║
║    Ares Systems | P1 B4 | S2951    ║  ║    Inspect and repair water…       ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S2368         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Dust storm  ║
║ WATER     545                      ║  ║ alert remains active.…             ║
║ ENERGY    1080                     ║  ║ Helios… -> Mars… | Requesting      ║
║ FOOD      700                      ║  ║ additional materials…              ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ Mars experiences a persistent dust ║  ║ 00:25 | AI directive: Persistent…  ║
║ storm limiting solar energy        ║  ║ 06:36 | 🌪️ Dust storm damaged…     ║
║ despite high solar activity.       ║  ║ 06:36 | Martian day 30 has begun   ║
║ Colonies focus on shielding solar  ║  ║ 00:20 | AI directive: Mild Solar…  ║
║ arrays and maintaining water       ║  ║ 06:35 | Martian day 29 has begun   ║
║ recycling systems to sustain       ║  ╚════════════════════════════════════╝
║ operations. Resource management    ║                                        
║ remains critical as conditions     ║                                        
║ challenge energy and water avail…  ║                                        
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
