from datetime import datetime
import pytz

def convert_timezone(time_to_convert: datetime, from_tz: str, to_tz: str) -> datetime:
    """
    Converts a datetime object from one time zone to another.

    :param time_to_convert: The datetime object to convert.
    :param from_tz: The source time zone as a string (e.g., "America/New_York").
    :param to_tz: The target time zone as a string (e.g., "Asia/Tokyo").
    :return: The converted datetime object in the target time zone.
    """
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)

    # Localize the given time to the source time zone
    localized_time = from_timezone.localize(time_to_convert)

    # Convert to the target time zone
    converted_time = localized_time.astimezone(to_timezone)

    return converted_time

# Example Usage:
if __name__ == "__main__":
    # Define the time to convert (without timezone info)
    time_to_convert = datetime(2025, 3, 8, 12, 0, 0)  # 12:00 PM

    # Convert from New York time to Tokyo time
    converted_time = convert_timezone(time_to_convert, "America/New_York", "Asia/Tokyo")

    print("Converted Time:", converted_time)
