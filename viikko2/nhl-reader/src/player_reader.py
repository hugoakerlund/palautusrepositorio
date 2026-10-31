from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players

