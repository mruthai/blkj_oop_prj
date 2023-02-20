import random


class Deck():
    def __init__(self):
        self.points = 0
        self.deck = {
    "2 ♣️" : 2, "3 ♣️": 3, "4 ♣️": 4, "5 ♣️": 5, "6 ♣️": 6, "7 ♣️": 7, "8 ♣️": 8, "9 ♣️": 9, "10 ♣️" : 10, "J ♣️" : 10, "Q ♣️" : 10, "K ♣️" : 10, "A ♣️" : 11, 
    "2 ♥️" : 2, "3 ♥️": 3, "4 ♥️": 4, "5 ♥️": 5, "6 ♥️": 6, "7 ♥️": 7, "8 ♥️": 8, "9 ♥️": 9, "10 ♥️" : 10, "J ♥️" : 10, "Q ♥️" : 10, "K ♥️" : 10, "A ♥️" : 11, 
    "2 ♠️" : 2, "3 ♠️": 3, "4 ♠️": 4, "5 ♠️": 5, "6 ♠️": 6, "7 ♠️": 7, "8 ♠️": 8, "9 ♠️": 9, "10 ♠️" : 10, "J ♠️" : 10, "Q ♠️" : 10, "K ♠️" : 10, "A ♠️" : 11, 
    "2 ♦️" : 2, "3 ♦️": 3, "4 ♦️": 4, "5 ♦️": 5, "6 ♦️": 6, "7 ♦️": 7, "8 ♦️": 8, "9 ♦️": 9, "10 ♦️" : 10, "J ♦️" : 10, "Q ♦️" : 10, "K ♦️" : 10, "A ♦️" : 11,
    }
    
"""Global deck"""
give_cards = Deck()    
update_deck = give_cards.deck.copy()
"""Players """
class Player():
    def __init__(self):
        self.points = 0
        self.player_has = []
   
    def player_start_hand(self):
        
        # print(update_deck)
        player_hand = random.sample(update_deck.keys(), k=2)
        self.player_has.append(player_hand)
        # print(player_has)
        del update_deck[self.player_has[0][0]]
        del update_deck[self.player_has[0][1]]
        
        for hand in self.player_has:
            deks = Deck()
            self.points += deks.deck[hand[0]]
            self.points += deks.deck[hand[1]]
        print(player_hand)
        print(f"{self.points}")
        return player_hand
    
    def hit_stand(self):
        # print(update_deck)
        hit_hand = random.sample(update_deck.keys(), k=1)
        self.player_has.append(hit_hand)
        print(self.player_has)
        del update_deck[self.player_has[0][0]]
        print(self.player_has)
        for hand in self.player_has:
            deks = Deck()
            self.points += deks.deck[hand[0]]
            # total_points = sum(deks.deck[hand[0]])
        # print(hit_hand)
        # print(f"{total_points}")
        return hit_hand
            
        
    
class Dealer():
    def __init__(self):
        self.points = 0

    def dealer_start_hand(self):
        dealer_has = []
        # print(update_deck)
        dealer_hand = random.sample(update_deck.keys(), k=2)
        dealer_has.append(dealer_hand)
        # print(dealer_has)
        del update_deck[dealer_has[0][0]]
        del update_deck[dealer_has[0][1]]
        
        for hand in dealer_has:
            deks = Deck()
            self.points += deks.deck[hand[0]]
            self.points += deks.deck[hand[1]]
        print(dealer_hand)
        print(f"{self.points}")
        return dealer_hand
    

accesspd = Player()
accesspd.player_start_hand()
accesspd = Player()
accesspd.hit_stand()
accesspd = Player()
# accesspd.dealer_start_hand()
# accesspd.add_card_value()



    #inhertiance 