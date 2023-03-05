# Dice roller

import re
import random

# FUNCTIONS
def standard_roll(user_input):
    # Take the string apart and split into list of integers
    roll_input_list = user_input.split('d')

    num_of_dice = int(roll_input_list[0])
    num_of_sides = int(roll_input_list[1])

    # Generate random number with num_of_sides as the maximum value a number of times equal to num_of_dice
    i = 0
    dice_rolls = []
    while i != num_of_dice:
        i += 1
        roll = random.randint(1, num_of_sides)
        dice_rolls.append(roll)

    # Print dice_rolls and total of all values
    print(f'Total: {sum(dice_rolls)} {dice_rolls}')

def modified_roll(user_input):
    # Split the input into parts
    regex = f'(\d+)|(\+)|(\-)'
    roll_input = re.findall(regex, user_input)

    # Tidy up roll_input
    roll_input = [item for sublist in roll_input for item in sublist if item]

    # TODO: Detect what type of operator is at the end of the roll
    num_of_dice = int(roll_input[0])
    num_of_sides = int(roll_input[1])
    operator = roll_input[2]
    modifier = int(roll_input[3])
    total = 0

    # Generate random number with num_of_sides as the maximum value a number of times equal to num_of_dice
    i = 0
    dice_rolls = []
    while i != num_of_dice:
        i += 1
        roll = random.randint(1, num_of_sides)
        dice_rolls.append(roll)

    total = sum(dice_rolls)

    # Detect what type of operator is used and apply it to total roll
    if operator == '+':
        total += modifier
    else:
        total -= modifier

    # Return total including modifier
    print(f'Total: {total} {dice_rolls} {operator} {modifier}')


# USER INPUT VALIDATION
while True:
    # Take input from user as dice roll string(e.g. 2d12)
    roll_input = input("Enter your dice roll or 'help': ").lower()

    # Check that the string has a "d" in between 2 numbers
    standard_roll_regex = f'^[0-9]+d[0-9]+$' # Checks for a number, followed by a 'd',  followed by another number
    modified_roll_regex = f'^[0-9]+d[0-9]+[+\-*\/][0-9]+$' # Check for the same as above but followed by a mathematical operator

    if roll_input == 'help':
        print('Work in progress. Help menu goes here...')
    elif re.search(standard_roll_regex, roll_input):
        standard_roll(roll_input)
    elif re.search(modified_roll_regex, roll_input):
        modified_roll(roll_input)
    else:
        print("Invalid entry. Try 'help'")
        continue

