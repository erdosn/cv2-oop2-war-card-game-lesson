"""
Contains
 - Rules
 - Applies to players
 - Deck Changes happen here
"""
from player import Player
from deck import Deck


class War():


    def __init__(self, 
                 player1_name='gandalf', 
                 player1_win_slogan="Great Game!", player1_lose_slogan="Great Game!",
                 player2_name='saruman', 
                 player2_win_slogan="Great Game!", player2_lose_slogan="Great Game!"):

        self.player1 = Player(name=player1_name,   
                              win_slogan=player1_win_slogan,
                              lose_slogan=player1_lose_slogan) 
        self.player2 = Player(name=player2_name,   
                              win_slogan=player2_win_slogan,
                              lose_slogan=player2_lose_slogan)

        self.deck = Deck()
        self.middle_cards = []
        self.round_number = 0
        self.deal()
    

    def deal(self):
        player1_hand = self.deck.cards[0::2]
        player2_hand = self.deck.cards[1::2]
        self.player1.hand = player1_hand
        self.player2.hand = player2_hand
        print("Dealt the cards")
        pass


    def add_to_middle(self, cards):
        self.middle_cards.extend(cards)
    
    def reset_middle(self):
        self.middle_cards = []

    def play_round(self):
        print("Playing round!")
        p1_card = self.player1.draw_one()
        p2_card = self.player2.draw_one()
        self.add_to_middle(cards=[p1_card, p2_card])
        if p1_card > p2_card:
            self.round_number += 1
            self.player1.take_winnings(cards=self.middle_cards)
            print("Player 1 wins Round!")
            self.reset_middle()
        elif p2_card > p1_card:
            self.round_number += 1
            self.player2.take_winnings(cards=self.middle_cards)
            print("Player 2 wins Round!")
            self.reset_middle()
        else:
            self.play_war()


    def play_war(self):
        print("Time for WAAARRR!!!!")
        # draw 2 cards add them to middle
        p1_facedown = self.player1.draw_one()
        p2_facedown = self.player2.draw_one()
        self.add_to_middle(cards=[p1_facedown, p2_facedown])
        # drawing face up is playing a normal round
        self.play_round()
        pass


    def play_game(self):
        while self.player1.hand and self.player2.hand:
            self.play_round()
            if self.round_number%15 == 0:
                print("-"*50)
                print("Round Number = {}".format(self.round_number))
                print(self.player1.hand)
                print(self.player2.hand)
                print(len(self.player1.hand) + len(self.player2.hand))
                print("-"*50)

        if self.player1.hand:
            print("{} Wins!".format(self.player1.name))
        if self.player2.hand:
            print("{} Wins!".format(self.player2.name))


if __name__=="__main__":
    war = War()
    war.play_game()