# Dice roller

import re
import random

while True:
    # Take input from user as dice roll string(e.g. 2d12)
    roll_input = input("Enter your dice roll: ").lower()
    print(roll_input)

    # Check that the string has a "d" in between 2 numbers
    regex = f'[0-9]+d[0-9]+'
    if re.search(regex, roll_input):
        print("Regex passed. Move on to rng.")
        break
    else:
        print("Invalid entry. Loop back to input")
        continue

# Take the string apart and split into list of integers
roll_input_list = roll_input.split('d')
print(roll_input_list)

num_of_dice = int(roll_input_list[0])
num_of_sides = int(roll_input_list[1])

print(f'Number of dice: {num_of_dice}')
print(f'Number of sides: {num_of_sides}')

# Generate random number with num_of_sides as the maximum value a number of times equal to num_of_dice
i = 0
dice_rolls = []
while i != num_of_dice:
    i += 1
    roll = random.randint(1, num_of_sides)
    dice_rolls.append(roll)
    print(f'Roll {i}: {roll}')

# Print dice_rolls and total of all values
print(f'Total: {sum(dice_rolls)} {dice_rolls}')