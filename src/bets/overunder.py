"""
Class for Over Under Bet
  - unde(.5)
  - over(.5)
"""
from bet import Bet
from football.game import Game

class OverUnder(Bet):
    """
    >>> [ x for x in OverUnder().over(0.5) ]
    [(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    >>> [ x for x in OverUnder().under(0.5) ]
    [(0, 0)]
    """

    def over(self, goals):
        for (home, away) in Game(3).score_combinaison():
            if float(home + away) > goals:
                yield (home, away)

    def under(self, goals):
        for (home, away) in Game(3).score_combinaison():
            if float(home + away) < goals:
                yield (home, away)
