# try:
#     f = open('simple.txt','r')
#     f.write('Test write to simple text!')
# except IOError:     # the error 'IOError' does not need to be specified...just 'except' will do the job
#     print('Error: Could not find or read data!')
# else:
#     print('Success')
#     f.close()

try:
    f = open('simple.txt','r')
    f.write('Test write to simple text!')
except:
    print('Error: Could not find or read data!')
# 'finally' block runs even after error
finally:
    print('I always work no matter what!')