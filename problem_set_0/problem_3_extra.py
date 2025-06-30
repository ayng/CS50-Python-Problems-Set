# Making Faces

# Concept: Using functions, string replacement, and working with specific patterns.

"""
Practice Problems:

1.	Emoji Replacer

Write a program emoji_replace.py that converts text-based emoticons like :D to 😁 and :P to 😜.
Example:
Input: I am happy :D but also hungry :P
Output: I am happy 😁 but also hungry 😜

"""

def main():
    text = input("What? ")
    print(convert(text))

def convert(input_text):
    return(input_text).replace(":D", "😁").replace(":P", "😜")

main()




"""
2.	Abbreviation Expander

Write a program expand_abbreviations.py that replaces common abbreviations in a sentence with their full forms.
Example:
Input: brb, going afk
Output: be right back, going away from keyboard

"""

def main():
    text2 = input("What? ")
    print(extended(text2))

def extended(input_text_2):
    return(input_text_2).replace("brb", "be right back").replace("afk", "away from keyboard")

main()

"""

3.	Case Converter Function
Write a function convert_case(input_string, to_case) where to_case can be uppercase, lowercase, or capitalize, and it returns the appropriately converted string. 
Implement a main function to test this behavior.

"""

# Come back to this once I understand conditionals or dictionaries.