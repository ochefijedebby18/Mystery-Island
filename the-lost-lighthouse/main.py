from game import (
    new_game,
    move_player,
    collect_item,
    show_inventory,
    available_actions,
    light_lighthouse,
    is_win,
    is_loss
)


def display_intro():
    print("\n================================")
    print("     MYSTERY ISLAND")
    print("     THE LOST LIGHTHOUSE")
    print("================================")

    print("""
A terrible storm has stranded you on Mystery Island.

The lighthouse is dark.
The bridge is locked.
A rescue boat is expected soon.

Find useful objects, explore the island,
and restore the lighthouse beacon before
your energy runs out.

Good luck!
""")


def display_status(player):
    print("\n--------------------------------")
    print(f"Explorer: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print(f"Inventory: {show_inventory(player)}")
    print("--------------------------------")


def display_scene(player):
    location = player["location"]

    scenes = {
        "Beach": "You wake up on a quiet beach. Something lies in the sand.",
        "Jungle": "You enter a thick jungle. Strange sounds surround you.",
        "Cave": "You discover a dark cave with an old stone passage.",
        "Old Bridge": "You reach an unstable bridge leading to the lighthouse.",
        "Lighthouse": "You stand inside the abandoned lighthouse."
    }

    print("\n" + scenes[location])


def game_menu(player):
    while not player["game_over"]:

        display_status(player)
        display_scene(player)

        print("\nWhat would you like to do?")
        print("1. Move")
        print("2. Collect item")
        print("3. Check inventory")
        print("4. Light lighthouse")
        print("5. Quit")

        choice = input("\nChoose an option: ").strip().lower()

        if choice == "1":
            destinations = available_actions(player)

            print("\nAvailable destinations:")

            for index, destination in enumerate(destinations, 1):
                print(f"{index}. {destination}")

            destination_choice = input(
                "Where would you like to go? "
            ).strip()

            if destination_choice.isdigit():
                number = int(destination_choice)

                if 1 <= number <= len(destinations):
                    destination = destinations[number - 1]

                    if move_player(player, destination):
                        print(f"You moved to {destination}.")

                        if player["game_over"]:
                            print("You used your final energy point!")
                    else:
                        print("You cannot move there.")
                else:
                    print("Invalid destination number.")
            else:
                print("Please enter a number.")

        elif choice == "2":
            if collect_item(player):
                print("You successfully collected an item!")
            else:
                print("There is nothing useful to collect here.")

        elif choice == "3":
            inventory = show_inventory(player)

            if inventory:
                print("\nYour items:", ", ".join(inventory))
            else:
                print("\nYour inventory is empty.")

        elif choice == "4":
            if light_lighthouse(player):
                print("\nTHE LIGHTHOUSE IS ON!")
                print("A rescue boat spots your beacon.")
                print("Congratulations! YOU ESCAPED MYSTERY ISLAND!")
            else:
                print(
                    "\nYou cannot light the lighthouse yet. "
                    "You need to be inside it and have the lantern."
                )

        elif choice in ("5", "q", "quit", "exit"):
            player["game_over"] = True
            print("\nYou decided to leave the island unexplored.")

        else:
            print("Invalid choice. Please select 1, 2, 3, 4 or 5.")


def play_game():
    display_intro()

    name = input("What is your name, explorer? ").strip()

    if not name:
        name = "Explorer"

    player = new_game(name)

    game_menu(player)

    if is_loss(player):
        print("\nGAME OVER!")
        print("Your energy ran out before you could activate the beacon.")

    elif not is_win(player):
        print("\nThanks for playing!")


def main():
    while True:
        play_game()

        replay = input("\nWould you like to play again? (yes/no): ")
        replay = replay.strip().lower()

        if replay not in ("yes", "y"):
            print("\nThanks for exploring Mystery Island!")
            break


if __name__ == "__main__":
    main()
