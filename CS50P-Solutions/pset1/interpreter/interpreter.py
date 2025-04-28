# Get user input for a mathematical expression
e = input("Expression: ")

# Split the expression into three parts (x, operator, z) based on spaces
x, y, z = e.split(" ")

# Convert x and z to float type for numerical operations
x = float(x)
z = float(z)

# Check the operator and perform the corresponding mathematical operation
if y == "+":
    # If the operator is addition, print the result of x + z
    print(x + z)
elif y == "-":
    # If the operator is subtraction, print the result of x - z
    print(x - z)
elif y == "*":
    # If the operator is multiplication, print the result of x * z
    print(x * z)
else:
    # If the operator is not addition, subtraction, or multiplication, assume division and print the result of x / z
    print(x / z)
"""
This code takes a mathematical expression as input (in the form of "x operator z"), 
splits it into its components, converts the numeric parts to float, and then performs the corresponding operation based on the operator. 
If the operator is not one of "+", "-", or "*", it assumes division ("/"). The result is then printed.
"""