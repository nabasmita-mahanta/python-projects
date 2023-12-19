# Write a python program to shuffle deck of cards.

import random, itertools

deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Hearts", "Diamonds"]))

random.shuffle(deck)
print(deck)

for i in range(5):
    print(deck[i][0], "of", deck[i][1])



