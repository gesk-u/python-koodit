# Define empty set
s = set()

while True:
        # Get name or exit program
        name = input("Add Name or an empty space if you want to exit program: ")
        if name == "":
            break
        elif name in s:
            print("Existing name")
        else:
            print("New name")
            s.add(name)
print(s)
