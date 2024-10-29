def start_adventure(): #start function
    print("Welcome to the start of your exploration chose a route to travel. Do you:")
    print("1.  north") # 3 player choices
    print("2.  east")
    print("4.  west")
    choice = input(" chose an option to continue on")
    if choice == "1":
        travel_north()
    elif choice == "2":
        travel_east()
    elif choice == "4":
        travel_west()
    else:
        print("Wrong choice. Try again.")
        start_adventure()
def travel_north(): # what happens when you chose one of the 3 options
    print("You start walking north but realize it's to cold")
def travel_east():
    print("You start riding your horse east until you find something disturbing on the way")
def travel_west():
    print("You start traveling west but end up in the middle of a dessert")