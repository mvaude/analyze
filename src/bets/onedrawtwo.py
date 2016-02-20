"""
Class for the bet 1-N-2
three different possibilities:
  - home: Victory Team 1
  - away: Victory Team 2
  - draw: No Team Won
"""

from bet import Bet
from football.game import (Game,
                           home_win,
                           away_win)

class OneDrawTwo(Bet):
    """
    Class with different attributes and method:
    - attributes:
      - scores_home: scores possibilities for home victory
      - scores_away: scores possibilities for home victory
      - scores_draw: scores possibilities for home victory
    >>> test = OneDrawTwo(0)
    >>> test.name == '1-N-2'
    True
    """
    def __init__(self, maxScores):
        self.max = maxScores
        self.name = '1-N-2'
    def home(self):
        """
        Generator for home score combinaison
        >>> [ x for x in OneDrawTwo(3).home() ]
        [(1, 0), (2, 0), (2, 1)]
        """
        for (home, away) in Game(self.max).score_combinaison():
            if home_win(home, away):
                yield (home, away)

    def away(self):
        """
        Generator for home score combinaison
        >>> [ x for x in OneDrawTwo(3).away() ]
        [(0, 1), (0, 2), (1, 2)]
        """
        for (home, away) in Game(self.max).score_combinaison():
            if away_win(home, away):
                yield (home, away)
