#!/usr/bin/env python3
"""
🛡️ Cheating Validation
"""

import json
import os
import sys

def validate_player(filename):
    """Check player data for suspicious values"""
    try:
        with open(f'players/{filename}', 'r') as f:
            player = json.load(f)

        resources = player.get('resources', {})

        # Check for impossible values
        for res, val in resources.items():
            if val < 0:
                print(f"🚨 NEGATIVE RESOURCES for {filename}: {res}={val}")
                return False
            if val > 10000:
                print(f"🚨 SUSPICIOUSLY HIGH {res}: {val}")
                return False

        # Check buildings
        buildings = player.get('buildings', [])
        if len(buildings) > 100:
            print(f"🚨 SUSPICIOUSLY MANY buildings: {len(buildings)}")
            return False

        return True

    except Exception as e:
        print(f"❌ Validation error {filename}: {e}")
        return False

def main():
    if not os.path.exists('players'):
        print("✅ No players to check")
        return

    all_valid = True
    for filename in os.listdir('players'):
        if filename.endswith('.json') and filename != '.gitkeep':
            if not validate_player(filename):
                all_valid = False

    if all_valid:
        print("✅ All checks passed")
        sys.exit(0)
    else:
        print("🚫 Violations detected!")
        sys.exit(1)

if __name__ == '__main__':
    main()
