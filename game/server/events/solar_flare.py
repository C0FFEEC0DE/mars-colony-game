#!/usr/bin/env python3
"""
⚡ Solar Flare
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

    event_msg = "⚡ MASSIVE SOLAR FLARE!"
    facts = [event_msg, "Energy +50% for next turn", "Take cover from radiation"]
    print(event_msg)
    print("   ⚡ Energy +50% for next turn")
    print("   🛡️ Take cover! Radiation!")

    world['solar_activity'] = 150  # Above normal
    flavor = attach_event_flavor(world, "solar_flare", facts)

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': flavor["broadcast"]
    })

    save_world(world)

if __name__ == '__main__':
    main()
