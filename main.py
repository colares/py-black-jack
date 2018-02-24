import random
import os


def clear():
    os.system('clear')


class Deck(object):
    def __init__(self, cards):
        # hearts, diamonds, clubs, spades
        self.cards = cards

    def get_card(self):
        return self.cards.pop()


class Card(object):
    # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
    # example u'\U0001f0d1'
    icons = {
        'na': '\U0001f0a0',
        'sa': '\U0001f0a1',
        's2': '\U0001f0a2',
        's3': '\U0001f0a3',
        's4': '\U0001f0a4',
        's5': '\U0001f0a5',
        's6': '\U0001f0a6',
        's7': '\U0001f0a7',
        's8': '\U0001f0a8',
        's9': '\U0001f0a9',
        's10': '\U0001f0aa',
        'sj': '\U0001f0ab',
        'sq': '\U0001f0ad',
        'sk': '\U0001f0ae',
        'ha': '\U0001f0b1',
        'h2': '\U0001f0b2',
        'h3': '\U0001f0b3',
        'h4': '\U0001f0b4',
        'h5': '\U0001f0b5',
        'h6': '\U0001f0b6',
        'h7': '\U0001f0b7',
        'h8': '\U0001f0b8',
        'h9': '\U0001f0b9',
        'h10': '\U0001f0ba',
        'hj': '\U0001f0bb',
        'hq': '\U0001f0bd',
        'hk': '\U0001f0be',
        'da': '\U0001f0c1',
        'd2': '\U0001f0c2',
        'd3': '\U0001f0c3',
        'd4': '\U0001f0c4',
        'd5': '\U0001f0c5',
        'd6': '\U0001f0c6',
        'd7': '\U0001f0c7',
        'd8': '\U0001f0c8',
        'd9': '\U0001f0c9',
        'd10': '\U0001f0ca',
        'dj': '\U0001f0cb',
        'dq': '\U0001f0cd',
        'dk': '\U0001f0ce',
        'ca': '\U0001f0d1',
        'c2': '\U0001f0d2',
        'c3': '\U0001f0d3',
        'c4': '\U0001f0d4',
        'c5': '\U0001f0d5',
        'c6': '\U0001f0d6',
        'c7': '\U0001f0d7',
        'c8': '\U0001f0d8',
        'c9': '\U0001f0d9',
        'c10': '\U0001f0da',
        'cj': '\U0001f0db',
        'cq': '\U0001f0dd',
        'ck': '\U0001f0de'
    }

    def __init__(self,number,suit,value):
        self.number = number
        self.suit = suit
        self.value = value

    def __str__(self):
        return Card.icons[self.suit + self.number]

    def __repr__(self):
        return Card.icons[self.suit + self.number]


class Person(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cards = []

    def __str__(self):
        return "I'm person %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "I'm person %s" % self.name

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        for c in self.cards:
            print(c, end="")

    def count(self):
        res = 0
        ace = False
        for c in self.cards:
            if c.number == 'a':
                ace = True
                continue
            res += c.value
        if not ace:
            return res
        if res + 11 > 21:
            res += 1
            return res
        res += 11
        return res


class Player(Person):

    def __init__(self, name, balance):
        Person.__init__(self, name, balance)

    def __str__(self):
        return "Player %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "Player %s" % self.name


class Dealer(Person):

    def __init__(self, name):
        Person.__init__(self, name, 10000000) # it's a casino :)

    def __str__(self):
        return "Dealer %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "Dealer %s" % self.name

    def show_cards(self,reveal=False):
        print(self.cards[0], end="")
        print(Card.icons['na'], end="")


class Table(object):
    def __init__(self, deck, players):
        self.deck = deck
        self.dealer = Dealer('1')
        self.players = players
        self.bets = {}

    def distribute_cards(self):
        for i in range(0,2):
            for p in [self.dealer] + self.players: # todo use lambda
                p.add_card(deck.get_card())

    def flush_cards(self):
        self.dealer.cards = []
        for p in self.players: # todo use lambda
            p.cards = []

    def flush_bets(self):
        self.bets = {}

    def print_board(self):
        print(self.dealer, end=": ")
        self.dealer.show_cards()
        print("")
        for p in self.players:
            print(p, "Balance: ",str(p.balance).rjust(8), ", Bet", str(self.bets[id(p)]).rjust(8), end=": ")
            p.show_cards()
            print("")

    def black_jack(self, player):
        return player.count() == 21

    def bust(self, player):
        return player.count() > 21




def num_players_setup():
    while True:
        try:
            num_players = int(input("How many players? 1 to 5: "))
        except:
            print("Ops! This is not a valid number of players. Try it again. ")
            continue
        else:
            break

    clear()
    print(num_players, 'players.')
    return num_players


def players_setup(num_players):
    players = []
    for p in range(0,num_players):
        while True:
            try:
                name = str(p+1)
                balance = float(input("Set player " + name + " wallet balance:"))
                players.append(Player(name, balance))
            except:
                print("Ops! This is not a valid wallet balance. Try it again. ")
                continue
            else:
                break
    return players


def deck_setup():
    deck = Deck([Card(n, s, v) for n, s, v in [
            ('a', 'h', 1), ('2', 'h', 2), ('3', 'h', 3), ('4', 'h', 4), ('5', 'h', 5), ('6', 'h', 6), ('7', 'h', 7),
            ('8', 'h', 8), ('9', 'h', 9), ('10', 'h', 10), ('j', 'h', 10), ('q', 'h', 10), ('k', 'h', 10),
            ('a', 'd', 1), ('2', 'd', 2), ('3', 'd', 3), ('4', 'd', 4), ('5', 'd', 5), ('6', 'd', 6), ('7', 'd', 7),
            ('8', 'd', 8), ('9', 'd', 9), ('10', 'd', 10), ('j', 'd', 10), ('q', 'd', 10), ('k', 'd', 10),
            ('a', 'c', 1), ('2', 'c', 2), ('3', 'c', 3), ('4', 'c', 4), ('5', 'c', 5), ('6', 'c', 6), ('7', 'c', 7),
            ('8', 'c', 8), ('9', 'c', 9), ('10', 'c', 10), ('j', 'c', 10), ('q', 'c', 10), ('k', 'c', 10),
            ('a', 's', 1), ('2', 's', 2), ('3', 's', 3), ('4', 's', 4), ('5', 's', 5), ('6', 's', 6), ('7', 's', 7),
            ('8', 's', 8), ('9', 's', 9), ('10', 's', 10), ('j', 's', 10), ('q', 's', 10), ('k', 's', 10)
        ]])
    random.shuffle(deck.cards)

    return deck





def play(table):
    """
    novo jogo
    - dealer distribui as cartas
    - dealer tem black jack?
    -- fim da mão
    - para cada jogador:
    --- enquanto não parar ou bust
    ---- quer continuar ou parar?
    - dealer revela as cartas
    -- quem ganhou (count > dealer), ganha a apost
    -- quem perdeu (count <= dealer), perde a aposta
    - limpa o jogo

    :param table:
    :return:
    """
    while True:
        # bets

        table.flush_bets()
        for p in table.players:
            while True:
                try:
                    bet = float(input("Set your bet (max " + str(p.balance) + "):"))
                    table.bets[id(p)] = bet
                except:
                    print("Ops! This is not a valid bet. Try it again. ")
                    continue
                else:
                    break

        table.flush_cards()
        table.distribute_cards()
        clear()
        table.print_board()
        if table.black_jack(table.dealer):
            print("dealer has black jack. hand is over")

            continue

        for player_round in table.players:
            while True:
                clear()
                table.print_board()

                if table.bust(player_round):
                    print("player", player_round.name,"bust")
                    break

                if table.black_jack(player_round):
                    print("player", player_round.name, "blackjack")
                    break

                try:
                    print('Player ', player_round.name)
                    option = int(input("1 - Hit   2 - Stand: "))
                except:
                    print("Ops! This is not a valid number of players. Try it again. ")
                    continue

                if option == 2:
                    print(option,'stand!')
                    break

                if option == 1:
                    player_round.add_card(deck.get_card())

        res = None
        while res not in ["a","q"]:
            res = input("Play (a)gain or (q)uit?:").lower()

        if res == "q":
            print("See you soon, raccoon! :)")
            break
        continue


"""
Main
"""
"""
Regras pra implementar:
Se o dealer tem o black jack. Hand is over
Bust --> perde todo o dinheiro para o dealer
Quem tiver black jack, ganha o mesmo amount  de volta do dealer
https://www.youtube.com/watch?v=idB-7FUaC-g

"""

deck = deck_setup()
num_players = num_players_setup()
players = players_setup(num_players)
table = Table(deck, players)
play(table)
