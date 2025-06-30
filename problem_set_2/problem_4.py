"""

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. 

Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user’s input will be uppercase. 

Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 

Assume that s will be a str. 

You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Validate each requirement
    if not start(s):
        return False

    if not length(s):
        return False
    
    if not numbers_at_end(s):
        return False
    
    return True

# Ensure the first two characters are letters
def start(s):
    if s[:2].isalpha():
        return True
    else:
        return False

# Ensure the length of characters is greater than or equal to 2 but less than or equal to 6
def length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

# Check if numbers are only at the end of the plate and follow the rules:
# 1. Numbers must appear only at the end of the plate.
# 2. The first number cannot be '0'.
def numbers_at_end(s):
    numbers_started = False  # This flag tracks if we've encountered the first number.

    for c in s:  # Loop through each character in the string.
    
        if c.isdigit():  # If the character is a number:
            if numbers_started == False:  # If it's the first number we've encountered:
                if c == '0':  # Plates cannot start with a '0' as the first number.
                    return False  # Return False because this violates the rule.
                numbers_started = True  # Update the flag to indicate numbers have started.

        elif numbers_started:  # If we encounter a letter *after* numbers have started:
            return False  # Return False because letters cannot follow numbers.
    
    return True  # If no rules are broken, the plate is valid.

main()