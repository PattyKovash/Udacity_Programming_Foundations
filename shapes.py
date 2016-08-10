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
		
def draw(draw_func, size, color, speed, x_pos, y_pos, num_rotate):
	"""
	Draws a geometric shape.
	"""

	WIDTH = 400
	HEIGHT = 400
	SPEED = 10


	frame = turtle.Screen()
	frame.setup(WIDTH, HEIGHT)
	frame.bgcolor("grey")

	shape = turtle.Turtle()
	shape.color(color, color)
	shape.speed(SPEED)
	shape.setposition(x_pos, y_pos)
	rotate(shape, draw_func, size, num_rotate)

	frame.exitonclick()

draw(draw_square, 100, "white", 10, 0, 0, 36)
