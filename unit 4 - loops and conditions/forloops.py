# for Loops

# for loops allow the programmer to repeat, or what we call loop

# write a program that prints the numbers one through ten

#for <tem var> in <list>:

# range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0,10):       # 0 is the start value, 10 is the stop value
    print(i)

top_foods = ["eggs benedict", "fried chicken", "mac n chese"]
#go through every food in top foods
# repeats everything in the for loop for each item in the list
#where food equals the current item
for food in top_foods:
    print(food)


groceries = ["milk", "eggs", "bread", "butter", "apples"]

purchased_item = input("what item did you buy?\n>")

for grocery in groceries:
    if grocery == purchased_item.lower():
        print(grocery + " checked off the list")
        groceries.remove(grocery)

print (groceries)

import random
sum = 0
numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
for i in numbers:
    

    