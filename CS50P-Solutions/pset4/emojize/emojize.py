import emoji

# Function to convert emoticons to emoji using the emoji library
def emojize(emo):
    # Use the emoji.emojize() function to convert emoticons to emoji
    # The 'language' parameter is set to 'alias' to use emoji aliases
    test = emoji.emojize(emo, language='alias')
    return test

# Get user input for an emoticon
emoticon = input("Input: ")

# Call the emojize function and print the result
print(emojize(emoticon))

"""
This code uses the emoji library to convert emoticons to emoji. 
The emojize function takes an emoticon as input, converts it using emoji aliases, and then prints the resulting emoji. 
The user is prompted to input an emoticon, and the script displays the corresponding emoji.
"""