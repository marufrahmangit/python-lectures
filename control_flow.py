# if-elif-else

# if 1<2:
#     print('first block')
#     if 20<3:
#         print('second block')
#
#
# if 1>2:
#     print('hello')
# elif 3 == 3:
#     print('elif ran')
# else:
#     print('last')


# loops

# for loops

# for loop on list
# seq = [1,2,3,4,5,6]
#
# for jelly in seq:
#     # code here
#     print(jelly)
#     print('hello')

# for loop on dictionary
# d = {'sam':1,'frank':2,'dan':3}

# for item in d:
    # print(item) # print keys
    # print(d[item])  # print values

# alternative methods

# print keys... alternate: for item in d.keys
# for val in d.values():
#     print(val)
#
# # print values... alternate: for item in d.values
# for key in d.keys():
#     print(key)


# list of tuples
# mypair = [(1,2), (3,4), (5,6)]
# for item in mypair:
#     print(item)
#
# # tuple unpacking
# for tup1,tup2 in mypair:
#     # print(tup1)
#     # print(tup2)
#     # switching the order
#     print(tup2)
#     print(tup1)


# while loop
# i = 1
# while (i<5):
#     print('i is {}'.format(i))
#     i = i + 1

# range functions - quickly generate int based on start and end points

# x = list(range(0,5))
# print(x)

# add the step over value as 3rd parameter: in this case step over by 2
# y = list(range(0,20,2))
# print(y)

# example
# for item in range(10):
#     print(item)

# list comprehension
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)

# Now write the above code in list comprehension

out = [num**2 for num in x]
print(out)