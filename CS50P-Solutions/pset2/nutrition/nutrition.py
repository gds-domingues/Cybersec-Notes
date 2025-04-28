# Get user input for a fruit item (case-insensitive and stripped of leading/trailing whitespaces)
fruit = input('Item: ').lower().strip()

# Dictionary of fruit names and their corresponding calorie values
calories = dict([('apple', 130),
                 ('avocado', 50),
                 ('banana', 110),
                 ('grapefruit', 60),
                 ('grapes', 90),
                 ('honeydew melon', 50),
                 ('kiwifruit', 90),
                 ('lemon', 15),
                 ('lime', 20),
                 ('nectarine', 60),
                 ('orange', 80),
                 ('peach', 60),
                 ('pear', 100),
                 ('plums', 70),
                 ('strawberries', 50),
                 ('sweet cherries', 100),
                 ('tangerine', 50),
                 ('watermelon', 80)])

# Iterate over the keys in the calories dictionary
for k in calories:
    # Check if the user input matches a fruit name in the dictionary
    if fruit == k:
        # If a match is found, print the corresponding calorie value
        print('Calories: ', calories[fruit])
    elif fruit != k:
        # If no match is found, continue to the next iteration
        continue
    else:
        # This else branch is redundant and will never be executed
        # It can be removed without affecting the functionality
        break

"""
This code checks if the user input (fruit) matches a key in the calories dictionary and prints the corresponding calorie value if a match is found. 
The use of continue in the loop ensures that it moves to the next iteration when no match is found. 
The else branch at the end of the loop is redundant and can be removed without affecting the functionality.
"""