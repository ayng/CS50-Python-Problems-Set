import random


# def main():
#     level = get_level()
#     score = 0

#     while tries < 3:



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

#main()
# if __name__ == "__main__":
#     main()