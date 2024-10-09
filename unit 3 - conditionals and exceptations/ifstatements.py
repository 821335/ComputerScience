# if statements evaluate boolean expressions
# make decisions about which code to run next

#take a temperature
# print "<temperature> is hot" if the temperature is >= 80
# otherwise, print "<temperature> is not hot"
temperature = input("what is the temperature?\n>")
temperature = int(temperature)
# if, boolean expression, :
# sort of like a function, no parenthesis!
if temperature >= 80:       # if the bool evaulates to true, go inside
    print("the tempertaure is " + str(temperature) + " degrees.")
    print(str(temperature) + " degrees is hot")

else: # else takes no condition and runs when the if above is false
    # otherwise...
    print("the temperature is " + str(temperature) + " degrees.")
    print(str(temperature) + "degrees is not hot")



real_password = "skibidi68"
input_password = input("please enter the password\n>")

if input_password == real_password:
    print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")



answer_one = input("Give me a integer greater then 1576")
answer_one = int(answer_one)
print(answer_one > 1576)

answer_two = input("give me a float that is greater then 3.14")
answer_one = float(answer_two)
print(answer_one > 3.14)

answer_three = input("what's the real password?\n>")
real_password = "school"
input_password+ input("enther the password\n>")

if input_password == real_password:
    print("access granted")

else:
    print("access denied")

answer_four = input("Give me a interger that is greater then or equal to 1")
answer_four = int(answer_four)
print(answer_four >= 99)


                    