names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

olga = names.index("Olga") #find index in the list
print(olga)
names.append("Matti")

# If (value) in data (structure)
if "Matti" in names:
    print("Matti was found!")
else:
    print("Matti was not found")
