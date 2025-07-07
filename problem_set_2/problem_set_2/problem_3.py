"""

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) 
omitted, whether inputted in uppercase or lowercase.

"""

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    original = input("Orignal text: ")
    print(convert(original))

def convert(text):
    result = ""

    for c in text:
        if c in vowels:
            continue
        else:
            result += c # Take the current value of 'result' and add to it
    
    return result

main()
