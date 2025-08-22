a = float(input("Math: "))
b = float(input("Physics: "))
c = float(input("Programming: "))

maximum = 300
total = a + b + c
final_grade = total/3
percentage = ((total * 100)/maximum)
print(f"Final grade: {percentage :.2f}")
