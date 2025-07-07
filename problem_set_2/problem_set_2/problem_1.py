"""

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.

"""

def main():
    camel_case = input("camel case: ")
    print(snake_case(camel_case))

def snake_case(original):
    snake_string = "" # Start with an empty string

    for c in original: # Loop through each character in the string
        if c.isupper(): # If the character is uppercase
            snake_string += "_" + c.lower() # Add an underscore + the lowercase letter
        else:
            snake_string += c # If it's lowercase, add it as-is
    return snake_string

main()

