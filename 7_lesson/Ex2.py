numbers = []
s = set()
def unique_numbers():
    while True:
            number = input("Add number: ")
            if number == "":
                break
            elif number.isnumeric(): # check if number is int DO NOT WORK for float
                n = float(number)
                numbers.append(n)
                s.add(n)
            else:
                print("Use numbers only!")
    return s, numbers

s, numbers = unique_numbers()

print(f"Set: {s}")
print(f"Number of unique numbers {len(s)}")
print(f"List: {numbers}")
