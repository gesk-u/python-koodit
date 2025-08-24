import random

# Choose random number from 1 to 10
num = random.randint(1, 10)

# Infinite loop that breaks when user's gues is correct
while True:
    # Avoid value error
    try:
        user_num = int(input("Guess number from 1 to 10: "))
    except ValueError:
        print("Enter an integer from 1 to 10")
        continue    # goes back if wrong value(not int)

    if user_num < num:
        print("Too low")
    elif user_num > num:
        print("Too high")
    else:
        print("Correct")
        break