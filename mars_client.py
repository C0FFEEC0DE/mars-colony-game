#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════╗
║  🚀 RED PLANET - Game Client for Claude Code                           ║
║  Uses Claude's built-in tools "unintended"                              ║
╚═══════════════════════════════════════════════════════════════════════╝

LAUNCH:
    python3 mars_client.py

REQUIREMENTS:
    - Claude Code with access to all tools
    - Git repository configured as remote origin
"""

import json
import os
import re
import shlex
import sys
import random
import time
from datetime import datetime

# ANSI colors for beautiful output
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m'
}

PLAYERS_DIR = 'players'
LOCAL_STATE_DIR = '.mars'
CURRENT_PLAYER_POINTER = os.path.join(LOCAL_STATE_DIR, 'current_player')
LOCAL_TASKS_FILE = os.path.join(LOCAL_STATE_DIR, 'tasks.json')

def color(text, color_name):
    """Colorize text"""
    return f"{COLORS.get(color_name, '')}{text}{COLORS['reset']}"

def ensure_local_state_dir():
    """Create local-only state directory"""
    os.makedirs(LOCAL_STATE_DIR, exist_ok=True)

def sanitize_player_slug(name):
    """Create a filesystem-safe player slug"""
    slug = re.sub(r'[^\w-]+', '_', name.strip().lower(), flags=re.UNICODE)
    slug = slug.strip('._')
    return slug or 'player'

def player_file_from_name(name):
    """Build player file path from colonist name"""
    return os.path.join(PLAYERS_DIR, f'{sanitize_player_slug(name)}.json')

def unique_player_file(name):
    """Find a unique player file path"""
    base_slug = sanitize_player_slug(name)
    candidate = os.path.join(PLAYERS_DIR, f'{base_slug}.json')
    suffix = 2

    while os.path.exists(candidate):
        candidate = os.path.join(PLAYERS_DIR, f'{base_slug}_{suffix}.json')
        suffix += 1

    return candidate

def save_current_player_pointer(player_file):
    """Persist local pointer to the active player profile"""
    ensure_local_state_dir()
    with open(CURRENT_PLAYER_POINTER, 'w', encoding='utf-8') as f:
        f.write(player_file)

def migrate_legacy_player_file():
    """Move legacy shared player file to a per-player filename"""
    legacy_file = os.path.join(PLAYERS_DIR, 'current_player.json')
    if not os.path.exists(legacy_file):
        return None

    try:
        with open(legacy_file, 'r', encoding='utf-8') as f:
            player = json.load(f)
    except (OSError, json.JSONDecodeError):
        return None

    player_file = unique_player_file(player.get('name', 'player'))
    os.replace(legacy_file, player_file)
    save_current_player_pointer(player_file)
    return player_file

def get_current_player_file():
    """Resolve the local player profile path"""
    if os.path.exists(CURRENT_PLAYER_POINTER):
        with open(CURRENT_PLAYER_POINTER, 'r', encoding='utf-8') as f:
            player_file = f.read().strip()
        if player_file and os.path.exists(player_file):
            return player_file

    return migrate_legacy_player_file()

def header():
    """Display beautiful header with ASCII art"""
    print("\n" + "=" * 70)
    print(color("""
     _____  ______ ____  _____ _______ ______
    |  __ \\|  ____|  _ \\|  __ \\__   __|  ____|
    | |__) | |__  | |_) | |__) | | |  | |__
    |  _  /|  __| |  _ <|  __ /  | |  |  __|
    | | \\ \\| |____| |_) | |      | |  | |____
    |_|  \\_\\______|____/|_|      |_|  |______|

         🔴 MARS COLONY SURVIVAL GAME 🔴
    """, 'red'))
    print(color("""
        🚀  Uses GitHub as Game Server  🚀
        🤖  Runs Inside Claude Code  🤖
        ⚡  Git Commands = Game Mechanics  ⚡
    """, 'cyan'))
    print("=" * 70 + "\n")

def load_player_data():
    """Load player data"""
    player_file = get_current_player_file()
    if player_file and os.path.exists(player_file):
        with open(player_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def load_world_state():
    """Load world state"""
    world_file = 'world_state.json'
    if os.path.exists(world_file):
        with open(world_file, 'r') as f:
            return json.load(f)
    return {"error": "Sync with server first: git pull"}

def save_player_data(data, player_file=None):
    """Save player data"""
    os.makedirs(PLAYERS_DIR, exist_ok=True)
    player_file = player_file or get_current_player_file()
    if not player_file:
        raise RuntimeError("Current player file is not configured")

    with open(player_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    save_current_player_pointer(player_file)

def register_player():
    """Register new colonist"""
    print(color("\n👤 NEW COLONIST REGISTRATION", 'cyan'))
    print("-" * 50)

    while True:
        name = input(color("Enter colonist name: ", 'yellow')).strip()
        if not name:
            print(color("❌ Colonist name cannot be empty!", 'red'))
            continue

        player_file = player_file_from_name(name)
        if os.path.exists(player_file):
            print(color(f"❌ Colonist name already taken: {player_file}", 'red'))
            continue
        break

    corp = input(color("Corporation name: ", 'yellow'))

    player = {
        "name": name,
        "corporation": corp,
        "resources": {
            "oxygen": 100,
            "water": 50,
            "energy": 100,
            "food": 50,
            "materials": 20
        },
        "buildings": ["habitat_module"],
        "colonists": 5,
        "last_login": datetime.now().isoformat(),
        "turns_today": 0
    }

    save_player_data(player, player_file)

    print(color(f"\n✅ Welcome to Mars, {name}!"))
    print(color(f"   Corporation: {corp}", 'green'))
    print(color(f"   Player file: {player_file}", 'cyan'))
    print(color(f"   Starting resources: {player['resources']}", 'cyan'))

    # Create first commit
    print(color("\n📝 Creating first base...", 'yellow'))
    os.system(f'git add {shlex.quote(player_file)}')
    os.system(f'git commit -m "NEW_COLONIST: {name} from {corp}"')
    print(color("✅ Done! Now run: git push", 'green'))

    return player

def show_status(player, world):
    """Show colony status"""
    print(color("\n📊 COLONY STATUS", 'cyan'))
    print("-" * 50)

    if player:
        print(color(f"👤 Colonist: {player['name']} ({player['corporation']})", 'green'))
        print(color(f"👥 Population: {player['colonists']} people", 'yellow'))

        print(color("\n💎 RESOURCES:", 'cyan'))
        for res, val in player['resources'].items():
            status_color = 'green' if val > 50 else 'yellow' if val > 20 else 'red'
            bar = '█' * int(val / 5) + '░' * (20 - int(val / 5))
            print(f"  {res.capitalize():12} [{color(bar, status_color)}] {val}")

        print(color(f"\n🏗️  Buildings: {', '.join(player['buildings'])}", 'blue'))

    if world and 'day' in world:
        print(color(f"\n🌍 Mars Day: #{world['day']}", 'magenta'))
        print(color(f"☀️  Solar Activity: {world.get('solar_activity', 'N/A')}%", 'yellow'))

        if world.get('current_event'):
            print(color(f"\n⚠️  ACTIVE EVENT: {world['current_event']}", 'red'))

        ai = world.get('ai', {})
        daily_event = ai.get('daily_event', {})
        if daily_event:
            print(color(f"\n🤖 AI DIRECTIVE: {daily_event.get('headline', 'Pending')}", 'cyan'))
            print(color(f"   {daily_event.get('summary', 'No summary available.')}", 'white'))

        missions = ai.get('missions', [])[:3]
        if missions:
            print(color("\n🎯 MISSION BOARD:", 'cyan'))
            for idx, mission in enumerate(missions, 1):
                print(color(f"  {idx}. {mission.get('title', 'Untitled')}", 'green'))
                print(color(f"     Objective: {mission.get('objective', 'Stand by')}", 'white'))
                print(color(f"     Reward: {mission.get('reward_hint', 'Unknown')}", 'yellow'))

        transmissions = ai.get('npc_transmissions', [])[:2]
        if transmissions:
            print(color("\n📡 NPC TRANSMISSIONS:", 'cyan'))
            for transmission in transmissions:
                sender = transmission.get('sender', 'Mars Control')
                recipient = transmission.get('recipient', 'All colonies')
                message = transmission.get('message', 'No message')
                print(color(f"  {sender} -> {recipient}", 'magenta'))
                print(color(f"     {message}", 'white'))

def dig_ice():
    """Dig for ice (converts to water)"""
    player = load_player_data()
    if not player:
        print(color("❌ Register first!", 'red'))
        return

    found = random.randint(3, 15)
    energy_cost = 5

    if player['resources']['energy'] < energy_cost:
        print(color("❌ Not enough energy!", 'red'))
        return

    player['resources']['energy'] -= energy_cost
    player['resources']['water'] += found
    player['turns_today'] += 1

    save_player_data(player)

    print(color(f"\n🧊 Digging for ice...", 'cyan'))
    time.sleep(0.5)
    print(color(f"✅ Found: {found} kg water", 'green'))
    print(color(f"⚡ Spent: {energy_cost} energy", 'yellow'))

    commit_action(f"DIG_ICE: +{found}kg water by {player['name']}")

def mine_materials():
    """Mine materials"""
    player = load_player_data()
    if not player:
        print(color("❌ Register first!", 'red'))
        return

    found = random.randint(2, 8)
    energy_cost = 8

    if player['resources']['energy'] < energy_cost:
        print(color("❌ Not enough energy!", 'red'))
        return

    player['resources']['energy'] -= energy_cost
    player['resources']['materials'] += found
    player['turns_today'] += 1

    save_player_data(player)

    print(color(f"\n⛏️  Mining materials...", 'cyan'))
    time.sleep(0.5)
    print(color(f"✅ Found: {found} units of materials", 'green'))

    commit_action(f"MINE: +{found} materials by {player['name']}")

def build():
    """Build new structure"""
    player = load_player_data()
    if not player:
        print(color("❌ Register first!", 'red'))
        return

    buildings = {
        "1": {"name": "solar_panel", "cost": {"materials": 10}, "output": "+20 energy/turn"},
        "2": {"name": "greenhouse", "cost": {"materials": 15, "water": 20}, "output": "+10 food/turn"},
        "3": {"name": "oxygen_generator", "cost": {"materials": 20, "energy": 30}, "output": "+15 oxygen/turn"},
        "4": {"name": "habitat", "cost": {"materials": 25, "energy": 20, "water": 10}, "output": "+5 colonists"},
        "5": {"name": "research_lab", "cost": {"materials": 30, "energy": 50}, "output": "research"},
    }

    print(color("\n🏗️  CONSTRUCTION", 'cyan'))
    print("-" * 50)
    for key, b in buildings.items():
        cost_str = ', '.join([f"{k}={v}" for k, v in b['cost'].items()])
        print(f"  {key}. {b['name']}")
        print(f"     Cost: {cost_str}")
        print(f"     Effect: {b['output']}\n")

    choice = input(color("Select building (1-5) or Enter to cancel: ", 'yellow'))

    if choice not in buildings:
        return

    building = buildings[choice]

    # Check resources
    for res, cost in building['cost'].items():
        if player['resources'].get(res, 0) < cost:
            print(color(f"❌ Not enough {res}!", 'red'))
            return

    # Deduct resources
    for res, cost in building['cost'].items():
        player['resources'][res] -= cost

    player['buildings'].append(building['name'])
    player['turns_today'] += 1

    save_player_data(player)

    print(color(f"\n✅ Built: {building['name']}!"))
    print(color(f"   Effect: {building['output']}", 'green'))

    commit_action(f"BUILD: {building['name']} by {player['name']}")

def commit_action(message):
    """Create git commit with action"""
    print(color(f"\n📝 Saving to server...", 'yellow'))
    player_file = get_current_player_file()
    if not player_file:
        print(color("❌ No active player profile found", 'red'))
        return

    os.system(f'git add {shlex.quote(player_file)} world_state.json 2>/dev/null')
    result = os.system(f'git commit -m "{message}" --quiet 2>/dev/null')
    if result == 0:
        print(color("✅ Saved locally", 'green'))
        print(color("   Run git push to send to server!", 'cyan'))
    else:
        print(color("⚠️  No changes to save", 'yellow'))

def sync_with_server():
    """Sync with server via git"""
    print(color("\n🔄 SYNCING WITH SERVER", 'cyan'))
    print("-" * 50)

    print(color("   git fetch origin...", 'yellow'))
    os.system('git fetch origin --quiet')

    print(color("   git pull origin main...", 'yellow'))
    result = os.system('git pull origin main --quiet 2>/dev/null')

    if result == 0:
        print(color("✅ Sync completed!", 'green'))
        world = load_world_state()
        if world.get('current_event'):
            print(color(f"\n⚠️  WARNING: {world['current_event']}", 'red'))
    else:
        print(color("⚠️  Sync conflict!", 'red'))
        print(color("   Someone else made a move. Resolve conflict manually.", 'yellow'))

def send_drone():
    """Send autonomous drone - Agent tool as exploration mechanic"""
    player = load_player_data()
    if not player:
        print(color("❌ Register first!", 'red'))
        return

    print(color("\n🤖 AUTONOMOUS DRONE (Agent)", 'cyan'))
    print(color("In Claude Code: This would use the Agent tool to autonomously explore", 'yellow'))
    print(color("and find resources without player interaction!", 'yellow'))
    print()
    print(color("📡 Launching drone...", 'blue'))
    time.sleep(1)

    # Simulate drone exploration
    found = random.choice([
        ("ice", random.randint(5, 20)),
        ("minerals", random.randint(3, 10)),
        ("anomaly", 1),
        ("nothing", 0)
    ])

    if found[0] == "ice":
        player['resources']['water'] += found[1]
        print(color(f"✅ Drone found ice deposit: +{found[1]} water", 'green'))
    elif found[0] == "minerals":
        player['resources']['materials'] += found[1]
        print(color(f"✅ Drone found mineral vein: +{found[1]} materials", 'green'))
    elif found[0] == "anomaly":
        print(color("🛸 Drone detected unusual signal... needs investigation!", 'magenta'))
    else:
        print(color("⚠️ Drone found nothing in this sector", 'yellow'))

    player['resources']['energy'] -= 10
    save_player_data(player)
    commit_action(f"DRONE: exploration by {player['name']}")

def setup_cron():
    """Setup resource reminders - CronCreate as life support mechanic"""
    print(color("\n⏰ RESOURCE MONITORING (CronCreate)", 'cyan'))
    print(color("In Claude Code: This would use CronCreate to schedule reminders", 'yellow'))
    print(color("when oxygen/food/water are critically low!", 'yellow'))
    print()
    print(color("Available reminders:", 'green'))
    print("  1. Oxygen alert (every 4 hours)")
    print("  2. Food check (daily)")
    print("  3. Water monitoring (every 6 hours)")
    print("  4. Cancel all reminders")

    choice = input(color("\nSelect reminder (1-4): ", 'yellow'))

    if choice == '1':
        print(color("\n✅ Cron job scheduled: 'Check oxygen levels'", 'green'))
        print(color("   Command: CronCreate - cron '0 */4 * * *'", 'cyan'))
        print(color("   Reminder: 🫁 Check oxygen - colonists need to breathe!", 'cyan'))
    elif choice == '2':
        print(color("\n✅ Cron job scheduled: 'Daily food check'", 'green'))
        print(color("   Command: CronCreate - cron '0 9 * * *'", 'cyan'))
        print(color("   Reminder: 🍎 Check food supplies for colonists", 'cyan'))
    elif choice == '3':
        print(color("\n✅ Cron job scheduled: 'Water monitoring'", 'green'))
        print(color("   Command: CronCreate - cron '0 */6 * * *'", 'cyan'))
        print(color("   Reminder: 💧 Check water - hydroponics need it!", 'cyan'))
    elif choice == '4':
        print(color("\n✅ All cron reminders cancelled", 'green'))
    else:
        print(color("❌ Invalid choice", 'red'))

def view_tasks():
    """View construction queue - TaskList as colony management"""
    print(color("\n📋 CONSTRUCTION QUEUE (TaskList)", 'cyan'))
    print(color("In Claude Code: This would use TaskCreate to manage", 'yellow'))
    print(color("build queue and track research progress!", 'yellow'))
    print()

    # Load or create tasks
    ensure_local_state_dir()
    tasks_file = LOCAL_TASKS_FILE
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r', encoding='utf-8') as f:
            tasks = json.load(f)
    else:
        tasks = []

    if not tasks:
        print(color("📭 Queue is empty", 'yellow'))
        print(color("\nTo add tasks, use:", 'cyan'))
        print(color("  TaskCreate --subject 'Build Solar Panel' --description 'Need 10 materials'", 'green'))
    else:
        print(color(f"📋 Active tasks ({len(tasks)}):", 'green'))
        for i, task in enumerate(tasks, 1):
            status = task.get('status', 'pending')
            print(f"  {i}. [{status}] {task.get('subject', 'Unknown')}")

def memory_log():
    """Log game events to memory - Memory tool as colony history"""
    print(color("\n🧠 COLONY HISTORY (Memory)", 'cyan'))
    print(color("In Claude Code: This would use the Memory tool to save", 'yellow'))
    print(color("important events, player strategies, and survival notes", 'yellow'))
    print(color("that persist across game sessions!", 'yellow'))
    print()

    player = load_player_data()
    if not player:
        print(color("❌ Register first!", 'red'))
        return

    print(color("Available memory actions:", 'green'))
    print("  1. Save important discovery")
    print("  2. Log rival colony intel")
    print("  3. Record survival tip")
    print("  4. View memory log")

    choice = input(color("\nSelect action (1-4): ", 'yellow'))

    if choice == '1':
        note = input(color("What did you discover? ", 'cyan'))
        print(color(f"\n✅ Saved to Memory: '{note}'", 'green'))
        print(color("   This would be stored in: ~/.claude/projects/.../memory/", 'cyan'))
        print(color("   And persist across Claude sessions!", 'cyan'))
    elif choice == '2':
        player_name = input(color("Rival colony name: ", 'cyan'))
        intel = input(color("What did you learn? ", 'cyan'))
        print(color(f"\n✅ Intel on '{player_name}' saved to Memory", 'green'))
    elif choice == '3':
        tip = input(color("Survival tip: ", 'cyan'))
        print(color(f"\n✅ Tip saved: '{tip}'", 'green'))
    elif choice == '4':
        print(color("\n📜 Memory would show saved entries from previous sessions", 'cyan'))
        print(color("   - Last discovery: Underground ice at sector 7", 'white'))
        print(color("   - Rival intel: Player 'MarsKing' low on oxygen", 'white'))
        print(color("   - Survival tip: Always build solar panels first!", 'white'))
    else:
        print(color("❌ Invalid choice", 'red'))

def show_help():
    """Show help"""
    print(color("\n📖 HELP", 'cyan'))
    print("-" * 50)
    print(color("""
ABOUT:
  Red Planet is a multiplayer survival strategy.
  GitHub repository is the game server.
  Uses Claude Code tools in unintended ways!

COMMANDS:
  status  - Show colony status
  dig     - Dig for ice (water)
  mine    - Mine materials
  build   - Build structure
  sync    - Sync with server
  drone   - Send autonomous drone (Agent)
  cron    - Setup resource reminders (CronCreate)
  tasks   - View construction queue (TaskList)
  memory  - Colony history log (Memory)
  help    - This help
  quit    - Exit

CLAUDE TOOLS AS GAME MECHANICS:
  Memory      - Colony history that persists across sessions
  CronCreate  - Schedule oxygen/water consumption reminders
  TaskList    - Construction and research queue
  Agent       - Autonomous drone explorers
  Read/Edit   - Colony sensors/repairs
  Bash        - Git operations as game moves

GAME CYCLE:
  1. Make a move (dig/mine/build/drone)
  2. Commit auto-saves locally
  3. git push sends move to server
  4. GitHub Actions process events
  5. git pull gets world updates

RESOURCES:
  [O2] Oxygen - consumed each turn
  [H2O] Water - for food and building
  [E] Energy - for all actions
  [F] Food - keeps colonists alive
  [M] Materials - for construction
""", 'green'))

def main():
    """Main game loop"""
    header()

    # Check git repository
    if not os.path.exists('.git'):
        print(color("❌ ERROR: This is not a git repository!", 'red'))
        print(color("   First: git init && git remote add origin <URL>", 'yellow'))
        sys.exit(1)

    # Check registration
    player = load_player_data()
    if not player:
        print(color("🚀 Welcome to Mars!", 'green'))
        print(color("   You've been chosen to build the first colony.", 'yellow'))
        player = register_player()
    else:
        print(color(f"🚀 Welcome back, {player['name']}!"))

    world = load_world_state()
    show_status(player, world)

    # Main loop
    while True:
        print(color("\n┌──────────────────────────────────────────────────┐", 'cyan'))
        print(color("│  COMMANDS: status | dig | mine | build          │", 'white'))
        print(color("│           sync | drone | cron | tasks | memory │", 'white'))
        print(color("│           help | quit                           │", 'white'))
        print(color("└──────────────────────────────────────────────────┘", 'cyan'))

        cmd = input(color("\n➜ ", 'green')).lower().strip()

        if cmd in ['quit', 'exit', 'q']:
            print(color("\n👋 See you on Mars!", 'cyan'))
            break
        elif cmd == 'drone':
            send_drone()
        elif cmd == 'cron':
            setup_cron()
        elif cmd == 'tasks':
            view_tasks()
        elif cmd == 'memory':
            memory_log()
        elif cmd == 'status':
            player = load_player_data()
            world = load_world_state()
            show_status(player, world)
        elif cmd == 'dig':
            dig_ice()
        elif cmd == 'mine':
            mine_materials()
        elif cmd == 'build':
            build()
        elif cmd == 'sync':
            sync_with_server()
        elif cmd == 'help':
            show_help()
        else:
            print(color("❌ Unknown command. Type 'help' for help.", 'red'))

if __name__ == "__main__":
    main()
