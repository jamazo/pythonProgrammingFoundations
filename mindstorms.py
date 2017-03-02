import turtle
def draw_square(some_turtle):
	for i in range (0, 4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_triangle(some_turtle):
	for i in range (0, 3):
		some_turtle.forward(100)
		some_turtle.left(120)

def draw_shapes():

	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("white")
	draw_square(brad)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("black")
	angie.circle(100)

	pedro = turtle.Turtle()
	pedro.shape("arrow")
	pedro.color("blue")
	draw_triangle(pedro)



	window.exitonclick()

draw_shapes()