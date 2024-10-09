# string functions
# a group of like-functions that manipulate strings
# the modify strings
# super easy and convenient to use
# python would really not be fun without them

#   .Lower()
# converts a string to all lowercase
input_answer =  "Lord of The Rings"
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# converts a string to uppercase!
x = "hello world".upper()
print(x)    # prints HELLOW WORLD

# .capitalize()
# converts to lowercase, them capitalizes the first letter
y = "HeL10 wOrLd".capitalize()
print(y)        # print "Hello world"

# .title()
# converts a string to titlecase
#capital first letters of words
z = "HeL10 wOrLd".title()
print(z)    # print "Hello World"

# .swapcase()
# it inverts the casing of eac character
q = "Hello World!".swapcase()
print(q)        #prints "hELLO wORLD!"