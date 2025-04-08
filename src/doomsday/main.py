from doomsday import generate_random_date, is_day_of_week
import click

@click.command()
@click.option("--proleptic", default=False, help="Generate proleptic Gregorian dates.")
@click.option("--repeat", default=False, help="Repeat the game indefinitely.")
def doomsday_game(proleptic, repeat) -> None:
    """
    Play the Doomsday game. Generates a random date and asks the user to guess the day of the week.
    """
    random_date = generate_random_date(proleptic=proleptic)
    weekday_guess: str = click.prompt(f"Date: {random_date.strftime("%d %B %Y")} (Enter day of the week) ")
    if weekday_guess == "exit":
        click.echo("Exiting the game.")
        return
    if is_day_of_week(random_date, weekday_guess):
        click.echo("Correct!")
    else:
        click.echo("Incorrect!")
    click.echo(f"Date: {random_date.strftime('%d %B %Y')} is a {random_date.strftime("%A")}.")

