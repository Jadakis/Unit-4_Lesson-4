from turtle import *
import random
worf = Turtle()

worf.color("brown")
worf.pensize(3)
worf.speed(0)
worf.shape("turtle")
worf.turtlesize(2)

def drawSquare():
	for x in range(2):
		worf.forward(50)
		worf.left(90)
		worf.forward(50)
		worf.left(90)
		worf.forward(50)
		worf.left(90)
		worf.forward(50)
		worf.left(90)

drawSquare()

mainloop()