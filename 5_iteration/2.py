names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

names.append("Matti")

print(names)

names.remove("Pekka")
print(names)

names.insert(2, "Teppo")
print(names)

names2 = ["Allu", "Ninni"]

names.extend(names2)  #join two lists
print(names)
