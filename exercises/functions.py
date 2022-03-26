# problem 1

# given a list of integers, return true if the sequence of numbers 1,2,3
# appears in the list somewhere

# for example:

# arrayCheck([1,1,2,3,1]) -> True
# arrayCheck([1,1,2,4,1]) -> False
# arrayCheck([1,1,2,1,2,3]) -> True

# def array_check(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
#             return True
#     return False
#
# array = array_check([1,1,2,1,2,3])
# print(array)


# problem 2

# given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo"

# For example:

# stringBits('Hello') -> 'Hlo'
# stringBits('Hi') -> 'H'
# stringBits('Heeololeo') -> 'Hello'

# method 1: using algorithm
# def string_bits(mystring):
#     result = ""
#     for i in range(len(mystring)):
#         if i%2==0:
#             result = result + mystring[i]
#     return result
# mystring_check = string_bits('Heeololeo')
# print(mystring_check)

# method 2: using python slice notation

# def string_bits(mystring):
#     result = mystring[::2]
#     return result
#
# check = string_bits('Heeololeo')
# print(check)


# problem 3

# given two strings return True if either of the strings appears at
# the very end of the other string, ignoring upper/lower case
# differences (in other words, the computation should not be
# "case sensitive")

# Note: s.Lower() returns the lowercase version of a string

# for example:

# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

# method 1: python endswith method
# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
#     return (b.endswith(a) or a.endswith(b))
#
# other = end_other('AbC', 'HiaBc')
# print(other)

# method 2: using algorithm
# def end_other(a,b):
#     a = a.lower()
#     b = b.lower()
#     return a[-(len(b)):] == b or a == b[-len(a):]
#
# other = end_other('AbC', 'HiaBc')
# print(other)


# problem 4

# given a string, return a string where for every char in the
# original, there are two chars.

# doubleChar('The') -> 'TThhee'
# doubleChar('AAbb') -> 'AAAAbbbb'
# doubleChar('Hi-There') -> 'HHii--TThheerree'

# method 1: using list append method by converting to list
# and then converting back to string using python join method

# def double_char(mystring):
#     to_list = []
#     for i in mystring:
#         to_list.append(i*2)
#     return to_list
#
# double = double_char('The')
# listToStr = ''.join([str(item) for item in double])
# print(listToStr)

# method 2: using list append method

# def double_char(mystring):
#     str = ''
#     to_list = []
#     for i in mystring:
#         to_list.append(i*2)
#     for item in to_list:
#         str += item
#     return str
#
# double = double_char('The')
# print(double)

# method 3:
# def double_char(mystring):
#     result = ''
#     for char in mystring:
#         result += char*2
#     return result
#
# double = double_char('Hi-There')
# print(double)

# problem 5

# given 3 int values, a b c, return their sum. However, if any of the values is
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except
# 15 and 16 do not count as teens. Write a separate helper "def fix_teen(n):"
# that takes in an int value and returns that value fixed for the teen rule

# this way, you avoid repeating the teen code 3 times (i.e., "decomposition")
# Define the helper below and at the same indent level as the main no_teen_sum().
#
# Examples:
#
# no_teen_sum(1,2,3) -> 6
# no_teen_sum(2,13,1) -> 3
# no_teen_sum(2,1,14) -> 3

# def no_teen_sum(a,b,c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
#
#
# def fix_teen(n):
#     if n in [13,14,17,18,19]:
#         return 0
#     return n
#
# test = no_teen_sum(1,15,1)
# print(test)

# problem 6

# return the number of even integers in the given array

# examples:

# count_evens([2,1,2,3,4]) -> 3
# count_evens([2,2,0]) -> 3
# count_evens([1,3,5]) -> 0

# def count_evens(nums):
#     count = 0
#     for i in nums:
#         if i%2 == 0:
#             count += 1
#     return count
#
# test = count_evens([1,2,1,2,3,4,5,8])
# print(test)


















