age = int(input("How old are you "))

if 15 <= age < 18:
    weight = float(input("How much do you weigh? "))

if age >= 18 or age >= 15 and weight >= 55:
    print("You can use the medicine")
else:
    print("You cannot use the medicine.")