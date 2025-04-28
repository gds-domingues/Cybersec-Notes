# Import the inflect module and alias it as 'inf'
import inflect as inf

# Function to print the plural form of a list of items
def print_plural(items):
    # Create an inflect engine
    p = inf.engine()
    # Join the items using the inflect engine to get their plural form
    plurals = p.join(items)
    # Print a farewell message with the plural form of the items
    print('Adieu, adieu, to', plurals)

# List to store user inputs
user_inputs = []

# Main function to continuously prompt the user for input
def main():
    while True:
        try:
            # Get user input and append it to the list
            item = input()
            user_inputs.append(item)
        except EOFError:
            # If an EOFError occurs (end of input), call the print_plural function and break out of the loop
            print_plural(user_inputs)
            break

# Call the main function when the script is executed
if __name__ == "__main__":
    main()

"""
This code continuously prompts the user for input, appends each input to a list, 
and prints a farewell message with the plural form of the collected items when an EOFError occurs (end of input). 
The inflect module is used to handle the pluralization of the items. 
The loop breaks and the farewell message is printed when the user triggers an EOFError (e.g., using Ctrl+D on Unix-based systems).
"""