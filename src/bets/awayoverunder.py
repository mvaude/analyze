"""
Class for Over Under Bet
  - unde(.5)
  - over(.5)
"""
from bet import Bet


class OverUnder(Bet):
    """
    >>> from football.game import Game
    >>> [ score for score in OverUnder(Game(3)).over(0.5) ]
    [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> [ score for score in OverUnder(Game(3)).under(0.5) ]
    [(0, 0)]
    """
    def __init__(self, game):
        self.game = game

    def over(self, goals):
        """
        >>> from football.game import Game
        >>> test = OverUnder(Game(2))
        >>> [ score for score in test.over(0.5)]
        [(0, 1), (1, 0), (1, 1)]
        """
        for (home, away) in self.game.score_combinaison():
            if float(home + away) > goals:
                yield (home, away)

    def under(self, goals):
        """
        >>> from football.game import Game
        >>> test = OverUnder(Game(2))
        >>> [ score for score in test.under(0.5)]
        [(0, 0)]
        """
        for (home, away) in self.game.score_combinaison():
            if float(home + away) < goals:
                yield (home, away)
