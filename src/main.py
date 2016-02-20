from bets.bet import Bet

def combinaison(score1, score2):
    for x in score1:
        for y in score2:
            yield (x, y)

def bet_1(x, y):
    """
    Bet 1-N-2
    Possibility 1
    """
    if x > y: return True

def bet_2(x, y):
    """
    Bet 1-N-2
    Possibility N
    """
    if x == y: return True

def bet_3(x, y):
    """
    Bet 1-N-2
    Possibility 2
    """
    if y > x: return True

def bet_4(x, y):
    """
    Bet Double Chance
    Possibility 1N
    """
    if x >= y: return True

class Team(object):
    def __init__(self, name):
        self.name = name
        self.possible_scores = [x for x in range(6)]

class Match(object):
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.result = (0, 0)
        self.possible = combinaison(team1.possible_scores, team2.possible_scores)

def put_bet(scores, bet):
    for x in scores:
        if x not in bet: yield x

def print_comb(bets):
    comb = [ x for x in combinaison(range(5), range(5)) ]
    for bet in bets:
        comb = [ x for x in put_bet(comb, [ x for x in bet.possible() ]) ]
    return comb

if __name__ == '__main__':
    turin = Team('Juventus Turin')
    bayern = Team('Bayern Munich')
    today = Match(turin, bayern)
    comb = [ x for x in today.possible ]
    possible = len(comb) + 1
    betting = [ Bet(bet_1), Bet(bet_3) ]
    print('After: {}'.format(print_comb(betting)))
