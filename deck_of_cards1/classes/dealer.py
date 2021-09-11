from classes.person import Person

class Dealer(Person):
    def __init__(self, name):
        super().__init__(name)

    def hit_until_17(self):
        self.calculate_total()
        if self.card_total < 17:
            self.get_cards(1)
            self.card_total = 0
            self.hit_until_17()
        else: return

    def calculate_total(self):
        self.card_total = 0
        for value in self.cards_dealt:
            self.card_total += value
        return self