## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-05-24T00:32:21.073109_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 54 | [SEASON] Early      ║  ║ Solar Activity Boosts Energy       ║
║ Spring                             ║  ║ Output                             ║
║ [TEMP] -77C | [SUN] 150% | [STORM] ║  ║ Solar activity has surged to 89%,  ║
║ NO                                 ║  ║ enhancing solar panel efficiency   ║
║ [EVENT] Trading Ship Arrives with  ║  ║ across all colonies today.         ║
║ Vital Supplies                     ║  ║ EFFECT solar_boost |               ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ solar_activity +5                  ║
║ [O2] 1000 | [H2O] 545 | [E] 1140   ║  ╚════════════════════════════════════╝
║ [FOOD] 1600 | [MAT] 650            ║                                        
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Solar Activity Boosts Energy  ║                                        
║ Output | solar_activity +5         ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Panel Arrays     ║
║    Dustline Agro | P1 B3 | S6565   ║  ║    Calibrate and realign solar…    ║
║ 2. Zoya Kade                       ║  ║ 2. Water Recycling System…         ║
║    Ares Systems | P1 B4 | S5934    ║  ║    Perform routine maintenance…    ║
║ 3. Irina Vale                      ║  ║ 3. Material Salvage from Past…     ║
║    Helios… | P1 B2 | S5073         ║  ║    Conduct a short expedition to…  ║
╚════════════════════════════════════╝  ╚════════════════════════════════════╝

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity is at a seasonal…         ║
║ ENERGY    1140                     ║  ║ Helios… -> Marco… | Irina reports  ║
║ FOOD      1600                     ║  ║ stable water…                      ║
║ MATERIALS 650                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 54, Mars experiences        ║  ║ 00:32 | A trading vessel from      ║
║ elevated solar activity boosting   ║  ║ Earth…                             ║
║ energy production potential.       ║  ║ 00:33 | A trading vessel from      ║
║ Colonies are encouraged to         ║  ║ Earth…                             ║
║ optimize solar arrays and maintain ║  ║ 12:21 | A massive solar flare is…  ║
║ critical systems like water        ║  ║ 00:32 | AI directive: Solar…       ║
║ recycling. Salvage operations      ║  ║ 12:18 | Underground ice pockets…   ║
║ offer opportunities to replenish   ║  ╚════════════════════════════════════╝
║ material stocks despite cold       ║                                        
║ tempera…                           ║                                        
║ A trading vessel from Earth has    ║                                        
║ docked, delivering 100 units of    ║                                        
║ food and 50 units of materials to  ║                                        
║ the colony's reserves. Operations  ║                                        
║ continue smoothly under clear      ║                                        
║ skies and elevated solar activity. ║                                        
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
