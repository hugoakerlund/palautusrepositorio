from matchers import *

class QueryBuilder:
    def __init__(self, match=All):
        self._match=match

    def plays_in(self, team):
        def create_plays_in_matcher():
            matcher = self._match()
            return And (matcher, PlaysIn(team))
        return QueryBuilder(create_plays_in_matcher)

    def has_at_least(self, value, attr):
        def create_has_at_least_matcher():
            matcher = self._match()
            return And(matcher, HasAtLeast(value, attr))
        return QueryBuilder(create_has_at_least_matcher)

    def has_fewer_than(self, value, attr):
        def create_has_fewer_than_matcher():
            matcher = self._match()
            return And(matcher, HasFewerThan(value, attr))
        return QueryBuilder(create_has_fewer_than_matcher)

    def build(self):
        return self._match()

