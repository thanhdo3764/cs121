# Imports let us pull in functionality from other Python files
# They should always be the first thing in a file, if you need them.

from example import sayHi

# this import says 'look for a file called example.py and get the sayHi function
# from it'. Python will look in the same directory as this file first,
# and then check its other libraries if it can't find your import.


# this function is defined in example.py, but we can call it because we imported it.
sayHi()