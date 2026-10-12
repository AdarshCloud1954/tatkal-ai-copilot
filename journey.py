
from datetime import date


def collect_journey():
    print("\n=== Tatkal AI Copilot ===")
    print("Enter your journey preferences.\n")

    source = input("From station code: ").strip().upper()
    destination = input("To station code: ").strip().upper()
    journey_date = input("Journey date (YYYY-MM-DD): ").strip()

    travel_class = input(
        "Travel class (1A, 2A, 3A, SL, CC): "
    ).strip().upper()

    preferred_train = input(
        "Preferred train (or press Enter for any train): "
    ).strip()

    try:
        parsed_date = date.fromisoformat(journey_date)
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return None

    if parsed_date < date.today():
        print("Journey date cannot be in the past.")
        return None

    if not source or not destination or source == destination:
        print("Enter valid, different station codes.")
        return None

    valid_classes = {"1A", "2A", "3A", "SL", "CC"}

    if travel_class not in valid_classes:
        print("Invalid class. Choose 1A, 2A, 3A, SL, or CC.")
        return None

    journey = {
        "from": source,
        "to": destination,
        "date": journey_date,
        "class": travel_class,
        "quota": "TATKAL",
        "preferred_train": preferred_train,
    }

    print("\n=== Journey Details ===")
    for key, value in journey.items():
        print(f"{key}: {value or 'No preference'}")

    return journey


if __name__ == "__main__":
    collect_journey()
