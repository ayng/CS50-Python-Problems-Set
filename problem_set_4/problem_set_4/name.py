import sys
# sys.argv
# argv stands for argument vector. The list of all of the words I typed in my CLI before I hit enter

# Retrieve the value in index 1 of my command line below. Type 'python name.py Angel' to see 'hello, my name is Angel'
# sys.argv[1] retrieves whatever value I typed after 'python name.py...'
"""
print('hello, my name is', sys.argv[1])
"""

# Add an exception in case the user does not type their name after 'python name.py'
"""
try:
    print('hello, my name is', sys.argv[1])
except IndexError:
    print('Too few arguments')
"""

# We don't have to handle exceptions if we can check for the things we are worried about to provide refined advice.
# Using conditionals
"""
if len(sys.argv) < 2:
    print('Too few arguments')
elif len(sys.argv) > 2:
    print('Too many arguments')
else:
    print('hello, my name is', sys.argv[1])
"""

# There is something nice about keeping all of your error handling code separate from what needs to be executed
"""
if len(sys.argv) < 2:
    sys.exit('Too few arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many arguments')
print('hello, my name is', sys.argv[1])
"""

# Print multiple names if multiple names are provided
if len(sys.argv) < 2:
    sys.exit('Too few arguments')

for arg in sys.argv[1:]: # Slicing is introduced here. Start at index 1 and continue until the end to avoid printing the first argument 'hello, my name is name.py'
    print('hello, my name is', arg)

