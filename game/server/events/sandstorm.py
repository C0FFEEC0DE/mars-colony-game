#!/usr/bin/env python3
"""
🌪️ Major Sandstorm
"""

import json
from datetime import datetime

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def save_world(world):
    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

def main():
    world = load_world()

    event_msg = "🌪️ MASSIVE SANDSTORM!"
    print(event_msg)
    print("   All solar panels offline for 6 hours")

    world['current_event'] = event_msg
    world['dust_storm_active'] = True
    world['solar_activity'] = 0

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': event_msg
    })

    save_world(world)

if __name__ == '__main__':
    main()
