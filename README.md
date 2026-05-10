## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-10T00:28:48.301065_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 47 | [SEASON] Early      ║  ║ Solar Activity Boost Enhances      ║
║ Spring                             ║  ║ Energy Output                      ║
║ [TEMP] -42C | [SUN] 77% | [STORM]  ║  ║ Solar activity has risen to 72%,   ║
║ NO                                 ║  ║ improving solar panel efficiency   ║
║ [EVENT] Trading Ship Arrives with  ║  ║ and increasing energy availability ║
║ Vital Supplies                     ║  ║ across all colonies.               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1120   ║  ║ solar_activity +5                  ║
║ [FOOD] 1200 | [MAT] 450            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boost Enhances ║                                        
║ Energy Output | solar_activity +5  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S4748   ║  ║    Perform maintenance and…        ║
║ 2. Zoya Kade                       ║  ║ 2. Water Conservation Protocol     ║
║    Ares Systems | P1 B4 | S4393    ║  ║    Establish water recycling and…  ║
║ 3. Irina Vale                      ║  ║ 3. Materials Inventory Audit       ║
║    Helios… | P1 B2 | S3553         ║  ║    Conduct a full materials…       ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity levels have…              ║
║ ENERGY    1120                     ║  ║ Helios… -> Marco… | Requesting     ║
║ FOOD      1200                     ║  ║ assistance with…                   ║
║ MATERIALS 450                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ As Mars enters early spring on Sol ║  ║ 00:28 | AI directive: Solar…       ║
║ 47, solar activity has increased,  ║  ║ 00:28 | A trading vessel from      ║
║ boosting energy generation         ║  ║ Earth…                             ║
║ potential for all colonies. Water  ║  ║ 06:41 | Martian day 47 has begun   ║
║ conservation remains a priority    ║  ║ 00:29 | AI directive: Solar…       ║
║ due to limited reserves. Colonies  ║  ║ 06:34 | Martian day 46 has begun   ║
║ are focusing on resource           ║  ╚════════════════════════════════════╝
║ optimization to sustain operations ║                                        
║ amid the cold condition…           ║                                        
║ A trading vessel from Earth has    ║                                        
║ docked, delivering 100 units of    ║                                        
║ food and 50 units of materials to  ║                                        
║ the colony's reserves. Operations  ║                                        
║ continue smoothly under stable     ║                                        
║ conditions.                        ║                                        
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
