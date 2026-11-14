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


    def handle_draw(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        return "Deuce"


    def handle_greater_than_4(self):
        difference = self.m_score1 - self. m_score2
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        return "Win for player2"

    def handle_less_than_4(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score


    def get_score(self):
        if self.m_score1 == self.m_score2:
            return  self.handle_draw()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.handle_greater_than_4()

        return self.handle_less_than_4()
