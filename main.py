def main():
    print("===================================")
    print("     MYSTERY ISLAND ADVENTURE      ")
    print("===================================")
    print("\n===Welcome to mystery island===")
    print("You wake up on a mysterious island after a terrible storm.")
    print("Your mission is to restore the lighthouse beacon so that a rescue boat can find you.")
    print("INSTRUCTIONS:")
    print("1. Explore the island.")
    print("2. Collect useful objects.")
    print("3. Solves puzzles.")
    print("4. Make careful decisions.")
    print("5. Manage your energy. You have only five points!")
    print("\n Good Luck! \n")

    player_name = input("What is your name? ")
    print(f"Welcome, {player_name}!")
    print("Your adventure begins now!")

    print("\n======PLAYER STATUS======")
    player = {
        "player_name": player_name,
        "energy": 5,
        "location": "Beach",
        "inventory": [],
        "escaped": False
    }
    
    print(f"Name: {player['player_name']}")
    print(f"Energy: {player['energy']}")
    print(f"Location: {player['location']}")
    print(f"Inventory: {player['inventory']}")
    print(f"Escaped: {player['escaped']}")
    print("==========================\n")

    while True:
        print("What would you like to do")
        print("1. Explore location.")
        print("2. Move to another location.")
        print("3. Pick up an object.")
        print("4. View inventory.")
        print("5. View player status.")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(player["location"])
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print()
        elif choice == "5":
            print()
        elif choice == "6":
            print("Thanks for playing Mystery Island!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
