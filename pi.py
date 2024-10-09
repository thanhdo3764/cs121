import random
import math
def approxPi(darts):
	#approximate pi by selecting darts random points
	insideCircle = 0
	#loop over appropriate number of darts
	for i in range(darts):
		#pick a random point 
		randX = random.uniform(0,1)
		randY = random.uniform(0,1)
		#distance <= radius
		#distance **2 <= radius **2
		if randX**2+randY**2 <= 1:
			#update counter of some kind
			insideCircle += 1
	#figure out ratio
	piQuarters = insideCircle / darts
	#return something
	return piQuarters * 4

def main():
	n = int(input("number of darts:"))
	print("Approximation with  n =", n, ":", approxPi(n))

if __name__ == '__main__':
	main()