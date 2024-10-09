# write code that prints the values 1-15,
# but replaces multiples of 3 with "fizz",
# multiples of 5 with "buzz", and multiples 
# of both with "fizzbuzz"

def fizzbuzz():
    ''' does fizzbuzz using if/elif to specify all cases '''
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()

def differentFizzbuzz():
    ''' tells print not to include a newline, so fizz and buzz naturally combine'''
    for i in range(1, 16):
        if i % 3 == 0:
            # the end option to print tells it what to print
            # at the end of a single output. It defaults
            # to printing a newline, but here I ask it to 
            # print nothing.
            print("fizz", end="") 
        if i % 5 == 0:
            print("buzz", end="")
        if i % 3 != 0 and i % 5 != 0:
            print(i, end="")
        print() # print a newline character

differentFizzbuzz()
