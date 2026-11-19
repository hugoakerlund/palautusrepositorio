from statistics import Statistics
from player_reader import PlayerReader
from parse import parse

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = parse("team = PHI and assists >= 10 and goals < 10 or team = EDM and points >= 50")

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
