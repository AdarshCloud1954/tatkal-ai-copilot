
from datetime import datetime


# Dummy data for testing only.
# These are not verified live train schedules.
TRAINS = [
    {
        "name": "Rajdhani Express",
        "departure": "18:30",
        "travel_class": "3A",
        "duration_hours": 22,
    },
    {
        "name": "Telangana Express",
        "departure": "16:00",
        "travel_class": "3A",
        "duration_hours": 26,
    },
    {
        "name": "Sample Superfast Express",
        "departure": "20:15",
        "travel_class": "3A",
        "duration_hours": 24,
    },
    {
        "name": "Sample Sleeper Express",
        "departure": "19:00",
        "travel_class": "SL",
        "duration_hours": 27,
    },
]


def rank_trains(
    preferred_train="",
    travel_class="3A",
    departure_after="00:00",
):
    try:
        requested_time = datetime.strptime(
            departure_after, "%H:%M"
        ).time()
    except ValueError:
        raise ValueError("Departure time must use HH:MM format.")

    results = []

    for train in TRAINS:
        if train["travel_class"] != travel_class:
            continue

        train_time = datetime.strptime(
            train["departure"], "%H:%M"
        ).time()

        # Exclude trains departing before the requested time.
        if train_time < requested_time:
            continue

        score = 0

        if preferred_train and (
            preferred_train.lower() in train["name"].lower()
        ):
            score += 50

        score += 20
        score += max(0, 30 - train["duration_hours"])

        results.append((score, train))

    results.sort(key=lambda item: item[0], reverse=True)
    return results


if __name__ == "__main__":
    preferred = input("Preferred train: ").strip()
    travel_class = input("Class (3A or SL): ").strip().upper()
    departure_after = input("Departure after (HH:MM): ").strip()

    try:
        ranked = rank_trains(
            preferred,
            travel_class,
            departure_after,
        )

        print("\n=== Ranked Sample Trains ===")

        if not ranked:
            print("No matching sample trains.")
        else:
            for score, train in ranked:
                print(
                    f'{train["name"]} | '
                    f'Departure: {train["departure"]} | '
                    f'Duration: {train["duration_hours"]} hours | '
                    f'Score: {score}'
                )

    except ValueError as error:
        print(f"Error: {error}")
