# Learning how to use the Turtle functions

import turtle

def draw_square(some_turtle):
    for loop in range (0,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("yellow")
    brad.speed(10)
    i = 0
    while i < 37:
        draw_square(brad)
        brad.right(10)
        
        angie = turtle.Turtle()
        angie.shape("arrow")
        angie.color("red")

# Let's have a little fun with some math. Putting in a factor of -1 to
# a variable exponent will allow us to create a symmetric mirror.
        
        angie.circle(i*15*(-1)**i)
        angie.speed(2)

        jonny = turtle.Turtle()
        jonny.shape("classic")
        jonny.color("white")
        jonny.speed(2)
        for loop in range (0,3):
            jonny.forward(i*15*(-1)**i)
            jonny.left(120)
        i = i + 1
    window.exitonclick()

draw_shapes()
