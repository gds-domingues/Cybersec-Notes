import requests as rq
import sys

# Function to fetch the current Bitcoin price in USD from the Coindesk API
def get_price():
    try:
        r = rq.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        return r.json()['bpi']['USD']['rate_float']
    except requests.exceptions.RequestException:
        sys.exit("Connection error")

# Main function to handle command-line arguments and print formatted Bitcoin prices
def main():
    try:
        # Check the number of command-line arguments
        if len(sys.argv) == 1:
            # If no arguments provided, get the current Bitcoin price
            price = get_price()
        elif len(sys.argv) == 3 and (sys.argv[1] == '-p' or sys.argv[1] == '--price'):
            # If two arguments provided with '-p' or '--price' flag, set the price to the specified value
            price = float(sys.argv[2])
            if price < 0:
                sys.exit("Price must be positive")
        else:
            try:
                # If one argument provided, calculate the Bitcoin price based on the specified multiplier
                price = get_price()
                price = float(price) * float(sys.argv[1])
                formatted_price = "{:.4f}".format(price)
                formatted_price = float(formatted_price)
                print(f"${formatted_price:,}")  # Format with commas
            except ValueError:
                sys.exit("Price must be a number")
    except ValueError:
        sys.exit("Usage: python price.py [-p PRICE]")

    # Exit with code 1 on success

# Entry point to the script
if __name__ == "__main__":
    main()
"""
This script fetches the current Bitcoin price from the Coindesk API, 
and it can be run with optional command-line arguments to specify a custom price or a multiplier for the current price. 
It handles various error cases and prints formatted Bitcoin prices.
"""