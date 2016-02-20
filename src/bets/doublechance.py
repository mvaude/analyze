"""
Class for the bet double chance
three different possibilities:
  - win: Victory from Team 1 or Team 2
  - home: Victory from Team 1 or Draw
  - away: Victory from Team 2 or Draw
"""

from bet import Bet
from football.game import (Game,
                           home_win,
                           away_win,
                           draw)

class DoubleChance(Bet):
    """
    Class with different attributes and method:
    - attributes:
      - scores_home: scores possibilities for home victory
      - scores_away: scores possibilities for home victory
      - scores_draw: scores possibilities for home victory
    >>> test = DoubleChance(0)
    >>> test.name == 'Double Chance'
    True
    """
    def __init__(self, maxScores):
        self.max = maxScores
        self.name = 'Double Chance'
    def win(self):
        """
        Generator for win score combinaison
        >>> [ x for x in DoubleChance(3).win() ]
        [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        """
        for (home, away) in Game(self.max).score_combinaison():
            if home_win(home, away) or away_win(home, away):
                yield (home, away)

    def home(self):
        """
        Generator for home score combinaison
        >>> [ x for x in DoubleChance(3).home() ]
        [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
        """
        for (home, away) in Game(self.max).score_combinaison():
            if home_win(home, away) or draw(home, away):
                yield (home, away)

    def away(self):
        """
        Generator for home score combinaison
        >>> [ x for x in DoubleChance(3).away() ]
        [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        """
        for (home, away) in Game(self.max).score_combinaison():
            if away_win(home, away) or draw(home, away):
                yield (home, away)
