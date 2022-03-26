# problem 1
s = 'django'

# index to print 'd'
print(s[0])

# index to print 'o'
print(s[-1])

# index to print 'djan'
print(s[:-2])

# index to print 'jan'
print(s[1:4])

# index to print 'go'
print(s[4:])

# index to reverse the string
print(s[::-1])


# problem 2
l = [3,7,[1,4,'hello']]

# reassign hello to goodbye
l[2][2] = 'goodbye'
print(l)


# problem 3

# keys and indexing to grab hello from the following dictionaries
d1 = {'simple_key': 'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

# problem 4

#  use set to find unique values of list
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

# problem 5

# use print formatting
age = 4
name = 'Sammy'

print("Hello my dog's name is {n} and he is {a} years old".format(n=name,a=age))


