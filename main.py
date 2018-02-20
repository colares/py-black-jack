import random, os


def clear():
    os.system('clear')


class Deck(object):

    def __init__(self):
        # hearts, diamonds, clubs, spades
        self.cards = [
            ('a', 'h', 1), ('2', 'h', 2), ('3', 'h', 3), ('4', 'h', 4), ('5', 'h', 5), ('6', 'h', 6), ('7', 'h', 7),
            ('8', 'h', 8), ('9', 'h', 9), ('10', 'h', 10), ('j', 'h', 10), ('q', 'h', 10), ('k', 'h', 10),
            ('a', 'd', 1), ('2', 'd', 2), ('3', 'd', 3), ('4', 'd', 4), ('5', 'd', 5), ('6', 'd', 6), ('7', 'd', 7),
            ('8', 'd', 8), ('9', 'd', 9), ('10', 'd', 10), ('j', 'd', 10), ('q', 'd', 10), ('k', 'd', 10),
            ('a', 'c', 1), ('2', 'c', 2), ('3', 'c', 3), ('4', 'c', 4), ('5', 'c', 5), ('6', 'c', 6), ('7', 'c', 7),
            ('8', 'c', 8), ('9', 'c', 9), ('10', 'c', 10), ('j', 'c', 10), ('q', 'c', 10), ('k', 'c', 10),
            ('a', 's', 1), ('2', 's', 2), ('3', 's', 3), ('4', 's', 4), ('5', 's', 5), ('6', 's', 6), ('7', 's', 7),
            ('8', 's', 8), ('9', 's', 9), ('10', 's', 10), ('j', 's', 10), ('q', 's', 10), ('k', 's', 10)
        ]
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()


class Person(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return "I'm person %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "I'm person %s" % self.name

    def add_card(self, card):
        self.cards.append(card)

    def count(self):
        res = 0
        ace = False
        for c in self.cards:
            if c[0] == 'a':
                ace = True
                continue
            res += c[2]
        if not ace:
            return res
        if res + 11 > 21:
            res += 1
            return res
        res += 11
        return res

    def black_jack(self):
        return self.count() == 21

    def bust(self):
        return self.count() > 21


class Player(Person):

    def __init__(self, name):
        Person.__init__(self, name)

    def __str__(self):
        return "Player %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "Player %s" % self.name


class Dealer(Person):

    def __init__(self, name):
        Person.__init__(self, name)

    def __str__(self):
        return "Dealer %s" % self.name

    def __repr__(self):
        # used by print(list(l))
        return "Dealer %s" % self.name





def menu():
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
    print("Let's play!")
    return num_players


def main(num_players):
    deck = Deck()
    players = [Player(i) for i in range(0, num_players)]

    for turn in range(0,2):
        for p in players:
            p.add_card(deck.get_card())

    for p in players:
        print(p)
        print(p.cards)
        print("")

    # while True:
    #     try:
    #         num_players = int(input("How many players? 1 to 5: "))
    #     except:
    #         print("Ops! This is not a valid number of players. Try it again. ")
    #         continue
    #     else:
    #         break


num_players = menu()
main(num_players)