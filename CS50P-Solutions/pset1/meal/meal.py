# Function to convert time from HH:MM format to a decimal representation
def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(':')
    # Convert hours and minutes to float type for decimal representation
    hours = float(hours)
    minutes = float(minutes)
    # Calculate the total time in hours
    return hours + minutes / 60

# Function to determine meal time based on the given time
def meal_time_indicator(time):
    # Convert the input time to a decimal representation
    time_in_hours = convert(time)

    # Check if the time falls within specified meal time ranges
    if 7.0 <= time_in_hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("Dinner time")

# Main function to get user input and call the meal_time_indicator function
def main():
    # Get user input for the current time
    user_time = input("What Time is It?: ")
    # Call the meal_time_indicator function with the user-provided time
    meal_time_indicator(user_time)

# Entry point to the program
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
"""
This code takes a time input in HH:MM format, converts it to a decimal representation, 
and then checks if it falls within specified ranges for breakfast, lunch, or dinner. 
The result is printed based on the time provided by the user.
"""