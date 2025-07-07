"""
Implement a program that:
    - Expects the user to provide 2 CL arguments
        - The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house
        - the name of a new csv to write as output, whose columns should be, in order, first, last, and house
    - Converts that input to that output, splitting each name into a first name and last name. 
    - If the user does not provide exactly 2 CL arguments, or if the first cannot be read, the program should exit via sys.exit() 
"""
import sys
import csv

def main():
    # Ensure the user provided valid CL arguments
    check_command_line_args()
    # Create empty list to store name and house
    empty_list = []
    # Read the file
    with open(sys.argv[1], 'r', encoding = 'utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader) # Skip the first row
        for line in reader:
            # Convert list to string to modify
            line = str(line) 
            last_name, first_name, house = line.split(',') # Split by comma
            # Clean the string
            last_name = last_name[2:].lstrip().rstrip() # Clean last name
            first_name = first_name.lstrip().rstrip() # Clean first name
            house = house[:-2].lstrip().rstrip() # Clean the house
            # Append dictionary to empty_list
            empty_list.append({
                'Last Name': last_name, 
                'First Name': first_name, 
                'House': house
                })
    
    # Write empty_list to the file
    with open(sys.argv[2], 'w', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = ['Last Name', 'First Name', 'House'])
        writer.writeheader()
        for row in empty_list:
            writer.writerow(row)

def check_command_line_args():
    # Ensure the user entered 2 command line arguments
    if len(sys.argv) != 3:
        print('Invalid input: You need 3 arguments in your command-line argument.')
    # Ensure the output file ends with '.csv'
    elif not sys.argv[2].endswith('.csv'):
        print("Invalid input: The extension of your output file must end with '.csv'.")
    else:
        # Ensure the input file exist
        try:
            with open(sys.argv[1]) as f:
                pass
        except FileNotFoundError:
            print(f'Invalid input: The file you are attempting to read is not found.')

main()