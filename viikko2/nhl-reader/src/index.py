from player_reader import PlayerReader
from player_stats import PlayerStats

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationalities = stats.get_nationalities()
    seasons = stats.get_seasons()

    season = Prompt.ask("Season", choices=seasons, default="2024-25")

    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities, default="")

        if not nationality:
            break

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Season {season} players from {nationality}")
        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="left", style="red", no_wrap=True)
        table.add_column("Goals", justify="left", style="green", no_wrap=True)
        table.add_column("Assists", justify="left", style="yellow", no_wrap=True)
        table.add_column("Points", justify="left", style="purple", no_wrap=True)

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))


        console = Console()
        console.print(table)


if __name__ == "__main__":
    main()
