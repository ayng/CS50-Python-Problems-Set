import cowsay
import sys

"""
if len(sys.argv) == 2:
    cowsay.cow('hello, ' + sys.argv[1])
"""

"""
if len(sys.argv) == 2:
    cowsay.trex('hello, ' + sys.argv[1])
"""
# Find module 'sayings' read it from left to right top to bottom and import the hello function but by the time it reads the file, the last line of code 'main()' gets called
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])