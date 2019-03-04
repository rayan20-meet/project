from turtle import *
import random
import math
from blast import Blast
from shoot import Shoot
from tal_maya_ball_blast import Ball
import time
import turtle


turtle.hideturtle()

bg = turtle.Screen()
bg.setup(800,800)
bg.bgpic("/home/student/Desktop/space-game-background.v1.gif")
turtle.bgpic("/home/student/Desktop/space-game-background.v1.gif")


tracer(0,2)
frame = 1
shots=[]
running = True
blast_1= Blast(-200,-300,70)
def movearound():
	blast_1.goto(getcanvas().winfo_pointerx() - screen_width*2, -300)
	x = blast_1.pos()[0]
	y = blast_1.pos()[1] + blast_1.r - 0.5
	if frame % 10 == 0:
		shoot = Shoot(x, y, 10)
		shots.append(shoot)

screen_width = getcanvas().winfo_width()/2
screen_height = getcanvas().winfo_height()/2
first_r = 100
first_y = (screen_height - first_r )- 10								
first_x = random.randint(-screen_width + first_r+3, screen_width-first_r-3)

first_ball = Ball(first_x, first_y, first_r, 0, color)
Ball.Balls.append(first_ball)
# b = (screen_height*2 + 5)/math.fabs(dy)

def collide(shoot_a, ball_a):
	if shoot_a is ball_a:
		return False
	d= math.sqrt(math.pow(shoot_a.pos()[0]-ball_a.pos()[0],2)+math.pow(shoot_a.pos()[1]-ball_a.pos()[1],2))
	if shoot_a.r+ball_a.r<= d:
		return False 
	else:
		print(len(Ball.Balls))
		return True

#import threading

# def instantiateBall():
#   threading.Timer(2.0, instantiateBall).start()
#   new_ball = Ball(first_x, first_y, first_r, 0)
#   Ball.Balls.append(new_ball)

# instantiateBall()

while running:
	first_r = 100
	first_y = (screen_height - first_r )- 10
	first_x = random.randint(-screen_width + first_r+3, screen_width-first_r-3)
	movearound()
	for shoot in shots:
		shoot.move()
	for b in Ball.Balls:
		b.move(screen_width, screen_height)	
		for shoot_a in shots:
			if collide(shoot_a, b):
				print("collision")
				b.split()
				if b in Ball.Balls:
					Ball.Balls.remove(b)
				b.reset()
				shoot_a.reset()
				shots.remove(shoot_a)
			if shoot_a.ycor()  >= screen_height:
				shots.remove(shoot_a)
				del shoot_a



	frame += 1
	time.sleep(0.001)
	update()

	
turtle.mainloop()