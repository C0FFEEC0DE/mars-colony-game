#!/usr/bin/env python3
"""
🌪️ Major Sandstorm
"""

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from game.server.ai_content import attach_event_flavor

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def save_world(world):
    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

def main():
    world = load_world()

    event_msg = "🌪️ MASSIVE SANDSTORM!"
    facts = [event_msg, "All solar panels offline for 6 hours"]
    print(event_msg)
    print("   All solar panels offline for 6 hours")

    world['dust_storm_active'] = True
    world['solar_activity'] = 0
    flavor = attach_event_flavor(world, "sandstorm", facts)

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': flavor["broadcast"]
    })

    save_world(world)

if __name__ == '__main__':
    main()
