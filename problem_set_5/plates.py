def main():
    response = input('Plate: ')
    if is_valid(response):
        print('Valid')
    else:
        print('Invalid')

def is_valid(s):

    # Requirement #1: length of s must be within 2 and 6 characters
    if 2 <= len(s) <= 6:
        pass
    else:
        return False
    
    # Requirement #2: must start with at least two letters
    if s[:2].isalpha():
        pass
    else:
        return False

    # Requirement #3: Numbers can't be used in the middle of the plate.
    # Requirement #4: First number can't be 0
    number_started = 0
    for c in s:
        if c.isnumeric():
            if number_started == 0:
                if c == 0:
                    return False
                else:
                    number_started += 1
            else:
                continue
        elif c.isalpha():
            if number_started == 0:
                continue
            else:
                return False
        else:
            return False
            
    return True
        
if __name__ == '__main__':
    main()
