"""
In a file called taqueria.py, implement a program that enables a user to place an order, 
prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
After each inputted item, 
    - ✅ display the total cost of all items inputted thus far, 
    - ✅ prefixed with a dollar sign ($) and formatted to two decimal places. 
    - ✅ Treat the user’s input case insensitively. 
    - Ignore any input that isn’t an item. 
    - ✅ Assume that every item on the menu will be titlecased.
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
"""
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            order = input('What would you like to order: ').lower().title()
            if order in menu:
                total += menu[order]
                print(f'The total cost of your items so far is: ${total:.2f}')
            else:
                print("Item not found. Please order something from the menu.")
        except EOFError:
            break
main()

"""
Notes:

- To get a value from a dictionary, you use this syntax: dictionary[key]

- EOFError: End Of File Error
happens when the input stream is closed unexpectedly, or more commonly, 
when the user explicitly signals the end of input by pressing Ctrl+D (on Unix/Linux/macOS) or Ctrl+Z (on Windows).
In this context, it's an elegant way for the user to indicate they're finished ordering.
Once detected, the loop immediately exits due to the break statement.
"""
