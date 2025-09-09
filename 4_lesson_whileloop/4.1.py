"""rounds = int(input("How many greetings: "))

finished_round = 0

while finished_round < rounds:
    print("Hello")
    finished_round += 1"""

"""command = input("Enter command: ")
while command != "stop":
    print("We are free, what to do, let's " + command)
    command = input("Enter command: ")

print("Execution stopped explicitly.")"""

import random

dice1 = dice2 = rolls = 0

while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls += 1

print(f"Rolled {rolls:d} times.")