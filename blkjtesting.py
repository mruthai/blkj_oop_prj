import random

deck = {
    "2 ♣️" : 2, "3 ♣️": 3, "4 ♣️": 4, "5 ♣️": 5, "6 ♣️": 6, "7 ♣️": 7, "8 ♣️": 8, "9 ♣️": 9, "10 ♣️" : 10, "J ♣️" : 10, "Q ♣️" : 10, "K ♣️" : 10, "A ♣️" : 11, 
    "2 ♥️" : 2, "3 ♥️": 3, "4 ♥️": 4, "5 ♥️": 5, "6 ♥️": 6, "7 ♥️": 7, "8 ♥️": 8, "9 ♥️": 9, "10 ♥️" : 10, "J ♥️" : 10, "Q ♥️" : 10, "K ♥️" : 10, "A ♥️" : 11, 
    "2 ♠️" : 2, "3 ♠️": 3, "4 ♠️": 4, "5 ♠️": 5, "6 ♠️": 6, "7 ♠️": 7, "8 ♠️": 8, "9 ♠️": 9, "10 ♠️" : 10, "J ♠️" : 10, "Q ♠️" : 10, "K ♠️" : 10, "A ♠️" : 11, 
    "2 ♦️" : 2, "3 ♦️": 3, "4 ♦️": 4, "5 ♦️": 5, "6 ♦️": 6, "7 ♦️": 7, "8 ♦️": 8, "9 ♦️": 9, "10 ♦️" : 10, "J ♦️" : 10, "Q ♦️" : 10, "K ♦️" : 10, "A ♦️" : 11,
    }

#reveal player hand

playerhand = random.sample(deck.keys(), k=2)
print(playerhand)
p_points = 0

for hand in playerhand:
    p_points += deck[hand]

print(p_points)

hit = random.sample(deck.keys(), k=1)
print(hit)

if playerhand <= 21:
    print("bust")

for hand in playerhand:
    p_points += deck[hand]

print(p_points)

#reveal dealer hand
dealer = random.sample(deck.keys(), k= 1)

# for v in deck.values():



print(dealer)
