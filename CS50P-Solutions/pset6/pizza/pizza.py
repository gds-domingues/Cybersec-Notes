import sys
import csv
import tabulate

# Check the number of command-line arguments
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# Check if the provided argument is a CSV file
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

try:
    # Try to open the CSV file in read mode
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    # Exit if the file is not found
    sys.exit("File does not exist")

# Use the CSV reader to read data from the file
reader = csv.reader(file, delimiter=',')
headers = next(reader)  # Get the header row

# Read the remaining rows from the CSV file
tables = [row for row in reader]

# Use tabulate to create a formatted table
result = tabulate.tabulate(tables, headers, tablefmt="grid")

# Print the tabulated result
print(result)


"""
This script reads a CSV file, extracts the headers and data, 
and then prints the data in a grid format using the tabulate library. 
The script checks for the correct number of command-line arguments, 
verifies that the file has a .csv extension, 
and handles the case where the file is not found.
"""