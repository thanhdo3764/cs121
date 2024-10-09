import turtle
from turtle import *

def triangle(l):
	for i in range(3):
		forward(l)
		left(120)

triangle(500)
turtle.getcanvas().postscript(file='art.ps', colormode='color')