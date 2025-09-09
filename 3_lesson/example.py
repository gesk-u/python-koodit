age = int(input("How old are you? "))

if age >= 65:
    print("You are retired!")
elif age >= 18:
    print("You are working age.")
elif age >= 7:
    print("You are still in school")
else:
    print("You are a small child")