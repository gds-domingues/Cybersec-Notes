def main():
    # Get user input and print the result of the validation
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        # Split the IP address into four octets
        w, x, y, z = ip.split('.')
        
        # Convert octets to integers
        w, x, y, z = int(w), int(x), int(y), int(z)
        
        # Check if each octet is within the valid range
        if w > 255 or x > 255 or y > 255 or z > 255:
            return False
        elif w == '' or x == '' or y == '' or z == '':
            return False  # Check for empty octets
        else:
            return True
    except ValueError:
        return False  # ValueError occurs if conversion to int fails

if __name__ == "__main__":
    main()

"""
The script correctly checks for the correct number of octets (four) and attempts to convert them to integers.
It checks if each octet is within the valid range (0-255).
The check for empty octets (w == '' or x == '' or y == '' or z == '') may not work as expected. If the input string has consecutive dots, 
the split method may produce empty strings. You might want to consider additional checks or use a more robust method for IPv4 validation.
Your script returns False for a ValueError, which occurs if conversion to an integer fails. This is reasonable for basic validation.
"""