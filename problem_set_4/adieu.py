"""
Implement a program that prompts the user for names, one per line, until the user inputs control-d.
Assume the user will input at least one name.
Then, bid adieu to those names, separating two names with one and, three names with two commas and one and, 
and n names with n - 1 commas and one and, as in the below:

Adieu, adieu to Liesl
Adieu, adieu to Liesl and Friedrich
Adieu, adieu to Liesl, Friedrich, and Louisa
Adieu, adieu to Liesl, Friedrich, Louisa, and Kurt
"""

import inflect
p = inflect.engine()

# Initiate empty list
names = []

# Collect entries and store them in 'names' list
try:
    while True:
        name = input('Please Enter a name: ')
        names.append(name)
except EOFError:
    print('\nYou stopped entering names. Your response has been recorded.')

# Use inflect to join names with proper punctuation
formatted_names = p.join(names)

# Print the farewell message
print(f'Adieu, adieu, to ' + formatted_names)












