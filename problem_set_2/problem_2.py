"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

# Method below solves the problem by defining a function

def main():
    total = 0 # Initialize total amount collected
    while total < 50: # Loop until the total reaches at least 50 cents
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25: # Check if the coin is valid
            total += coin # Add valid coin to total. Take the current value of total and add coin to it.
            due = 50 - total
            if total < 50: # Only show the amount due if more money needed
                print(f'Amount Due: {due}')
        else:
            print("Invalid coin, please insert 5, 10, or 25 cents.")
    change = total - 50 # Calculate and display the amount owed
    print(f'Change Owed: {change}')

main()


