#!/usr/bin/env python3
"""
🛸 Traders from Earth
"""

import json
import random
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

    event_msg = "🛸 TRADING SHIP FROM EARTH!"
    facts = [event_msg, "Food +100 to global pool", "Materials +50 to global pool"]
    print(event_msg)
    print("   📦 New resources available for trade")

    # Add resources to global pool
    world['global_resources']['food'] += 100
    world['global_resources']['materials'] += 50

    flavor = attach_event_flavor(world, "traders", facts)
    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': flavor["broadcast"]
    })

    save_world(world)

if __name__ == '__main__':
    main()
