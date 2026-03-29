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

### 4. Setup Personal Token

For automated commits on behalf of server:

1. Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Scopes: `repo` (all sub-items)
4. Copy token

5. In repository: Settings → Secrets and variables → Actions
6. New repository secret:
   - Name: `GITHUB_TOKEN`
   - Value: your token

### 5. Allow Push for Actions

Settings → Actions → General:

```
☑️ Allow GitHub Actions to create and approve pull requests
☑️ Read and write permissions
```

## Working Workflows

| Workflow | File | Triggers |
|----------|------|----------|
| 🚀 Mars Day | `mars_day.yml` | Every 4 hours |
| ⚡ Random Events | `random_events.yml` | Every hour (chance) |
| 💰 Economy | `economy.yml` | Every 15 minutes |
| 🛡️ Anti-Cheat | `anti_cheat.yml` | On every push |

## Manual Launch

Any workflow can be triggered manually:

1. GitHub → Actions → [Select workflow]
2. Click "Run workflow"
3. Runs on main branch

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
    - cron: '0 */4 * * *'  # Every 4 hours
```

Cron format:
```
minute hour day_of_month month day_of_week
*/15 * * * *  = every 15 minutes
0 */4 * * *   = every 4 hours
0 * * * *     = every hour
```

### Disable Processes

Delete file from `.github/workflows/` or comment out:

```yaml
# on:
#   schedule:
#     - cron: '*/15 * * * *'
```

## Security

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
```

### GitHub Actions Logs

Download artifacts (if configured) or view in console.

---

**Server ready to go!** 🚀
