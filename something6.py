from turtle import *

bean = Turtle()

bean.color("black")
bean.pensize(5)
bean.speed(9)
bean.shape("turtle")

def drawStar():
	for x in range(5):
		bean.forward(50)
		bean.left(144)

def row():
	for x in range(3):
		drawStar()
		bean.penup()
		bean.forward(70)
		bean.pendown()

def drawGrid():
	for y in range(4):
		row()
		bean.penup()
		bean.backward(210)
		bean.right(90)
		bean.forward(60)
		bean.left(90)
		bean.pendown()



	

mainloop()
