# TO DO!!
# * LINE 72: Ask why get_name is used instead of get_name(). It is explained in the video, so feed chatgpt the transcript and have it simplify

# -----------------------------------

# # Read, interpret, and parse a csv file
# with open('students.csv') as file:
#     for line in file:
#         row = line.rstrip().split(',') # take the current line, remove the white space at the end, whatever the result is call split to return a list
#         print(f'{row[0]} is in {row[1]}')

# -----------------------------------

# # Read, interpret, and parse a csv file
# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',') # take the current line, remove the white space at the end, whatever the result is call split to return a list
#         print(f'{name} is in {house}')

# -----------------------------------

# What if I want to sort?
# THIS IS NOT WRONG, BUT I AM SORTING THE ENTIRE LINE BUT ITS NOT WELL DESIGNED
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         # Before printing, store it in the list to accumulate and sort later
#         students.append(f'{name} is in {house}')

# for student in sorted(students):
#     print(student)

# -----------------------------------

# temporarily, create a dictionary that stores name with house

# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {} # create an empty dictionary to store each student
#         student['name'] = name # the key 'name' holds the name that was stripped
#         student['house'] = house # the key 'house' hoolds the house that was stripped
#         # Append to the students list that particular student (which is a dictionary)
#         students.append(student)

# for student in students:
#     print(f'{student['name']} is in {student['house']}') # access each key 'name' and each key 'house from the dictionaries in the students list


# -----------------------------------

# Let's sort by the students names instead, not the entire sentence

# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house} # Create a dictionary with keys 'name' and 'house' and populate values for each key
#         # Append to the students list that particular student (which is a dictionary)
#         students.append(student)

# # Return the student's name from a dictionary
# def get_name(student):
#     return student['name']

# # Sort this list (students) by looking at this key (name) in each dictionary:
# # Python allows you to pass functions as arguments into other functions
# for student in sorted(students, key = get_name): # REVEIW THIS IN MORE DETAIL. 
#     print(f'{student['name']} is in {student['house']}') # access each key 'name' and each key 'house from the dictionaries in the students list

# -----------------------------------

# Let's sort by the students names instead, not the entire sentence SIMPLIFIED
# **********************
# INTRODUCTION TO LAMBDA
# **********************
# If you are defining a variable and then immediately using it, there are workarounds to simplify the code
# Similarily, if you are defining a function and then immediately using it, there are workarounds to simplify the code
# Use lambda
# lambda function is an anonymous function, a function without a name.
# why? bc you don't need to give it a name if you are only going to call it in one place

"""
key = lambda student: student['name']
lambda says hey python here comes a function without a name
that function takes a parameter. Here it is called student bc this function is called on every dictionary in students list
What do I want to return?
    - well given a student, I want to index into that dictionary and access the name so the name is returned.
"""

# students = []

# with open('students.csv') as file:
#     for line in file:
#         name, house = line.rstrip().split(',')
#         student = {'name': name, 'house': house} # Create a dictionary with keys 'name' and 'house' and populate values for each key
#         # Append to the students list that particular student (which is a dictionary)
#         students.append(student)

# # Sort this list (students) by looking at this key (name) in each dictionary:
# # Python allows you to pass functions as arguments into other functions
# for student in sorted(students, key = lambda student: student['name']): # REVEIW THIS IN MORE DETAIL. 
#     print(f'{student['name']} is in {student['house']}') # access each key 'name' and each key 'house from the dictionaries in the students list

# -----------------------------------

# Additionally, we can do this by using the csv.reader function

# import csv

# students = []

# with open('students.csv') as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({'name': name, 'home': home})

# for student in sorted(students, key = lambda student: student['name']):
#     print(f'{student['name']} is from {student['home']}')

# -----------------------------------

# # Use a dictionary reader
# import csv

# students = []

# with open('students.csv') as file:
#     reader = csv.DictReader(file) # Iterates top to bottom loading each line of text as a dictionary of columns. Automatic access to column names
#     for row in reader:
#         students.append({'name': row['name'], 'home': row['home']}) 

# for student in sorted(students, key = lambda student: student['name']):
#     print(f'{student['name']} is from {student['home']}')

# -----------------------------------

# Write into a csv

# Delete the contents of students except for the headers name,home

# import csv

# name = input('What is your name: ')
# home = input('Where is your home: ')

# with open('students.csv', 'a') as file: # open in append mode to add more students to the file instead of overwriting
#     writer = csv.writer(file) # writer function takes the file as an argument
#     writer.writerow([name, home]) # pass into writerow() the line that I want to write on the file

# -----------------------------------


import csv

name = input('What is your name: ')
home = input('Where is your home: ')

with open('students.csv', 'a') as file: # open in append mode to add more students to the file instead of overwriting
    writer = csv.DictWriter(file, fieldnames = ['name', 'home']) # DictWriter is a dictionary writer
    writer.writerow({'name': name, 'home': home})
