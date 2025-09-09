seasons = ("spring", "summer", "autumn", "winter")
# Unpack tuple using variables
(spring, summer, autumn, winter) = seasons

while True:
    try:
        month_num = int(input("Month number: "))
        if 1 <= month_num <= 12:    # Check if the number is within month-numbers
            break
        else:
            print("Use the number from 1 to 12")
            continue
    except ValueError:
        print("Use integer numbers to define a month")

# Print out the season according to 'month_num'
if month_num == 12 or 1 <= month_num <= 2:
    print(f"Season: {winter}")
elif 3 <= month_num <= 5:
    print(f"Season: {spring}")
elif 6 <= month_num <= 8:
    print(f"Season: {summer}")
else:
    print(f"Season: {autumn}")
