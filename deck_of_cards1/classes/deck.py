from . import card

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                    self.cards.append( card.Card( s , 10 , str_val ) )
                    continue
                elif i == 11:
                    str_val = "Jack"
                    self.cards.append( card.Card( s , 10 , str_val ) )
                    continue
                elif i == 12:
                    str_val = "Queen"
                    self.cards.append( card.Card( s , 10 , str_val ) )
                    continue
                elif i == 13:
                    str_val = "King"
                    self.cards.append( card.Card( s , 10 , str_val ) )
                    continue
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

