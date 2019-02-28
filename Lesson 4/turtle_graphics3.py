from turtle import *
import random
freddy = Turtle()

freddy.color("red")
freddy.pensize(3)
freddy.speed(0)
freddy.shape("turtle")
freddy.turtlesize(2)

def drawHexagon():
	for x in range(6):
		freddy.forward(50)
		freddy.left(60)

drawHexagon()

mainloop()