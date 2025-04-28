# Initialize an empty dictionary to store products and their counts
products = {}

try:
    # Infinite loop to continuously read input until an EOFError occurs
    while True:
        # Get user input for a product and convert it to lowercase
        item = input().lower()

        # Check if the product is already in the dictionary
        if item in products:
            # If yes, increment the count
            products[item] += 1
        else:
            # If not, add the product to the dictionary with a count of 1
            products[item] = 1

# Catch EOFError to handle the end of input
except EOFError:
    # Sort the items in the dictionary based on their keys
    sorted_items = sorted(products.items())

    # Iterate through the sorted items and print the counts and product names in uppercase
    for key, value in sorted_items:
        print(f"{value} {key.upper()}")

"""
This code continuously reads user input for product names, keeps track of the count of each product in a dictionary, 
and prints the sorted counts along with the corresponding product names in uppercase when an EOFError occurs. 
The input is case-insensitive, as all product names are converted to lowercase.
"""