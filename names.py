"""
names = []

for _ in range(3):
    name = input('What is your name: ')
    names.append(name)

for name in sorted(names):
    print(f'hello, {name}')

"""
# -----------------------------------

"""
name = input('What is your name: ')

# Write names to a file
with open('names.txt', 'a') as file: # 'a' for append. The structure here reads as with, function in question, as, specify the name of the variable that should be assigned the return value of open
    file.write(f'{name}\n')

"""

# -----------------------------------

"""
# Write code that reads an existing file
with open('names.txt', 'r') as file:
    lines = file.readlines() # Read all the lines in a file and store them as a list

# Iterate through each line and print them
for line in lines:
    print('hello,', line.rstrip()) # Strip off at the end of the line the actual new line
"""

# -----------------------------------

# # Simplified
# with open('names.txt', 'r') as file: # open the file
#     for line in file: 
#         print('hello,', line.rstrip())

# -----------------------------------

"""
# Simplified Sorted
names = []

with open('names.txt') as file: # default is 'r' aka read
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f'hello, {name}')
"""

# -----------------------------------

# # Simplified sorted even more
# with open('names.txt') as file:
#     for line in sorted(file):
#         print('hello,', line.rstrip())

# -----------------------------------

# # Simplified sorted in reverse
# names = []

# with open('names.txt') as file: # default is 'r' aka read
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names, reverse = True):
#     print(f'hello, {name}')

# -----------------------------------

# What if we want to store information like a student's name and their house?
# Create a csv 'students.csv': code students.csv





