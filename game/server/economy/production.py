#!/usr/bin/env python3
"""
🌱 Food Production (hydroponics)
"""

import json
import os

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

                # Greenhouses produce food
                greenhouse_count = buildings.count('greenhouse')
                if greenhouse_count > 0:
                    food_produced = greenhouse_count * 10
                    water_needed = greenhouse_count * 5

                    if player['resources']['water'] >= water_needed:
                        player['resources']['food'] += food_produced
                        player['resources']['water'] -= water_needed
                        print(f"🍎 {player['name']}: +{food_produced} food")

                save_player(filename, player)
            except:
                pass

    print("✅ Production complete")

if __name__ == '__main__':
    main()
