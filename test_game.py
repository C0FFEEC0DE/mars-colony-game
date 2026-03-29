#!/usr/bin/env python3
"""
🧪 AUTOMATED TESTS for Mars Colony Game
Run with: python3 test_game.py
"""

import json
import os
import sys
import subprocess
from pathlib import Path

def test_python_syntax():
    """Test all Python files compile without errors"""
    print("🐍 Testing Python syntax...")
    errors = []
    py_files = list(Path('.').rglob('*.py'))
    # Exclude common non-source directories
    exclude_dirs = {'__pycache__', 'venv', '.venv', 'env', '.env', '.git', 'node_modules', '.pytest_cache'}
    py_files = [f for f in py_files if not any(excl in str(f) for excl in exclude_dirs)]

    for py_file in py_files:
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'py_compile', str(py_file)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                errors.append(f"{py_file}: {result.stderr}")
        except Exception as e:
            errors.append(f"{py_file}: {e}")

    if errors:
        print(f"❌ {len(errors)} Python files failed syntax check:")
        for err in errors:
            print(f"   {err}")
        return False
    else:
        print(f"✅ All {len(py_files)} Python files syntax OK")
        return True

def test_json_validity():
    """Test all JSON files are valid"""
    print("\n📋 Testing JSON validity...")
    errors = []
    json_files = list(Path('.').rglob('*.json'))
    # Exclude common non-source directories
    exclude_dirs = {'__pycache__', 'venv', '.venv', 'env', '.env', '.git', 'node_modules'}
    json_files = [f for f in json_files if not any(excl in str(f) for excl in exclude_dirs)]

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json.load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{json_file}: {e}")

    if errors:
        print(f"❌ {len(errors)} JSON files invalid:")
        for err in errors:
            print(f"   {err}")
        return False
    else:
        print(f"✅ All {len(json_files)} JSON files valid")
        return True

def test_imports():
    """Test game modules can be imported"""
    print("\n📦 Testing module imports...")
    errors = []

    # Add game to path
    sys.path.insert(0, os.getcwd())

    modules = [
        'game',
        'game.server',
        'game.server.day_cycle',
        'game.server.weather',
        'game.server.leaderboard',
        'game.server.economy.consumption',
        'game.server.economy.production',
        'game.server.economy.energy',
        'game.server.events.meteor_shower',
    ]

    for module in modules:
        try:
            __import__(module)
        except Exception as e:
            errors.append(f"{module}: {e}")

    if errors:
        print(f"❌ {len(errors)} modules failed import:")
        for err in errors:
            print(f"   {err}")
        return False
    else:
        print(f"✅ All {len(modules)} modules imported successfully")
        return True

def test_game_logic():
    """Test basic game logic"""
    print("\n🎮 Testing game logic...")
    errors = []

    # Test world_state.json structure
    try:
        with open('world_state.json', 'r', encoding='utf-8') as f:
            world = json.load(f)
        required_keys = ['day', 'solar_activity', 'events_log']
        for key in required_keys:
            if key not in world:
                errors.append(f"world_state.json missing key: {key}")
    except Exception as e:
        errors.append(f"world_state.json: {e}")

    # Test player data structure
    try:
        test_player = {
            "name": "Test",
            "corporation": "TestCorp",
            "resources": {
                "oxygen": 100,
                "water": 50,
                "energy": 100,
                "food": 50,
                "materials": 20
            },
            "buildings": ["habitat_module"],
            "colonists": 5,
            "last_login": "2026-03-29T00:00:00",
            "turns_today": 0
        }
        # Validate JSON serialization
        json_str = json.dumps(test_player)
        loaded = json.loads(json_str)
        assert loaded['name'] == "Test"
    except Exception as e:
        errors.append(f"Player data structure: {e}")

    if errors:
        print(f"❌ {len(errors)} logic tests failed:")
        for err in errors:
            print(f"   {err}")
        return False
    else:
        print("✅ Game logic tests passed")
        return True

def test_github_actions():
    """Test GitHub Actions workflow files"""
    print("\n⚙️ Testing GitHub Actions workflows...")
    errors = []
    workflow_files = list(Path('.github/workflows').glob('*.yml'))

    # Basic YAML validation
    import yaml
    for wf_file in workflow_files:
        try:
            with open(wf_file, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
        except Exception as e:
            errors.append(f"{wf_file}: {e}")

    if errors:
        print(f"❌ {len(errors)} workflow files invalid:")
        for err in errors:
            print(f"   {err}")
        return False
    else:
        print(f"✅ All {len(workflow_files)} workflow files valid")
        return True

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("🧪 MARS COLONY GAME - AUTOMATED TEST SUITE")
    print("=" * 60)
    print()

    results = []
    results.append(("Python Syntax", test_python_syntax()))
    results.append(("JSON Validity", test_json_validity()))
    results.append(("Module Imports", test_imports()))
    results.append(("Game Logic", test_game_logic()))

    # Check if PyYAML available
    try:
        import yaml
        results.append(("GitHub Actions", test_github_actions()))
    except ImportError:
        print("\n⚠️  PyYAML not installed, skipping GitHub Actions tests")
        print("    Install with: pip install pyyaml")

    print()
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    passed = sum(1 for _, r in results if r)
    total = len(results)
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {name}")

    print()
    if passed == total:
        print(f"🎉 ALL {total} TESTS PASSED!")
        return 0
    else:
        print(f"⚠️  {total - passed}/{total} TESTS FAILED")
        return 1

if __name__ == '__main__':
    exit(run_all_tests())
