from datetime import date
from doomsday import days

days_reversed: dict[int, str] = {val: key for key, val in days.items()}

def anchor_day_century(date: date) -> int:
    """Calculate the anchor day for the century of a given date.

    Args:
        date (date): `datetime.date` object representing the date.

    Raises:
        ValueError: If the date is before 1583. The Gregorian calendar was introduced in 1582.

    Returns:
        int: The anchor day for the century of the given date.
    """
    if date.year < 1583:
        raise ValueError("Date must be after 1582.")
    century = date.year // 100
    anchor_days = [1, 6, 4, 2]
    return anchor_days[century % 4]

def anchor_day_year(date: date, verbose: bool = False) -> int:
    """Calculates the doomsday for the year of a given date.
    Verbose mode prints the steps of this using the "odd+11" method.

    Args:
        date (date): `datetime.date` representing the date.
        verbose (bool, optional): If True, prints the steps of the calculation. Defaults to False.

    Returns:
        int: The doomsday for the year of the given date.
    """
    T = date.year % 100  # last two digits of the year
    if verbose:
        print(f"Let T be the last two digits of the year, T = {T}")
    # if T is odd, we add 11
    if T % 2 == 1:
        T += 11
        if verbose:
            print(f"T is odd, so we add 11 to T to get T = {T}")
    T /= 2  # divide T by 2
    if verbose:
        print(f"Divide T by 2 to get T = {T}")
    # if T is odd, we add 11
    if T % 2 == 1:
        T += 11
        if verbose:
            print(f"T is odd, so we add 11 to T to get T = {T}")
    T = 7 - (T % 7)
    if verbose:
        print(f"Subtract T mod 7 from 7 to get T = {T}")
    # we count forward T days from the anchor day of the century
    century_anchor = anchor_day_century(date)
    doomsday = (century_anchor + T) % 7
    if verbose:
        print(f"Add T to the anchor day of the century to get doomsday = {doomsday}")
    return doomsday




