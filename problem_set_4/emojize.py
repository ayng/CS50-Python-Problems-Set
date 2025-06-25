import emoji

# print(emoji.emojize(":thumbs_up:"))

"""
In a file called emojize.py, 
implement a program that prompts the user for a str in English and outputs the 'emojized' version of that str, 
converting any codes (or aliases) therein to their corresponding emoji.
"""

def main():
    e = input("Please enter an emoji in string format: ")
    print(converted(e))

def converted(text):
    return emoji.emojize(text, language="alias")

main()
