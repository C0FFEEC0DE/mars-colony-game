#!/usr/bin/env python3
"""
Utilities for aggregating world state and rendering README summaries.
"""

from __future__ import annotations

import json
from pathlib import Path

WORLD_FILE = Path("world_state.json")
README_FILE = Path("README.md")
PLAYERS_DIR = Path("players")
README_START = "<!-- WORLD_SUMMARY:START -->"
README_END = "<!-- WORLD_SUMMARY:END -->"


def load_world():
    with WORLD_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_world(world):
    with WORLD_FILE.open("w", encoding="utf-8") as f:
        json.dump(world, f, indent=2)


def load_players():
    players = []
    if not PLAYERS_DIR.exists():
        return players

    for path in sorted(PLAYERS_DIR.glob("*.json")):
        with path.open("r", encoding="utf-8") as f:
            player = json.load(f)
        player["_filename"] = path.name
        players.append(player)

    return players


def calculate_score(player):
    resources = player.get("resources", {})
    score = 0
    score += resources.get("oxygen", 0) * 1
    score += resources.get("water", 0) * 2
    score += resources.get("energy", 0) * 1
    score += resources.get("food", 0) * 3
    score += resources.get("materials", 0) * 5
    score += len(player.get("buildings", [])) * 50
    score += player.get("colonists", 0) * 100
    return score


def update_world_metrics(world, players):
    world["active_colonists"] = sum(player.get("colonists", 0) for player in players)
    world["total_buildings"] = sum(len(player.get("buildings", [])) for player in players)

    global_resources = world.setdefault("global_resources", {})
    for resource in ("oxygen", "water", "energy", "food", "materials"):
        global_resources.setdefault(resource, 0)

    leaderboard = []
    for player in players:
        leaderboard.append(
            {
                "name": player.get("name", "Unknown"),
                "corp": player.get("corporation", "Unknown"),
                "score": calculate_score(player),
                "colonists": player.get("colonists", 0),
                "buildings": len(player.get("buildings", [])),
            }
        )

    leaderboard.sort(key=lambda item: item["score"], reverse=True)
    world["leaderboard"] = leaderboard[:10]
    return world


def _md(value):
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def render_world_summary(world, players):
    event = world.get("current_event") or "None"
    mars_date = world.get("mars_date") or f"Sol {world.get('day', '?')}"
    resources = world.get("global_resources", {})
    market = world.get("market", {})
    recent_events = list(reversed(world.get("events_log", [])[-5:]))

    lines = [
        README_START,
        f"_Auto-updated daily. Last world update: {_md(world.get('last_updated', 'unknown'))}_",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Martian day | {_md(mars_date)} |",
        f"| Season | {_md(world.get('season', 'Unknown'))} |",
        f"| Temperature | {_md(world.get('temperature', 'Unknown'))}°C |",
        f"| Solar activity | {_md(world.get('solar_activity', 'Unknown'))}% |",
        f"| Dust storm | {'Yes' if world.get('dust_storm_active') else 'No'} |",
        f"| Active event | {_md(event)} |",
        f"| Active colonists | {_md(world.get('active_colonists', 0))} |",
        f"| Total buildings | {_md(world.get('total_buildings', 0))} |",
        f"| Registered players | {_md(len(players))} |",
        "",
        "### Global Resources",
        "",
        "| Oxygen | Water | Energy | Food | Materials |",
        "|---|---|---|---|---|",
        f"| {_md(resources.get('oxygen', 0))} | {_md(resources.get('water', 0))} | {_md(resources.get('energy', 0))} | {_md(resources.get('food', 0))} | {_md(resources.get('materials', 0))} |",
        "",
        "### Market Prices",
        "",
        "| Oxygen | Water | Food | Materials |",
        "|---|---|---|---|",
        f"| {_md(market.get('oxygen_price', 0))} | {_md(market.get('water_price', 0))} | {_md(market.get('food_price', 0))} | {_md(market.get('materials_price', 0))} |",
        "",
        "### Colony Standings",
        "",
    ]

    if world.get("leaderboard"):
        lines.extend(
            [
                "| Rank | Colonist | Corporation | Colonists | Buildings | Score |",
                "|---|---|---|---|---|---|",
            ]
        )
        for rank, entry in enumerate(world["leaderboard"], start=1):
            lines.append(
                f"| {rank} | {_md(entry.get('name', 'Unknown'))} | {_md(entry.get('corp', 'Unknown'))} | {_md(entry.get('colonists', 0))} | {_md(entry.get('buildings', 0))} | {_md(entry.get('score', 0))} |"
            )
    else:
        lines.append("_No registered players yet._")

    lines.extend(["", "### Recent Events", ""])

    if recent_events:
        lines.extend(["| Time | Event |", "|---|---|"])
        for entry in recent_events:
            lines.append(f"| {_md(entry.get('time', 'unknown'))} | {_md(entry.get('event', 'unknown'))} |")
    else:
        lines.append("_No world events logged yet._")

    lines.extend(["", README_END, ""])
    return "\n".join(lines)


def write_readme_summary(world, players):
    readme = README_FILE.read_text(encoding="utf-8")
    summary = render_world_summary(world, players)

    if README_START in readme and README_END in readme:
        start = readme.index(README_START)
        end = readme.index(README_END) + len(README_END)
        updated = readme[:start].rstrip() + "\n\n" + summary + readme[end:]
    else:
        updated = readme.rstrip() + "\n\n" + summary + "\n"

    README_FILE.write_text(updated, encoding="utf-8")
