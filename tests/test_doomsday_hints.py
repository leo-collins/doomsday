import pytest
from datetime import date
from doomsday.doomsday_hints import anchor_day_century, days_reversed

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