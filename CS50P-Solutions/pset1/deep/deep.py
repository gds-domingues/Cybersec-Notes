# Get user input, convert to lowercase, and remove leading/trailing whitespaces
a = input("What is the answer to the great question of life, the universe, and everything? ").lower().strip()

# Check if the user input is equal to "42", "forty two", or "forty-two"
if a == "42" or a == "forty two" or a == "forty-two":
    # If true, print "yes"
    print("yes")
# If the input does not match any of the specified conditions
else:
    # Print "no"
    print("no")
"""
This code asks the user a question and checks
if the input is equal to different variations of the answer ("42", "forty two", or "forty-two"). 
If there is a match, it prints "yes"; otherwise, it prints "no"
"""