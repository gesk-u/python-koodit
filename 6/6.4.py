def main():
    # Get number of elements for the future list
    num_numbers = int(input("How many elements are in your list?\n"))
    numbers = []
    for i in range(num_numbers):
        # Add integers to the list
        while True:
            try:
                number = int(input(f"Number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Use integers only!")

    print(f"The sum of the numbers is: {listsum(numbers)}")

# Returns the sum of the list
def listsum(numbers):
    return sum(numbers)

main()