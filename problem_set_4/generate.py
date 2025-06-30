
# All of the functions I'm calling (.choice, for example) have to be associated with the module 'random'
# Hence why I have 'random.choice' below
import random

coin = random.choice(['heads', 'tails'])
print(coin)

# This loads the function choice into the scope of the file I'm working with.
# I no longer have to specify which choice function I mean
# This 
from random import choice

# Generate a random number between 1 and 10 (inclusive)
number = random.randint(1, 10)
print(number)

# Shuffle the argument (list) 
cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)
