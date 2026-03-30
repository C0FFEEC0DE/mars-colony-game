#!/usr/bin/env python3
"""
Safe AI content generation for the Mars colony game.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
from datetime import datetime
from pathlib import Path
from urllib import error, request

ROOT_DIR = Path(__file__).resolve().parents[2]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from game.server.world_snapshot import load_players, load_world, save_world

API_URL = "https://models.github.ai/inference/chat/completions"
DEFAULT_MODEL = os.getenv("MARS_AI_MODEL", "openai/gpt-4.1-mini")
MAX_EVENTS_LOG = 50

SAFE_EFFECTS = {
    "water_cache": {"target": "resource", "field": "water", "min": 25, "max": 120, "label": "Emergency water cache"},
    "food_relief": {"target": "resource", "field": "food", "min": 15, "max": 80, "label": "Emergency food shipment"},
    "materials_find": {"target": "resource", "field": "materials", "min": 10, "max": 60, "label": "Salvage boom"},
    "oxygen_leak": {"target": "resource", "field": "oxygen", "min": 10, "max": 70, "sign": -1, "label": "Oxygen loss"},
    "energy_surge": {"target": "resource", "field": "energy", "min": 20, "max": 100, "label": "Grid surge"},
    "solar_boost": {"target": "world", "field": "solar_activity", "min": 5, "max": 30, "label": "Solar boost"},
    "cold_snap": {"target": "world", "field": "temperature", "min": 3, "max": 15, "sign": -1, "label": "Cold snap"},
}


def ensure_ai_state(world):
    """Create the shared AI section in world state."""
    ai = world.setdefault("ai", {})
    ai.setdefault("daily_event", {})
    ai.setdefault("missions", [])
    ai.setdefault("npc_transmissions", [])
    ai.setdefault("news_summary", "")
    ai.setdefault("event_flavor", {})
    ai.setdefault("last_diagnostics", {})
    return ai


def trim_text(value, limit, default):
    """Normalize generated text into a compact single line or paragraph."""
    text = " ".join(str(value or "").split())
    if not text:
        text = default
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def clamp(value, low, high):
    """Clamp numeric values into a safe range."""
    return max(low, min(high, int(value)))


def truncate_events_log(world):
    """Keep the event log from growing forever."""
    world["events_log"] = world.get("events_log", [])[-MAX_EVENTS_LOG:]


def summarize_world(world, players):
    """Build a concise world summary for prompts and fallback logic."""
    leaderboard = world.get("leaderboard", [])[:3]
    leaders = ", ".join(
        f"{entry.get('name', 'Unknown')}:{entry.get('score', 0)}"
        for entry in leaderboard
    ) or "no leaderboard"
    resources = world.get("global_resources", {})
    return {
        "day": world.get("day", 0),
        "mars_date": world.get("mars_date", "Unknown"),
        "season": world.get("season", "Unknown"),
        "temperature": world.get("temperature", 0),
        "solar_activity": world.get("solar_activity", 0),
        "dust_storm_active": world.get("dust_storm_active", False),
        "resources": resources,
        "player_count": len(players),
        "leaderboard": leaders,
    }


def extract_json(text):
    """Parse model output even if it comes wrapped in markdown fences."""
    content = text.strip()
    if content.startswith("```"):
        lines = content.splitlines()
        if lines:
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        content = "\n".join(lines).strip()

    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1:
        content = content[start : end + 1]

    return json.loads(content)


def decode_message_content(payload):
    """Handle string and structured message content shapes."""
    message = payload["choices"][0]["message"]["content"]
    if isinstance(message, str):
        return message
    if isinstance(message, list):
        parts = []
        for item in message:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(item.get("text", ""))
        return "\n".join(parts)
    return str(message)


def snippet(value, limit=220):
    """Trim diagnostic strings for logs and world state."""
    text = " ".join(str(value or "").split())
    if len(text) > limit:
        return text[: limit - 1] + "…"
    return text


def build_diagnostics(**kwargs):
    """Create a compact diagnostics object."""
    diagnostics = {
        "provider": "github_models",
        "model": DEFAULT_MODEL,
        "api_url": API_URL,
        "disabled": os.getenv("MARS_DISABLE_GITHUB_MODELS") == "1",
        "token_present": False,
        "token_source": "none",
        "status": "unknown",
        "http_status": None,
        "reason": "",
        "response_excerpt": "",
    }
    diagnostics.update(kwargs)
    return diagnostics


def get_models_token():
    """Prefer an explicit token, fall back to Actions GITHUB_TOKEN."""
    explicit = os.getenv("MARS_AI_TOKEN")
    if explicit:
        return explicit, "MARS_AI_TOKEN"

    inherited = os.getenv("GITHUB_TOKEN")
    if inherited:
        return inherited, "GITHUB_TOKEN"

    return "", "none"


def log_diagnostics(prefix, diagnostics):
    """Print one compact diagnostic line for workflow logs."""
    reason = diagnostics.get("reason") or "ok"
    status = diagnostics.get("status", "unknown")
    http_status = diagnostics.get("http_status")
    token_source = diagnostics.get("token_source", "none")
    message = (
        f"{prefix}: provider={diagnostics.get('provider')} "
        f"status={status} http={http_status} token={token_source} reason={reason}"
    )
    print(snippet(message, 280))
    excerpt = diagnostics.get("response_excerpt")
    if excerpt:
        print(snippet(f"{prefix} response: {excerpt}", 280))


def call_github_models(system_prompt, user_prompt):
    """Call GitHub Models, returning parsed JSON and diagnostics."""
    token, token_source = get_models_token()
    diagnostics = build_diagnostics(
        token_present=bool(token),
        token_source=token_source,
    )
    if diagnostics["disabled"]:
        diagnostics["status"] = "disabled"
        diagnostics["reason"] = "MARS_DISABLE_GITHUB_MODELS=1"
        return None, diagnostics

    if not token:
        diagnostics["status"] = "skipped"
        diagnostics["reason"] = "missing token in env; set GITHUB_TOKEN or MARS_AI_TOKEN"
        return None, diagnostics

    body = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 900,
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    req = request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=20) as response:
            raw = response.read().decode("utf-8")
            diagnostics["http_status"] = getattr(response, "status", 200)
            payload = json.loads(raw)
    except error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        diagnostics["status"] = "http_error"
        diagnostics["http_status"] = exc.code
        diagnostics["reason"] = snippet(exc.reason or "HTTP error", 140)
        diagnostics["response_excerpt"] = raw
        return None, diagnostics
    except error.URLError as exc:
        diagnostics["status"] = "network_error"
        diagnostics["reason"] = snippet(getattr(exc, "reason", exc), 140)
        return None, diagnostics
    except TimeoutError:
        diagnostics["status"] = "timeout"
        diagnostics["reason"] = "request timed out"
        return None, diagnostics
    except json.JSONDecodeError as exc:
        diagnostics["status"] = "decode_error"
        diagnostics["reason"] = snippet(exc, 140)
        return None, diagnostics

    try:
        result = extract_json(decode_message_content(payload))
        diagnostics["status"] = "ok"
        diagnostics["reason"] = "request succeeded"
        return result, diagnostics
    except (KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        diagnostics["status"] = "invalid_response"
        diagnostics["reason"] = snippet(exc, 140)
        diagnostics["response_excerpt"] = payload
        return None, diagnostics


def fallback_daily_payload(world, players):
    """Generate deterministic daily content when AI is unavailable."""
    summary = summarize_world(world, players)
    resources = summary["resources"]
    effects = [
        "water_cache",
        "food_relief",
        "materials_find",
        "oxygen_leak",
        "energy_surge",
        "solar_boost",
        "cold_snap",
    ]
    seed = summary["day"] * 97 + len(players) * 13 + resources.get("materials", 0)
    rng = random.Random(seed)
    effect_type = effects[seed % len(effects)]
    effect_config = SAFE_EFFECTS[effect_type]
    magnitude = rng.randint(effect_config["min"], effect_config["max"])

    mission_templates = [
        {
            "title": "Secure ridge ice cores",
            "briefing": "Survey drones marked a shallow ice seam outside the main habitat ring.",
            "objective": "Bring back intact samples before the sun angle drops.",
            "reward_hint": "Water and science prestige",
            "risk": "Moderate exposure and rover wear",
        },
        {
            "title": "Patch the thermal grid",
            "briefing": "Heat loss is climbing in the outer utility corridor.",
            "objective": "Repair or reinforce one weak point before the next cold cycle.",
            "reward_hint": "Energy stability and spare materials",
            "risk": "Low risk, high urgency",
        },
        {
            "title": "Recover a silent beacon",
            "briefing": "A relay beacon stopped broadcasting west of the colony.",
            "objective": "Reach the site, recover telemetry, and mark salvageable parts.",
            "reward_hint": "Materials and map intel",
            "risk": "Navigation errors in dust",
        },
    ]
    rng.shuffle(mission_templates)

    transmissions = [
        {
            "sender": "Mars Control",
            "recipient": "All colonies",
            "message": "Keep your reports short and your seals tighter. Conditions are changing faster than forecast.",
        },
        {
            "sender": "Orbital Relay",
            "recipient": players[0]["name"] if players else "Lead colonist",
            "message": "Your telemetry is the cleanest on the planet today. Do not waste that advantage.",
        },
    ]

    return {
        "daily_event": {
            "headline": "Operations drift into a new rhythm",
            "summary": (
                f"Sol {summary['day']} opens with thin margins, nervous operators, and one narrow chance "
                f"to shift the colony balance before the next weather swing."
            ),
            "effect_type": effect_type,
            "magnitude": magnitude,
        },
        "missions": mission_templates[:3],
        "npc_transmissions": transmissions,
        "news_summary": (
            f"Sol {summary['day']} begins in {summary['season']} with {summary['player_count']} active colonies. "
            f"Temperature holds near {summary['temperature']}C, solar activity sits at {summary['solar_activity']}%, "
            f"and the current leaders are {summary['leaderboard']}."
        ),
    }


def validate_daily_payload(payload, world, players):
    """Validate and sanitize model daily content."""
    fallback = fallback_daily_payload(world, players)
    daily = payload.get("daily_event", {}) if isinstance(payload, dict) else {}
    missions = payload.get("missions", []) if isinstance(payload, dict) else []
    transmissions = payload.get("npc_transmissions", []) if isinstance(payload, dict) else []
    news_summary = payload.get("news_summary", "") if isinstance(payload, dict) else ""

    effect_type = daily.get("effect_type", fallback["daily_event"]["effect_type"])
    if effect_type not in SAFE_EFFECTS:
        effect_type = fallback["daily_event"]["effect_type"]

    effect_cfg = SAFE_EFFECTS[effect_type]
    magnitude = clamp(
        daily.get("magnitude", fallback["daily_event"]["magnitude"]),
        effect_cfg["min"],
        effect_cfg["max"],
    )

    clean_missions = []
    for mission in missions[:3]:
        if not isinstance(mission, dict):
            continue
        clean_missions.append(
            {
                "title": trim_text(mission.get("title"), 60, "Untitled mission"),
                "briefing": trim_text(mission.get("briefing"), 180, "Mission briefing pending."),
                "objective": trim_text(mission.get("objective"), 120, "Hold position and gather data."),
                "reward_hint": trim_text(mission.get("reward_hint"), 60, "Operational advantage"),
                "risk": trim_text(mission.get("risk"), 60, "Unknown"),
            }
        )
    if not clean_missions:
        clean_missions = fallback["missions"]

    clean_transmissions = []
    for transmission in transmissions[:3]:
        if not isinstance(transmission, dict):
            continue
        clean_transmissions.append(
            {
                "sender": trim_text(transmission.get("sender"), 32, "Mars Control"),
                "recipient": trim_text(transmission.get("recipient"), 32, "All colonies"),
                "message": trim_text(transmission.get("message"), 180, "Maintain station and await further orders."),
            }
        )
    if not clean_transmissions:
        clean_transmissions = fallback["npc_transmissions"]

    return {
        "daily_event": {
            "headline": trim_text(daily.get("headline"), 72, fallback["daily_event"]["headline"]),
            "summary": trim_text(daily.get("summary"), 220, fallback["daily_event"]["summary"]),
            "effect_type": effect_type,
            "magnitude": magnitude,
        },
        "missions": clean_missions,
        "npc_transmissions": clean_transmissions,
        "news_summary": trim_text(news_summary, 280, fallback["news_summary"]),
    }


def apply_effect(world, effect_type, magnitude):
    """Apply one validated effect to the world in a deterministic way."""
    effect_cfg = SAFE_EFFECTS[effect_type]
    sign = effect_cfg.get("sign", 1)
    delta = magnitude * sign

    if effect_cfg["target"] == "resource":
        resources = world.setdefault("global_resources", {})
        field = effect_cfg["field"]
        before = resources.get(field, 0)
        after = max(0, before + delta)
        resources[field] = after
    else:
        field = effect_cfg["field"]
        before = world.get(field, 0)
        after = before + delta
        if field == "solar_activity":
            after = min(150, max(0, after))
        world[field] = after

    return {
        "label": effect_cfg["label"],
        "target": effect_cfg["field"],
        "delta": after - before,
        "before": before,
        "after": after,
    }


def build_daily_prompt(world, players):
    """Create the prompt for daily narrative content."""
    summary = summarize_world(world, players)
    player_lines = []
    for player in players[:5]:
        resources = player.get("resources", {})
        player_lines.append(
            f"- {player.get('name')} of {player.get('corporation')}: "
            f"{player.get('colonists', 0)} colonists, "
            f"resources O2={resources.get('oxygen', 0)} W={resources.get('water', 0)} "
            f"E={resources.get('energy', 0)} F={resources.get('food', 0)} M={resources.get('materials', 0)}"
        )

    effect_names = ", ".join(sorted(SAFE_EFFECTS))
    prompt = f"""
World state:
- Mars day: {summary['mars_date']}
- Season: {summary['season']}
- Temperature: {summary['temperature']}C
- Solar activity: {summary['solar_activity']}%
- Dust storm active: {summary['dust_storm_active']}
- Global resources: {json.dumps(summary['resources'])}
- Leaderboard: {summary['leaderboard']}

Players:
{chr(10).join(player_lines) or "- No active players"}

Return valid JSON only with this shape:
{{
  "daily_event": {{
    "headline": "short title",
    "summary": "1-2 sentence world event",
    "effect_type": "one of: {effect_names}",
    "magnitude": 1
  }},
  "missions": [
    {{
      "title": "mission title",
      "briefing": "short setup",
      "objective": "clear task",
      "reward_hint": "brief reward",
      "risk": "brief risk"
    }}
  ],
  "npc_transmissions": [
    {{
      "sender": "faction or Mars Control",
      "recipient": "all colonies or one colony",
      "message": "short transmission"
    }}
  ],
  "news_summary": "2-3 sentences summarizing the world for a README"
}}

Rules:
- Keep the tone grounded sci-fi, not comedy.
- Missions must be achievable by a small colony.
- Produce 1 to 3 missions.
- Produce 1 to 3 transmissions.
- The effect_type must be one of the allowed values exactly.
- Magnitude must stay modest and believable.
"""
    return prompt.strip()


def generate_daily_content(world, players):
    """Generate, validate, and apply daily AI content."""
    ai = ensure_ai_state(world)
    current_sol = world.get("mars_date", f"Sol {world.get('day', '?')}")
    if ai.get("last_generated_sol") == current_sol and ai.get("daily_event"):
        ai["last_diagnostics"] = build_diagnostics(
            status="cached",
            reason=f"daily content already generated for {current_sol}",
        )
        log_diagnostics("AI diagnostics", ai["last_diagnostics"])
        return "cached", ai["daily_event"]

    system_prompt = (
        "You are a mission director for a Mars colony simulation. "
        "Return only compact JSON. Do not include markdown."
    )
    payload, diagnostics = call_github_models(system_prompt, build_daily_prompt(world, players))
    source = "github_models" if payload is not None else "fallback"
    if payload is None:
        payload = fallback_daily_payload(world, players)
        diagnostics["fallback"] = True
    else:
        diagnostics["fallback"] = False
    ai["last_diagnostics"] = diagnostics
    log_diagnostics("AI diagnostics", diagnostics)

    clean = validate_daily_payload(payload, world, players)
    effect_result = apply_effect(
        world,
        clean["daily_event"]["effect_type"],
        clean["daily_event"]["magnitude"],
    )

    timestamp = datetime.now().isoformat()
    ai["daily_event"] = {
        "headline": clean["daily_event"]["headline"],
        "summary": clean["daily_event"]["summary"],
        "effect": {
            "type": clean["daily_event"]["effect_type"],
            "magnitude": clean["daily_event"]["magnitude"],
            "result": effect_result,
        },
        "source": source,
        "generated_at": timestamp,
    }
    ai["missions"] = clean["missions"]
    ai["npc_transmissions"] = clean["npc_transmissions"]
    ai["news_summary"] = clean["news_summary"]
    ai["last_generated"] = timestamp
    ai["last_generated_sol"] = current_sol
    world["last_updated"] = timestamp

    world.setdefault("events_log", []).append(
        {"time": timestamp, "event": f"AI directive: {clean['daily_event']['headline']}"}
    )
    truncate_events_log(world)
    return source, ai["daily_event"]


def fallback_event_payload(event_key, facts):
    """Fallback flavor text for deterministic events."""
    fact_text = "; ".join(facts) if facts else "field conditions remain unstable"
    templates = {
        "meteor_shower": {
            "headline": "Meteor fragments streak across the colony sky",
            "broadcast": f"Salvage teams report a brief window for collection: {fact_text}.",
        },
        "ice_discovery": {
            "headline": "A fresh ice seam opens beneath the regolith",
            "broadcast": f"Extraction crews are rerouting drills immediately: {fact_text}.",
        },
        "sandstorm": {
            "headline": "A wall of dust is crossing the grid",
            "broadcast": f"Operations shift to storm posture until visibility returns: {fact_text}.",
        },
        "solar_flare": {
            "headline": "Radiation monitors spike as the sun lashes the colony",
            "broadcast": f"Power teams are balancing the surge while shelters stay sealed: {fact_text}.",
        },
        "traders": {
            "headline": "An orbital trader opens an unexpected supply window",
            "broadcast": f"Cargo handlers move fast before the burn window closes: {fact_text}.",
        },
        "discovery": {
            "headline": "Research teams report a discovery worth a second look",
            "broadcast": f"Science crews are locking the site down for analysis: {fact_text}.",
        },
    }
    return templates.get(
        event_key,
        {
            "headline": "Mars operations shift unexpectedly",
            "broadcast": f"Colony command issues a short alert: {fact_text}.",
        },
    )


def build_event_prompt(world, event_key, facts):
    """Create the prompt for one event flavor packet."""
    summary = summarize_world(world, [])
    fact_text = "\n".join(f"- {fact}" for fact in facts) or "- No extra facts"
    return f"""
Write compact JSON only for a Mars colony event bulletin.

World:
- Mars day: {summary['mars_date']}
- Temperature: {summary['temperature']}C
- Solar activity: {summary['solar_activity']}%
- Dust storm active: {summary['dust_storm_active']}

Event key: {event_key}
Facts:
{fact_text}

Return:
{{
  "headline": "short dramatic but grounded title",
  "broadcast": "1-2 sentence flavor bulletin"
}}

Rules:
- Keep facts consistent.
- Ground the language in hard-sci-fi operations, not fantasy.
- Do not invent new mechanical effects.
"""


def attach_event_flavor(world, event_key, facts):
    """Generate flavor text for a deterministic random event."""
    system_prompt = (
        "You write short mission-control bulletins for a Mars survival sim. "
        "Return only JSON."
    )
    payload, diagnostics = call_github_models(system_prompt, build_event_prompt(world, event_key, facts))
    source = "github_models" if payload is not None else "fallback"
    if payload is None:
        payload = fallback_event_payload(event_key, facts)
        diagnostics["fallback"] = True
    else:
        diagnostics["fallback"] = False
    log_diagnostics(f"AI flavor diagnostics [{event_key}]", diagnostics)

    headline = trim_text(payload.get("headline"), 72, fallback_event_payload(event_key, facts)["headline"])
    broadcast = trim_text(payload.get("broadcast"), 220, fallback_event_payload(event_key, facts)["broadcast"])

    ai = ensure_ai_state(world)
    ai["event_flavor"] = {
        "event_key": event_key,
        "headline": headline,
        "broadcast": broadcast,
        "source": source,
        "generated_at": datetime.now().isoformat(),
        "diagnostics": diagnostics,
    }
    world["current_event"] = headline
    return ai["event_flavor"]


def clear_event_flavor(world):
    """Remove stale event flavor when the world resets into a new day."""
    ai = ensure_ai_state(world)
    ai["event_flavor"] = {}


def run_daily_pipeline():
    """CLI entrypoint for the daily AI refresh."""
    players = load_players()
    world = load_world()
    source, event = generate_daily_content(world, players)
    save_world(world)
    print(f"🤖 AI daily briefing generated via {source}: {event['headline']}")


def main():
    """Run the daily AI stage."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--daily", action="store_true", help="Generate daily AI content")
    args = parser.parse_args()

    if args.daily or not any(vars(args).values()):
        run_daily_pipeline()


if __name__ == "__main__":
    main()
