# 2 functions
print("Hello, world!")                  #"Hello, world!" is the parameter
input("Please enter your username\n>") # \n is called an escape character
 # \n starts a new line (linebreak)
# input is never required


# variables
#Syntax
# <name> = <value>
x = 5

#snake naming convention - all lowercase, underscore for spaces
# CONCISE: Short and descriptive
username = "osowski"    #Define string ("string" of characters)
fav_animal = "Lion"     #define string ("string" of characters)
total_poptarts = 12     #define intergers (whole number)
percent_complete = 23.52        #define float (decimal number)
is_cool = True                  #Define Boolean (true/false)
first_letter = "c"              #define character (single symbol)

total_poptarts = 8      #Reassign


# Aritmetic Operators
# +  -  *  /  **  %  //
print(4 + 4)    #> 8
print("4" + "4")    #> 44
print("cat" + "dog")    #> catdog
print("cat" * 3)    #> catcatcat
print("cat" + 3)    #> error: cannot use + for string and int

#make some working programs
#1. add two numbers using input
x = int(input("what is x?\n>"))      # input() always returns a string
x - int(x)
y = input("what is y>\n>")      # even if you type in a number
y = int(y)
print(x + y)


# 2. converts celcius to farenheight
temp_celcius = input("what is the temperature in celcius?\n>")
temp_celcius = int(temp_celcius)
temp_farenheight= (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F")




#some coversion functions
str()
int()
float()
bin()
bool()

#The stuff that goes between the parenthesis is called PARAMETERS
#Paramaters are the values that the function needs to run



#functions
#functions are a lot like variables
# they can be recalled from memory by calling their name
# store information
# variables store values, functions store code
def potato():       # def keyword + name + () + :
    print("potato")         # lines indented underneath are "inside" the function

# functions are not ran when they are are defined
# they must be called by their name to run
potato()        # every function call needs open and closed parenthesis
                # even if it has no parameters

def jump(how_high):
    print("You jumpped " + str(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("z", "a",  "c", "k", "o", "s", "o", "w", "s", "k", "i")

#functions can have many many lines
def top_tem_games():
    print("1. E;dem ring")
    print("2. Blacks ops 4")
    print("3. rocket league")
    print("4. fortnite")
    print("5. Warzone two")
    print("6. minecraft")
    print("7. Rainbow six siege")
    print("8. NCAA 25")
    print("9. Madden 25")
    print("10. Apex legends")

# Global and Local variables!!
#Scope refers to the context in which the variable was defined
#GLOBAL - defined at no indentation level
#LOCAL - definded inside of a function
    
#global varibales can be used anywhere
todd = "cool guy"       #global variable- no indentation level

def my_function():
    smith = "not cool guy"  #local variable- define in a function
    tpdd = "strange guy"            #local variable even though it has the same name
    print(todd)     #prints the local variable todd
    # when you call a varibale in a function
    # it searches local variables first, then global variables

#If you want to reassign a global variable inside of a function
todd = "cool guy"
def my_function():
    global todd             #In this function, whenever I call todd
                             # I mean the global todd, not the local
    todd = "strange guy"    #reassign todd - global
    print(todd)             # print todd - global

#return functions
#functions can also return values
#the value that is returned is sent back to where the function was called
#this is very similar to how a variable works
#the function does its work and returns and answer back
def add2(x, y):
    return x + y        #returns the sum of x and y to where the function was called

add2(2,10)              
