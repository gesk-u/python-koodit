# Ask user the information
g = input("Gender (M/F): ")
h = int(input("hemoglobin value (g/l): "))

# Check gender (outer if). Check hemoglobin level(inner if statements)
if g == "F" or g == "f":
    if h < 134:
        print("The hemoglobin value is low")
    elif  h > 167:
        print("The hemoglobin value is too high")
    else:
        print("The hemoglobin value is normal")
elif g == "M" or g == "m":
    if h < 117:
        print("The hemoglobin value is low")
    elif h > 155:
        print("The hemoglobin value is too high")
    else:
        print("The hemoglobin value is normal")

else:
    print("Invalid gender input. Please enter 'M' or 'F'.")