import random as rn

try:
    # Get user input for the level
    n = input('Level: ')
    n = int(n)
except ValueError:
    # Handle the case where the input for the level is not a valid integer
    pass

# Infinite loop to continuously prompt the user for guesses
while True:
    try:
        # Get user input for the guess
        p = input('Guess: ')
        p = int(p)
        
        # Generate a random number within the specified level
        s = rn.randrange(0, n, 1)

        # Compare the guess with the random number
        if p < s:
            print('Too small!')
        elif p > n:
            # If the guess is greater than the specified level, continue to the next iteration
            continue
        elif p > s:
            print('Too large!')
        elif p == s:
            print('Just right!')
            # Break out of the loop if the guess is correct
            break
        else:
            # Continue to the next iteration if none of the above conditions are met
            continue
    except IndexError:
        # Handle the case where an IndexError occurs (e.g., if the specified level is 0)
        pass
    except ValueError:
        # Handle the case where the input for the guess is not a valid integer
        pass

"""
This code is a guessing game where the user needs to guess a randomly generated number within a specified level. 
The program provides feedback on whether the guess is too small, too large, or just right. 
The loop continues until the correct guess is made. 
The provided code includes error handling for cases where the user inputs non-integer values or the level is 0.
"""