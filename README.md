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
                  players/*.json
                  events/
```

## 📁 Project Structure

```
mars_colony_game/
├── mars_client.py          # 🎮 Game client
├── world_state.json        # 🌍 Global state
├── .github/workflows/      # ⚙️ Game processes
│   ├── mars_day.yml        # Day cycle (every 4h)
│   ├── random_events.yml   # Random events
│   ├── economy.yml         # Economy (every 15m)
│   └── anti_cheat.yml      # Fairness check
├── game/server/            # 🖥️ Server scripts
│   ├── day_cycle.py
│   ├── weather.py
│   ├── events/
│   └── economy/
├── players/                # 👤 Player data
└── docs/
    ├── PLAYER_INSTRUCTIONS.md
    └── CI_CD_SETUP.md
```

## 🎯 Features

### Git as Game Mechanic

- **Save** = `git commit`
- **Multiplayer** = `git push` + `git pull`
- **Conflicts** = PvP encounters
- **History** = complete game record

### GitHub Actions as World

- **Martian sol** = Cron every 4 hours
- **Sandstorms** = Random events
- **Economy** = Automatic calculations
- **Anti-cheat** = Push validation

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
