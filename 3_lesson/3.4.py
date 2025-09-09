wage = float(input("Hourly wage: "))
h_worked = float(input("Hours worked: "))
day = input("The day of the week: ").capitalize()
d_wage = wage * h_worked

print(f"Hourly wage: {wage}")
print(f"Hours worked {h_worked}")
print(f"Day of the week: {day}")

if day == "Sunday":
    wage = wage * 2
    d_wage = wage * h_worked
    print(f"Daily wages: {d_wage}")
else:
    print(f"Daily wages: {d_wage}")
