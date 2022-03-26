# GLOBAL AND LOCAL
# s = 'GLOBAL VARIABLE'
#
# def func():
#     mylocal = 10
#     # print(locals())     # locals returns dictionary of local variables
#     # print(globals())    # globals returns dictionary of all global variables
#     print(globals()['s'])    # global variables defined as 's'
# func()

# ASSIGN FUNCTIONS TO VARIABLES
# def hello(name='Maruf'):
#     return 'hello ' + name
#
# # print(hello())
#
# mynewgreet = hello
# print(mynewgreet())

# FUNCTIONS WITHIN FUNCTIONS
# def hello(name='Maruf'):
#     print('The hello function was run')
#
#     def greet():
#         return 'This string is inside greet'
#
#     def welcome():
#         return 'This string is inside welcome'
#
#     # print(greet())
#     # print(welcome())
#     # print('End of hello')
#
#     if name == 'Maruf':
#         return greet
#     else:
#         return welcome
#
# # hello()
#
# x = hello()
# print(x())

# def hello():
#     return 'Hi Maruf!'
#
# def other(func):
#     print("Hello")
#     print(func())
#
# other(hello)    # hello does not have parenthesis because it is not returning what hello function returns

def new_decorator(func):
    def wrap_func():
        print('Code here before executing func')
        func()
        print('func() has been called')
    return wrap_func

# def func_needs_decorator():
#     print('This func is in need of a decorator')

# func_needs_decorator = new_decorator(func_needs_decorator)

# the above line can be done in the following way
@new_decorator
def func_needs_decorator():
    print('This func is in need of a decorator')

func_needs_decorator()