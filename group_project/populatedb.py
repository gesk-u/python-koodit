from functions import *
import story


# Establish a connection to the MariaDB server
def main():
    # ask to show the story
    storyDialog = input("Do you want to read the background story? (Y/N): ")
    if storyDialog == 'Y':
        # print wrapped string line by line
        for line in story.getStory():
            print(line)
    # GAME SETTINGS
    print("When you are ready to start, ")
    player = input("type player name: ")

    # boolean for game over and print
    game_over = False
    win = False

    # start money = 1000
    money = 1000
    # start range in km = 2000
    player_range = 2000

    # score = 0
    score = 0

    # boolean for diamond found
    diamond_found = False

    # all airports
    all_airports = get_airports()
    # start airport ident
    start_airport = all_airports[0]["ident"]
    # current airport
    current_airport = start_airport

    # game id
    game_id = new_game(money, start_airport, player, player_range, all_airports)

    # GAME LOOP
    while not game_over:
        # get current airport info
        airport = get_airport_info(current_airport)
        # show game status
        print(f"You are at {airport['name']}")
        print(f"You have {money:.0f}$ and {player_range:.0f}km of range")
        # pause
        input("\033[32mPress Enter to continue...\033[0m")
        # if airport has goal ask if player wants to open it
        # check goal type and add/subtract money accordingly
        goal = check_goal(game_id, current_airport)

        if goal:
            question = input(
                f'''Do you want to open lootbox for {"100$ or " if money > 100 else ""}{"50km range" if player_range > 50 else ""}? M = money, R = range, enter to skip: ''')

            while question not in ("", "M", "R"):
                print("Invalid choice. Use 'R' or 'M', or press Enter to skip.")
                question = input(
                    f'''Do you want to open lootbox for {"100$ or " if money > 100 else ""}{"50km range" if player_range > 50 else ""}? M = money, R = range, enter to skip: ''')

            if not question == "":
                if question == "M":
                    money -= 100
                    win = win_g(goal)
                    money = open_chest(goal, money)
                elif question == 'R':
                    player_range -= 50
                    win = win_g(goal)
                    money = open_chest(goal, money)
        # pause
        input("\033[32mPress Enter to continue...\033[0m")

        # ask to buy fuel/range
        if money > 0:
            question2 = input("Do you want to buy a fuel? 1$ = 2km of range. Enter amount or press enter.")
            if not question2 == '':
                question2 = float(question2)
                if question2 > money:
                    print(f"You don't have enough money.")
                else:
                    player_range += question2 * 2
                    money -= question2
                    print(f"You have now {money:.0f}$ and {player_range:.0f}km of range")
            # pause
            input("\033[32mPress Enter to continue...\033[0m")

        # if no range, game over
        # show airports in range. if none, game over
        airports = airports_in_range(current_airport, all_airports, player_range)
        print(f"\33[34mThere are {len(airports)} airports in range: \033[0m")
        if len(airports) == 0:
            print("You are our of range.")
            game_over = True
        else:
            print(f"Airports: ")
            for airport in airports:
                ap_distance = calculate_distance(current_airport, airport['ident'])
                print(f"{airport['name']}, icao: {airport['ident']}, distance: {ap_distance:.0f}km")
            # ask for destination
            dest = input("Enter destination icao: ")
            selected_distance = calculate_distance(current_airport, dest)
            player_range -= selected_distance
            update_location(dest, player_range, money, game_id)
            current_airport = dest
            if player_range < 0:
                game_over = True


    # if game is over loop stops
    # show game result
    print(f'''{'You won!' if win else 'You lost!'}''')
    print(f'''You have {money:.0f}$''')
    print(f'''Your range is {player_range:.0f}km''')

if __name__ == "__main__":
    main()