import time

def primeBattle(low, high):
    l = [] #create empty list
    print(range(low, high+1))
    for x in range(low, high+1): #checks every number in range
        if x > 0: #if x is positive
            if x % 7 == 0: #if x is divisible by 7
                if x % 5 != 0: #if x is not a multiple of 5
                    l.append(x)
    return l

#Factorial as covered in class
def facRec(n):
    if n <= 1:
        return 1
    else:
        return n*facRec(n-1)

def facForLoop(n):
    ans = 1 #ans will be multiplied by each subsequent number
    for x in range(1, n+1): #ans will be multiplied by numbers from n to 1
        ans *= x
    return ans

def facWhileLoop(n):
    ans = 1 #ans will be multiplied by each subsequent number
    while n > 0: #Loops until n is 0
        ans *= n #ans is multiplied by the current n value
        n -= 1 #n is subtracted by 1 until n == 0
    return ans

def testFactorialTimes():
    n = 10
    print('Testing Recursion...')
    start = time.time()
    results = facRec(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing While Loop...')
    start = time.time()
    results = facWhileLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing For Loop...')
    start = time.time()
    results = facForLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)
testFactorialTimes()


def coolMatrix(x, y):
    l = [] #empty list l
    for i in range(0,x): #loops and counts row i from 0 to x
        row = [] #empty row list
        for j in range(0, y): #loops and counts column j from 0 to y
            row.append(i-j) #adds i-j to the end of row[]
        l.append(row) #filled up row[] is added to matrix l
    return l
print(coolMatrix(1,2))