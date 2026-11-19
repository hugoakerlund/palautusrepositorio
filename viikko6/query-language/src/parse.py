import re

from matchers import And, Not, Or
from query_builder import QueryBuilder


class QuerySyntaxError(ValueError):
    """Raised when a query is empty or does not follow the query language."""


_TOKEN_PATTERN = re.compile(r"\s*(>=|[<>()=]|-?\d+|[A-Za-z_][A-Za-z0-9_-]*)")


class _Parser:
    def __init__(self, query):
        self._tokens = self._tokenize(query)
        self._position = 0

    @staticmethod
    def _tokenize(query):
        if not isinstance(query, str) or not query.strip():
            raise QuerySyntaxError("Query must not be empty")

        tokens = []
        position = 0
        while position < len(query):
            if not query[position:].strip():
                break
            match = _TOKEN_PATTERN.match(query, position)
            if match is None:
                raise QuerySyntaxError(
                    f"Invalid character at position {position}: {query[position]!r}"
                )
            tokens.append(match.group(1))
            position = match.end()

        return tokens

    def parse(self):
        matcher = self._parse_or()
        if self._position != len(self._tokens):
            self._error(f"Unexpected token {self._current()!r}")
        return matcher

    def _parse_or(self):
        matchers = [self._parse_and()]
        while self._accept("or"):
            matchers.append(self._parse_and())
        return matchers[0] if len(matchers) == 1 else Or(*matchers)

    def _parse_and(self):
        matchers = [self._parse_not()]
        while self._accept("and"):
            matchers.append(self._parse_not())
        return matchers[0] if len(matchers) == 1 else And(*matchers)

    def _parse_not(self):
        if self._accept("not"):
            return Not(self._parse_not())
        return self._parse_primary()

    def _parse_primary(self):
        if self._accept("("):
            matcher = self._parse_or()
            self._expect(")")
            return matcher
        return self._parse_condition()

    def _parse_condition(self):
        attribute = self._expect_identifier("Expected an attribute or 'team'")
        operator = self._current()

        if attribute == "team" and operator == "=":
            self._advance()
            team = self._expect_identifier("Expected a team name after '='")
            return QueryBuilder().plays_in(team).build()

        if attribute != "team" and operator in (">=", "<"):
            self._advance()
            value_token = self._current()
            if value_token is None or re.fullmatch(r"-?\d+", value_token) is None:
                self._error(f"Expected an integer after '{operator}'")
            self._advance()
            value = int(value_token)
            query = QueryBuilder()
            if operator == ">=":
                return query.has_at_least(value, attribute).build()
            return query.has_fewer_than(value, attribute).build()

        self._error("Expected 'team = <name>', '<attribute> >= <number>' or '<attribute> < <number>'")

    def _expect_identifier(self, message):
        token = self._current()
        if (
            token is None
            or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", token) is None
            or token in {"and", "or", "not"}
        ):
            self._error(message)
        self._advance()
        return token

    def _expect(self, expected):
        if not self._accept(expected):
            self._error(f"Expected {expected!r}")

    def _accept(self, token):
        if self._current() == token:
            self._advance()
            return True
        return False

    def _current(self):
        if self._position >= len(self._tokens):
            return None
        return self._tokens[self._position]

    def _advance(self):
        self._position += 1

    def _error(self, message):
        raise QuerySyntaxError(f"{message} at token {self._position + 1}")


def parse(query):
    """Parse a query string and return a matcher for it."""
    return _Parser(query).parse()
