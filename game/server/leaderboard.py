#!/usr/bin/env python3
"""
🏆 Leaderboard
"""

import json
import os

def load_player(filename):
    with open(f'players/{filename}', 'r') as f:
        return json.load(f)

def calculate_score(player):
    """Calculate player score"""
    score = 0
    resources = player.get('resources', {})

    # Points for resources
    score += resources.get('oxygen', 0) * 1
    score += resources.get('water', 0) * 2
    score += resources.get('energy', 0) * 1
    score += resources.get('food', 0) * 3
    score += resources.get('materials', 0) * 5

    # Points for buildings
    score += len(player.get('buildings', [])) * 50

    # Points for colonists
    score += player.get('colonists', 0) * 100

    return score

def main():
    leaderboard = []

    if os.path.exists('players'):
        for filename in os.listdir('players'):
            if filename.endswith('.json') and filename != '.gitkeep':
                try:
                    player = load_player(filename)
                    score = calculate_score(player)
                    leaderboard.append({
                        'name': player['name'],
                        'corp': player.get('corporation', 'Unknown'),
                        'score': score,
                        'colonists': player.get('colonists', 0),
                        'buildings': len(player.get('buildings', []))
                    })
                except:
                    pass

    # Sort by score
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    # Save
    with open('world_state.json', 'r') as f:
        world = json.load(f)

    world['leaderboard'] = leaderboard[:10]  # Top 10

    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

    print("🏆 Leaderboard updated:")
    for i, p in enumerate(leaderboard[:5], 1):
        print(f"   {i}. {p['name']} ({p['corp']}): {p['score']} points")

if __name__ == '__main__':
    main()
