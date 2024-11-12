# dictionary is a type of collection like list
# a list is a collection of items in a sequence
# a dictionary is different
# dictionaries store data in key-value pairs
# you can retreive data quickly by using a unique key
# instead of retreving it by index (position)


# example
# lists use brackets, dictionaires use braces

brett = {
    "name": "Brett",
    "age": 15,
    "city": "St micheal",
    "pets": 2,
    "height": 6.1
}
# each key must be unique

# Retreving values from a dictionary

print(brett["age"])

# .get allows you to retreive a value without erroring
#when the key doesn't exist
# the second parameter is what is given if value is not found
print(brett.get("height"))
print(brett.get("weight", "fortnite"))


# you can add values to a dictionary

brett["country"] = "USA"

# you can modify values
brett["age"] = 16

print(brett)

# remove entries
brett.pop("pets")

# iterate through a dictionary using a for loop

for key, value in brett.items():
    print(key + ":" str(value))

# dictionary functions
print(brett.keys()) # returns all keys
print(brett.values())   # returns all values
print(brett.items())        # returns all pairs
print(brett.clear())        #removes all items from the dict