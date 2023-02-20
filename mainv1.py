
import random
"""Pseudo Code"""



class Deck_of_cards():
    def __init__(self):
        self.full_deck = {
    "2 ♣️" : 2, "3 ♣️": 3, "4 ♣️": 4, "5 ♣️": 5, "6 ♣️": 6, "7 ♣️": 7, "8 ♣️": 8, "9 ♣️": 9, "10 ♣️" : 10, "J ♣️" : 10, "Q ♣️" : 10, "K ♣️" : 10, "A ♣️" : 11, 
    "2 ♥️" : 2, "3 ♥️": 3, "4 ♥️": 4, "5 ♥️": 5, "6 ♥️": 6, "7 ♥️": 7, "8 ♥️": 8, "9 ♥️": 9, "10 ♥️" : 10, "J ♥️" : 10, "Q ♥️" : 10, "K ♥️" : 10, "A ♥️" : 11, 
    "2 ♠️" : 2, "3 ♠️": 3, "4 ♠️": 4, "5 ♠️": 5, "6 ♠️": 6, "7 ♠️": 7, "8 ♠️": 8, "9 ♠️": 9, "10 ♠️" : 10, "J ♠️" : 10, "Q ♠️" : 10, "K ♠️" : 10, "A ♠️" : 11, 
    "2 ♦️" : 2, "3 ♦️": 3, "4 ♦️": 4, "5 ♦️": 5, "6 ♦️": 6, "7 ♦️": 7, "8 ♦️": 8, "9 ♦️": 9, "10 ♦️" : 10, "J ♦️" : 10, "Q ♦️" : 10, "K ♦️" : 10, "A ♦️" : 11 
    }
        self.dealt_deck = {}
       

    
    
    def shuffle_deck(self):
        random.shuffle(self.full_deck)
        
    def deal(self):
        one_card = self.full_deck.pop()
        return one_card
    
    def hold_dealt_card(self):
        move_card = random.self.full_deck 



    
        
class Hands():
    def __init__(self):
        self.playercards = {}
        self.dealercards = {}
        self.card_value = 0

    def give_card_to_player_or_deal(self, add_card):
        self.card_value += self.deck_of_cards





class Game_play():
    def __init__(self):
        pass

    def run(self):
        while True:

            player_choice = input("Would you like to play?(y/n) ").lower()
            
            if player_choice == "y":
                self.playermove()
            elif player_choice == "n":
                print("Have a good day")
                return

    def player(self):
        print("Here we go")
        while True:
            playa_choice = input("Would like to HIT or STAND? (h/s): ")

            if playa_choice == "n":
                pass #player is given card
        
    
    

    def playermove(self):
        print("test")

    


blackjack = Game_play()
blackjack.run()


        


