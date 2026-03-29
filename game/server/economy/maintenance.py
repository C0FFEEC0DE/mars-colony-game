#!/usr/bin/env python3
"""
🔧 Degradation and Maintenance
"""

import json
import os
import random

def load_player(filename):
    with open(f'players/{filename}', 'r') as f:
        return json.load(f)

def save_player(filename, player):
    with open(f'players/{filename}', 'w') as f:
        json.dump(player, f, indent=2)

def main():
    if not os.path.exists('players'):
        return

    for filename in os.listdir('players'):
        if filename.endswith('.json') and filename != '.gitkeep':
            try:
                player = load_player(filename)
                buildings = player.get('buildings', [])

                # Random breakdown (1% chance per building)
                if buildings and random.random() < 0.01:
                    broken = random.choice(buildings)
                    # Just notify for now, complex mechanics later
                    print(f"🔧 {player['name']}: {broken} needs repair")

                save_player(filename, player)
            except:
                pass

    print("✅ Integrity check complete")

if __name__ == '__main__':
    main()
