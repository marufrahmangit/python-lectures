# tuples are like lists but are immutable- cannot change something by calling an index
t = (1,2,3)
print(t[0])
t = ('a', True, 123)
print(t)
# t[0] = 'NEW' # reassignment not possible with tuple!


# sets are unordered collections of unique elements
x = set()
x.add(1)
x.add(2)

# even though 4 is added three times, only printed once (unique element)
x.add(4)
x.add(4)
x.add(4)
x.add(0.1)
print(x)

converted_set = set([1,1,1,1,1,2,2,2,3,3,3,3,3])
print(converted_set)
# booleans - true/false
# True
# False

