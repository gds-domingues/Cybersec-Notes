# Dictionary of products and their prices
products = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize a variable to keep track of the total cost
total = 0

try:
    # Infinite loop to continuously prompt the user for items
    while True:
        try:
            # Get user input for an item and capitalize the first letter of each word
            item = input('Item: ').title()
        except EOFError:
            # Break out of the loop if an EOFError occurs
            break

        # Check if the item is in the products dictionary
        if item in products:
            # Retrieve the price of the item from the dictionary
            price = products[item]
            # Add the price to the total cost
            total += price
            # Print the current total cost formatted as currency
            print(f"${total:.2f}")
        else:
            # If the item is not found, print a message and continue to the next iteration
            print("Item not found")
            continue

# Catch KeyboardInterrupt to handle manual interruption (Ctrl+C)
except KeyboardInterrupt:
    pass

"""
This code simulates a point-of-sale system where the user can input items, 
and the program calculates and displays the running total based on the prices of the items in the products dictionary. 
The input is case-sensitive, and the KeyboardInterrupt exception is caught to allow the user to interrupt the program using Ctrl+C.
"""

