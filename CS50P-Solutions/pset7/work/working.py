import re

# Function to find work times in the input string
find_work_times = lambda x: re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b", x, re.IGNORECASE)

# Regular expressions to check if a string has minutes, hours, or both
has_mins_regex = lambda x: re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", x)
has_hours_regex = lambda x: re.match(r"^(1[0-2]|0?[1-9])", x)

def main():
    # Prompt the user for input and print the converted working hours
    hours: str = input("Hours: ").strip()
    print(convert(hours))

# Function to handle the case where minutes are present in the time string (AM)
def handle_has_mins_AM(minutes: re.Match[str], work_hours: list[str]) -> list[str]:
    # Extract groups from the regex match
    group_1: int = int(minutes.group(1))
    group_2: int = int(minutes.group(2))

    if group_1 < 1 or group_1 > 12:
        raise ValueError

    elif group_1 == 12:
        return [*work_hours, f"00:{group_2}"]

    elif group_1 <= 9:
        return [*work_hours, f"0{group_1}:{group_2}0"]

    return [*work_hours, f"{group_1}:{group_2}0"]

# Function to handle the case where hours are present in the time string (AM)
def handle_has_hours_AM(hours: re.Match[str], work_hours: list[str]) -> list[str]:
    # Extract groups from the regex match
    group_1: int = int(hours.group(1))

    if group_1 == 12:
        return [*work_hours, f"00:00"]

    elif group_1 <= 9:
        return [*work_hours, f"0{group_1}:00"]

    return [*work_hours, f"{group_1}:00"]

# Function to handle the case where minutes are present in the time string (PM)
def handle_has_mins_PM(minutes: re.Match[str], work_hours: list[str]) -> list[str]:
    # Extract groups from the regex match
    group_1: int = int(minutes.group(1))
    group_2: int = int(minutes.group(2))

    if group_1 > 12 or group_1 < 1:
        raise ValueError

    elif group_1 == 12:
        return [*work_hours, f"12:{group_2}0"]
    return [*work_hours, f"{group_1 + 12}:{group_2}0"]

# Function to handle the case where hours are present in the time string (PM)
def handle_has_hours_PM(hours: re.Match[str], work_hours: list[str]) -> list[str]:
    # Extract groups from the regex match
    group_1: int = int(hours.group(1))

    if int(group_1) == 12:
        return [*work_hours, f"12:00"]
    return [*work_hours, f"{group_1 + 12}:00"]

# Function to handle the case when the time is in the AM period
def handle_AM(time: str, work_hours: list[str]) -> list[str]:
    if minutes := has_mins_regex(time):
        return handle_has_mins_AM(minutes, work_hours)

    elif hours := has_hours_regex(time):
        if int(time) > 12 or int(time) < 1:
            raise ValueError
        return handle_has_hours_AM(hours)
    raise ValueError

# Function to handle the case when the time is in the PM period
def handle_PM(time: str, work_hours: list[str]) -> list[str]:
    if minutes := has_mins_regex(time):
        return handle_has_mins_PM(minutes, work_hours)

    elif hours := has_hours_regex(time):
        if int(time) > 12 or int(time) < 1:
            raise ValueError
        return handle_has_hours_PM(hours)
    raise ValueError

# Main function to convert the input working hours string
def convert(s: str) -> str:
    work_hours: list[str] = []

    # Find the work times in the input string
    work_times: list = find_work_times(s)

    # Check if there are exactly 2 work times
    if len(work_times) != 2:
        raise ValueError

    # Process each work time
    for time in work_times:
        time: str = str(time).lower()

        # Check if the time is in the AM period
        if " am" in time:
            time: str = time.strip(" am")
            work_hours = handle_AM(time, work_hours)

        # Check if the time is in the PM period
        elif " pm" in time:
            time: str = time.strip(" pm")
            work_hours = handle_PM(time, work_hours)

    # Check if the converted working hours list has exactly 2 elements
    if len(work_hours) == 2:
        return f"{work_hours[0]} to {work_hours[1]}"
    raise ValueError

# Entry point of the script
if __name__ == "__main__":
    main()

"""
The Python script is designed to convert a user-input string containing working hours in a 
human-readable format (e.g., "9 am to 5 pm") into a standardized format (e.g., "09:00 to 17:00"). 
The script utilizes regular expressions to identify and extract the working hours from the input string. It then handles cases where minutes, 
hours, or both are present, considering the AM and PM periods. 
The conversion is performed by manipulating the time components and building a list of formatted working hours. 
The script provides a clear separation of concerns by using functions to handle different scenarios and maintain readability. Additionally, 
the main function interacts with the user by taking input and printing the converted working hours. 
The code aims to provide a robust solution for converting varied input formats into a consistent time representation.
"""