
from datetime import datetime, timedelta
import sys


def time_since(start_time_str):
    # parse input time (HH:MM)
    start_time = datetime.strptime(start_time_str, "%H:%M").replace(
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day
    )

    now = datetime.now()

    # If the time is in the future (e.g. past midnight), assume it's from yesterday
    if start_time > now:
        start_time -= timedelta(days=1)

    diff = now - start_time
    return diff

if __name__ == "__main__":
    start_input = input("Enter start time (HH:MM): ")

    diff = time_since(start_input)

    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) / 60

    print(f"Time since start: {hours} hours and {int(minutes)} minutes.")

    if diff.seconds <= (6*3600):
        hours_with_pause = hours
        min_with_pause = minutes
    elif diff.seconds > (6*3600) and diff.seconds < (6*3600 + 30*60):
        hours_with_pause = 6
        min_with_pause = 0
    elif diff.seconds >= (6*3600 + 30*60) and diff.seconds < (9*3600 + 30*60):
        sec_with_pause = diff.seconds - (30*60)
        hours_with_pause = sec_with_pause // 3600
        min_with_pause = (sec_with_pause % 3600) / 60
    elif diff.seconds >= (9*3600 + 30*60) and diff.seconds < (9*3600 + 45*60):
        hours_with_pause = 9
        min_with_pause = 0
    else:
        sec_with_pause = diff.seconds - (45*60)
        hours_with_pause = sec_with_pause // 3600
        min_with_pause = (sec_with_pause % 3600) / 60

    print(f"Time with pause since start: {hours_with_pause} hours and {int(min_with_pause)} minutes.")
