import re

# patterns = ['term1', 'term2']
#
# text = 'This is a string with term1, not the other!'

# for pattern in patterns:
#     print('I am searching for ' + pattern)
#
#     if re.search(pattern,text):
#         print('Match')
#     else:
#         print('No Match')

# text1 = 'term1'
#
# match = re.search('term1',text1)
# print(type(match))

# FIND THE STARTING POSITION OF A PATTERN

# print(match.start())

# SPLIT A TERM

# split_term = '@'
# email = 'user@email.com'
#
# print(re.split(split_term,email))

# FIND ALL INSTANCES OF A PATTERN

# print(re.findall('match','test phrase match in middle...match'))        # finding match in twice



def mult_re_find(patterns,phrase):
    for pat in patterns:
        print("Searching for patterns {}".format(pat))
        print(re.findall(pat,phrase))
        print('/n')

# test_phrase = 'sdsd.....dddddsddsddsddd.....ssdsssssdsss....sdsdsdsdsds'

# test_pattern = ['sd*']  # 0 or more d after s
# test_pattern = ['sd+']  # 1 or more d after s
# test_pattern = ['sd?']  # 0 or 1 d after s
# test_pattern = ['sd{3}']  # 3 d after s
# test_pattern = ['sd{2,3}']  # 2 or 3 d after s
# test_pattern = ['s[sd]']  # one or more s or one or more d after s

test_phrase = 'This is a string! but is a punctuation. How can we remove it?'

# ^ character removes all the punctuations
test_pattern = ['[^!.?]+']

# return lower case characters
test_pattern = ['[a-z]+']

# return upper case characters
test_pattern = ['[A-Z]+']

# return digits
test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
test_pattern = [r'\d+']
# return non-digits
test_pattern = [r'\D+']
# return sequence of white space
test_pattern = [r'\s+']
# return sequence of non-white space
test_pattern = [r'\S+']
# return alphanumeric characters
test_pattern = [r'\w+']
# return non-alphanumeric characters
test_pattern = [r'\W+']

mult_re_find(test_pattern,test_phrase)