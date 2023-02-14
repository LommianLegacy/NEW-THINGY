def Holding(p1card, p2card):

    print("Player 1 has: " + str(p1card) +"\n)")
    print("Player 2 has: " + str(p2card) +"\n)")

import random
deck = list(range(2,15))*4
random.shuffle(deck)
p1 = deck[:26]
p2 = deck[26:]
pile = []


while len(p1) != 0 or len(p1) != 0:

    p1card =p1.pop(0)
    p2card =p2.pop(0)
    pile.append(p1card)
    pile.append(p2card)

    Holding(p1card, p2card)

    if p1card > p2card:
        print("Player 1 won")
        p1.extend(pile)
        pile.clear()




    elif p1card < p2card:
        print("Player 2 won")
        p2.extend(pile)
        pile.clear()


    elif p1card == p2card:
        print("war")
        pile.append(p1.pop(0))
        pile.append(p2.pop(0))