# for loop lets you iterate a list
# great for looping a set number of times
# but what if we need to loop an uncertain number of times
# ex. entering your password.
# you could get it right the first time
# it could take you a million tries
# or anything in between

real_pass = "potato45"
entered_pass = ""

attempts = 0
# A while loop continues looping untill the condition is no longer true
while real_pass != entered_pass:      
    # check if the entered password matches the real one
    # Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1
    #check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print( str(attempts) + " attempts ")
        print("try again...")
        
        #end password checking
print("welcome")

# with while loops, you need to be careful for infinite loops
# An infinite loop happens when you enter a while loop that can never be escaped
# example (do not click run...)
#count = 0
#while True:
    #count += 1
    #print("count")

# real world example:
# " type "exit" to quit

user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print("you entered: " + user_input)

print("all done")