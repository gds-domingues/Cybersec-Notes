import sys
import csv

def main():
    # Check command-line arguments and process data
    check()
    scourgify()

def check():
    # Check the number and format of command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Input file is not a CSV file")

def scourgify():
    try:
        # Open input and output CSV files
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")

    except FileNotFoundError:
        sys.exit("Could not read file")

    # Create a CSV reader for the input file
    column_data = csv.DictReader(input_file, delimiter=",")

    # Create a CSV writer for the output file with specified columns
    column_writer = csv.DictWriter(output_file, ["first", "last", "house"])

    # Write header to the output file
    column_writer.writeheader()

    # Process each row and write modified data to the output file
    for row in column_data:
        last, first = row["name"].split(",")
        column_writer.writerow({
            "first": first.strip(),
            "last": last,
            "house": row["house"]
        })

if __name__ == "__main__":
    main()

"""
This script follows a modular structure with a main function and two sub-functions (check and scourgify). 
It checks the command-line arguments for correctness, processes the data from the input CSV file, 
and writes the modified data to the output CSV file.
"""