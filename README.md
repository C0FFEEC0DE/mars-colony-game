## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-07-16T00:24:10.428867_

```text
╔═══════ LIVE WORLD SNAPSHOT ════════╗  ╔════════ AI DAILY DIRECTIVE ════════╗
║ [SOL] Sol 61 | [SEASON] Early      ║  ║ Enhanced Solar Activity Boosts     ║
║ Spring                             ║  ║ Energy                             ║
║ [TEMP] -65C | [SUN] 150% | [STORM] ║  ║ Solar activity has surged to 150%, ║
║ NO                                 ║  ║ increasing solar panel efficiency  ║
║ [EVENT] Massive Solar Flare        ║  ║ across all colonies, providing an  ║
║ Detected on Sol 61                 ║  ║ unexpected energy surplus today.   ║
║ [POP] 3 | [BLD] 9 | [PLY] 3        ║  ║ EFFECT solar_boost |               ║
║ [O2] 1000 | [H2O] 545 | [E] 1160   ║  ║ solar_activity +0                  ║
║ [FOOD] 2200 | [MAT] 950            ║  ╚════════════════════════════════════╝
║ [MKT] O2 0 H2O 0 F 0 M 0           ║                                        
║ [AI] Enhanced Solar Activity       ║                                        
║ Boosts Energy | solar_activity +0  ║                                        
╚════════════════════════════════════╝                                        

╔═════════ COLONY STANDINGS ═════════╗  ╔══════════ MISSION BOARD ═══════════╗
║ 1. Marco Quinn                     ║  ║ 1. Optimize Solar Arrays           ║
║    Dustline Agro | P1 B3 | S7509   ║  ║    Adjust solar panel…             ║
║ 2. Zoya Kade                       ║  ║ 2. Water Supply Inspection         ║
║    Ares Systems | P1 B4 | S7498    ║  ║    Conduct a full inspection and…  ║
║ 3. Irina Vale                      ║  ╚════════════════════════════════════╝
║    Helios… | P1 B2 | S6203         ║                                        
╚════════════════════════════════════╝                                        

╔════════ RESOURCE RESERVES ═════════╗  ╔════════ NPC TRANSMISSIONS ═════════╗
║ OXYGEN    1000                     ║  ║ Mars Control -> all… | Solar       ║
║ WATER     545                      ║  ║ activity peak detected.…           ║
║ ENERGY    1160                     ║  ║ Helios… -> Marco… | Request        ║
║ FOOD      2200                     ║  ║ collaboration on energy…           ║
║ MATERIALS 950                      ║  ╚════════════════════════════════════╝
╚════════════════════════════════════╝                                        

╔═════════ COLONY NEWS FEED ═════════╗  ╔══════════ RECENT EVENTS ═══════════╗
║ On Sol 61 during early spring on   ║  ║ 00:24 | AI directive: Enhanced…    ║
║ Mars, a solar activity spike has   ║  ║ 00:24 | A massive solar flare has… ║
║ enhanced energy production colony- ║  ║ 12:27 | On Sol 61, our receivers…  ║
║ wide. Temperatures remain frigid   ║  ║ 06:42 | Martian day 61 has begun   ║
║ at -65C with stable conditions and ║  ║ 00:21 | AI directive: Early        ║
║ no dust storms. Colonies are       ║  ║ Spring…                            ║
║ focusing on maximizing energy      ║  ╚════════════════════════════════════╝
║ resources and securing water       ║                                        
║ supplies ahead of the s…           ║                                        
║ A massive solar flare has          ║                                        
║ increased energy levels by 50% for ║                                        
║ the next turn. All personnel       ║                                        
║ advised to take cover from         ║                                        
║ elevated radiation exposure.       ║                                        
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
