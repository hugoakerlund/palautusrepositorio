import unittest

from parse import QuerySyntaxError, parse
from player import Player


class ParseSyntaxErrorTests(unittest.TestCase):
    def test_empty_queries_raise_query_syntax_error(self):
        for query in ("", "   "):
            with self.subTest(query=query):
                with self.assertRaises(QuerySyntaxError):
                    parse(query)

    def test_query_syntax_error_is_a_value_error(self):
        with self.assertRaises(ValueError):
            parse("goals = 10")

    def test_invalid_queries_raise_query_syntax_error(self):
        invalid_queries = (
            "goals = 10",
            "team =",
            "goals >=",
            "team = NYR and",
            "team = NYR @",
        )
        for query in invalid_queries:
            with self.subTest(query=query):
                with self.assertRaises(QuerySyntaxError):
                    parse(query)


class ParseConditionTests(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player", "NYR", 15, 5)

    def test_team_condition(self):
        self.assertTrue(parse("team = NYR").test(self.player))
        self.assertFalse(parse("team = BOS").test(self.player))

    def test_at_least_condition(self):
        self.assertTrue(parse("goals >= 15").test(self.player))
        self.assertFalse(parse("goals >= 16").test(self.player))

    def test_fewer_than_condition(self):
        self.assertTrue(parse("goals < 16").test(self.player))
        self.assertFalse(parse("goals < 15").test(self.player))

    def test_properties_can_be_used_as_attributes(self):
        self.assertTrue(parse("points >= 20").test(self.player))

    def test_trailing_whitespace_is_allowed(self):
        self.assertTrue(parse("team = NYR   ").test(self.player))


class ParseLogicalOperatorTests(unittest.TestCase):
    def setUp(self):
        self.nyr_player = Player("NYR Player", "NYR", 15, 5)
        self.bos_player = Player("BOS Player", "BOS", 5, 2)

    def test_not_negates_condition(self):
        self.assertFalse(parse("not team = NYR").test(self.nyr_player))
        self.assertTrue(parse("not team = NYR").test(self.bos_player))

    def test_not_can_negate_parenthesized_expression(self):
        matcher = parse("not (team = NYR or goals < 10)")
        self.assertFalse(matcher.test(self.nyr_player))
        self.assertFalse(matcher.test(self.bos_player))
        self.assertTrue(matcher.test(Player("Other", "EDM", 10, 0)))

    def test_and_has_precedence_over_or(self):
        matcher = parse("team = NYR or team = BOS and goals >= 10")
        self.assertTrue(matcher.test(self.nyr_player))
        self.assertFalse(matcher.test(self.bos_player))

    def test_parentheses_override_precedence(self):
        matcher = parse("(team = NYR or team = BOS) and goals >= 10")
        self.assertTrue(matcher.test(self.nyr_player))
        self.assertFalse(matcher.test(self.bos_player))

    def test_nested_parentheses_and_not(self):
        matcher = parse("not ((team = NYR or team = BOS) and goals >= 10)")
        self.assertFalse(matcher.test(self.nyr_player))
        self.assertTrue(matcher.test(self.bos_player))

    def test_malformed_parentheses_and_operators_are_rejected(self):
        invalid_queries = (
            "(team = NYR",
            "team = NYR)",
            "()",
            "not",
            "not and team = NYR",
            "team = NYR or or goals < 10",
        )
        for query in invalid_queries:
            with self.subTest(query=query):
                with self.assertRaises(QuerySyntaxError):
                    parse(query)


if __name__ == "__main__":
    unittest.main()
