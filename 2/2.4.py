count = 3
integers = []
for i in range(count):
    while True:
        num = input(f"Integer {i + 1}: ")
        try:
            integers.append(int(num))
            break
        except ValueError:
            print("The number must be an integer. Please try again.")

sum_int = sum(integers)
product = integers[0] * integers[1] * integers[2]
avg_int = sum(integers)/ count

print(f"Sum: {sum_int}\nProduct: {product}\nAverage of the numbers: {avg_int :.2f}")
