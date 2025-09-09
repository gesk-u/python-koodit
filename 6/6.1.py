import random

def main():
    value = 0
    while value != 6:
        value = dice()
        print(value)

# Function that returns random value from 1 to 6
def dice():
    return random.randint(1, 6)

main()