import random

class Card_deck():
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
        
    def deal_card(self):
        deal_card = random.sample(update_deck.keys(), k =2)
        self.player_deck.append(deal_card)
        del update_deck[self.player_deck[0][0]]
        self.player_pts += self.deck[self.player_deck[0][0]]
        self.player_pts += self.deck[self.player_deck[0][1]] #dictionary into list, key into the list [[]]

        return deal_card
    
    
    def hit_deck(self):
        hit_hand = random.sample(update_deck.keys(), k=1)
        self.player_deck.append(hit_hand)
        del update_deck[self.player_deck[self.player_hit][0]]
        deks = Card_deck()
        self.player_pts += deks.deck[self.player_deck[self.player_hit][0]]
        self.player_hit += 1
        print(f"{self.player_deck}")
        self.hit_hand_ace()


    def hit_hand_ace(self):
        aces = "A ♣️ A ♥️ A ♠️ A ♦️"  
        if self.player_pts > 21:
            for hand in self.player_deck:
                for single in hand:
                    if single in aces:
                       self.player_pts -= 10
        else:
            print(f"You Bust")
            player_active = False
            dealer_active = False
        if self.dealer_pts > 21:
            for hand in self.dealer_deck:
                for single in hand:
                    if single in aces:
                       self.dealer_pts -= 10
        else:
            print(f"You WIN!")
            player_active = False
            dealer_active = False

    def dealer_play(self): #player standing
        deal_card_dealer = random.sample(update_deck.keys(), k =2)
        self.dealer_deck.append(deal_card_dealer)
        del update_deck[self.dealer_deck[0][0]]
        self.dealer_pts += self.deck[self.dealer_deck[0][0]]
        self.dealer_pts += self.deck[self.dealer_deck[0][1]]
        return deal_card_dealer

    def dealer_cont(self):
        hit_hand = random.sample(update_deck.keys(), k=1)
        self.dealer_deck.append(hit_hand)
        del update_deck[self.dealer_deck[self.dealer_hit][0]]
        deks = Card_deck()
        self.dealer_pts += deks.deck[self.dealer_deck[self.dealer_hit][0]]
        self.dealer_hit += 1
        print(f"{self.dealer_deck}")

"""Global deck"""        
give_cards = Card_deck()    
update_deck = give_cards.deck.copy()

class Game_play():
    def __init__(self):
        self.getcd = Card_deck()

    def run(self):
        player_active = False
        dealer_active = False
        while True:
            player_choice = input("Playing Blackjack? (y/n) ").lower()
            if player_choice == "y":
                player_active = True
                dealer_active = True
                
                print(f"Your cards {self.getcd.deal_card()}")
                print(f"Your value {self.getcd.player_pts}")
                print(f"Dealer has {self.getcd.dealer_play()[0]}")
                while player_active or dealer_active:
                    
                    player_choice = input("Would like to HIT or STAND? (h/s): ")

                    if player_choice == "h":
                        self.getcd.hit_deck()

                    elif player_choice == "s":
                        self.getcd.dealer_play()
                        break
                    else:
                        print("Test print")

            elif player_choice == "n":
                    print("Have a good day")
                    return
            

accesspd = Game_play()
accesspd.run()

