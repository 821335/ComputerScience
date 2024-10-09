score = 0

a1 = input("what is a float less then or equal to 19.8\n>")




a2 = input("what's the temperature\n>")


a3 = input("what's the weather outside")


a4 = input("what season are we in\n>")

a5 = input("What is my favorite video game\n>")


def tally_score():
    if  a1 == "19.5":
        score = score + 1

    if a2 == "65":
        score = score + 1

    if a3 == "sunny":
        score = score + 1

    if a4 == "fall":
        score = score + 1

    if a5 == "NCAA 25":
        score = score + 1
print(score)
tally_score()


        

