def main():
    num_numbers = int(input("How many elements are in your list?\n"))
    numbers = []
    for i in range(num_numbers):
        while True:
            try:
                number = int(input(f"Number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Use integers only!")

    print(f"Original list: {numbers}")
    print(f"All-uneven-numbers-removed list: {we_not_like_uneven(numbers)}")

# Removes uneven numbers
def we_not_like_uneven(numbers):
    for n in numbers[:]:
        if n % 2 != 0:
            numbers.remove(n)
    return numbers



main()