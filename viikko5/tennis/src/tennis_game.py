class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1


    def get_draw_situation(self):
        match self.player1_score:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
        return "Deuce"


    def get_advantage_situation(self):
        advantage = self.player1_score - self. player2_score

        if abs(advantage) >= 2:
            return self.get_winner(advantage)

        elif advantage == 1:
            return "Advantage player1"
        return "Advantage player2"

    def get_winner(self, advantage):
        if advantage >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_game_situation(self):
        score = ""
        player_score = self.player1_score
        for player in range(1, 2 + 1):
            if player == 2:
                score += "-"
                player_score = self.player2_score

            match player_score:
                case 0:
                    score += "Love"
                case 1:
                    score += "Fifteen"
                case 2:
                    score += "Thirty"
                case 3:
                    score += "Forty"
        return score


    def get_score(self):
        advantage_point = 4
        if self.player1_score == self.player2_score:
            return self.get_draw_situation()

        elif self.player1_score >= advantage_point or \
             self.player2_score >= advantage_point:
                return self.get_advantage_situation()

        return self.get_game_situation()
