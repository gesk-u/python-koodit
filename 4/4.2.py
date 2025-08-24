# Infinite loop
while True:
    inch = float(input("Inches: ")) # Ask for inches
    if inch < 0:                    # Break loop if value is negative
        print("Program ended")
        break
    cm = 2.54 * inch                # Convert inches to cm
    print(f"Centimeters: {cm:.2f}") # Print result