import turtle

def draw_shapes():

	count = 0
	counter = 0

	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle() #grab a turtle
	brad.shape("triangle")
	brad.color("white")
	brad.speed(2)

	while (count < 4):
		brad.forward(100) #move forward
		brad.right(90) #turns right 90 degrees
		count += 1

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("black")
	angie.circle(100)

	pedro = turtle.Turtle()
	pedro.shape("arrow")
	pedro.color("blue")

	while (counter < 3):
		pedro.forward(100)
		pedro.left(120)

		counter += 1

	window.exitonclick()

draw_shapes()