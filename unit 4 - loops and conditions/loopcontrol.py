# loop control statements
# allow you to change how loops operate
# Do things like quit the loop early, skip the current loop, and even do nothing
# break, continue, and pass

# break
# exits a loop prematurely, before it was supposed to end

#example

bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruit:

    if fruit == "bug":
        print("uh oh, you found a bug in the bag...")
        break       # the break statement exits the loop immediately and continues
    else:
        print("You ate a " + fruit)


# continue
# skips the current loop
# it does not exit the entire loop, just moves on to the next iteration


# example   
orders = [15, 30, 35, 23, 100, 3, 10, 22]

# only apply discount for oders above $20

for order in orders:
    if order < 20:
        continue  # skips the rest if the loop iteration and goes to the next iteration
    print("$" str(order) " order discount 5% to $" + str(order * .95))




# pass
# does nothing
# usually used as a placeholder while writing code
# text adventure project
    
if True:
    pass

def enter_forest():
    pass

def swim_river():
    pass