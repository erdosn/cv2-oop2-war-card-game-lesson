import random

class Deck(object):

    def __init__(self):
        self.deck = list(range(2, 14))*4


    def shuffle(self):
        random.shuffle(self.deck)


if __name__=="__main__":
    deck = Deck()
    print(deck.deck)
    print("\n")
    deck.shuffle()
    print(deck.deck)
    print("\n")