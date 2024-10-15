# exception handling
# Write a program that asks for two numbers and adds them

# if  =  try
# elif  =  except specific error type
# else = except
def divide_two_numbers():
    try:
        x = int(input("Whats the first number?\n>"))
        y = int(input("Whats the second number\n>"))
        print(x / y)

    except TypeError:
        print("please enter a number....")
        divide_two_numbers()

    except ZeroDivisionError:
        print("cannot divide by zero...")
        divide_two_numbers()


divide_two_numbers()

