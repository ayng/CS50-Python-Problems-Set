"""
Fuel gauges indicate, often with fractions, 
just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 
1/2 indicates that a tank is 50% full, 
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, 
implement a program that prompts the user for a fraction, 
formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest integer, 
how much fuel is in the tank. 

If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

# Use Control + C to enable/disable GitHub Copilot.
# Use ^ + Command + I to enable/disable Copilot chat.
# Control + Option + N to Run Code

"""
Tips
- raise = “Something went wrong — fix it or catch it.” " or “Uh-oh! Something went wrong — I’m sending up a flare.”
- except = “What to do about it if something goes wrong.” or “I caught the problem. Here’s how I’m going to handle it.”

- try: Attempt something that might break
- except: Catch the error and decide how to respond
- raise: Throw an error if something is wrong
"""

# Define a program
def main():
    while True:

        """ Okay, let me ATTEMPT to run everything inside this try block**. 
        If anything breaks, Ill look for an except. """
        
        try:
            # Ask the user for fraction
            fraction = input( 'Enter a fraction: ' )

            # Condition #1: 
            """ 
                - Input must be a fraction denoted by '/'
                - and split the input into numerator and denominator 
            """
            try:
                numerator, denominator = fraction.split( '/' )
            except ValueError:
                raise ValueError("You did not enter a valid fraction (e.g., 3/4).")
            
            # Condition #2: Fraction must contain integers 
            try:
                numerator, denominator = int(numerator), int(denominator)
            except ValueError:
                raise ValueError('You entered invalid characters in your fraction.')
            
            # Condition #3: numerator cannot be greater than denominator
            if numerator > denominator:
                raise ValueError('The numerator cannot be bigger than the denominator.')
            
            # Condition #4: Denominator cannot be 0
            if denominator == 0:
                raise ZeroDivisionError("The denominator cannot be zero.")
            
            # If all try's are successful, print the fraction
            print(f'The fraction you entered is: {fraction}')
            # Calculate the percentage of the fraction
            percentage = round((numerator / denominator) * 100)
            # 
            if percentage <= 1:
                print('E (Empty)')
            elif percentage >= 99:
                print('F (Full)')
            else:
                print(f'Fuel indicator: {percentage}%')
            break

        except ValueError as e:
            print(f'Error: {e}')
        except ZeroDivisionError as e:
            print(f'Error: {e}')

main()