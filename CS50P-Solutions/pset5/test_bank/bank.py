def main():
    # Get user input for greeting and convert it to lowercase
    greeting = input().lower()
    
    # Call the value function with the input and print the result
    a = value(greeting)
    print(a)

def value(greeting):
    # Check the prefix of the greeting and assign a numerical value accordingly
    if greeting.startswith("hello"):
        greeting = 0
        return greeting
    elif greeting.startswith("h"):
        greeting = 20
        return greeting
    else:
        greeting = 100
        return greeting

# Entry point to the script
if __name__ == "__main__":
    main()

"""
This script essentially categorizes user input based on its prefix. If the input starts with "hello," 
it assigns a value of 0; if it starts with "h," it assigns a value of 20; otherwise, it assigns a value of 100. 
The script then prints the resulting value.
"""