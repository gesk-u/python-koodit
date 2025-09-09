def main():
    gallons = 0
    while gallons >= 0: # if user use 0 for 'gallons' it exits program
        try:
            gallons = float(input("The quantity of gasoline in American gallons: "))
        except ValueError:
            print("Use numbers only!")
            continue
        if gallons > 0:
            l = convert(gallons)    # use function to get converted variable
            print(f"the number converted to litres: {l:.2f}")
    print("Exit")

# Convert gallons to liters
def convert(gallons):
    return gallons * 3.8
main()