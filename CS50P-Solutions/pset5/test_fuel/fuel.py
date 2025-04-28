def main():
    # Get user input for the fraction
    fraction = input('Fraction: ')
    
    # Call the convert function to convert the fraction to a percentage
    percentage = convert(fraction)
    
    # Call the gauge function to categorize the percentage and return the result
    result = gauge(percentage)
    
    # Print the result
    print(result)

def convert(fraction):
    # Split the fraction into numerator and denominator
    x, y = fraction.split('/')
    
    # Convert the numerator and denominator to integers
    x = int(x)
    y = int(y)
    
    # Calculate the percentage and round it
    p = round((x / y) * 100)
    
    # Convert the percentage to an integer and return it
    return int(p)

def gauge(percentage):
    # Categorize the percentage based on certain conditions
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        # Return the formatted percentage as a string
        return f'{percentage}%'

if __name__ == "__main__":
    main()

"""
This script calculates the percentage of a given fraction and then categorizes it as 'F' if it's greater than or equal to 99%, 
'E' if it's less than or equal to 1%, or returns the formatted percentage as a string otherwise.
"""