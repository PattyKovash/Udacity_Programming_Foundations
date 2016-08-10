# Draw geometric shape out of squares

# By PK
# Udacity Programming Foundations
# August 2016

import turtle

def draw_square(turt, width):
	"""
	Takes a Turtle object and integer rep. the width of the
	square as arguments. Draws 1 square. 
	"""
	for i in range(4):
		turt.forward(width)
		turt.right(90)

def draw():
	"""
	Draws a geometric shape out of squares
	"""

	WIDTH = 400
	HEIGHT = 400
	SPEED = 6


	frame = turtle.Screen()
	frame.setup(WIDTH, HEIGHT)
	frame.bgcolor("grey")

	# square turtle
	square = turtle.Turtle()
	square.color("white", "white")
	square.speed(SPEED)
	square.fill(True)
	square.setposition(0, 0)


	for i in range(36):
		draw_square(square, 200)
		square.right(10)


	square.fill(False)	
	frame.exitonclick()

draw()
