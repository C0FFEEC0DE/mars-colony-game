#!/usr/bin/env python3
"""
⚡ Energy Generation
"""

import json
import os

def load_player(filename):
    with open(f'players/{filename}', 'r') as f:
        return json.load(f)

def save_player(filename, player):
    with open(f'players/{filename}', 'w') as f:
        json.dump(player, f, indent=2)

def load_world():
    with open('world_state.json', 'r') as f:
        return json.load(f)

def main():
    world = load_world()
    solar_efficiency = world.get('solar_activity', 80) / 100

    if not os.path.exists('players'):
        return

    for filename in os.listdir('players'):
        if filename.endswith('.json') and filename != '.gitkeep':
            try:
                player = load_player(filename)
                buildings = player.get('buildings', [])

                # Solar panels (don't work during storms)
                if not world.get('dust_storm_active', False):
                    panel_count = buildings.count('solar_panel')
                    if panel_count > 0:
                        energy_produced = int(panel_count * 20 * solar_efficiency)
                        player['resources']['energy'] += energy_produced
                        print(f"⚡ {player['name']}: +{energy_produced} energy")
                else:
                    print(f"🌪️ {filename}: solar panels offline (storm)")

                # Oxygen generators
                oxy_count = buildings.count('oxygen_generator')
                if oxy_count > 0:
                    energy_cost = oxy_count * 10
                    if player['resources']['energy'] >= energy_cost:
                        player['resources']['energy'] -= energy_cost
                        player['resources']['oxygen'] += oxy_count * 15
                        print(f"🫁 {player['name']}: +{oxy_count * 15} oxygen")

                save_player(filename, player)
            except:
                pass

    print("✅ Energy cycle complete")

if __name__ == '__main__':
    main()
