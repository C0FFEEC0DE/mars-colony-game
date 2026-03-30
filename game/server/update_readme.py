#!/usr/bin/env python3
"""
Refresh aggregate world metrics and the README world snapshot.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from game.server.world_snapshot import (
    load_players,
    load_world,
    save_world,
    update_world_metrics,
    write_readme_summary,
)


def main():
    players = load_players()
    world = load_world()
    world = update_world_metrics(world, players)
    save_world(world)
    write_readme_summary(world, players)
    print(f"📘 README updated for {len(players)} players")


if __name__ == "__main__":
    main()
