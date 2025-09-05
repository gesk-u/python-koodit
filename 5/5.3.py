# Get input
integer = input("Integer: ")
# Handling ValueError
while True:
    try:
        integer = int(integer)
        break
    except ValueError:
        print("Use integer")
        continue
# Find if 'integer' is divisible by any number
# besides 1 and itself
for i in range(2, integer):
    if integer % i == 0:
        print("Not a prime number")
        break
else:
    print("Integer is a prime number")

