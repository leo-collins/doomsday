from datetime import date
from doomsday import days

days_reversed: dict[int, str] = {val: key for key, val in days.items()}

def anchor_day_century(date: date) -> int:
    """
    Calculate the anchor day for the century of a given date.
    """
    if date.year < 1583:
        raise ValueError("Date must be after 1582.")
    century = date.year // 100
    anchor_days = [1, 6, 4, 2]  # Anchor days for the centuries 1700, 1800, 1900, and 2000 respectively
    return anchor_days[century % 4]

def anchor_day_year(date: date) -> int:
    ...

