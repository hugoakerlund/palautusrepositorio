import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "assists": "20",
                "goals": "10",
                "games": "82",
                "team": "TOR",
            }),
            Player({
                "name": "Player Two",
                "nationality": "SWE",
                "assists": "30",
                "goals": "15",
                "games": "82",
                "team": "BOS",
            }),
            Player({
                "name": "Player Three",
                "nationality": "FIN",
                "assists": "25",
                "goals": "20",
                "games": "82",
                "team": "TOR",
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(self.players))

    def test_top_scorers_by_nationality_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player One"],
        )

    def test_top_scorers_by_nationality_returns_empty_for_unknown_nationality(self):
        self.assertEqual(
            self.stats.top_scorers_by_nationality("USA"),
            [],
        )

    def test_top_scorers_by_team_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("TOR")

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player One"],
        )

    def test_top_scorers_by_team_returns_empty_for_unknown_team(self):
        self.assertEqual(self.stats.top_scorers_by_team("NYR"), [])

    def test_get_nationalities_returns_sorted_unique_values(self):
        self.assertEqual(self.stats.get_nationalities(), ["FIN", "SWE"])

    def test_get_teams_returns_sorted_unique_values(self):
        self.assertEqual(self.stats.get_teams(), ["BOS", "TOR"])

    def test_get_seasons_returns_supported_seasons(self):
        self.assertEqual(
            self.stats.get_seasons(),
            [
                "2018-19",
                "2019-20",
                "2020-21",
                "2021-22",
                "2022-23",
                "2023-24",
                "2024-25",
                "2025-26",
            ],
        )

    def test_top_goal_scorers_returns_requested_number_in_order(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player Two"],
        )

    def test_top_goal_scorers_returns_all_players_when_limit_is_larger(self):
        result = self.stats.top_goal_scorers(10)

        self.assertEqual(
            [player.name for player in result],
            ["Player Three", "Player Two", "Player One"],
        )


if __name__ == "__main__":
    unittest.main()
