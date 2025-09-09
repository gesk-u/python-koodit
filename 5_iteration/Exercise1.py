# List of predefined colors:
colors = ["red", "green", "blue"]

# Ask favorite color from user
color = input("Your favorite color: ").lower()

# Check if color in our list
if color in colors:
    print("Your favorite color is one of the primary colors!")
else:
    print("Your favorite color can be created by combining different amounts of red, green, and blue (RGB)")
