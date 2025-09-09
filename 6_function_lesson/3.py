def print_greeting(greeting, times):
    for i in range(times):
        print(greeting + " round" + str(i + 1))

    return
a = input("Enter the greeting you with to be printed: ")
b = int(input("Enter the number of times you wish to make iterations: "))

print_greeting(a, b)
