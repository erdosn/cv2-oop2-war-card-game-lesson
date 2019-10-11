from player import Player
from deck import Deck


class War(object):

    def __init__(self, player1=None, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.deck = Deck()
        self.deck.shuffle()
        self.pile = []

    def deal_cards(self):
        for index, card in enumerate(self.deck.deck):
            if index % 2 == 0:
                self.player1.cards.append(card)
            else:
                self.player2.cards.append(card)

    def check_empty(self):
        return self.player1.cards == [] or self.player2.cards == []

    def play_war(self):
        for i in range(3):
            if not self.check_empty():
                self.pile.append(self.player1.draw_card())
                self.pile.append(self.player2.draw_card())
            else:
                self.declare_winner()
        self.play_round()

    def play_round(self):
        player1_card = self.player1.draw_card()
        player2_card = self.player2.draw_card()
        self.pile.extend([player1_card, player2_card])
        if player1_card > player2_card:
            self.player1.cards.extend(self.pile)
        elif player1_card < player2_card:
            self.player2.cards.extend(self.pile)
        else:
            print("Declare War!")
            self.play_war()

        self.reset_pile()

    def reset_pile(self):
        self.pile = []

    def declare_winner(self):
        if self.player1.cards:
            print(self.player1.winning_slogan)
            print(self.player2.losing_slogan)
        else:
            print(self.player1.losing_slogan)
            print(self.player2.winning_slogan)
        exit(0)

    def play_game(self):
        war.deal_cards()
        while True:
            if self.check_empty():
                self.declare_winner()
            war.play_round()


if __name__ == "__main__":
    player1 = Player(name="Andrew", winning_slogan="GG", losing_slogan="GG, well played")
    player2 = Player(name="Rahkeem", winning_slogan="Major Medical Yeah!", losing_slogan="yeah :/")
    war = War(player1=player1, player2=player2)
    war.play_game()
