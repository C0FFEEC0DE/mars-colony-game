#!/usr/bin/env python3
"""
🌡️ Mars Weather
"""

import json
import random
from datetime import datetime

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def save_world(world):
    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

def main():
    world = load_world()

    # Seasons on Mars
    season_num = (world['day'] % 668) // 167  # 668 sols in a year
    seasons = ['Early Spring', 'Spring', 'Summer', 'Fall', 'Winter']
    world['season'] = seasons[season_num]

    # Dust storm probability
    if random.random() < 0.1:  # 10% chance
        world['dust_storm_active'] = True
        print("🌪️ WARNING: Dust storm on the horizon!")
    else:
        world['dust_storm_active'] = False
        print("☀️ Weather is stable")

    save_world(world)

if __name__ == '__main__':
    main()
