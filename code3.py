
import time
import random


def run_task3():
    result3 = "Rolled a D100: " + str(random.randint(1, 100))

    return result3

def roll_custom_dice(sides):
    if sides <= 0:
        return "Number of sides must be positive."
    result = f"Rolled a D{sides}: {random.randint(1, sides)}"
    return result