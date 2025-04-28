def main():
    # Get the cost of the meal from the user and convert it to a floating-point number
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Get the desired tip percentage from the user and convert it to a floating-point number
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount by multiplying the meal cost and the tip percentage
    tip = dollars * percent
    
    # Print the calculated tip amount formatted with two decimal places
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the dollar sign from the input string and convert the result to a floating-point number
    d_w = d.replace("$", "")
    return float(d_w)

def percent_to_float(p):
    # Remove the percentage sign from the input string, convert to a floating-point number, and divide by 100
    p_w = p.replace("%", "")
    p_w = float(p_w) / 100
    return float(p_w)

# Call the main function to run the program
if __name__ == "__main__":
    main()

    """
    This code take user input for the cost of a meal and the desired tip percentage, 
    calculates the tip amount, and then prints the result. The dollars_to_float and 
    percent_to_float functions handle the conversion of input strings to floating-point 
    numbers, removing any extra characters like dollar signs or percentage signs.
    """