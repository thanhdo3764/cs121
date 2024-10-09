#Returns the nth Fibonacci number
def fib(n):
    #checks if n is negative
    if n < 0:
        return None
    #base case n == 0
    elif n == 0:
        return 0
    #base case n == 1
    elif n == 1:
        return 1
    #base case n == 2
    elif n == 2:
        return 1
    #recursive case that adds the last two Fibonacci numbers
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
