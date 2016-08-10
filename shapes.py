# Draw geometric shapes

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

def draw_triangle(turt, side_len):
	"""
	Takes a Turtle object and int as an argument.
	Draws 1 equilateral triangle with side_len length. 
	"""

	for i in range(3):
		turt.forward(side_len)
		turt.right(120)

def draw_circle(turt, rad):
	"""
	Takes a Turtle object and draws a circle with radius rad.
	"""
	turt.circle(rad)

def rotate(turt, draw_func, size, rot_num):
	"""
	Takes as arguments a Turtle object, draw function, int for size, 
	and int between 1 - 36 rep. number of rotations. Draws shape and
	rotates Turtle object rot_num times. 
	"""
	for i in range(rot_num):
		draw_func(turt, size)
		turt.left(10)
		
def draw():
	"""
	Draws a geometric shape.
	"""

	WIDTH = 400
	HEIGHT = 400
	SPEED = 10


	frame = turtle.Screen()
	frame.setup(WIDTH, HEIGHT)
	frame.bgcolor("grey")

	# # square turtle
	# square = turtle.Turtle()
	# square.color("white", "white")
	# square.speed(SPEED)
	# square.fill(True)
	# square.setposition(0, 0)
	# rotate(square, draw_square, 100, 36)

	# # triangle turtle
	# triangle = turtle.Turtle()
	# triangle.color("white", "white")
	# triangle.speed(SPEED)
	# triangle.setposition(0, 0)
	# rotate(triangle, draw_triangle, 100, 36)

	# circle turtle
	circle = turtle.Turtle()
	circle.color("white", "white")
	circle.speed(SPEED)
	circle.fill(True)
	circle.setposition(0, 0)
	rotate(circle, draw_circle, 100, 36)

	# square.fill(False)	
	frame.exitonclick()

draw()
