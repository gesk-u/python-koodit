integer = input("Integer: ")

while True:
    try:
        integer = int(integer)
        break
    except ValueError:
        print("Try integer")
        continue

if integer < 0:
    print(-1 * integer)

print(integer)