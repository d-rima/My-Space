import turtle
tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)

def rotate_right():
    current_heading = tim.heading()
    tim.setheading(current_heading + 5)

def rotate_left():
    current_heading = tim.heading()
    tim.setheading(current_heading - 5)

screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.onkey(key = "Right", fun = rotate_right)
screen.onkey(key = "Left", fun = rotate_left)







screen.exitonclick()