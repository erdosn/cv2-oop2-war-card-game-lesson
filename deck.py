"""
This file is going to be used to create a deck of cards
For our Game of War
"""
from random import shuffle

cards = list(range(1, 14))

class Deck():

    def __init__(self):
        self.cards = cards * 4
        shuffle(self.cards)




# Use this to test your code
if __name__=="__main__": # this is suuuper standard
    mydeck = Deck()
    print("Created Deck Object, shuffling cards")
    print("here is your deck")
    print(mydeck.cards)
    # verify deal
    print(mydeck.cards[0::2])
    print(mydeck.cards[1::2])