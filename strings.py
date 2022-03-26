# indexing #
# strings are immutable- cannot change something by calling an index
myString = 'abcdefg'

# return everything after and including index 2
print(myString[2:])
# return everything between index 2 to index 5...NOTE: index 2 is included but index 5 is excluded
print(myString[2:5])
# return everything up to index 3...NOTE: index 3 is excluded
print(myString[:3])
# return everything stepping over every single (1) index
print(myString[::1])
# return everything stepping over every two (2) indices
print(myString[::2])
# return everything
print(myString[:])


# basic methods #

x = 'hello world'

# upper case
print(x.upper())

# capitalize
print(x.capitalize())

# split string...NOTE: default split by space
print(x.split())

# split by specific letter...NOTE: will remove the letter specified
print(x.split('o'))

# print formatting... NOTE: brackets prints the parameter strings in the format method
a = "Item One: {} Item Two: {}".format("dog", "cat")
print(a)
# print formatting specifying variables...NOTE: variables can be switched inside the brackets
b = "Item One: {two} Item Two: {one}".format(one="dog",two="cat")
print(b)