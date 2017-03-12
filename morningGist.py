'''Gist'''
import random


class Player(object):
    '''Player'''
    name_ = ""

    def __init__(self, name):
        '''init'''
        self.hand = []
        self.name_ = name
        self.score = -100


class Card(object):
    '''Card'''

    def __init__(self):
        '''init'''
        self.rand = random.randrange(1, 3) * 5
        if self.rand == 10:
            self.name_ = "Dark"
        else:
            self.name_ = "Light"


def three_ten_17(players):
    ''' Game '''
    for numc in range(len(players) * 5):
        players[numc / 5].score = 0
        players[numc / 5].hand.append(Card())
        if numc % 5 == 4:
            for numofcards in range(5):
                players[numc / 5].score += players[numc /
                                                   5].hand[numofcards].rand
    players = sorted(players, key=lambda x: x.score)
    return players[0], players[1].score


GAME_NUMBER = 0
RUNNING = True
while RUNNING:
    PLAYERS_ = [Player("Duck"), Player("Fish"), Player("Snake")]
    WINNER = three_ten_17(PLAYERS_)
    GAME_NUMBER += 1
    for x in range(3):
        GAME_NUMBER + 1
        print_string = "Winner: {}, Score: {}, Game: {}" .format(
            WINNER[0].name_,
            WINNER[1],
            GAME_NUMBER
        )
    print print_string

    if GAME_NUMBER == 3:
        RUNNING = False
raw_input()
