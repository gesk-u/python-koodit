import random

def main():
    value = 0
    sides = 0
    while True:
        try:
            sides = int(input("Number of sides: "))
            break
        except ValueError:
            print("Use integer!")
            continue
    # iterates until random 'value' is not equal to the number of sides
    while value != sides:
        value = dice(sides)
        print(value)

# Function that returns random value from 1 to 'sides'
def dice(sides):
    return random.randint(1, sides)

main()