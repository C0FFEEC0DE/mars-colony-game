#!/usr/bin/env python3
"""
🔍 Scientific Discovery
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

    discoveries = [
        "🔍 Underground caverns discovered",
        "📡 Strange signal on 1420 MHz detected",
        "🧪 Unknown bacteria in soil sample",
        "💎 Rare mineral deposits found",
        "🛸 Ancient ruins... or just rocks?"
    ]

    discovery = random.choice(discoveries)
    print(discovery)

    world['current_event'] = discovery
    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': discovery
    })

    save_world(world)

if __name__ == '__main__':
    main()
