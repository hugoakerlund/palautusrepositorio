class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = int(player_dict['assists'])
        self.goals = int(player_dict['goals'])
        self.games = int(player_dict['games'])
        self.team = player_dict['team']
        self.points = self.set_points()

    def set_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:20} \
                {self.goals} + {self.assists} = {self.points}"
