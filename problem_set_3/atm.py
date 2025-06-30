"""

Create a Python program named atm.py simulating a simple ATM withdrawal scenario:

✅ Ask the user for a withdrawal amount.
✅The ATM allows withdrawals in multiples of 20 dollars only.
✅Raise a custom exception called InvalidWithdrawalError if the user inputs a number that isn't a multiple of 20.
✅Handle the exception gracefully by printing a message and prompting again.
✅If the user inputs anything other than an integer, catch the built-in exception (ValueError) and prompt again.
✅Once a valid withdrawal occurs, print "Withdrawal successful!".


"""
class InvalidWithdrawalError(Exception):
    pass

def main():
    while True:
        try:
            amount = int(input('How much would you like to withdraw? '))
            if amount % 20 == 0: # If the amount is a multiple of 20
                print('Withdrawal successful!')
                break
            else:
                raise InvalidWithdrawalError

        except ValueError as e:
            print(f'Incorrect input, please enter valid input')
        
        except InvalidWithdrawalError as e:
            print(f'Error occurred: Please make sure withdrawal amount is a multiple of 20.')
        
        except EOFError as e:
            print(f'\nYou exited the program.')
            break

main()

