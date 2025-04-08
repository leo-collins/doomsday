from doomsday import generate_random_date, is_day_of_week

def doomsday_game() -> None:
    """
    Ask the user for the day of the week and verify it is correct.
    """
    random_date = generate_random_date()
    weekday_guess: str = input(f"Date: {random_date.strftime("%d %B %Y")} (Enter day of the week) ")
    if weekday_guess == "exit":
        print("Exiting the game.")
        return
    if is_day_of_week(random_date, weekday_guess):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"Date: {random_date.strftime('%d %B %Y')} is a {random_date.strftime("%A")}.")

