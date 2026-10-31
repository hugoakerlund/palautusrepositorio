import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    nationality = "FIN"
    players = get_players_of_nationality(response, nationality)

    print(f"Players from {nationality}:\n")
    for player in players:
        print(player)


def get_players_of_nationality(response, nationality):
    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == nationality:
            players.append(player)

    return players


if __name__ == "__main__":
    main()
