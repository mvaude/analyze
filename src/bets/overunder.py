"""
Class for Over Under Bet
  - unde(.5)
  - over(.5)
"""
from bet import Bet


class OverUnder(Bet):
    """
    >>> from football.game import Game
    >>> [ x for x in OverUnder(Game(3)).over(0.5) ]
    [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> [ x for x in OverUnder(Game(3)).under(0.5) ]
    [(0, 0)]
    """
    def __init__(self, game):
        self.game = game

    def over(self, goals):
        for (home, away) in self.game.score_combinaison():
            if float(home + away) > goals:
                yield (home, away)

    def under(self, goals):
        for (home, away) in self.game.score_combinaison():
            if float(home + away) < goals:
                yield (home, away)
