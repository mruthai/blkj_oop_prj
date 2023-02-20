import random

class Card_deck():
    """Blackjack Class with all game conditions"""
    def __init__(self):
        self.player_pts = 0
        self.player_deck = []
        self.player_hit = 1
        self.dealer_pts = 0
        self.dealer_deck = []
        self.dealer_hit = 1
        self.deck = {
    "2 ♣️" : 2, "3 ♣️": 3, "4 ♣️": 4, "5 ♣️": 5, "6 ♣️": 6, "7 ♣️": 7, "8 ♣️": 8, "9 ♣️": 9, "10 ♣️" : 10, "J ♣️" : 10, "Q ♣️" : 10, "K ♣️" : 10, "A ♣️" : 11, 
    "2 ♥️" : 2, "3 ♥️": 3, "4 ♥️": 4, "5 ♥️": 5, "6 ♥️": 6, "7 ♥️": 7, "8 ♥️": 8, "9 ♥️": 9, "10 ♥️" : 10, "J ♥️" : 10, "Q ♥️" : 10, "K ♥️" : 10, "A ♥️" : 11, 
    "2 ♠️" : 2, "3 ♠️": 3, "4 ♠️": 4, "5 ♠️": 5, "6 ♠️": 6, "7 ♠️": 7, "8 ♠️": 8, "9 ♠️": 9, "10 ♠️" : 10, "J ♠️" : 10, "Q ♠️" : 10, "K ♠️" : 10, "A ♠️" : 11, 
    "2 ♦️" : 2, "3 ♦️": 3, "4 ♦️": 4, "5 ♦️": 5, "6 ♦️": 6, "7 ♦️": 7, "8 ♦️": 8, "9 ♦️": 9, "10 ♦️" : 10, "J ♦️" : 10, "Q ♦️" : 10, "K ♦️" : 10, "A ♦️" : 11,
    }   
        self.update_deck = self.deck.copy()
        
    def deal_card(self):
        """Method for player to start the game with two cards & add up the value of cards"""
        deal_card = random.sample(self.update_deck.keys(), k =2)
        self.player_deck.append(deal_card)
        del self.update_deck[self.player_deck[0][0]]
        self.player_pts += self.deck[self.player_deck[0][0]]
        self.player_pts += self.deck[self.player_deck[0][1]] #dictionary into list, key into the list [[]]
        self.hit_hand_ace()
        return deal_card
    
    def hit_deck(self):
        """Method for player to hit hand + add up the sum of the amount of cards they have"""
        hit_hand = random.sample(self.update_deck.keys(), k=1)
        self.player_deck.append(hit_hand)
        del self.update_deck[self.player_deck[self.player_hit][0]]
        deks = Card_deck()
        self.player_pts += deks.deck[self.player_deck[self.player_hit][0]]
        self.player_hit += 1
        self.hit_hand_ace
        print(f"You have {self.player_pts} pts. {self.player_deck}")
        return hit_hand
        
    def player_decision(self):
        """Method that determine the sum of points after player hits"""
        if self.player_pts > 21:
            self.hit_hand_ace
            print(f"\nYou BUST {self.player_pts} pts. {self.player_deck}")
            print(f"Dealer WINS with: {self.dealer_pts} pts. {self.dealer_deck}")
        elif self.player_pts < 21:
            self.hit_deck()
            print(f"{self.player_deck} {self.player_pts}")
            
    def hit_hand_ace(self):
        """Method for player with aces"""
        getgp = Game_play()
        aces = "A ♣️ A ♥️ A ♠️ A ♦️"  
        if self.player_pts > 21:
            for hand in self.player_deck:
                for add_card in hand:
                    if add_card in aces:
                       self.player_pts -= 10
                       print(f"You have {self.player_pts} pts. {self.player_deck}")
                    else:
                        print(f"You BUST {self.player_deck} {self.player_pts} pts.")
                        getgp.dealer_active
                        getgp.player_active
                        self.reset_deck()
                        return

    def dealer_play(self):
        """Dealer Method - given to card but 1 is shown"""
        deal_card_dealer = random.sample(self.update_deck.keys(), k =2)
        self.dealer_deck.append(deal_card_dealer)
        del self.update_deck[self.dealer_deck[0][0]]
        self.dealer_pts += self.deck[self.dealer_deck[0][0]]
        self.dealer_pts += self.deck[self.dealer_deck[0][1]]
        return deal_card_dealer

    def dealer_decision(self):
        getgp = Game_play()
        """"Method that determines if the dealer looses and the player wins"""
        if self.dealer_pts > 21:
            print(f"\nYou Win{self.player_deck} {self.player_pts} pts.")
            print(f"Dealer Bust{self.dealer_deck} {self.dealer_pts} pts.")
        elif self.dealer_pts < 17:
            self.dealer_cont()
        elif self.dealer_pts >= 17:
            if self.dealer_pts < self.player_pts:
                print(f"You Win: {self.player_deck} {self.player_pts} pts.")
                print(f"Dealer Bust: { self.dealer_deck} {self.dealer_pts} pts.")
                getgp.player_active
                getgp.dealer_active
                self.reset_deck()
            elif self.dealer_pts > self.player_pts:
                print(f"You Bust: {self.player_deck} {self.player_pts} pts.")
                print(f" Dealer Wins: { self.dealer_deck} {self.dealer_pts} pts.")
                getgp.dealer_active
                getgp.player_active
                self.reset_deck()
            elif self.dealer_pts == self.player_pts:
                print(f"TIE GAME")
                print(f"Your hand :   {self.player_deck} {self.player_pts} pts. ")
                print(f"Dealers hand: { self.dealer_deck} {self.dealer_pts} pts.")
                getgp.dealer_active
                getgp.player_active
                self.reset_deck()

    def dealer_cont(self): 
        """Player hits Stand and dealer continues"""
        hit_hand = random.sample(self.update_deck.keys(), k=1)
        self.dealer_deck.append(hit_hand)
        del self.update_deck[self.dealer_deck[self.dealer_hit][0]]
        deks = Card_deck()
        self.dealer_pts += deks.deck[self.dealer_deck[self.dealer_hit][0]]
        self.dealer_hit += 1
        self.dealer_ace()

    def dealer_ace(self):
        """Method for checking how dealer deals with aces"""
        getgp = Game_play()
        aces = "A ♣️ A ♥️ A ♠️ A ♦️"  
        if self.dealer_pts > 21:
            for hand in self.dealer_deck:
                for single in hand:
                    if single in aces:
                        self.dealer_pts -= 10
                        self.dealer_decision()
                    else:
                        print(f"Dealer BUST {self.dealer_deck} {self.dealer_pts} pts.")
                        print(f"You WIN {self.player_deck} {self.player_pts} pts.")
                        getgp.dealer_active
                        getgp.player_active
                        self.reset_deck()
                        return
        else:
            self.dealer_decision()

    def reset_deck(self):
        """Method to rest the deck, dealer and player cards and points"""
        self.update_deck.clear()
        self.update_deck = self.deck.copy()
        self.dealer_deck.clear()
        self.player_deck.clear()
        self.dealer_hit = 1
        self.player_hit = 1
        self.dealer_pts = 0
        self.player_pts = 0    

class Game_play():
    """Class that handles all the human interaction"""
    def __init__(self):
        self.getcd = Card_deck()
        self.player_active = False
        self.dealer_active = False

    def run(self):
        while True:
            player_choice = input("Playing Blackjack? (y/n) ").lower()
            if player_choice == "y":
                
                self.player_active = True
                self.dealer_active = True
                
                print(f"Your cards {self.getcd.deal_card()}")
                print(f"Your value {self.getcd.player_pts}")
                print(f"\nDealer has {self.getcd.dealer_play()[0]}")
                while self.player_active or self.dealer_active:
                    
                    player_choice = input("Would like to HIT or STAND? (h/s): ")

                    if player_choice == "h":
                        self.getcd.hit_deck()

                    elif player_choice == "s":
                        self.getcd.dealer_decision()
                        break

            elif player_choice == "n":
                    print("Have a good day! Bye Now")
                    return
            
accesspd = Game_play()
accesspd.run()

