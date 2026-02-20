
import time
import random


def run_task5():
    list1 = ["Deal going on in a alleyway", "Guy walks up to you and gives you something", "Someone offers a deal", "You find a book on the ground", "You see someone getting robbed", "You see a fight break out" , "You see a rich guy", "You see a beggar", "You get robbed", "You see a suspicious person", "You see a crazy guy", "You see a building on fire", "You see a Rich guy drop his wallet", "You see a protest", "You see a rare species guy", "You see a murder", "You see a celebrity", "You see a homeless person", "You see a drug deal", "You see a fight break out", "You see a robbery", "You see a kidnapping"]
    result5 = "Encounter Generated: " + str(random.choice(list1))

    return result5
