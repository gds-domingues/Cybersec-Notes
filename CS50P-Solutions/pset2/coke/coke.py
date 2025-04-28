# Initial amount due
amount_due = 50

# Infinite loop to simulate a vending machine until the user decides to exit
while True:
    # Display the current amount due
    print("Amount Due:", amount_due)

    # Get user input for the coin to be inserted
    insert_coin = input("Insert Coin: ")
    insert_coin = int(insert_coin)

    # Check if the inserted coin is a valid denomination (5, 10, 25, or 50)
    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25 or insert_coin == 50:
        # Calculate the change owned after the coin is inserted
        change_owned = amount_due - insert_coin

        # Check if there is still remaining amount due after the coin is inserted
        if change_owned > 0:
            # Update the amount due if change is still owed
            amount_due = amount_due - insert_coin
        elif change_owned < 0:
            # If change is negative, the user has overpaid, calculate the change and exit the loop
            change_owned = (change_owned * (-1))
            print("Change Owed:", change_owned)
            break
        else:
            # If change is zero, exit the loop
            print("Change Owed:", change_owned)
            break
"""
This code simulates a vending machine where the user can insert coins (5, 10, 25, or 50) to pay the amount due. 
It calculates the change owed to the user or exits the loop if the amount is fully paid. 
The user can keep inserting coins until the desired amount is paid or receive change if they overpay.
"""
