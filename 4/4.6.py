import random

def main():
    # Get user's input
    while True:
        try:
            user_points = int(input("Points: "))
            break
        except ValueError:
            print("Points must be whole number")
    # Count number of inside-circle points
    n_inside = 0
    for i in range(user_points):
        x = rand_x()
        y = rand_y()
        if x**2 + y**2 < 1:
            n_inside += 1
    # Calculate approximate pi-number
    pi = (4 * n_inside)/user_points
    # Print pi
    print(f"Approximate pi: {pi}")

# Generate random x or -x with 50% probability for each
def rand_x():
    x1 = random.random()
    x2 = -1*random.random()

    rp = random.random()

    if rp < 0.5:
        rx = x1
        return rx
    else:
        rx = x2
        return rx

# Generate random y or -y with 50% probability for each
def rand_y():
    y1 = random.random()
    y2 = -1*random.random()

    rp = random.random()

    if rp < 0.5:
        ry = y1
        return ry
    else:
        ry = y2
        return ry

main()