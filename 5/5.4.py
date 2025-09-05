# Empty list
cities = []

# Get 5 cities input.
for i in range(5):
    city = input(f"City {i + 1}: ")
    try:
        city = str(city)
        cities.append(city)
    except ValueError:                  # Handle value error
        print("No numbers. Try again")

# Print out 5 cities one per line
for i in range(len(cities)):
    print(cities[i])