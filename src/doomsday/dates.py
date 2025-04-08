from datetime import date
import random
from calendar import isleap

days: dict[str, int] = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

def generate_random_date(proleptic: bool = True) -> date:
    """Generates random date.

    Args:
        proleptic (bool, optional): If True, generates a proleptic Gregorian date, i.e. can be before 1582. Defaults to True.

    Returns:
        date: Random date.
    """
    if proleptic:
        year = random.randint(1, 3000)
    else:
        year = random.randint(1583, 3000)
    month = random.randint(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        # February, check for leap year
        if isleap(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    return date(year, month, day)


def is_day_of_week(date_obj: date, day_of_week: str) -> bool:
    """
    Check if the given date is a specific day of the week.
    """
    return date_obj.weekday() == days[day_of_week]