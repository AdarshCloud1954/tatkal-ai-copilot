
import json
from pathlib import Path

PREFERENCES_FILE = Path(__file__).with_name("preferences.json")


def load_preferences():
    if not PREFERENCES_FILE.exists():
        return {}

    try:
        with PREFERENCES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load preferences: {error}")
        return {}


def save_preferences(preferences):
    with PREFERENCES_FILE.open("w", encoding="utf-8") as file:
        json.dump(preferences, file, indent=4)

    print("Preferences saved successfully.")


if __name__ == "__main__":
    preferences = load_preferences()

    print("=== Saved Journey Preferences ===")
    if preferences:
        for key, value in preferences.items():
            print(f"{key}: {value}")
    else:
        print("No saved preferences found.")
