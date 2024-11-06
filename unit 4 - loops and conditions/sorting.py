# import random
import random

#genrate a list of five random integers from 0-99
nums = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]

# print the list before it is sorted
print(nums)

#define the function
def bubble_sort(nums):  #take the list as a parameter
    #create a variable for how many steps we are taking, start at zero
    steps = 0

    #check if the list is sorted as many times as their are list items
    for j in range(0,len(nums)-1):
        #iterate through every item in the list
        for i in range(0, len(nums) - 1):

            #check if the current list item is greater than the next list item
            if nums[i] > nums[i+1]
                nums[i]. nums[i+1] = nums[i+1]. nums[i]
                steps += 1
    
    
    print(nums)
    print("completed in " + str(steps) + " steps ")

            


bubble_sort(nums)




