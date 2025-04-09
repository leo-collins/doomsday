from doomsday import generate_random_date, is_day_of_week, anchor_day_century, anchor_day_year, calculate_day
import click

@click.command()
@click.option("--explain", is_flag=True, default=False, help="Show explanation for the Doomsday algorithm.")
@click.option("--repeat", is_flag=True, default=False, help="Repeat the game indefinitely.")
@click.option("--proleptic", is_flag=True, default=False, help="Generate proleptic Gregorian dates (dates before 1583).")
def doomsday_game(explain: bool, proleptic: bool, repeat: bool) -> None:
    """
    Play the Doomsday game. Generates a random date and asks the user to guess the day of the week.
    """
    i = 0
    correct = 0
    while True:
        if repeat and i == 0:
            click.echo("Repeating indefinitely. Type 'exit' to exit the game.")
        random_date = generate_random_date(proleptic=proleptic)
        weekday_guess: str = click.prompt(f"Date: {random_date.strftime("%d %B %Y")} (Enter day of the week)", type=str)
        if weekday_guess == "exit":
            click.echo(f"You got {correct} / {i + 1} correct.")
            click.echo("Exiting the game.")
            break
        if is_day_of_week(random_date, weekday_guess):
            click.echo(click.style("Correct! ", fg="green"), nl=False)
            correct += 1
        else:
            click.echo(click.style("Incorrect! ", fg="red"), nl=False)
        click.echo(f"{random_date.strftime('%d %B %Y')} is a {random_date.strftime("%A")}.")
        if explain:
            click.echo("---Explanation---")
            anchor_day_century(random_date, verbose=True)
            anchor_day_year(random_date, verbose=True)
            calculate_day(random_date, verbose=True)
        if not repeat:
            break
        i += 1

