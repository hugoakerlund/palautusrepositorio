import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url, timeout=5000).json()
        self.players = self.read_players()

    def read_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players

    def get_players(self):
        return self.players
