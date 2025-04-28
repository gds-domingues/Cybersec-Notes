# Infinite loop to repeatedly prompt the user for a fraction
while 1:
    try:
        # Get user input for a fraction and split it into numerator and denominator
        split = input('Fraction: ')
        x, y = split.split('/')
        x = int(x)
        y = int(y)

        # Calculate the percentage value of the fraction and round it
        p = round((x / y) * 100)
        p = int(p)

        # Check the percentage value and print the corresponding grade
        if p >= 99:
            print('F')
            break
        elif p <= 1:
            print('E')
            break
        else:
            print(f'{p}%')
            break
    except ValueError:
        # Handle the case where the input cannot be converted to integers
        pass
    except ZeroDivisionError:
        # Handle the case where the denominator is zero
        pass

"""
This code continuously prompts the user for a fraction, calculates its percentage value, and prints a corresponding grade. 
It uses a try-except block to catch ValueErrors (when the input cannot be converted to integers) and ZeroDivisionError (when the denominator is zero), 
allowing the program to keep running even if invalid inputs are provided. The loop breaks when a valid input is processed and the corresponding grade is printed.
"""
