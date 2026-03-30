#!/usr/bin/env python3
"""
Utilities for aggregating world state and rendering README summaries.
"""

from __future__ import annotations

import json
import textwrap
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


def _box_lines(title, rows, content_width=34):
    title_text = f" {title} "
    content_width = max(content_width, len(title_text))
    wrapped_rows = []
    for row in rows:
        segments = textwrap.wrap(str(row), width=content_width) or [""]
        wrapped_rows.extend(segments)

    top = "╔" + title_text.center(content_width + 2, "═") + "╗"
    body = [f"║ {row.ljust(content_width)} ║" for row in wrapped_rows]
    bottom = "╚" + ("═" * (content_width + 2)) + "╝"
    return [top, *body, bottom]


def _box(title, rows, content_width=34):
    return "\n".join(_box_lines(title, rows, content_width=content_width))


def _merge_boxes(left_lines, right_lines, gap="  "):
    height = max(len(left_lines), len(right_lines))
    left_width = max(len(line) for line in left_lines)
    right_width = max(len(line) for line in right_lines)
    padded_left = left_lines + ([" " * left_width] * (height - len(left_lines)))
    padded_right = right_lines + ([" " * right_width] * (height - len(right_lines)))
    return "\n".join(
        f"{left.ljust(left_width)}{gap}{right.ljust(right_width)}"
        for left, right in zip(padded_left, padded_right)
    )


def _fit(text, width):
    text = str(text)
    if len(text) <= width:
        return text.ljust(width)
    if width <= 1:
        return text[:width]
    return text[: width - 1] + "…"


def _short(text, width):
    text = str(text).replace("\n", " ")
    if len(text) <= width:
        return text
    return textwrap.shorten(text, width=width, placeholder="…")


def render_world_summary(world, players):
    event = world.get("current_event") or "None"
    mars_date = world.get("mars_date") or f"Sol {world.get('day', '?')}"
    resources = world.get("global_resources", {})
    market = world.get("market", {})
    ai = world.get("ai", {})
    daily_event = ai.get("daily_event", {})
    missions = ai.get("missions", [])
    transmissions = ai.get("npc_transmissions", [])
    news_summary = ai.get("news_summary", "")
    event_flavor = ai.get("event_flavor", {})
    recent_events = list(reversed(world.get("events_log", [])[-5:]))
    headline_rows = [
        f"[SOL] {mars_date} | [SEASON] {world.get('season', 'Unknown')}",
        f"[TEMP] {world.get('temperature', 'Unknown')}C | [SUN] {world.get('solar_activity', 'Unknown')}% | [STORM] {'YES' if world.get('dust_storm_active') else 'NO'}",
        f"[EVENT] {event}",
        f"[POP] {world.get('active_colonists', 0)} | [BLD] {world.get('total_buildings', 0)} | [PLY] {len(players)}",
        f"[O2] {resources.get('oxygen', 0)} | [H2O] {resources.get('water', 0)} | [E] {resources.get('energy', 0)}",
        f"[FOOD] {resources.get('food', 0)} | [MAT] {resources.get('materials', 0)}",
        f"[MKT] O2 {market.get('oxygen_price', 0)} H2O {market.get('water_price', 0)} F {market.get('food_price', 0)} M {market.get('materials_price', 0)}",
    ]
    if daily_event:
        effect = daily_event.get("effect", {})
        result = effect.get("result", {})
        headline_rows.append(
            f"[AI] {daily_event.get('headline', 'Pending')} | {result.get('target', 'directive')} {result.get('delta', 0):+}"
        )
    reserve_rows = [
        f"OXYGEN    {resources.get('oxygen', 0)}",
        f"WATER     {resources.get('water', 0)}",
        f"ENERGY    {resources.get('energy', 0)}",
        f"FOOD      {resources.get('food', 0)}",
        f"MATERIALS {resources.get('materials', 0)}",
    ]
    standings_rows = []
    for rank, entry in enumerate(world.get("leaderboard", []), start=1):
        standings_rows.extend(
            [
                f"{rank}. {_short(entry.get('name', 'Unknown'), 28)}",
                f"   {_short(entry.get('corp', 'Unknown'), 14)} | P{entry.get('colonists', 0)} B{entry.get('buildings', 0)} | S{entry.get('score', 0)}",
            ]
        )
    if not standings_rows:
        standings_rows = ["NO REGISTERED PLAYERS"]

    ai_event_rows = [
        daily_event.get("headline", "AI directive pending"),
        daily_event.get("summary", "No AI directive generated yet."),
    ]
    if daily_event:
        effect = daily_event.get("effect", {})
        result = effect.get("result", {})
        ai_event_rows.append(
            f"EFFECT {effect.get('type', 'unknown')} | {result.get('target', 'n/a')} {result.get('delta', 0):+}"
        )

    mission_rows = []
    for idx, mission in enumerate(missions[:3], start=1):
        mission_rows.append(f"{idx}. {_short(mission.get('title', 'Untitled'), 30)}")
        mission_rows.append(f"   {_short(mission.get('objective', 'Stand by'), 31)}")
    if not mission_rows:
        mission_rows = ["MISSION BOARD OFFLINE"]

    transmission_rows = [
        f"{_short(item.get('sender', 'Mars Control'), 14)} -> {_short(item.get('recipient', 'All'), 10)}"
        f" | {_short(item.get('message', ''), 34)}"
        for item in transmissions[:3]
    ] or ["NO TRANSMISSIONS"]

    news_rows = [news_summary] if news_summary else ["No colony news generated yet."]
    if world.get("current_event") and event_flavor:
        news_rows.append(event_flavor.get("broadcast", ""))

    event_rows = [
        f"{str(entry.get('time', 'unknown'))[11:16]} | {_short(entry.get('event', 'unknown'), 28)}"
        for entry in recent_events
    ] or ["NO WORLD EVENTS LOGGED"]

    dashboard_rows = [
        _merge_boxes(
            _box_lines("LIVE WORLD SNAPSHOT", headline_rows),
            _box_lines("AI DAILY DIRECTIVE", ai_event_rows),
        ),
        _merge_boxes(
            _box_lines("COLONY STANDINGS", standings_rows),
            _box_lines("MISSION BOARD", mission_rows),
        ),
        _merge_boxes(
            _box_lines("RESOURCE RESERVES", reserve_rows),
            _box_lines("NPC TRANSMISSIONS", transmission_rows),
        ),
        _merge_boxes(
            _box_lines("COLONY NEWS FEED", news_rows),
            _box_lines("RECENT EVENTS", event_rows),
        ),
    ]

    lines = [
        README_START,
        f"_Auto-updated daily. Last world update: {_md(world.get('last_updated', 'unknown'))}_",
        "",
        "```text",
        "\n\n".join(dashboard_rows),
        "```",
    ]

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
