def main():
    # Get user input for a word
    word = input("Input: ")
    
    # Call the shorten function to remove vowels from the word
    shortened_word = shorten(word)
    
    # Print the shortened word
    print("Output: " + shortened_word)

# Function to remove vowels from a word
def shorten(word):
    # Initialize an empty string to store the word without vowels
    word_without_vowels = ""
    
    # Iterate through each letter in the word
    for letter in word:
        # Check if the lowercase version of the letter is not a vowel
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # Add the letter to the word without vowels
            word_without_vowels += letter
    
    # Return the word without vowels
    return word_without_vowels

# Entry point to the script
if __name__ == "__main__":
    main()

"""
This script removes vowels from a given word and prints the shortened version of the word. 
The shorten function iterates through each letter in the word, 
and if the lowercase version of the letter is not a vowel, it adds the letter to the result. 
The main function gets user input, calls the shorten function, and prints the result.
"""