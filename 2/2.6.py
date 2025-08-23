import random
# Lists for 3- and 4-digits codes
code_3 = []
code_4 = []

#Iterates 3 times and adds 3 random digits to 'code_3'
for i in range(3):
    a = str(random.randint(0, 9))   # Generate a random digit between 0 and 9
    code_3.append(a)

#Iterates 4 times and adds 4 random digits to 'code_4'
for i in range(4):
    a = str(random.randint(1, 6))   # Generate a random digit between 1 and 6
    code_4.append(a)

# Join the list of characters into a single string and print the 3-digit code
code = "".join(code_3)
print(code)

# Join the list of characters into a single string and print the 4-digit code
code = "".join(code_4)
print(code)

