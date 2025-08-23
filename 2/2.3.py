# Ask for length
length = float(input("Length: "))

# Ask for width
width = float(input ("Width: "))

# Calculate perimetr
P = 2 * (length + width)

# Calculate area of rectangle
A = length * width

#Print perimetr and area with two decimal places
print(f"Perimeter: {P:.2f}\nArea: {A:.2f}")
