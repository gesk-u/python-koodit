# pre-made dictionary with the ICAO codes and airport names from the web
airports = {
    "KJFK": "John F. Kennedy International Airport (New York, USA)",
    "KLAX": "Los Angeles International Airport (Los Angeles, USA)",
    "EGLL": "London Heathrow Airport (London, UK)",
    "LFPG": "Paris Charles de Gaulle Airport (Paris, France)",
    "EDDF": "Frankfurt am Main Airport (Frankfurt, Germany)",
    "RJTT": "Tokyo Haneda Airport (Tokyo, Japan)",
    "ZBAA": "Beijing Capital International Airport (Beijing, China)",
    "OMDB": "Dubai International Airport (Dubai, UAE)",
    "YSSY": "Sydney Kingsford Smith Airport (Sydney, Australia)",
    "CYYZ": "Toronto Pearson International Airport (Toronto, Canada)"
}
# Go through options as long as we need.
while True:
    try:
        # The list of options
        action = int(input("Do you want to:\n(1) enter a new airport;\n(2) fetch the information of an existing airport;\n(3) quit?\nChoose 1, 2 or 3: "))
        # Add new ICAO and airport name
        if action == 1:
            code, name = input("ICAO code:"), input("Name of the airport: ")
            if code in airports:    # handle the case if the ICAO already exists
                print("Airport is already in the base")
            else:
                airports[code] = name
        # Fetch airports that already in dictionary
        elif action == 2:
            code = input("Enter ICAO code to fetch the airport: ").upper()
            if code in airports:
                print(f"Airport name: {airports[code]}")
            else:   #handle case if airport is not in the dictionary
                print("The airport is not in the base")
        # Quit option
        elif action == 3:
            print("You exited program")
            break
        # If user use any other number but 1, 2 nor 3
        else:
            print("Choose 1, 2 or 3")
            continue
    except ValueError:              # If user use string as input
        print("Use 1, 2 or 3")

