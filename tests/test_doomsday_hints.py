import pytest
from datetime import date
from doomsday.doomsday_hints import anchor_day_century, anchor_day_year, days_reversed, calculate_day

@pytest.mark.parametrize(
    "year, expected_anchor_day",
    [
        (1600, "Tuesday"),
        (1700, "Sunday"),
        (1800, "Friday"),
        (1900, "Wednesday"),
        (2000, "Tuesday"),
        (2100, "Sunday"),
        (2200, "Friday"),
        (2300, "Wednesday"),
    ],
)
def test_anchor_day_century(year: int, expected_anchor_day: str):
    """
    Test the anchor day for the century.
    """
    date_obj = date(year, 1, 1)
    assert days_reversed[anchor_day_century(date_obj)] == expected_anchor_day

@pytest.mark.parametrize(
        "date_obj, doomsday",
        [
            (date(2025, 1, 1), "Friday"),
            (date(2024, 1, 1), "Thursday"),
            (date(2023, 1, 1), "Tuesday"),
            (date(2022, 1, 1), "Monday"),
            (date(2021, 1, 1), "Sunday"),
            (date(1945, 1, 1), "Wednesday"),
            (date(1847, 1, 1), "Sunday"),
            (date(1799, 1, 1), "Thursday"),
            (date(2080, 1, 1), "Thursday"),
            (date(2079, 1, 1), "Tuesday")
        ]
)
def test_year_anchor_day(date_obj: date, doomsday: str):
    """
    Test the anchor day for the year.
    """
    assert days_reversed[anchor_day_year(date_obj)] == doomsday

@pytest.mark.parametrize(
        "date_obj, expected_day",
        [
            (date(2025, 4, 9), "Wednesday"),
            (date(2000, 9, 11), "Monday"),
            (date(2024, 2, 29), "Thursday"),
            (date(2000, 2, 29), "Tuesday"),
            (date(1900, 2, 28), "Wednesday"),
            (date(1900, 3, 1), "Thursday"),
            (date(1985, 9, 18), "Wednesday"),
        ]
)
def test_day(date_obj: date, expected_day: str):
    """
    Test the day of the week.
    """
    assert days_reversed[calculate_day(date_obj)] == expected_day