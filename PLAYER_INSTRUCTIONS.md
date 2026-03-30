# 🚀 PLAYER INSTRUCTIONS: Red Planet

## 🎮 How This Game is Different

This game **runs inside Claude Code** and uses Claude's tools in completely unintended ways:

| Claude Tool | Normal Use | Game Use |
|-------------|-----------|----------|
| `Read` | Read code | Read colony sensors |
| `Edit` | Edit code | Repair broken systems |
| `Bash` | Run commands | Execute git operations |
| `AskUserQuestion` | Clarify requirements | **Critical decisions** |

**You play by chatting with Claude!**

## Quick Start

### 1. Preparation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mars_colony_game.git
cd mars_colony_game

# Ensure you have access to Claude Code
# (or run client directly via python)
```

### 2. Launch via Claude Code

```bash
# Launch Claude Code in game folder
claude

# Inside Claude Code run:
python3 mars_client.py
```

### 3. Alternative Launch (without Claude)

```bash
python3 mars_client.py
```

## How to Play

### Registration

On first launch you'll be asked to enter:
- **Colonist name** - your in-game name
- **Corporation** - your company name

The client creates your personal file as `players/<colonist>.json`.
That is the file you commit and push to become an active player.

### Commands

| Command | Description |
|---------|-------------|
| `status` | Show colony status |
| `dig` | Dig for ice → water |
| `mine` | Mine materials |
| `build` | Build structure |
| `sync` | Sync with server |
| `help` | Show help |
| `quit` | Exit |

### Game Cycle

```
1. Make a move (dig/mine/build)
   ↓
2. Commit auto-saves locally
   ↓
3. git push sends move to server
   ↓
4. GitHub Actions process events
   ↓
5. git pull gets other players' updates
```

The local session pointer lives in `.mars/current_player` and is not committed.

### Resources

| Resource | Icon | Purpose |
|----------|------|---------|
| Oxygen | 🫁 | Essential for life |
| Water | 💧 | Drinking, hydroponics |
| Energy | ⚡ | All actions |
| Food | 🍎 | Keep colonists alive |
| Materials | 🧱 | Construction |

### Construction

| Building | Cost | Effect |
|----------|------|--------|
| Solar Panel | 10 materials | +20 energy/turn |
| Greenhouse | 15 mat, 20 water | +10 food/turn |
| Oxygen Generator | 20 mat, 30 energy | +15 O₂/turn |
| Habitat | 25 mat, 20 en, 10 water | +5 colonists |
| Research Lab | 30 mat, 50 energy | Research |

## Multiplayer

### Sync

```bash
# Get updates
claude → sync
# Or: git pull origin main

# Send your move
claude → [make move]
# Then: git push origin main
```

Each player should only edit their own `players/<colonist>.json` file.

### Conflicts

If two players move simultaneously:
1. `git pull origin main` gets others' changes
2. Git auto-merges data (usually)
3. If conflict - notify admin

### Events

- **🌪️ Sandstorms** - disable solar panels
- **🌠 Meteorites** - resources but damage risk
- **💧 Discoveries** - random resource bonuses
- **🛸 Traders** - global resources

## Tips

1. **Build Solar Panels first** - no energy = nothing works
2. **Watch oxygen** - at 0 colonists die
3. **Balance resources** - don't spend everything on one thing
4. **Sync often** - to see events

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Not a git repository" | `git init && git remote add origin URL` |
| "No connection" | Check git remote and access rights |
| Push conflict | `git pull` → resolve → `git push` |

---

**Good luck on Mars, colonist!** 🚀
