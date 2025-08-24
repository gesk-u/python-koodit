# Receive string input
while True:
    try:
        cabin_class = str(input("Cabin class of a cruise ship: "))
        cabin_class = cabin_class.strip().upper()   #remove extra spaces and convert to uppercase
        break
    except ValueError:
        print("Try again.Your cabin class does not include numbers")

# Check cabin class prints its description
if cabin_class == "LUX":
    print("LUX:upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")