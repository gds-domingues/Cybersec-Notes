import sys

# Check the number of command-line arguments
if len(sys.argv) > 2:
    sys.exit('Too many arguments')
if len(sys.argv) <= 1:
    sys.exit('Too few arguments')

# Check if the provided argument is a Python file
if '.py' not in sys.argv[1]:
    sys.exit('It is not a Python file')

try:
    # Try to open the file in read mode
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    # Exit if the file is not found
    sys.exit('File not found')

# Initialize a variable to count non-empty lines
lines = 0

# Iterate through each line in the file
for line in file.read().splitlines():
    # Skip empty lines
    if len(line.strip()) == 0:
        continue
    
    # Check if the line does not start with '#'
    if not line.strip().startswith('#'):
        lines += 1

# Print the count of non-empty lines
print(lines)

"""
This script uses command-line arguments to specify the Python file to be analyzed. 
It checks the number of non-empty lines in the file and excludes lines that start with the '#' character, which are considered comments in Python. 
If the file is not found or if there are issues with the command-line arguments, appropriate error messages are displayed, and the script exits.
"""