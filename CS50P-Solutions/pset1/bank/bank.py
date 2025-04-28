# Get user input and remove leading/trailing whitespaces, then convert to lowercase
user = input("Greeting: ").strip().lower()

# Check if the user input starts with "hello"
if user.startswith("hello"):
    # If true, print "$0"
    print("$0")
# Check if the user input starts with "h" (but not "hello" as it was checked before)
elif user.startswith("h"):
    # If true, print "$20"
    print("$20")
# If none of the above conditions are met
else:
    # Print "$100"
    print("$100")
"""
the code provides different responses based on the user's input. 
If the input starts with "hello," it prints "$0". If it starts with just "h," it prints "$20". 
Otherwise, it prints "$100"
"""