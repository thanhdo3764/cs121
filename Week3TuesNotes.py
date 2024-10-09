#Returns factorial of parameter N
def fac(N):
	if N <= 1:
		return 1
	else:
		return N * fac(N-1)
print(fac(2))

list = [1,2,3,4,5]
print(list)
print(list[1:])

#Returns the length of a list or string
def mylength(s):
	#base case
	if s == []:
		return 0
	#recursive
	else:
		return 1 + mylength(s[:-1])
print(mylength([1]))

#Returns the largest element in a list
def mymax(L):
	print(L)
	#empty list
	if len(L) == 0:
		return None
	#else if length is 1
	elif len(L) == 1:
		return L[0]
	#There must be 2 elements in L
	else:
		if L[1] < L[0]:
			return mymax(L[0:1]+L[2:])
		elif L[0] < L[1]:
			return mymax(L[1:])
print(mymax([1,2,3,4,5,6,7,1]))