#!/usr/bin/env python3
"""
🌪️ Dust Storm Processing
"""

import json
import random
import os
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

    if not world['dust_storm_active']:
        print("✅ No storms")
        return

    print("🌪️ Active dust storm!")

    # Damage to all players
    if os.path.exists('players'):
        for filename in os.listdir('players'):
            if filename.endswith('.json') and filename != '.gitkeep':
                try:
                    player = load_player(filename)

                    # Solar panel damage
                    if 'solar_panel' in player.get('buildings', []):
                        energy_loss = random.randint(20, 50)
                        player['resources']['energy'] = max(0, player['resources']['energy'] - energy_loss)
                        print(f"   ⚡ {player['name']}: -{energy_loss} energy")

                    # Visibility loss = can't mine
                    save_player(filename, player)
                except:
                    pass

    world['events_log'].append({
        'time': datetime.now().isoformat(),
        'event': '🌪️ Dust storm damaged colonies!'
    })

    save_world(world)

if __name__ == '__main__':
    main()
