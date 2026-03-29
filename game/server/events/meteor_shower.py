#!/usr/bin/env python3
"""
🌠 Meteor Shower
"""

import json
import os
import random
from datetime import datetime

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
    print(event_msg)

    world['current_event'] = event_msg

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

                # Chance of damage
                if random.random() < 0.2 and player.get('buildings'):
                    print(f"   ⚠️ {player['name']}: buildings damaged!")

                save_player(filename, player)
            except:
                pass

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': event_msg
    })

    save_world(world)

if __name__ == '__main__':
    main()
