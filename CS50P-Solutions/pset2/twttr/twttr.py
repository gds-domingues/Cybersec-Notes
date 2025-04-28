# Get user input
Input = input("Input: ")

# Initialize an empty list to store characters without vowels
string = []

# Iterate through each character in the input
for c in Input:
    # Check if the character is not a vowel (both lowercase and uppercase)
    if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u' and c != 'A' and c != 'E' and c != 'I' and c != 'O' and c != 'U':
        # If not a vowel, append it to the list
        string.append(c)

# Join the list of characters into a string
final = "".join(string)

# Print the resulting string without vowels
print("Output:", final)

"""
This code removes vowels from the user-provided input and prints the resulting string without vowels. 
It iterates through each character in the input, checks if it is a vowel, and appends non-vowel characters to the list. 
Finally, it joins the list into a string and prints the output.
"""