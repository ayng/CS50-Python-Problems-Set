import sys
from tabulate import tabulate
"""
In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
"""
def main():
    # Ensure user entered one CL argument
    check_command_line()
    # Create empty list to hold lines from csv
    empty_list = []
    try:
        with open(sys.argv[1], 'r', encoding = 'utf-8-sig') as file:
            for line in file:
                line = line.replace('"', '').lstrip().rstrip() # Remove quotation marks from each line
                split_line = line.split(',') # Split the line using commas
                empty_list.append(split_line) # Append the clean line to the empty_list
    except FileNotFoundError:
        print('File not found, please try again.')
    # Final print statement
    print(tabulate(empty_list,headers = "firstrow", tablefmt= 'grid'))

def check_command_line():
    # Check if user entered exactly one CL argument
    if len(sys.argv) != 2:
        sys.exit('You entered too many or too few command line arguments. Please only enter 2 command line arguments.')
    # Ensure user keyed in .csv file
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Your file does not have the proper extension (.csv).')

main()