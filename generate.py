# import random
# coin = random.choice(["heads", "tails"])
# print(coin)

## can be more specific with scope as such:

# from random import choice

# i = 0

# while i < 5:
#     coin = choice(["heads", "tails"])
#     print(coin)
#     i += 1

## get a random int

# import random

# number = random.randint(1, 10)
# print(number)

## shuffle cards

import random

cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)