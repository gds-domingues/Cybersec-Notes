# Import the regular expression module
import re

# Main function to prompt the user for input and display the count
def main():
    inp: str = input("Text: ")
    print(count(inp))

# Function to count occurrences of the word "um" at the beginning of a line or after whitespace
def count(s: str):
    # Use regular expression to find matches, ignoring case
    res: list[str] = re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE)
    # Return the count of matches
    return len(res)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

"""
This Python script utilizes the re module to count occurrences of the word "um" at the beginning of a line or after a whitespace in a given text. 
The main function prompts the user for input, and the count function processes the text using a regular expression. 
The script then outputs the count of occurrences. The regular expression pattern looks for "um" at the start of a line (^um\b) or after a whitespace ((?<=\s)um\b),
with case-insensitivity (re.IGNORECASE). The count is obtained using re.findall, and the result is printed to the user.
"""