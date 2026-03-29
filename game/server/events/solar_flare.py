#!/usr/bin/env python3
"""
⚡ Solar Flare
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

    event_msg = "⚡ MASSIVE SOLAR FLARE!"
    print(event_msg)
    print("   ⚡ Energy +50% for next turn")
    print("   🛡️ Take cover! Radiation!")

    world['current_event'] = event_msg
    world['solar_activity'] = 150  # Above normal

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': event_msg
    })

    save_world(world)

if __name__ == '__main__':
    main()
