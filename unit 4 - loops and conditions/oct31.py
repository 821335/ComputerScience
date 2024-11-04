# python has four types of collections
#tuple
#set
#list
#dictionary

#A list is a way to store more than one value in a single variable.
#those values in the list are called ITEMS
# ITEMS can be accessed by their index (position in the list)
#INDEX                      0                   1              2                  3             4
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of blood", "Iron ball", "bloodhounds fang"]

#INDEX          0      1    2       3
best_years = [1776, 1985, 1994, 1957]

#print the index of the value in the list
print(best_years.index(1985))

#Print the best elden ring weapon
print(best_elden_ring_weapons[0])

#print the worst of the best elden ring weapon
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#list items can be changed
best_elden_ring_weapons[3] = "Spiked fist"
print(best_elden_ring_weapons)

#Remove the last item in the list by its position in the list
# the .pop() function removes an item in a list by its position in the list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

#Remove an item by its value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

# add a new item to the end of a list
best_elden_ring_weapons.append("mohgwyn's sacred spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)

#Strings are lists
# strings are just a list of characters
word = "potato"
print(word[0])

