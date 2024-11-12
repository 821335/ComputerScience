import random


real_number = random.randint(0,101)
entered_number = ""

attempts = 0

while real_number != entered_number:
    entered_number = input("Please enter the number\n>")
    attempts = attempts +1
    if entered_number == real_number:
        print("CORRECT")
    elif entered_number > real_number:
        print("your guess is to high try again")
    elif entered_number < real_number:
        print("Your guess is to low try again")
    else:
        print("Wrong try guessing again")
        print(str(attempts) + " attempts ")
    
print("nice job")