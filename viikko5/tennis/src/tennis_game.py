class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1


    def get_draw_situation(self):
        match self.m_score1:
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"


    def handle_advantage(self):
        difference = self.m_score1 - self. m_score2
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_game_situation(self):
        score = ""
        player_score = 0
        for player in range(1, 2 + 1):
            if player == 1:
                player_score = self.m_score1
            else:
                score = score + "-"
                player_score = self.m_score2

            if player_score == 0:
                score = score + "Love"
            elif player_score == 1:
                score = score + "Fifteen"
            elif player_score == 2:
                score = score + "Thirty"
            elif player_score == 3:
                score = score + "Forty"
        return score


    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_draw_situation()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.handle_advantage()

        return self.get_game_situation()
