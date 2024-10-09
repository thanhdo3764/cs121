import random

myRandomNumber = random.randint(1,100)
adder = 50
while True:
	yourGuess += adder
	print(yourGuess)
	if yourGuess < myRandomNumber:
		print("Too low!")
		adder = int(adder/2)
		if adder == 0:
			adder = 1
	elif yourGuess > myRandomNumber and adder > 0:
		print("Too high!")
		adder = int(-1 * adder/2)
		if adder == 0:
			adder = -1
	else: # yourGuess == myRandomNumber
		break
print('Hurrah! You got it! It was', myRandomNumber)
