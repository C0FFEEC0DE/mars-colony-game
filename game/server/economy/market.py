#!/usr/bin/env python3
"""
📈 Market - Dynamic Prices
"""

import json
import random

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def save_world(world):
    with open('world_state.json', 'w') as f:
        json.dump(world, f, indent=2)

def main():
    world = load_world()

    # Initialize market if missing
    if 'market' not in world:
        world['market'] = {
            'oxygen_price': 1,
            'water_price': 2,
            'food_price': 3,
            'materials_price': 5
        }

    # Random fluctuations
    for resource in world['market']:
        change = random.uniform(0.9, 1.1)
        world['market'][resource] = int(world['market'][resource] * change)

    save_world(world)
    print("📈 Prices updated:")
    for res, price in world['market'].items():
        print(f"   {res}: {price}")

if __name__ == '__main__':
    main()
