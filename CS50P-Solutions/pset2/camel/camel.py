# Get user input for a variable name in camel case
camel_case_input = input("Enter a variable name in camel case: ")

# Initialize an empty string for the snake case version
snake_case_output = ''

# Iterate through each character in the camel case input
for char in camel_case_input:
    # Check if the character is uppercase
    if char.isupper():
        # If uppercase, add an underscore and the lowercase version of the character to the snake case output
        snake_case_output += '_' + char.lower()
    else:
        # If not uppercase, simply add the character to the snake case output
        snake_case_output += char

# Print the resulting snake case version
print(f"The snake case version is: {snake_case_output}")
"""
This code takes a variable name in camel case as input, converts it to snake case, and then prints the snake case version. 
It adds underscores before each uppercase letter and converts the uppercase letter to lowercase.
"""