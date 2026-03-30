#!/usr/bin/env python3
"""
🔍 Scientific Discovery
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

    discoveries = [
        "🔍 Underground caverns discovered",
        "📡 Strange signal on 1420 MHz detected",
        "🧪 Unknown bacteria in soil sample",
        "💎 Rare mineral deposits found",
        "🛸 Ancient ruins... or just rocks?"
    ]

    discovery = random.choice(discoveries)
    flavor = attach_event_flavor(world, "discovery", [discovery])
    print(flavor["headline"])

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': flavor["broadcast"]
    })

    save_world(world)

if __name__ == '__main__':
    main()
