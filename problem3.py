from turtle import *

bean = Turtle()

bean.color("blue")
bean.pensize(5)
bean.speed(9)
bean.shape("turtle")

def drawHex(side):
	for x in range(6):
			bean.forward(side)
			bean.left(60)

for y in range(25,1000,25):
	drawHex(y)

mainloop()