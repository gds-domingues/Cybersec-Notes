import random

# Function to get the user-selected level (1, 2, or 3)
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            
            # Check if the entered level is 1, 2, or 3
            if level not in [1, 2, 3]:
                raise ValueError()
            
            return level
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

# Function to generate a random integer based on the selected level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

# Main game logic
def main():
    score = 0
    level = get_level()

    # Loop for 10 questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attempts = 0
        # Allow the user up to 3 attempts for each question
        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                
                # Check if the user's answer is correct
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print('Incorrect answer. Try again.')
                    attempts += 1
            except ValueError:
                # Handle the case where the user enters a non-integer
                print("Invalid input. Please enter an integer.")
                attempts += 1
        else:
            # If the user exceeds 3 attempts, reveal the correct answer
            print(f"Correct answer: {correct_answer}")

    # Print the final score
    print(f"Your score: {score}")
    return 0

# Entry point to the script
if __name__ == "__main__":
    main()

"""
This code is a simple arithmetic quiz game where the user needs to answer addition questions. 
The user selects a level (1, 2, or 3), and for each question, they have up to 3 attempts to answer correctly. 
The final score is then displayed.
"""