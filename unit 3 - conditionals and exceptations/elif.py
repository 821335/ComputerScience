x = 0

if x > 0:       # > < == >= <= !=
    print("x is a positive number!")

elif x < 0:     # elif statement are always paired to an if
    print("x is a negative number!")


else:       # else statements are always paired to an if statement
            # else statemnts never take a condition
    print("x is  negative number!")


color = input("what color is the light")

if color.lower() == "green":        # only one IF
    print("go")


elif color.lower() == "red":            # no limit to how elifs you can use
    print("stop!")

elif color.lower() == "yellow":
    print("stop if safe")

else:
    print("call cops")



x = 10

if x > 5:
    print("x is greater than five")

if x > 8:
    print("x os greater than eight")

if x > 5:
    print("x is greater than eight")
elif x >8:
    print("x is greater than eight")