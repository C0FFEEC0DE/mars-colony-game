## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-04-24T00:25:31.606024_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 31 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -80C | [SUN] 88% | [STORM]  ║  ║ With solar activity at 83%,        ║
║ NO                                 ║  ║ colonies experience a moderate     ║
║ [EVENT] New Underground Caverns    ║  ║ increase in solar panel            ║
║ Mapped on Sol 31                   ║  ║ efficiency, improving energy       ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ generation today.                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1080   ║  ║ EFFECT solar_boost |               ║
║ [FOOD] 700 | [MAT] 200             ║  ║ solar_activity +5                  ║
║ [MKT] O2 0 H2O 0 F 0 M 0           ║  ╚════════════════════════════════════╝
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S3323   ║  ║    Recalibrate solar arrays at…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Initiative   ║
║    Ares Systems | P1 B4 | S3011    ║  ║    Implement water recycling…      ║
║ 3. Irina Vale                      ║  ║ 3. Early Spring Crop Assessment    ║
║    Helios… | P1 B2 | S2416         ║  ║    Inspect greenhouse crops for…   ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is higher than…           ║
║ ENERGY    1080                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      700                      ║  ║ collaboration on…                  ║
║ MATERIALS 200                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 31 of Early Spring, Mars    ║  ║ 00:25 | AI directive: Solar…       ║
║ colonies benefit from heightened   ║  ║ 12:20 | Exploration teams have…    ║
║ solar activity, improving energy   ║  ║ 06:36 | Martian day 31 has begun   ║
║ yields. Despite cold temperatures, ║  ║ 00:25 | AI directive: Persistent…  ║
║ resource management remains stable ║  ║ 06:36 | 🌪️ Dust storm damaged…     ║
║ with coordinated efforts to        ║  ╚════════════════════════════════════╝
║ optimize water and food supplies.  ║                                        
║ Colonists are focusing on          ║                                        
║ maximizing renewable en…           ║                                        
║ Exploration teams have located     ║                                        
║ stable underground caverns,        ║                                        
║ providing potential shelter        ║                                        
║ options. Current conditions remain ║                                        
║ harsh with -80C temperatures and   ║                                        
║ moderate solar activity at 83%.    ║                                        
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
