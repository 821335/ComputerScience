# nested if statements
# you are a prime memer or order is at least $25
# you are at least 18 years old or have parent consent

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >=18:
        print("you are eligible for free shipping")
    elif consent:
            print("you are eligible for free shipping")
    else:
            print("you are not eligible for free shipping")

elif cost >=25:
    if age >=18:
        print("you are eligible for free shipping")
    elif consent:
        print("you are eligible for free shipping")
    else:
        print("you are not eligible for free shipping")

else:
    print("you are not eligible for free shipping")



# do we need an umbrella
    
# we need an umbrella if it is raining and we are outside
raining = True
outside = True
# logical operators
if raining and outside:
     print("bring an umbrella")

else:
     print("don't bring an umbrella")
# nested if statements
if raining:
     if outside:
          print("you need to bring an umbrella")
     else:
          print("don't bring an umbrella")

else:
     print("don't bring an umbrella")
