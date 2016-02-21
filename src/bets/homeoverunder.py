"""
Class for Over Under Bet
  - unde(.5)
  - over(.5)
"""
from bet import Bet


class HomeOverUnder(Bet):
    """
    >>> from football.game import Game
    >>> test = HomeOverUnder(Game(3))
    >>> test.number
    2
    >>> [ score for score in test.bet(test.over, size=0.5) ]
    [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> [ score for score in test.bet(test.under, size=0.5) ]
    [(0, 0), (0, 1), (0, 2)]
    """
    def __init__(self, game):
        super(HomeOverUnder, self).__init__(game)
        self.name = "Home Team Over Under"
        self.number = 2

    @classmethod
    def over(cls, home, away, size):
        """
        >>> HomeOverUnder('').over(1, 0, 0.5)
        True
        """
        del away
        return float(home) > size

    @classmethod
    def under(cls, home, away, size):
        """
        >>> HomeOverUnder('').under(1, 0, 0.5)
        False
        """
        del away
        return float(home) < size
