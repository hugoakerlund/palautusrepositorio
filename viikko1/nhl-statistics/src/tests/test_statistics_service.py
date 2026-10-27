import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
                Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
                Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
                Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
                Player("Yzerman", "DET", 42, 56), # 42+56 = 98
                Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
                ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
                PlayerReaderStub()
                )

    def test_players_can_be_searched(self):
        found_player = self.stats.search("Semenko")
        expected_players = Player("Semenko", "EDM", 4, 12)

    def test_none_is_returned_is_player_does_not_exist(self):
        found_player = self.stats.search("does not exist")
        self.assertEqual(found_player, None)

    def test_players_of_team_can_be_retrieved(self):
        players = self.stats.team("EDM")
        names = sorted(list(map(lambda x: x.name, players)))

        expected_players = [
                Player("Semenko", "EDM", 4, 12),
                Player("Kurri",   "EDM", 37, 53),
                Player("Gretzky", "EDM", 35, 89)
                ]
        expected_names = sorted(list(map(lambda x: x.name, expected_players)))

        self.assertEqual(names, expected_names)

    def test_players_with_highest_scores_can_be_retrieved(self):
        players = self.stats.top(1)

        highest_score = players[0].name
        second_highest_score = players[1].name

        self.assertEqual(highest_score, "Gretzky")
        self.assertEqual(second_highest_score, "Lemieux")

    def test_players_with_most_goals_can_be_retrieved(self):
        players = self.stats.top(1, SortBy.GOALS)

        highest_score = players[0].name
        second_highest_score = players[1].name

        self.assertEqual(highest_score, "Lemieux")
        self.assertEqual(second_highest_score, "Yzerman")


    def test_players_with_most_assists_can_be_retrieved(self):
        players = self.stats.top(1, SortBy.ASSISTS)

        highest_score = players[0].name
        second_highest_score = players[1].name

        self.assertEqual(highest_score, "Gretzky")
        self.assertEqual(second_highest_score, "Yzerman")
