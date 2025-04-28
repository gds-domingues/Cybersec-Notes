from datetime import date, datetime  # Import necessary modules for handling dates and times
import sys  # Import the sys module for system-related functionality
import math  # Import the math module for basic arithmetic operations
import inflect  # Import the inflect module for converting numbers to words

p = inflect.engine()  # Create an inflect engine instance for number-to-words conversion

def get_user_date_of_birth():
    # Function to prompt the user for their date of birth and return it as a datetime.date object
    user_date_str = input("Enter your date of birth in YYYY-MM-DD format: ")
    try:
        user_date = datetime.strptime(user_date_str, '%Y-%m-%d').date()  # Convert input string to datetime.date
        return user_date
    except ValueError:
        sys.exit('Invalid date format. Please enter the date in YYYY-MM-DD format.')  # Exit the program if the format is invalid

def calculate_age_in_minutes(user_date):
    # Function to calculate the user's age in minutes based on their date of birth
    today = date.today()
    birth_datetime = datetime.combine(user_date, datetime.min.time())
    today_datetime = datetime.combine(today, datetime.min.time())
    age_difference = today_datetime - birth_datetime
    age_in_minutes = math.ceil(age_difference.total_seconds() / 60)  # Calculate age in minutes, rounding up
    return age_in_minutes

def convert_minutes_to_words(minutes):
    # Function to convert the given number of minutes to words using the inflect module
    words = p.number_to_words(minutes)
    words_without_and = words.replace(' and ', ' ')  # Remove 'and' from the word representation
    return words_without_and.capitalize()  # Capitalize the result

def main():
    # Main function to execute the program
    user_date_of_birth = get_user_date_of_birth()  # Get the user's date of birth
    age_in_minutes = calculate_age_in_minutes(user_date_of_birth)  # Calculate age in minutes
    age_in_words = convert_minutes_to_words(age_in_minutes)  # Convert age in minutes to words
    print(f"{age_in_words} minutes")  # Print the result in the format "X minutes", where X is the age in words

if __name__ == "__main__":
    main()  # Execute the main function if the script is run as the main program

"""
This Python script calculates and prints the user's age in minutes. 
It uses the datetime module to handle date and time operations, the inflect module to convert numbers to words, 
and basic arithmetic with the math module. The script begins by prompting the user to enter their date of birth in the 'YYYY-MM-DD' format, 
converting the input string to a datetime.date object. 
It then calculates the age in minutes by finding the difference between the current date and time and the user's birth date and time. 
The age in minutes is then converted to words using the inflect module, and the final result is printed in the format "X minutes," where X is the age in words. 
If the user enters an invalid date format, the program exits with an error message. 
The script is wrapped in a main() function, and the main block ensures that the script runs when executed as the main program.
"""