numbers = {"Viivi":"293983",
           "Ahmed":"390-940",
           "Pekka":"123091-2"}

print(numbers)

#Adding new value
numbers["Matti"] ="045-123456"

print(numbers)

name = input("give the name you want to access: ")

if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}.")
else:
    print("The name was not in the phonebook")