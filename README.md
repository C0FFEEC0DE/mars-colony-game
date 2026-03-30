## LIVE WORLD SNAPSHOT

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-03-30T11:17:57.131433_

```text
╔═══════════════════ LIVE WORLD SNAPSHOT ════════════════════╗
║ [SOL] Sol 3   [SEASON] Early Spring                        ║
║ [TEMP] -43C   [SUN] 94%   [STORM] NO                       ║
║ [EVENT] None                                               ║
║ [POP] 18   [BLD] 9   [PLY] 3                               ║
║ [O2] 1000   [H2O] 500   [E] 1000                           ║
║ [FOOD] 300   [MAT] 0                                       ║
╚════════════════════════════════════════════════════════════╝

╔════════════════════ RESOURCE RESERVES ═════════════════════╗
║ OXYGEN    1000                                             ║
║ WATER     500                                              ║
║ ENERGY    1000                                             ║
║ FOOD      300                                              ║
║ MATERIALS 0                                                ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ MARKET PRICES ═══════════════════════╗
║ [O2] 0   [H2O] 0                                           ║
║ [FOOD] 0   [MAT] 0                                         ║
╚════════════════════════════════════════════════════════════╝

╔═════════════════════ COLONY STANDINGS ═════════════════════╗
║ RK NAME             CORP                 POP BLD SCORE     ║
║  1 Marco Quinn      Dustline Agro          7   3  1558     ║
║  2 Zoya Kade        Ares Systems           5   4  1347     ║
║  3 Irina Vale       Helios Prospecting     6   2  1311     ║
╚════════════════════════════════════════════════════════════╝

╔══════════════════════ RECENT EVENTS ═══════════════════════╗
║ 2026-03-30T11:17:57.131451 | Martian day 3 has begun       ║
║ 2026-03-30T11:05:03.630608 | Martian day 2 has begun       ║
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
economy, random events, Mars day, and README summary stages in sequence.
