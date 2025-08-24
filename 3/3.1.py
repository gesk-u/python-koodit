r_size = 42     # Required size

# Get size of fish and prevent value error
while True:
    try:
        size = float(input("The length of a zander: "))
        break
    except ValueError:
        print("Use correct value")

# Check if a size is sufficient
if size < r_size:
    print(f"Your fish was {r_size - size} cm below the size limit. A zander must be 42 centimeters or longer to meet the size limit!")
else:
    print(f"Your fish meets size requirement!")

