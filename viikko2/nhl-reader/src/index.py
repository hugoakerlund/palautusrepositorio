from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats



def main():
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2024-25/players")
    stats = PlayerStats(reader)
    seasons = stats.get_seasons()
    season = Prompt.ask("Season", choices=seasons, default="2024-25")
    search_type = Prompt.ask(
        "Search by", choices=["nationality", "team"], default="nationality"
    )

    if search_type == "team":
        show_team_players(stats, season)
    else:
        show_nationality_players(stats, season)


def show_nationality_players(stats, season):
    nationalities = stats.get_nationalities()
    while True:
        nationality = Prompt.ask("Nationality", choices=nationalities, default="")
        if not nationality:
            break

        print_player_table(stats, nationality, season)


def show_team_players(stats, season):
    team = Prompt.ask("Team", choices=stats.get_teams())
    players = stats.top_scorers_by_team(team)
    table = build_table(season, f"for team {team}")
    add_players_to_table(table, players)
    print_table(table)


def print_player_table(stats, nationality, season):
    players = stats.top_scorers_by_nationality(nationality)
    table = build_table(season, f"from {nationality}")
    add_players_to_table(table, players)
    print_table(table)


def build_table(season, filter_description):
    table = Table(title=f"Season {season} players {filter_description}")
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="red", no_wrap=True)
    table.add_column("Goals", justify="left", style="green", no_wrap=True)
    table.add_column("Assists", justify="left", style="yellow", no_wrap=True)
    table.add_column("Points", justify="left", style="purple", no_wrap=True)
    return table


def add_players_to_table(table, players):
    for player in players:
        table.add_row(player.name, player.team, str(player.goals), \
                      str(player.assists), str(player.points))

def print_table(table):
    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
