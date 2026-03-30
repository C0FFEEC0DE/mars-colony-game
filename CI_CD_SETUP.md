# ⚙️ CI/CD SETUP: Red Planet

## For Server Administrators

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Name: `mars_colony_game` (or any other)
3. Make public or private (for friends)
4. **DO NOT** initialize README (already exists)
5. Create repository

### 2. Upload Code

```bash
# In mars_colony_game folder
git init
git add .
git commit -m "Initial game setup"

# Add your URL
git remote add origin https://github.com/YOUR_USERNAME/mars_colony_game.git
git branch -M main
git push -u origin main
```

### 3. Configure GitHub Actions

GitHub Actions are already configured in `.github/workflows/`. Just enable:

1. Go to repository → Settings → Actions → General
2. Select "Read and write permissions" for Workflow permissions
3. Save

### 4. GitHub Models Access

This repo uses **GitHub Models** directly from GitHub Actions.

Required:

- repository Actions workflow permissions must allow read/write access
- workflows that call models need `permissions: models: read`
- the repository or organization must allow GitHub Models

The built-in `secrets.GITHUB_TOKEN` is enough for:
- automated commits
- GitHub Models inference in Actions

You do **not** need to create a separate repository secret named `GITHUB_TOKEN`.

Optional:
- if you want to run model calls outside Actions, the code also supports `MARS_AI_TOKEN`
- this is an override, not a normal requirement

### 5. Allow Push for Actions

Settings → Actions → General:

```
☑️ Allow GitHub Actions to create and approve pull requests
☑️ Read and write permissions
```

## Working Workflows

| Workflow | File | Triggers |
|----------|------|----------|
| 🪐 Game Loop | `game_loop.yml` | Every 6 hours, with a daily AI/news pass at 00:00 UTC |
| 💰 Economy | `economy.yml` | Stage logic used by the Game Loop |
| ⚡ Random Events | `random_events.yml` | Stage logic used by the Game Loop |
| 🚀 Mars Day | `mars_day.yml` | Stage logic used by the Game Loop |
| 📘 World Summary | `world_summary.yml` | Stage logic used by the Game Loop |
| 🤖 AI Health Check | `ai_health_check.yml` | Manual live check for GitHub Models access |
| 🧪 Tests | `tests.yml` | Push/PR, except game-state-only updates |
| 🛡️ Anti-Cheat | `anti_cheat.yml` | Push/PR, except game-state-only updates |

## Manual Launch

Any workflow can be triggered manually:

1. GitHub → Actions → [Select workflow]
2. Click "Run workflow"
3. Runs on main branch

The Game Loop job also contains a daily AI stage that generates:
- a safe AI directive with a validated world effect
- a mission board for players
- colony news for the README
- NPC transmissions
- flavor text for deterministic random events

The `AI Health Check` workflow performs one live GitHub Models request without
changing world state. Use it to confirm:
- GitHub Models access is enabled
- `GITHUB_TOKEN` reaches the AI step
- inference is live, not fallback

## Monitoring

### Logs

GitHub → Actions → [Workflow run] → [Job]

### Notifications Setup

Settings → Notifications:
- Disable excess (otherwise spam)
- Keep "Actions" if you want to monitor

## Server Process Configuration

### Change Schedule

In workflow files change cron:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
```

Current defaults in this repo:

```yaml
# game_loop.yml
- cron: '0 */6 * * *'
```

Cron format:
```
minute hour day_of_month month day_of_week
0 */6 * * *   = every 6 hours
0 */12 * * *  = every 12 hours
0 0 * * *     = every day at 00:00 UTC
0 6 * * *     = every day at 06:00 UTC
```

Inside the orchestrator:
- economy runs every 6 hours
- random events run on the 00:00 and 12:00 UTC ticks
- Mars day runs on the 06:00 UTC tick
- daily AI content runs on the 00:00 UTC tick
- world summary runs on the 00:00 UTC tick

### Disable Processes

Disable the scheduler in `game_loop.yml` or comment out the cron:

```yaml
# on:
#   schedule:
#     - cron: '0 */6 * * *'
```

## Security

### Token Handling

- AI workflows use the built-in `secrets.GITHUB_TOKEN`
- the token is scoped only to AI-related steps, not the whole job
- logs show the token only as `***`
- diagnostics report the token source as `GITHUB_TOKEN` but never print the value

### Branch Protection

Settings → Branches → Add rule:
- Branch name pattern: `main`
- ☑️ Require a pull request before merging
- ☑️ Require approvals: 1
- ☑️ Require status checks to pass

### Anti-Cheat

Workflow `anti_cheat.yml` checks:
- Negative resources
- Suspiciously high values
- Impossible building counts

To reduce GitHub Actions usage, `tests.yml` and `anti_cheat.yml` ignore commits
that only change `world_state.json`, `players/**`, or `README.md`.

On detection:
1. Workflow fails with error
2. Can configure auto-ban

## Scaling

### More Players

At 50+ players:
1. Workflows may run slower
2. Consider sharding
3. Use GitHub Actions caching

### More Events

Create new in `game/server/events/`:

```python
#!/usr/bin/env python3
# game/server/events/my_event.py

def main():
    # Your logic
    pass

if __name__ == '__main__':
    main()
```

Add to `random_events.yml`:

```yaml
6)
  echo "🎯 MY EVENT!"
  python3 game/server/events/my_event.py
  ;;
```

## Debugging

### Local Check

```bash
# Simulate day cycle
python3 game/server/day_cycle.py

# Check economy
python3 game/server/economy/consumption.py

# Check AI locally without Actions token
python3 game/server/ai_content.py --healthcheck
```

### GitHub Actions Logs

Useful checks:
- `🪐 Game Loop` should show `AI diagnostics: ... status=ok http=200`
- `🤖 AI Health Check` should succeed without changing repo files
- if models are unavailable, diagnostics will tell you whether it is a token,
  HTTP, timeout, or response-format problem

---

**Server ready to go!** 🚀
