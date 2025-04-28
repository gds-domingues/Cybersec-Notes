import validators

def main():
    # Get user input and print the result of the email validation
    print(validate(input("Enter your email: ").strip()))

def validate(address):
    # Use the validators.email function to check if the address is valid
    return "Valid" if validators.email(address) else "Invalid"

if __name__ == "__main__":
    main()

"""
The script utilizes the validators library to validate email addresses, prompting the user to input an email and then determining its validity. 
The validate function checks if the entered string adheres to the standard email format using the validators.email function. 
The result, either "Valid" or "Invalid," is then displayed to the user. This approach offers a simple and effective means of basic email validation in Python.
"""