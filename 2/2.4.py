count = 3
# list that will store integers
integers = []

# Loop to get exactly 3 integers
for i in range(count):
    while True:
        num = input(f"Integer {i + 1}: ")
        try:
            integers.append(int(num))
            break
        except ValueError:
            print("The number must be an integer. Please try again.")

# Count the sum of integers
sum_int = sum(integers)

# Count the product of integers
product = integers[0] * integers[1] * integers[2]

# Count the average of integers
avg_int = sum(integers)/ count

# Print results
print(f"Sum: {sum_int}\nProduct: {product}\nAverage of the numbers: {avg_int :.2f}")
