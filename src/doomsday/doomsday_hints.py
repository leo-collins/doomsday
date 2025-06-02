from datetime import date
from doomsday import days
from calendar import isleap

days_reversed: dict[int, str] = {val: key for key, val in days.items()}
memorable_dates: dict[int, tuple[int, str]] = {
    1: (3, "3rd 3 years in 4, 4th in the 4th"),
    2: (28, "Last day of February"),
    3: (14, "Pi day"),
    4: (4, "4/4, 6/6, 8/8, 10/10, 12/12"),
    5: (9, "Working 9-5 at 7-11"),
    6: (6, "4/4, 6/6, 8/8, 10/10, 12/12"),
    7: (11, "Working 9-5 at 7-11"),
    8: (8, "4/4, 6/6, 8/8, 10/10, 12/12"),
    9: (5, "Working 9-5 at 7-11"),
    10: (10, "4/4, 6/6, 8/8, 10/10, 12/12"),
    11: (7, "Working 9-5 at 7-11"),
    12: (12, "4/4, 6/6, 8/8, 10/10, 12/12"),
}
months: dict[int, str] = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


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


def calculate_day(date: date, verbose: bool = False) -> int:
    """Calculates the day of the week for a given date using the Doomsday algorithm.

    Args:
        date (date): _description_
        verbose (bool, optional): _description_. Defaults to False.

    Returns:
        int: _description_
    """
    memorable_date, mnemonic = memorable_dates[date.month]
    year_doomsday = anchor_day_year(date)
    if isleap(date.year):
        if date.month in [1, 2]:
            memorable_date += 1
    if verbose:
        print("")
        print(f"Step 3: Calculate the day")
        print(f"1) The doomsday for {months[date.month]} is {memorable_date} ({mnemonic}).")

    if date.day > memorable_date:
        # if the day is greater than the doomsday, we count forward
        difference = date.day - memorable_date
        day_of_week = (year_doomsday + difference) % 7
        if verbose:
            print(f"2) The date is {difference} days after the doomsday.")
            print(f"   We do doomsday + {difference} (mod 7) to get the day of the week.")
            print(f"   The day of the week is {year_doomsday} + {difference % 7} = {day_of_week}, which is a {days_reversed[day_of_week]}.")
        return day_of_week
    elif date.day < memorable_date:
        # if the day is less than the doomsday, we count backward
        difference = memorable_date - date.day
        day_of_week = (year_doomsday - difference) % 7
        if verbose:
            print(f"2) The date is {difference} days before the doomsday.")
            print(f"   We do doomsday - {difference} (mod 7) to get the day of the week.")
            print(f"   The day of the week is {year_doomsday} - {difference % 7} = {day_of_week}, which is a {days_reversed[day_of_week]}.")
        return day_of_week
    else:
        # if the day is equal to the doomsday, we return the doomsday
        if verbose:
            print(f"2) The date is a doomsday.")
            print(f"   The day of the week is {year_doomsday}, which is a {days_reversed[year_doomsday]}.")
        return year_doomsday