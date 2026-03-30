# 🚀 RED PLANET

> Multiplayer survival strategy on Mars using GitHub as game server

```
╔═══════════════════════════════════════════════════════════════════════╗
║  🚀  R E D   P L A N E T  🚀                                            ║
║  Use git commands as game mechanics                                     ║
║  GitHub Actions = weather, events and economy                         ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## 🎮 Concept

This game **"abuses"** development tools to create unique gameplay:

| Tool | Normal Use | Game Use |
|------|-----------|----------|
| `git commit` | Save code | Build structure |
| `git push` | Send code | Publish move |
| `git pull` | Get code | Get events |
| GitHub Actions | CI/CD | Game engine |
| Cron | Task scheduler | Martian sol |

## 🚀 Quick Start

### For Players

See [PLAYER_INSTRUCTIONS.md](PLAYER_INSTRUCTIONS.md)

### For Administrators

See [CI_CD_SETUP.md](CI_CD_SETUP.md)

## 🌍 Live World Snapshot

<!-- WORLD_SUMMARY:START -->
_Auto-updated daily. Last world update: 2026-03-28T00:00:00Z_

| Metric | Value |
|---|---|
| Martian day | Sol 1 |
| Season | Early Spring |
| Temperature | -60°C |
| Solar activity | 85% |
| Dust storm | No |
| Active event | None |
| Active colonists | 18 |
| Total buildings | 9 |
| Registered players | 3 |

### Global Resources

| Oxygen | Water | Energy | Food | Materials |
|---|---|---|---|---|
| 1000 | 500 | 1000 | 300 | 0 |

### Market Prices

| Oxygen | Water | Food | Materials |
|---|---|---|---|
| 0 | 1 | 2 | 5 |

### Colony Standings

| Rank | Colonist | Corporation | Colonists | Buildings | Score |
|---|---|---|---|---|---|
| 1 | Marco Quinn | Dustline Agro | 7 | 3 | 1561 |
| 2 | Zoya Kade | Ares Systems | 5 | 4 | 1353 |
| 3 | Irina Vale | Helios Prospecting | 6 | 2 | 1329 |

### Recent Events

_No world events logged yet._

<!-- WORLD_SUMMARY:END -->



## 🏗️ Architecture

```
┌─────────────┐      git push      ┌──────────────────┐
│   Player 1  │ ─────────────────→ │  GitHub Repo     │
│  (Claude)   │                    │  (Game Server)   │
└─────────────┘                    └──────────────────┘
       │                                  │
       │ git pull                    GitHub Actions
       │                                  │
       └──────────────────────────←───────┘
                  world_state.json
                  players/<colonist>.json
                  events/
```

## 📁 Project Structure

```
mars_colony_game/
├── mars_client.py          # 🎮 Game client
├── world_state.json        # 🌍 Global state
├── .github/workflows/      # ⚙️ Game processes
│   ├── mars_day.yml        # Day cycle (daily)
│   ├── random_events.yml   # Random events (every 12h)
│   ├── economy.yml         # Economy (every 6h)
│   ├── world_summary.yml   # README world snapshot (daily)
│   └── anti_cheat.yml      # Fairness check
├── game/server/            # 🖥️ Server scripts
│   ├── day_cycle.py
│   ├── weather.py
│   ├── events/
│   ├── economy/
│   ├── world_snapshot.py
│   └── update_readme.py
├── players/                # 👤 Player data
├── .mars/                  # 🏠 Local player pointer/tasks (not committed)
├── PLAYER_INSTRUCTIONS.md  # 🧑‍🚀 Player guide
└── CI_CD_SETUP.md          # ⚙️ Admin guide
```

## 🎯 Features

### Git as Game Mechanic

- **Save** = `git commit`
- **Multiplayer** = `git push` + `git pull`
- **Conflicts** = PvP encounters
- **History** = complete game record

### GitHub Actions as World

- **Martian sol** = Cron once per day
- **Random events** = Cron every 12 hours
- **Economy** = Cron every 6 hours
- **README snapshot** = Daily world summary
- **Anti-cheat** = Validation for code/config pushes

### Claude Code Tools as Game Systems ("Abuse")

The game client runs **inside Claude Code** and uses its built-in tools in completely unintended ways:

| Claude Tool | Normal Purpose | In-Game Purpose |
|-------------|----------------|-----------------|
| `Read` | Read code files | Read colony sensors |
| `Edit` | Edit code | Repair damaged systems |
| `Bash` | Run commands | Execute git operations |
| `AskUserQuestion` | Clarify requirements | Critical life-or-death decisions |
| `Glob` | Find files | Scan terrain for resources |
| `Grep` | Search code | Find specific resources |
| **Memory** | Save user info | **Colony history that persists** |
| **CronCreate** | Schedule tasks | **Life support reminders (O₂/food/water)** |
| **TaskList** | Track work items | **Construction queue & research** |
| **Agent** | Delegate tasks | **Autonomous drone explorers** |

**The player plays by chatting with Claude!**

**NEW:** Colony history (`memory`), autonomous drones (`drone`), resource alerts (`cron`), build queue (`tasks`)!

## 🌟 Events

| Event | Effect |
|-------|--------|
| 🌪️ Sandstorm | -energy, stop mining |
| 🌠 Meteor shower | +materials, damage risk |
| 💧 Underground ice | +water for all players |
| ⚡ Solar flare | ++energy |
| 🛸 Traders | +global resources |

## 🛠️ Technologies

- **Python 3.11** - client and server
- **Git** - state synchronization
- **GitHub Actions** - game engine
- **JSON** - data storage

## 📜 License

MIT License - do whatever you want!

## 🤝 Contributing

PRs welcome! Ideas for new events, buildings, mechanics.

---

**Welcome to Mars!** 🚀🔴
