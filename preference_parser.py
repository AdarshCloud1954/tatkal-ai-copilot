
import re


def parse_request(request):
    text = request.lower()

    # Detect travel class.
    travel_class = "3A"

    class_patterns = {
        "1A": r"\b(1a|first ac|first class ac)\b",
        "2A": r"\b(2a|second ac|2 tier ac)\b",
        "3A": r"\b(3a|third ac|3 tier ac)\b",
        "SL": r"\b(sl|sleeper)\b",
        "CC": r"\b(cc|chair car)\b",
    }

    for class_name, pattern in class_patterns.items():
        if re.search(pattern, text):
            travel_class = class_name
            break

    # Detect preferred train.
    preferred_train = ""
    if "rajdhani" in text:
        preferred_train = "Rajdhani"
    elif "telangana express" in text:
        preferred_train = "Telangana Express"

    # Detect departure time.
    departure_after = "00:00"

    time_match = re.search(
        r"(?:after|from)\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?",
        text,
    )

    if time_match:
        hour = int(time_match.group(1))
        minute = int(time_match.group(2) or 0)
        meridiem = time_match.group(3)

        if minute > 59:
            raise ValueError("Invalid minute in departure time.")

        if meridiem:
            if not 1 <= hour <= 12:
                raise ValueError("Invalid 12-hour time.")
            if meridiem == "pm" and hour != 12:
                hour += 12
            elif meridiem == "am" and hour == 12:
                hour = 0
        elif not 0 <= hour <= 23:
            raise ValueError("Invalid 24-hour time.")

        departure_after = f"{hour:02d}:{minute:02d}"

    return {
        "preferred_train": preferred_train,
        "class": travel_class,
        "departure_after": departure_after,
    }


if __name__ == "__main__":
    request = input("Describe your train preferences: ")

    try:
        preferences = parse_request(request)

        print("\n=== Parsed Preferences ===")
        for key, value in preferences.items():
            print(f"{key}: {value or 'No preference'}")

    except ValueError as error:
        print(f"Invalid request: {error}")
