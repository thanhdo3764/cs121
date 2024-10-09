'''My image represents a landscape with mountains/hills, a river, and trees.'''
import turtle
from turtle import *

class MyDrawing():
	def __init__(self):
		self.horizonY = 50

	def drawSquare(self, l):
		turtle.reset()
		for i in range(4): #Go forward and turn 90 degrees 4 times
			forward(l)
			left(90)
		turtle.getcanvas().postscript(file='squareArt.ps', colormode = 'color')

	def drawTrunk(self, x, y, multiplier):
		penup()
		self.haze(238,197,145,y) #colors trunk based on y axis
		#trunk
		setpos(x,y)
		setheading(0)
		begin_fill()
		pendown()
		forward(50*multiplier)
		left(120)
		forward(70*multiplier)
		setheading(90)
		forward(150*multiplier)
		#branches
		right(70)
		for i in range(5):
			forward(100*multiplier)
			left(170)
			forward(100*multiplier)
			right(133)
		#other half of trunk
		setheading(270)
		forward(150*multiplier)
		right(30)
		forward(70*multiplier)
		setpos(x,y)
		end_fill()

	def drawLeaves(self, x, y, multiplier):
		penup()
		setpos(x+150*multiplier,y+300*multiplier)
		setheading(0)
		pendown()
		begin_fill()
		#Draws a circle of several fractions of circles
		for i in range(11):
			for j in range(11):
				forward(15*multiplier)
				left(18)
			right(165.3)
		end_fill()

	def drawTree(self, x, y, multiplier):
		self.haze(0,205,0,y) #colors outer leaves based on y axis
		self.drawLeaves(x,y,multiplier) #outer leaves
		self.haze(0,238,0,y) #colors inner leaves based on y axis
		self.drawLeaves(x,y+90*multiplier,0.7*multiplier) #inner leaves
		self.drawTrunk(x,y,multiplier) #draw trunk

	def haze(self, r, g, b, y):
		x=0 #haze multiplier
		red = 0
		blue = 0
		if y in range(-400,-200): #no haze
			x = 0
		if y in range(-200,-50): #haze level 1
			x = 0.375
		if y in range(-50,50): #haze level 2
			x = 0.625
		if y in range(50,401): #haze level 3
			x = 0.875
		if r < 135: #calculate red
			red = int((135-r)*x+r)
		else:
			red = int(r-(r-135)*x)
		if g < 206: #calculate green
			green = int((206-g)*x+g)
		else:
			green = int(g-(g-206)*x)
		if b < 235: #calculate blue
			blue = int((235-r)*x+r)
		else:
			blue = int(r-(r-235)*x)
		return color(red, green, blue)

	def drawForeground(self):
		color('forest green')
		penup()
		setpos(-400,self.horizonY)
		pendown()
		setheading(0)
		forward(800)
		begin_fill()
		setheading(270)
		forward(400+self.horizonY)
		setheading(180)
		forward(800)
		setheading(90)
		forward(400+self.horizonY)
		end_fill()

	def drawHills(self, nHills):
		for i in range(nHills): #for each hill
			color(134,191,220)
			begin_fill()
			penup()
			#set position at starting point for each hill
			setpos(-400+800/nHills*i,self.horizonY)
			setheading(0)
			pendown()
			#draw hills/mountains
			for j in range(3):
				forward(800/nHills)
				left(120)
			end_fill()
			self.drawSnow(nHills)	

	def drawSnow(self, nHills):
		color(190,255,255)
		penup()
		begin_fill()
		right(120)
		back((2/3)*800/nHills) #go to starting point of snow
		pendown()
		setheading(0)
		for i in range(4): #draw snow line
			left(30)
			forward(800/nHills/21)
			right(60)
			forward(800/nHills/21)
			setheading(0)
		left(120) #draw top of hills
		forward((1/3)*800/nHills)
		left(120)
		forward((1/3)*800/nHills)
		end_fill()

	def drawBackground(self, nHills):
		bgcolor(135,236,235)
		self.drawHills(nHills)

	def drawRiver(self, x):
		penup()
		color(115,190,255)
		setpos(x, self.horizonY)
		pendown()
		setheading(180)
		counter = 0
		begin_fill()
		#draws river
		for i in range(2):
			for j in range(4):
				for k in range(9): #curves river
					forward(10+counter**4)
					left(18)
				for k in range(9): #curves river back
					forward(5+counter**4)
					right(18)
				if i == 0:
					counter += 1 #River becomes slightly longer the further it travels
				else:
					counter -= 1
			if i == 0: #sets up for the river coming back up
				setheading(0)
				forward(530)
				setheading(19)
				counter = 3
		end_fill()

	def drawImage(self): #this is where the landscape is drawn
		#setup
		reset()
		setup(800,800)
		speed(0)
		#draws background and foreground elements
		self.drawBackground(2) #How many hills
		self.drawForeground()
		self.drawRiver(0) #what x coordinate is river
		#draws trees
		for i in range(5):
			self.drawTree(-400 + 160*i, 50, 0.15) #xcor, ycor, how big
		self.drawTree(70,0,0.25)
		self.drawTree(-50,50,0.15)
		self.drawTree(200, -300, 0.6)
		self.drawTree(-200, -200, 0.4)
		turtle.getcanvas().postscript(file='drawLandscape.ps', colormode = 'color')

def main():
	screen = Screen()
	screen.colormode(255)
	draw = MyDrawing()
	draw.drawImage()
	done()
	#draw.drawSquare(100)

if __name__ == '__main__':
	main()