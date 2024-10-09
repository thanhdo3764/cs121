import time
import random

"""LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
	if "a" in x:
		newList.append(x)

print(newList)

newList2 = [x for x in fruits if 'a' in x]
print(newList2)

fiftyZeros = [0 for x in range(50)]
print(fiftyZeros)

ucList = [x.upper() for x in fruits]
print(ucList)

x = 3
y = 5
listOfLists = [[i-j for j in range(y)] for i in range(x)]
print(listOfLists)
#--------------------------------------------------
"""
"""Counting indexes
fib = [0, 1, 1, 2, 3, 5, 8, 13]
counter = 0
for f in fib:
	print("Fib #", counter, "is", f)
	counter += 1

for i in range(len(fib)):
	print("Fib #", i, "is", fib[i])

for i, f in enumerate(fib):
	print("Fib #", i, "is", f)
#--------------------------------------------------
"""
"""Monte Carlos Randomness
def countDoubles(rolls):
	doubles = 0
	while rolls > 0:
		r1 = random.choice([1,2,3,4,5,6])
		r2 = random.choice(range(1,7))
		if r1 == r2:
			doubles += 1
		rolls -= 1	
	return doubles

def main():
	rollCount = [10,50,100,500,1000,5000,10000,100000]
	for r in rollCount:
		print(r, "rolls gives apparent odds of", countDoubles(r)/r)
if __name__ == '__main__':
	main()
#--------------------------------------------------
"""


















