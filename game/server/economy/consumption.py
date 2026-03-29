#!/usr/bin/env python3
"""
🫁 Colonist Resource Consumption
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
                colonists = player.get('colonists', 5)

                # Base consumption
                player['resources']['oxygen'] = max(0, player['resources']['oxygen'] - colonists * 2)
                player['resources']['food'] = max(0, player['resources']['food'] - colonists)
                player['resources']['water'] = max(0, player['resources']['water'] - colonists // 2)

                # Check starvation
                if player['resources']['food'] == 0:
                    player['colonists'] = max(1, player['colonists'] - 1)
                    print(f"⚠️ {player['name']}: colonists starving!")

                # Check oxygen
                if player['resources']['oxygen'] == 0:
                    player['colonists'] = max(1, player['colonists'] - 2)
                    print(f"🚨 {player['name']}: oxygen depletion!")

                save_player(filename, player)
            except:
                pass

    print("✅ Resource consumption complete")

if __name__ == '__main__':
    main()
