
from journey import collect_journey
from train_selector import rank_trains
from preferences import load_preferences, save_preferences
from preference_parser import parse_request


def main():
    saved = load_preferences()

    if saved:
        answer = input(
            "Use saved journey preferences? (y/n): "
        ).strip().lower()
    else:
        answer = "n"

    if answer == "y":
        journey = saved
        print("\nUsing saved journey preferences.")
    else:
        journey = collect_journey()

        if journey is None:
            return

    request = input(
        "\nDescribe your train preferences in English: "
    ).strip()

    try:
        parsed = parse_request(request)

        if parsed["preferred_train"]:
            journey["preferred_train"] = parsed["preferred_train"]

        journey["class"] = parsed["class"]
        journey["departure_after"] = parsed["departure_after"]

        save_preferences(journey)

        print("\n=== Preferences Applied ===")
        print(f'Preferred train: {journey["preferred_train"] or "Any"}')
        print(f'Class: {journey["class"]}')
        print(f'Departure after: {journey["departure_after"]}')

        ranked = rank_trains(
            preferred_train=journey["preferred_train"],
            travel_class=journey["class"],
            departure_after=journey["departure_after"],
        )

    except (ValueError, KeyError) as error:
        print(f"Could not process preferences: {error}")
        return

    print("\n=== Recommended Sample Trains ===")

    if not ranked:
        print("No matching sample trains found.")
        return

    for position, (score, train) in enumerate(ranked, start=1):
        print(
            f'{position}. {train["name"]} | '
            f'Departure: {train["departure"]} | '
            f'Duration: {train["duration_hours"]} hours | '
            f'Score: {score}'
        )

    print("\nResults use dummy data, not live IRCTC availability.")


if __name__ == "__main__":
    main()
