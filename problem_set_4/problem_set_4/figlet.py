import sys
from pyfiglet import Figlet
import random

"""
figlet = Figlet()
a = figlet.getFonts()
testing = random.choice(a)
figlet.setFont(font = testing)
print(figlet.renderText('angel'))"""


# Create the main function
def main():

    figlet = Figlet()
    # Gather the fonts in a list
    fonts = figlet.getFonts()
    # Randomize the fonts
    randomize_fonts = random.choice(fonts)

    # Promp the user for input
    text = input("Please enter your text here: ")

    # If zero command-line arguments
    if len(sys.argv) < 2:
        figlet.setFont(font=randomize_fonts)
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or "--font":
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))

main()
