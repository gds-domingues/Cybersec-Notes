# List of months
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Infinite loop to continuously prompt the user for a date
while True:
    # Get user input for a date
    date = input("Date: ")

    try:
        # Check if "/" is present in the date (mm/dd/yyyy format)
        if "/" in date:
            # Split the date into month, day, and year
            mm, dd, yyyy = date.split("/")
        # Check if "," is present in the date (month dd, yyyy format)
        elif "," in date:
            # Split the date into month and year
            mmdd, yyyy = date.split(", ")
            # Split the month and day
            mm, dd = mmdd.split(" ")
            # Find the index of the month in the months list and increment by 1
            mm = (months.index(mm)) + 1

        # Check if the month or day exceeds the valid range
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        # Catch various exceptions, such as ValueError for invalid month or day
        pass
    else:
        # Print the date in the format yyyy-mm-dd and break out of the loop
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break

"""
This code continuously prompts the user for a date and tries to parse it in two possible formats (mm/dd/yyyy or month dd, yyyy). 
It then checks if the month or day exceeds the valid range and prints the date in the format yyyy-mm-dd if successful. 
The input is case-sensitive for months (e.g., "January" must be spelled with an uppercase "J").
"""