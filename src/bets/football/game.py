"""
Class describe game and attributes and methods needed
"""

def home_win(home, away):
    """
    Return true if home wins
    >>> home_win(1, 0)
    True
    >>> home_win(0, 0)
    False
    >>> home_win(0, 1)
    False
    """
    return home > away


def away_win(home, away):
    """
    Return true if home wins
    >>> away_win(1, 0)
    False
    >>> away_win(0, 0)
    False
    >>> away_win(0, 1)
    True
    """
    return home < away


def draw(home, away):
    """
    Return true if home wins
    >>> draw(1, 0)
    False
    >>> draw(0, 0)
    True
    >>> draw(0, 1)
    False
    """
    return home == away


class Game(object):
    """
    Class of a game with simple conditions
    >>> Game(2).max
    2
    """
    def __init__(self, max_scores):
        self.max = max_scores

    def score_combinaison(self):
        """
        Generate a score combination
        >>> [ x for x in Game(3).score_combinaison() ]
        ... # doctest: +NORMALIZE_WHITESPACE
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1),
        (1, 2), (2, 0), (2, 1), (2, 2)]
        """
        for home in range(self.max):
            for away in range(self.max):
                yield (home, away)
