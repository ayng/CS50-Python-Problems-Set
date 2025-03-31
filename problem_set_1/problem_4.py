"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
"""

def main():
    # Prompt the user for input assuming input will be space-separated values
    expression = input("Enter x, y, z separated by spaces: ")

    # Use the split method to split the string int a list based on whitespace (by default)
    x, y, z = expression.split()

    # Turn x and z into integers
    x = int(x)
    z = int(z)

    # Creating the logic to handle +, - , *, and / all while formatting by one decimal place using Python's formatted string literals f - strings
    if y == "+":
        print(f'{x + z:.1f}')
    elif y == "-":
        print(f'{x - z:.1f}')
    elif y == "*":
        print(f'{x * z:.1f}')
    elif y == "/":
        print(f'{x / z:.1f}')
            
main()
