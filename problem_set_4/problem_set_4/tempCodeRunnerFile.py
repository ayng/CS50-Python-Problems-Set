import sys
try:
    print('hello, my name is', sys.arg[1])
except IndexError:
    print('Too few arguments')