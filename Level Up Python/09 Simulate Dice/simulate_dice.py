# Importing the randint function from the random module
from random import randint

# Importing the Counter class from the collections module
from collections import Counter


# Defining a function named roll_dice which takes variable number of dice and an optional num_trials argument
def roll_dice(*dice, num_trials=1_000_000):
    # Initializing an empty Counter object to store outcome counts
    counts = Counter()

    # Simulating rolling the dice for num_trials times
    for _ in range(num_trials):
        # Generating a random outcome for each die and summing them up
        counts[sum((randint(1, sides) for sides in dice))] += 1

    # Printing header for the output
    print('\nOUTCOME\tPROBABILITY')

    # Iterating over possible outcomes
    for outcome in range(len(dice), sum(dice) + 1):
        # Calculating probability for each outcome and printing it
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')


# List representing the number of sides on each die
lst = [4, 6, 6]

# Calling the roll_dice function with the elements of lst as arguments
roll_dice(*lst)
