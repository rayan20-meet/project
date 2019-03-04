import turtle
from turtle import *




class Blast(Turtle):
	def __init__(self, x,y,r):
		Turtle.__init__(self)
		self.x= x
		self.y= y
		self.r= r
		self.shape("circle")
		self.shapesize(r/10)
		self.pu()
		self.goto(x,y)

	
