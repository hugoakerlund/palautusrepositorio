from matchers import *

class QueryBuilder:
    def __init__(self, match=All):
        self._match=match

    def build(self):
        return self._match()

