from turtle import *

data = Turtle()

data.color("gold")
data.pensize(2)
data.speed(0)
data.shape("turtle")
data.turtlesize(3)

for x in range(12):
	# original shape
	data.forward(80)
	data.forward(100)	
	data.left(50)

	data.right(150)
	data.forward(50)
	data.circle(25)

mainloop()