# Ask a year. Takes only integers (no year is a float)
while True:
    try:
        year = int(input("Year: "))
        break
    except ValueError:
        print("Try again. No letters or floats")

# Check if leap year
if year % 400 == 0:
    print("The input year is a leap year")
elif year % 100 == 0:
    print("The input year is not a leap year")
elif year % 4 == 0:
    print("The input year is a leap year")
else:
    print("The input year is not a leap year")

