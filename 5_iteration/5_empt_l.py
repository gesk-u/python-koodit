# Empty list
names = []

name = input("Add a name to list: ")

while name != "":
    names.append(name)
    name = input("Add another name to the list: ")
print(names)