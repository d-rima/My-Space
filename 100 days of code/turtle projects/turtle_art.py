import turtle
import random

random_colors = ["red", "blue", 'green', 'orange', 'yellow', 'violet']
my_turtle = turtle.Turtle()
turtle.colormode(255)
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.speed("fastest")

shapes = [[3, 120], [4, 90], [5, 72], [6, 60], [7, 51.5], [8, 45], [9, 40], [10, 36]]
direccions = [0, 90, 180, 270]

def make_shape(sides, angle):
    color = random.choice(random_colors)
    my_turtle.color(color)
    for i in range(sides):
        my_turtle.forward(50)
        my_turtle.right(angle)

def perform_random():
    my_turtle.pensize(15)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.color(color)
    direccion = random.choice(direccions)
    my_turtle.setheading(direccion)
    my_turtle.forward(30)

def spirograph():
    my_turtle.circle(100)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.color(color)
    current_heading = my_turtle.heading()
    my_turtle.setheading(current_heading + 2)

def painting():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.color(color)
    my_turtle.pensize(15)
    my_turtle.forward(.1)
    my_turtle.penup()
    my_turtle.forward(30)
    my_turtle.pendown()

my_turtle.penup()
my_turtle.goto(-250, 250)
my_turtle.pendown()
for i in range(5):
    for i in range(16):
        painting()
    my_turtle.setheading(270)
    my_turtle.forward(.1)
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.pendown()
    my_turtle.setheading(180)
    for i in range(16):
        painting()
    my_turtle.setheading(270)
    my_turtle.forward(.1)
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.setheading(0)
    my_turtle.pendown()
for i in range(16):
    painting()













screen = turtle.Screen()
screen.exitonclick()