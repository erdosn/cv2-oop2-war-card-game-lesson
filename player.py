class Player(object):

    def __init__(self, name="", winning_slogan="", losing_slogan=""):
        self.name = name
        self.cards = []
        self.winning_slogan = winning_slogan
        self.losing_slogan = losing_slogan

    def draw_card(self):
        top_card = self.cards.pop(0)
        return top_card