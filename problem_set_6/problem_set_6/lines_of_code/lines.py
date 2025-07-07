import sys
"""
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file, 
excluding comments and blank lines. If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, 
or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) 
Assume that any line that only contains whitespace is blank.
"""
def main():
    # Check the CL arguments
    check_command_line_args()
    # Try to open the file
    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
        #print(lines)
    # If can't open, the file does not exist
    except FileNotFoundError as e:
        sys.exit(f'File does not exist: {e}')
    # Loop through the lines and count non blank and non comment lines
    counter = 0 # Initiate the counter
    for line in lines:
        line_no_left_space = line.lstrip()
        if line_no_left_space.startswith('#') or line_no_left_space == '':
            pass
        else:
            counter += 1
    print(f'The total number of non blank lines in your file {sys.argv[1]} is {counter}.')

# Function to check the CL arguments
def check_command_line_args():
    # Check how many elements in the CL
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    # Check if it is a Python file
    if not sys.argv[1].endswith('.py'):
        sys.exit('Not a Python file.')

main()