import turtle
from turtle import *

class Shoot(Turtle):
	def __init__(self, x,y,r):
		Turtle.__init__(self)
		self.hideturtle()
		self.pu()
		self.dy= 15
		self.x= x
		self.y= y
		self.r=r
		self.shape("circle")
		self.color("red")
		self.shapesize(1)
		self.goto(x,y)
		self.showturtle()
	def move(self):
		current_y = self.ycor()
		new_y = current_y + self.dy
		self.goto(self.xcor(),new_y)


	

	
