# Define a function named 'convert' that replaces ':)' with '🙂' and ':(' with '🙁'
def convert(a):
    a = a.replace(':)', '🙂')
    a = a.replace(':(', '🙁')
    return a

# Get user input
x = input()

# Call the 'convert' function to replace emoticons and update the string
x = convert(x)

# Print the updated string
print(x)
"""
This code defines a function named convert that replaces specific 
emoticons with corresponding Unicode emojis. It then takes user input, 
calls the convert function to replace the emoticons, and finally prints the updated string. 
The comments provide an explanation for each step in the process.
"""