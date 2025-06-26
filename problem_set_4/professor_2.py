import random

def main():
    # Prompt the user for a level
    level = get_level()
    
    # Initiate score
    score = 0

    # Generate 10 math problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        # Calculate the correct answer
        correct_answer = x + y

        # Initiate tries for each problem
        tries = 0

        # Prompt the user to solve each problem
        while tries < 3:
            try:
                response = int(input(f'{x} + {y} = '))
                if response == correct_answer:
                    score += 1
                else:
                    print('EEE')
                    tries += 1
            except ValueError:
                print('EEE')
                tries += 1

        if tries == 3:
            print(f'The correct answer is: {correct_answer}')
    
    print(f'Score: {score}/10')

# Prompt (re-prompt) the user for a level and return 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input('Level (1, 2, or 3): '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print('EEE')

# Return a randomly generated non-negative integer with level digits OR raise a ValueError if level is not 1, 2, or 3.
def generate_integer(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError('Invalid level')

main()
# if __name__ == "__main__":
#     main()