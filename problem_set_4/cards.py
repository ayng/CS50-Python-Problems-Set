import random

cards = ['jack', 'queen', 'king']

def main():
    random.seed(1) # Good way to debug. To be sure of the outcome.
    print(random.choices(cards, k = 2))

main()

