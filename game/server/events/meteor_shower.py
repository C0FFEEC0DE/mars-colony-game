#!/usr/bin/env python3
"""
🌠 Meteor Shower
"""

import json
import os
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

def load_player(filename):
    with open(f'players/{filename}', 'r') as f:
        return json.load(f)

def save_player(filename, player):
    with open(f'players/{filename}', 'w') as f:
        json.dump(player, f, indent=2)

def main():
    world = load_world()

    event_msg = "🌠 METEOR SHOWER!"
    facts = [event_msg]

    # Findings
    if not os.path.exists('players'):
        return

    for filename in os.listdir('players'):
        if filename.endswith('.json') and filename != '.gitkeep':
            try:
                player = load_player(filename)

                # Chance to find materials
                if random.random() < 0.5:
                    materials = random.randint(5, 20)
                    player['resources']['materials'] += materials
                    print(f"   💎 {player['name']} found {materials} materials in meteorites!")
                    facts.append(f"{player['name']} salvaged +{materials} materials")

                # Chance of damage
                if random.random() < 0.2 and player.get('buildings'):
                    print(f"   ⚠️ {player['name']}: buildings damaged!")
                    facts.append(f"{player['name']} reported building damage")

                save_player(filename, player)
            except:
                pass

    flavor = attach_event_flavor(world, "meteor_shower", facts)
    print(flavor["headline"])

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': flavor["broadcast"]
    })

    save_world(world)

if __name__ == '__main__':
    main()
