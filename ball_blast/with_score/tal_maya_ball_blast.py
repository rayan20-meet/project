from turtle import*
import random
import math 
#fix colorssssssssssssssssssss!!!!!!!!!!!!!


class Ball(Turtle):
	Balls = []
	first_count=10
	screen_width = getcanvas().winfo_width()/2
	screen_height = getcanvas().winfo_height()/2
	first_r = 100
	first_y = (screen_height - first_r )- 10								
	first_x = random.randint(-screen_width + first_r+3, screen_width-first_r-3)
	def __init__(self,x,y,r, one_0, color):
		color = (random.random(), random.random(), random.random())
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		
		dx = 0
		while dx == 0:
			dx = random.randint(-400, 500)
		
		dy = 0
		while dy == 0:
			dy = random.randint(-100,0)

		self.dx = dx / 100
		self.dy = dy / 100
		self.r = r
		self.one_0 = one_0
		self.color(color)
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(math.sqrt(r))
  
	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		current_y = self.ycor()
		new_y = current_y + self.dy
		new_x = current_x + self.dx
		self.goto(new_x,new_y)

		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		up_side_ball = new_y + self.r
		down_side_ball = new_y - self.r

		if right_side_ball > screen_width:
			self.dx = -self.dx

		if left_side_ball < -screen_width:
			self.dx = -self.dx
		
		if down_side_ball <= -screen_height:
			print("game over!!!")
			quit()

	def split(self):
		if self.r > 10 and self.one_0 is 0: #disappear if too small
			ball1 = Ball(self.xcor()-50, self.ycor()-50, self.r/2, 1, self.color)
			Ball.Balls.append(ball1)
			ball2 = Ball(self.xcor()+50, self.ycor()-50, self.r/2, 1, self.color)
			Ball.Balls.append(ball2)
			screen_width = getcanvas().winfo_width()/2
			screen_height = getcanvas().winfo_height()/2
			first_r = 100
			first_y = (screen_height - first_r )- 10								
			first_x = random.randint(-screen_width + first_r+3, screen_width-first_r-3)
			color = (random.random(), random.random(), random.random())
			new_ball = Ball(first_x, first_y, first_r, 0, color)
			Ball.Balls.append(new_ball)


# first_ball = Ball(first_x, first_y, dx, dy, first_r, first_count)
# Balls.append(first_ball)
# b = (screen_height*2 + 5)/math.fabs(dy)
# for i in range((int)(b)):
#     for a in Balls:
#         print(int(a.ycor()))
#         if (int(a.ycor()) == 0):
#             ball3 = Ball(first_x, first_y, dx, dy, first_r, first_count)
#             Balls.append(ball3)
#             a.split(a)
#             a.reset()
#     for b in Balls:
#         b.move(screen_width, screen_height)
#     update()





