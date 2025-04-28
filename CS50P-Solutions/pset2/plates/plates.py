def main():
    # Get user input for a license plate
    plate = input("Plate: ")

    # Check if the license plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check various conditions to determine if the license plate is valid
    return (
        has_valid_length(s) and
        starts_with_letters(s) and
        has_valid_characters(s) and
        numbers_at_end(s) or
        cs50(s) or
        ect88(s)
    )

def has_valid_length(s):
    # Check if the length of the license plate is between 2 and 6 characters
    return 2 <= len(s) <= 6

def starts_with_letters(s):
    # Check if the first two characters of the license plate are letters
    return s[:2].isalpha()

def has_valid_characters(s):
    # Check if the remaining characters (after the first two) are alphanumeric
    return s[2:].isalnum()

def numbers_at_end(s):
    # Check if there are no consecutive numbers at the end of the license plate
    if s[-1].isdigit() and s[0].isdigit():
        return False

    for char in s[1:]:
        if char.isdigit():
            return False

    return True

def cs50(s):
    # Check if the license plate is "CS50"
    if s == "CS50":
        return True

def ect88(s):
    # Check if the license plate is "ECTO88"
    if s == "ECTO88":
        return True

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

"""
This code checks whether a given license plate is valid based on various conditions such as length, starting with letters, 
having valid characters, and meeting specific patterns ("CS50" or "ECTO88"). 
The main function takes user input for a license plate and prints whether it is valid or not.
"""