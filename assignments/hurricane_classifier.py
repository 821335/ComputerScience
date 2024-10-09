x = int(input("what is the wind speed"))

if x < 74:
    print("tropical storm")

elif x < 96:
    print("category 1")

elif x < 111:
    print("category 2")

elif x < 130:
    print("category 3")

elif x < 157:
    print("category 4")

elif x >= 157:
    print("category 5")
