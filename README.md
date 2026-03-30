## SYSTEM STATUS

[![Game Loop](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/game_loop.yml)
[![Tests](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/tests.yml)
[![Anti-Cheat](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/anti_cheat.yml)
[![World Summary](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml/badge.svg)](https://github.com/C0FFEEC0DE/mars-colony-game/actions/workflows/world_summary.yml)

## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-03-30T12:39:58.394061_

```text
╔═══════════════════ LIVE WORLD SNAPSHOT ════════════════════╗
║ [SOL] Sol 6   [SEASON] Early Spring                        ║
║ [TEMP] -63C   [SUN] 83%   [STORM] NO                       ║
║ [EVENT] None                                               ║
║ [POP] 18   [BLD] 9   [PLY] 3                               ║
║ [O2] 1000   [H2O] 545   [E] 1000                           ║
║ [FOOD] 300   [MAT] 0                                       ║
║ [AI] Operations drift into a new rhythm | solar_activity   ║
║ +15                                                        ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ RESOURCE RESERVES ═════════════════════╗
║ OXYGEN    1000                                             ║
║ WATER     545                                              ║
║ ENERGY    1000                                             ║
║ FOOD      300                                              ║
║ MATERIALS 0                                                ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ MARKET PRICES ═══════════════════════╗
║ [O2] 0   [H2O] 0                                           ║
║ [FOOD] 0   [MAT] 0                                         ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ AI DAILY DIRECTIVE ════════════════════╗
║ Operations drift into a new rhythm                         ║
║ Sol 6 opens with thin margins, nervous operators, and one  ║
║ narrow chance to shift the colony balance before the next  ║
║ weather swing.                                             ║
║ EFFECT solar_boost | solar_activity +15                    ║
╚════════════════════════════════════════════════════════════╝

╔═════════════════════ COLONY STANDINGS ═════════════════════╗
║ RK NAME             CORP                 POP BLD SCORE     ║
║  1 Marco Quinn      Dustline Agro          7   3  1481     ║
║  2 Zoya Kade        Ares Systems           5   4  1308     ║
║  3 Irina Vale       Helios Prospecting     6   2  1223     ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ MISSION BOARD ═══════════════════════╗
║ 1. Secure ridge ice cores | REWARD Water and science       ║
║ prestige                                                   ║
║    OBJ Bring back intact samples before the sun angle      ║
║ drops.                                                     ║
║    RISK Moderate exposure and rover wear                   ║
║ 2. Patch the thermal grid | REWARD Energy stability and    ║
║ spare materials                                            ║
║    OBJ Repair or reinforce one weak point before the next  ║
║ cold cycle.                                                ║
║    RISK Low risk, high urgency                             ║
║ 3. Recover a silent beacon | REWARD Materials and map      ║
║ intel                                                      ║
║    OBJ Reach the site, recover telemetry, and mark         ║
║ salvageable parts.                                         ║
║    RISK Navigation errors in dust                          ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ NPC TRANSMISSIONS ═════════════════════╗
║ Mars Control -> All colonies | Keep your reports short and ║
║ your seals tighter. Conditions are changing faster than    ║
║ forecast.                                                  ║
║ Orbital Relay -> Irina Vale | Your telemetry is the        ║
║ cleanest on the planet today. Do not waste that advantage. ║
╚════════════════════════════════════════════════════════════╝

╔═════════════════════ COLONY NEWS FEED ═════════════════════╗
║ Sol 6 begins in Early Spring with 3 active colonies.       ║
║ Temperature holds near -63C, solar activity sits at 68%,   ║
║ and the current leaders are Marco Quinn:1481, Zoya         ║
║ Kade:1308, Irina Vale:1223.                                ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ RECENT EVENTS ═══════════════════════╗
║ 2026-03-30T12:39:58.394061 | AI directive: Operations      ║
║ drift into a new rhythm                                    ║
║ 2026-03-30T12:39:57.598851 | Martian day 6 has begun       ║
║ 2026-03-30T12:39:56.762403 | Science crews are locking the ║
║ site down for analysis: 📡 Strange signal on 1420 MHz       ║
║ detected.                                                  ║
║ 2026-03-30T12:31:37.314795 | AI directive: Operations      ║
║ drift into a new rhythm                                    ║
║ 2026-03-30T12:31:36.184965 | Martian day 5 has begun       ║
╚════════════════════════════════════════════════════════════╝
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
