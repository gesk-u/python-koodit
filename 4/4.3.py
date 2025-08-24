# List to store numbers
numbers = []

# Receive numbers and add them to 'numbers'
while True:
    user_num = input("Enter a number: ")
    if user_num == "":                      # Break loop if input is an empty string
        break
    try:                                    # Append number to 'numbers'
        num = float(user_num)
        numbers.append(num)
    except ValueError:                      # Ask to input value again in case of Value error
        print("Please try again. Use integer or float")

# Bubble sorting algorithm
n = len(numbers)

for i in range(n - 1):                  # Outer loop
    swap = False
    for a in range(n - 1 - i):          # Inner loop: compares adjacent
        if numbers[a] > numbers[a + 1]:
            tm = numbers[a]
            numbers[a] = numbers[a + 1]
            numbers[a + 1] = tm
            swap = True                # Boolean if swap occurred
    if not swap:                       # Optimization if no swaps just breaks iterations
        break


# Print out the result
print(f"The smallest number: {numbers[0]}")
print(f"The largest number: {numbers[n - 1]}")

