from datetime import date
from doomsday import days

days_reversed: dict[int, str] = {val: key for key, val in days.items()}

def anchor_day_century(date: date, verbose: bool = False) -> int:
    """Calculate the anchor day for the century of a given date.

    Args:
        date (date): `datetime.date` object representing the date.

    Returns:
        int: The anchor day for the century of the given date.
    """
    century = date.year // 100
    anchor_days = [1, 6, 4, 2]
    anchor_day = anchor_days[century % 4]
    if verbose:
        print("Step 1: Calculate the century anchor day")
        print(f"Century: {century * 100}, Century anchor day: {days_reversed[anchor_day]} ({anchor_day})")
    return anchor_day

def anchor_day_year(date: date, verbose: bool = False) -> int:
    """Calculates the doomsday for the year of a given date using the "odd + 11" method.

    Args:
        date (date): `datetime.date` representing the date.
        verbose (bool, optional): If True, prints the steps of the calculation. Defaults to False.

    Returns:
        int: The doomsday for the year of the given date.
    """
    T = date.year % 100  # last two digits of the year
    if verbose:
        print("")
        print("Step 2: Calculate the doomsday for the year")
        print(f"1) Let T be the last two digits of the year, T = {T}")
    # if T is odd, we add 11
    if T % 2 == 1:
        T += 11
        if verbose:
            print(f"2) T is odd, so we add 11 to T to get T = {T}")
    else:
        if verbose:
            print(f"2) T is even, so we don't add 11 to T")
    T //= 2  # divide T by 2
    if verbose:
        print(f"3) Divide T by 2 to get T = {T}")
    # if T is odd, we add 11
    if T % 2 == 1:
        T += 11
        if verbose:
            print(f"4) T is odd, so we add 11 to get T = {T}")
    else:
        if verbose:
            print(f"4) T is even, so we don't add 11 to T")
    T_mod7 = T % 7
    T = 7 - T_mod7
    if verbose:
        print(f"5) We calculate 7 - (T mod 7) = 7 - {T_mod7} = {T}")
    # we count forward T days from the anchor day of the century
    century_anchor = anchor_day_century(date)
    doomsday = (century_anchor + T) % 7
    if verbose:
        print(f"6) Add {T} to the anchor day of the century to get doomsday is {days_reversed[doomsday]} ({doomsday})")
    return doomsday


