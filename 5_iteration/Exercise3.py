numbers = []
value = input("New item: ")

while value != "0":
    if value.isnumeric():
        numbers.append(value)
        print("The list now:", numbers)
        print("The list in order:", sorted(numbers))
        value = input("New item or enter '0' to exit: ")
        continue
    else:
        print("Use numeric value or enter '0' to exit")
    value = input("New item: ")
print("Buy!")

#print(sorted(numbers) #no need to create a new variable