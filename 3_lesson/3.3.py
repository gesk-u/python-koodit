price = 5.90
name = input("Please, tell me your name: ").lower()

if name == "matti":
    print("Next please!")
else:
    num_por = int(input("How many portions do you want?\n"))
    print(f"The total cost is {price * num_por :.2f}")
    print("Next please!")
