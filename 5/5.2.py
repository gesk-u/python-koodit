# Create new list
numbers = []

# Loop to receive numbers
while True:
    number = input("Number: ")
    if number == "":            # Stops looping when input ""
        break
    try:                        # Check if input is float or int
        number = float(number)
        numbers.append(number)
    except ValueError:
        print("Use integers or floats!")
        continue
numbers.sort(reverse=True)  # Sort numbers from greatest to smallest

# Print out 5 the greatest numbers of the list
for i in range(5):
    print(numbers[i], end=" ")

print()