"""
General class for bets
"""


class Bet(object):
    """
    Class for a Bet
    """
    name = ""
    number = 0

    def __init__(self, game):
        self.game = game

    def bet(self, fun, **kwargs):
        """
        Generate combinaison included by bet
        """
        for (home, away) in self.game.score_combinaison():
            if fun(home=home, away=away, **kwargs):
                yield (home, away)
