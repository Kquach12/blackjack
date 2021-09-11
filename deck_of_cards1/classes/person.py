import random
from classes.deck import Deck

class Person:
    def __init__(self, name):
        self.name = name
        self.cards_dealt = []
        self.deck = Deck()
        self.card_total = 0

    def get_cards(self, num_of_cards):
        for cards in range(num_of_cards):
            random_card = random.randint(0, len(self.deck.cards) - 1)
            self.cards_dealt.append(self.deck.cards[random_card].point_val)
        return self
            
    def calculate_total(self):
        self.card_total = 0
        for value in self.cards_dealt:
            self.card_total += value
        return self
        # if self.card_total > 21:
        #     return False
        # else: return True
