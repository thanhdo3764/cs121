# when we import a file (see example2.py), Python automatically runs any code
# that isn't part of a function.
#
# That can lead to weird results like extra output, or programs waiting
# for input when we don't expect them to (which is a problem for Autolab)
#
# To get around that, we can structure out code so that if it's run directly
# e.g. with 
#       python3 example.py
# it does one thing, but if it's imported it does another.
#
# This file shows how to set that up

def sayHi():
    ''' prints 'hi' when called '''
    print('hi')

# note: the name 'main' is not required, but you should use it
def main():
    ''' run when the script is executed directly, but now when it's imported '''
    print('Hello, Worlds!')
    print('I am in examples')

# __name__ is an internal variable Python sets up for us which stores the
# name of the file being run.
# If a file is invoked directly (e.g. python3 example.py), the name will
# be listed as '__main__', otherwise we'll see a file name.
# We can use this to make sure some code only runs if we launch the file directly.

if __name__ == '__main__':
    # this code only runs if we launched this file directly
    main()