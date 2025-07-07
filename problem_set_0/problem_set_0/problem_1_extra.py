# Indoor Voice Advanced

# Concept: Understanding string manipulation and user input/output.

"""
1.	Shouting Back

Write a program shout.py that prompts the user for input and outputs the input in uppercase.
Example:
Input: hello world
Output: HELLO WORLD

"""

text = input("What? ").upper()
print(text)

"""
2.	Swap the Case

Write a program swap_case.py that prompts the user for input and outputs the input with all uppercase letters converted to lowercase and vice versa.
Example:
Input: Hello World
Output: hELLO wORLD

"""

text2 = input("What again? ").swapcase()
print(text2)

"""
3.	Remove the Vowels

Write a program no_vowels.py that prompts the user for input and outputs the input with all vowels removed.
Example:
Input: hello world
Output: hll wrld

"""

#code no_vowels.py

text3 = input("What? ")
translation = str.maketrans("","","aeiouAEIOU")
print(text3.translate(translation))