"""
Implement a program that will
- Prompt the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not positive prompt the user again.
- If the guess is smaller than that integer, the program should ouptut 'Too small!' and prompt the user again, etc.
"""

import random


def main():
    # Prompt for the level until a valid positive integer is given
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level <= 0:
            print("Please enter a positive number and try again.")

        else:
            random.seed(1)
            number = random.randint(1, level)
            print("A random number has been generated.")
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    continue

                if guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        break # Why is this break necessary?

main()
