from classes.person import Person

class Player(Person):
    def __init__(self, name, chips = 100):
        super().__init__(name)
        self.chips = chips
        self.bet = 0