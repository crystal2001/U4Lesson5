from turtle import *

bean = Turtle()

bean.color("blue")
bean.pensize(5)
bean.speed(9)
bean.shape("turtle")

def drawTriangle():
	for x in range(3):
		bean.forward(100)
		bean.left(120)

for x in range(12):
	drawTriangle()
	bean.left(30)

mainloop()