import random

def main():
    level = get_level()
    score = 0

    for _ in range(10): # 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == correct_answer:
                    score += 1
                else:
                    print('EEE')
                    tries += 1
            except ValueError:
                print('EEE')
                tries += 1
        
        if tries == 3:
            print(f'The correct answer was {correct_answer}')
    
    print(f'Score: {score}/10')
                

def get_level():
    while True:
        try:
            level = int(input('Enter a level (1, 2, or 3): '))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass # Ignore the bad input
        print('EEE')

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError('Invalid level')

main()
