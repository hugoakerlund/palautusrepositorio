class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        new_players = list(filter(lambda p: p.nationality == nationality, self.players))
        new_players.sort(key=lambda p: p.points, reverse=True)
        return new_players

    def top_scorers_by_team(self, team):
        new_players = list(filter(lambda p: p.team == team, self.players))
        new_players.sort(key=lambda p: p.points, reverse=True)
        return new_players

    def get_nationalities(self):
        nationalities = set()
        for player in self.players:
            nationalities.add(player.nationality)
        return sorted(list(nationalities))

    def get_teams(self):
        teams = set()
        for player in self.players:
            player_teams = player.team.split(', ')
            for team in player_teams:
                teams.add(team)
        return sorted(list(teams))

    def get_seasons(self):
        seasons = [
                "2018-19",
                "2019-20",
                "2020-21",
                "2021-22",
                "2022-23",
                "2023-24",
                "2024-25",
                "2025-26",
                ]
        return seasons

    def top_goal_scorers(self, how_many):
        new_players = sorted(self.players, key=lambda p: p.goals, reverse=True)
        return new_players[:how_many]
