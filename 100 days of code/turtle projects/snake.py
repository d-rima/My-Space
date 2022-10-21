import turtle
import random
import time

is_going = True

snake_segments = []

segment_positions = []

class part:
    def __init__(self, number, color, position, pen):
        part.number = number
        part.color = color
        part.position = position
        part.pen = pen

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))
        self.hideturtle()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))

scoreboard = Scoreboard()

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.tracer(0)
screen.listen()


food = turtle.Turtle()
food.color("yellow")
food.shape("circle")
food.penup()
food.goto(100, 100)

snake1 = turtle.Turtle()


snake2 = turtle.Turtle()
snake2.goto(-20, 0)

snake3 = turtle.Turtle()
snake3.goto(-40, 0)

snake_segments.append(snake1)
snake_segments.append(snake2)
snake_segments.append(snake3)

for segment in snake_segments:
    segment.penup()
    segment.shape("square")
    segment.color("white")

screen.update()

def turn_snake_up():
    if snake_segments[0].heading != 270:
        snake_segments[0].setheading(90)

def turn_snake_down():
    if snake_segments[0].heading != 90:
        snake_segments[0].setheading(270)

def turn_snake_right():
    if snake_segments[0].heading != 180:
        snake_segments[0].setheading(0)

def turn_snake_left():
    if snake_segments[0].heading != 0:
        snake_segments[0].setheading(180)

def eat_food():
    if snake_segments[0].distance(food) <= 30:
        food.hideturtle()
        randomX = random.randint(-270, 270)
        randomY = random.randint(-270, 270)
        food.goto(randomX, randomY)
        food.showturtle()
        add_segment()
        scoreboard.increase_score()


def add_segment():
    segment = turtle.Turtle()
    segment.hideturtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    segment.goto(segment_positions[(len(segment_positions) - 1)])
    segment.showturtle()
    snake_segments.append(segment)

def game_over():
    ycor = snake_segments[0].ycor()
    xcor = snake_segments[0].xcor()
    if ycor >= 280 or xcor >= 280 or ycor < -280 or xcor < -280:
        return True
    for i in range(len(snake_segments)):
        if snake_segments[0].distance((snake_segments[i])) == 0 and i != 0:
            return True

while is_going == True:
    time.sleep(.1)
    for i in range(len(snake_segments)):
        segment_positions.append(snake_segments[i].pos())
    for i in range(len(snake_segments)):
        if i == 0:
            snake_segments[i].forward(30)
            eat_food()
            if game_over() == True:
                is_going = False
            screen.update()
            screen.onkey(key="Up", fun = turn_snake_up)
            screen.onkey(key="Down", fun = turn_snake_down)
            screen.onkey(key="Right", fun = turn_snake_right)
            screen.onkey(key="Left", fun = turn_snake_left)
        else:
            snake_segments[i].goto(segment_positions[i-1])
            screen.update()
            screen.onkey(key="Up", fun = turn_snake_up)
            screen.onkey(key="Down", fun = turn_snake_down)
            screen.onkey(key="Right", fun = turn_snake_right)
            screen.onkey(key="Left", fun = turn_snake_left)
    segment_positions = []









screen.exitonclick()