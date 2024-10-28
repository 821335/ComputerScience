def start_adventure():
    print("You stand at the entrance of a dark forest. Do you:")
    print("1. Enter the forest")
    print("2. Turn back and go home")
    
    choice = input("> ")
    
    if choice == "1":
        enter_forest()
    elif choice == "2":
        go_home()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def enter_forest():
    print("You bravely step into the forest and hear strange noises...")
    # More encounters and choices follow

def go_home():
    print("You decide it's safer at home, but your adventure ends here.")
    # End of the game or new encounters

