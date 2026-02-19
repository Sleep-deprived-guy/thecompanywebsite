"""Separate module where you can put the code to run from Streamlit.

Replace `run_task()` contents with your actual code.
"""
import time
import random


def run_task():
    """Run user code and return a result string.

    This function is called by `streamlit_app.py` when the button is
    pressed. Modify it to perform whatever work you need.
    """
    # first names
    list1 = [
        "Dan",
        "Mark",
        "John",
        "Jerry",
        "Marvelo",
        "Hanz",
        "Tom",
        "Parker",
        "Peter",
        "Walter",
        "Aiden",
        "Eli",
        "Ivan",
        "Bob",
    ]
    # middle names
    list2 = [
        "Arnold",
        "Garnet",
        "John",
        "Ken",
        "Lee",
        "Farn",
        "Lorenzo",
        "Van",
        "Glen",
    ]
    # last names
    list3 = [
        "Martin",
        "Johnson",
        "Lenzworth",
        "Oliver",
        "Wornswallow",
        "Lorenzo",
        "Pennysworth",
        "Lee",
        "Parker",
    ]
    
    # generations
    list5 = ["II", "III", "", "", "", "","","","","","","","","","","",""]


    # Jobs
    list6 = [
        "Farmer",
        "Merchant",
        "Shop Owner",
        "Soldier",
        "State Soldier",
        "Miner",
        "Peasant",
        "Nobleman",
        "Scam artist",
        "Mage",
        "Thief",
    ]
    job = random.choice(list6)
    # titles
    if job == "Soldier" or job == "State Soldier":
        list4 = ["Sir", "General", "Captain", "", "", "", "", ""]
    else:
        list4 = ["Dr.", "Sir", "Lord", "", "", "", "", "", ""]
    
    part1 = random.choice(list1)
    part2 = random.choice(list2)
    part3 = random.choice(list3)
    part4 = random.choice(list4)
    part5 = random.choice(list5)

    name = f"{part4} {part1} {part2} {part3} {part5}"
    # Age
    part6 = list(range(18, 51))
    age = str(random.choice(part6))
    # Looks
    part7 = list(range(5, 10))
    looks = str(random.choice(part7))
    # family
    part8 = [1, 2]
    coinflip = random.choice(part8)
    if coinflip == 2:
        part9 = list(range(1, 5))
        part10 = random.choice(part9)
        part12 = ["Son", "Wife", "Daughter", "Dog", "Cat"]
        family = str(random.choices(part12, k=part10))
        # Putting it all together
        result = (
            f"{name} at his current age {age} has been working as a {job} for most his life. "
            f"People often say he's a {looks} out of 10 in looks. His family consists of: {family}"
        )
    else:
        result = (
            f"{name} at his current age {age} has been working as a {job} for most his life. "
            f"People often say he's a {looks} out of 10 in looks. He doesn't have a family"
        )

    return result
