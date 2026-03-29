#!/usr/bin/env python3
"""
🌅 Mars Day Cycle
Updates global world state
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

    # Increment day
    world['day'] += 1
    world['mars_date'] = f"Sol {world['day']}"
    world['last_updated'] = datetime.now().isoformat()

    # Random temperature
    world['temperature'] = random.randint(-80, -30)

    # Solar activity
    world['solar_activity'] = random.randint(60, 100)

    # Clear old events
    if world.get('current_event'):
        world['current_event'] = None

    # Log the day
    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': f'Martian day {world["day"]} has begun'
    })

    save_world(world)
    print(f"🌅 Mars Day {world['day']} has begun!")
    print(f"   Temperature: {world['temperature']}°C")
    print(f"   Solar activity: {world['solar_activity']}%")

if __name__ == '__main__':
    main()
