class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()


    def top_scorers_by_nationality(self, nationality):
        new_players = list(filter(lambda p: p.nationality == nationality, self.players))
        new_players.sort(key=lambda p: p.points, reverse=True)
        return new_players
