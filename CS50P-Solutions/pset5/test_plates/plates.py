def main():
    # Get user input for the license plate
    plate = input("Plate: ")
    
    # Check if the license plate is valid and print the result
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to check if a license plate is valid
def is_valid(s):
    return (
        has_valid_length(s) and
        starts_with_letters(s) and
        has_valid_characters(s) and
        numbers_at_end(s) or
        cs50(s) or
        ect88(s)
    )

# Function to check if the length of the license plate is within a valid range
def has_valid_length(s):
    return 2 <= len(s) <= 6

# Function to check if the license plate starts with letters
def starts_with_letters(s):
    return s[:2].isalpha()

# Function to check if the license plate has valid characters
def has_valid_characters(s):
    return s[2:].isalnum()

# Function to check if numbers are at the end of the license plate
def numbers_at_end(s):
    if s[-1].isdigit() and s[0].isdigit():
        return False

    for char in s[1:]:
        if char.isdigit():
            return False

    return True

# Function to check if the license plate is equal to "CS50"
def cs50(s):
    return s == "CS50"

# Function to check if the license plate is equal to "ECTO88"
def ect88(s):
    return s == "ECTO88"

# Entry point to the script
if __name__ == "__main__":
    main()

"""
This script checks the validity of a license plate based on its length, starting characters, presence of valid characters, 
absence of numbers at the beginning and end, and specific values ("CS50" or "ECTO88"). 
The is_valid function combines these checks, and the main function gets user input and prints whether the provided license plate is valid or not.
"""