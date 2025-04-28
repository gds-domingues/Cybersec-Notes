import sys
import random
from pyfiglet import Figlet

# Function to get a random font from the available fonts in pyfiglet
def get_random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    return random.choice(fonts)

# Main function to handle command-line arguments and generate Figlet text
def main():
    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # If no arguments provided, get a random font
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        # If two arguments provided with '-f' or '--font' flag, set the font to the specified value
        font_name = sys.argv[2]
    else:
        # If incorrect number or format of arguments, print usage message and exit
        sys.exit("Usage: python figlet.py [-f FONT_NAME]")

    # Create a Figlet object with the specified font
    figlet = Figlet(font=font_name)
    
    # Get user input for text to be transformed into Figlet art
    text = input("Enter text: ")
    
    # Generate Figlet art for the input text
    output = figlet.renderText(text)
    
    # Print the generated Figlet art
    print(output)

# Entry point to the script
if __name__ == "__main__":
    main()

"""
This script uses the pyfiglet library to generate Figlet text. 
The user can optionally specify a font using the -f or --font flag in the command line, 
or a random font will be chosen if no arguments are provided. 
The generated Figlet art is then printed.
"""