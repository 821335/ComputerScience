def top_five_movies(movie_1, movie_2, movie_3, movie_4, movie_5):
    print("My top five movies")
    print("1. " + movie_1)
    print("2. " + movie_2)
    print("3. " + movie_3)
    print("4. " + movie_4)
    print("5. " + movie_5)
          
top_five_movies("Deadpool 2", "Waterboy", "Blindside", "Fast and furios", "Spiderman")




x = 4
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

print(x)  
my_function()

def add(x, y):
    return x + y

sum = add(10, 9)
print(sum)

def calculate_tax(item, price, rate):
    print(price * rate)

calculate_tax("Baseball", 4.99, 0.06875)


    

