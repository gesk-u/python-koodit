first = int(input("Number: "))
size = int(input("Size: "))
second = int(input("Number 2: "))
count1 = 0
while count1 <= size:
    if count1 == 0:
        print(f"Number1\t|\tNumber2")
    print(f"{first * (count1 + 1)}\t\t|\t{second * (count1 + 1)}")
    count1 += 1
