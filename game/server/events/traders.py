#!/usr/bin/env python3
"""
🛸 Traders from Earth
"""

import json
import random
from datetime import datetime

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def save_world(world):
    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

def main():
    world = load_world()

    event_msg = "🛸 TRADING SHIP FROM EARTH!"
    print(event_msg)
    print("   📦 New resources available for trade")

    # Add resources to global pool
    world['global_resources']['food'] += 100
    world['global_resources']['materials'] += 50

    world['current_event'] = event_msg
    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': event_msg
    })

    save_world(world)

if __name__ == '__main__':
    main()
