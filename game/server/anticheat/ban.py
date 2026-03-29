#!/usr/bin/env python3
"""
🚫 Player Ban
"""

import argparse
import os
import json
from datetime import datetime

def ban_player(player_name):
    print(f"🚫 BANNING player: {player_name}")

    # Create ban record
    ban_record = {
        'player': player_name,
        'timestamp': datetime.now().isoformat(),
        'reason': 'Cheating'
    }

    # Add to ban list
    bans = []
    if os.path.exists('bans.json'):
        with open('bans.json', 'r') as f:
            bans = json.load(f)

    bans.append(ban_record)

    with open('bans.json', 'w') as f:
        json.dump(bans, f, indent=2)

    # Move player file (or delete)
    player_file = f'players/{player_name}.json'
    if os.path.exists(player_file):
        os.rename(player_file, f'players/{player_name}.json.banned')
        print(f"   Player file moved")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player', required=True)
    args = parser.parse_args()

    ban_player(args.player)

if __name__ == '__main__':
    main()
