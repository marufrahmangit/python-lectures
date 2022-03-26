# example
# x = 20
#
# def func():
#     x = 50
#     return x
#
# print(x) # prints global value of x
# x = func()
# print(x) # prints local value of x

# LAMBDA

# LOCAL
# lambda x: x**2

# ENCLOSING FUNCTION LOCALS
# name = 'This is a global name!'
#
# def greet():
#     name = 'sammy'
#
#     def hello():
#         print("hello " + name)
#
#     hello()
#
# greet()
# print(name)

# GLOBAL - not recommended
# x = 50
# def func():
#     global x
#     x = 1000
#
# print('Before function called x is ',x)
# func()
# print('After function called x is ',x)
