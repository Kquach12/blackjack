from classes.deck import Deck
from classes.person import Person
from classes.player import Player
from classes.dealer import Dealer


player = Player("Kenny")
dealer = Dealer("dealer")

def printCards():
    print(f"{player.name}'s Cards: {player.cards_dealt}; {player.card_total} \n{dealer.name}'s Cards: {dealer.cards_dealt}; {dealer.card_total}")
    

def calculateEarnings(isWinner):
    if isWinner:
        player.chips += player.bet
    else:
        player.chips -= player.bet

def gamePlay():

    player.calculate_total()

    action = input("Hit or Stay: ")
    if action == "Hit":
        player.get_cards(1)
        player.calculate_total()
        printCards()                            
        if player.card_total < 21:
            gamePlay()
        else: 
            print("Loser!")
            calculateEarnings(False)
    elif action == "Stay":
        dealer.get_cards(1)
        dealer.hit_until_17()
        printCards()
        if dealer.card_total > 21 or player.card_total > dealer.card_total:
            print("You win!")
            calculateEarnings(True)
        elif dealer.card_total == player.card_total:
            print("Push")
        else: 
            print("Loser!") 
            calculateEarnings(False)
    
    player.bet = 0
    player.cards_dealt = []
    dealer.cards_dealt =[]
    start()


def start():
    print(f"Your Chips: {player.chips}")
    start = input("Type Start to Begin! ")
    if start == "Start":
        player.bet = int(input("Place Bet: "))
        player.get_cards(2).calculate_total()
        dealer.get_cards(1).calculate_total()
        printCards()
        gamePlay()
    else: return

start()