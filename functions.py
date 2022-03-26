# def my_func(param1='python'):
#     print('my first {} function'.format(param1))
#     """
#         THIS IS A DOCSTRING
#     """
#
# my_func()

# return statements
# def hello():
#     return 'hello'
#
# result = hello()
# print(result)
#
# def addNum(num1, num2):
#     return num1+num2
#
# result = addNum(2,3)
# print(result)
# # type of data
# print(type(result))
#
# result = addNum('2','3')
# print(result)
# # type of data
# print(type(result))


# lambda expression

# Filter function- accepts other functions as input parameters
# mylist = [1,2,3,4,5,6,7,8,9]
# def even_bool(num):
#     return num%2 == 0
#
# evens = filter(even_bool,mylist)
# print(list(evens))

# do the above with lambda expression- useful when a function is only going to be used once
# lambda num:num%2==0
# evens = filter(lambda num:num%2==0,mylist)
# print(list(evens))

# general
# st = 'Go Sports! #Sports'
# print(st.lower())
# print(st.upper())
# print(st.split())
# print(st.split('#'))
# print(st.split('#')[1])

# 'in' keyword
print('x' in [1,2,4])
print('x' in [1,2,4,'x'])

