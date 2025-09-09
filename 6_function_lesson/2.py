def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"

print("At the beginning in the main program: " + city)

change()

print("At the end of the main program: " + city)
