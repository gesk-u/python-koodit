# Correct username and password
username = "python"
password = "rules"

count = 1

# Loop runs up to 5 times. Stops early if login succeeds
while count <= 5:
    print(f"Try {count}")   # the current attempt
    username_input = input("Username: ")
    password_input = input("Password: ")
    # Check if both username and password are correct
    if username_input == username and password_input == password:
        print("Welcome")
        break
    else:                       # Count number of remaining attempts
        tries = 5 - count
        if tries > 0:
                print(f"Please try again. {tries} out of 5 tries are left")
        else:                   # No tries left - 'Access denied'
            print("Access denied")
    count += 1
