import turtle
import random

screen = turtle.Screen()
screen.setup(width = 600, height = 600)
racer_info = []
colors = ["blue", "red", "yellow", "green", "orange"]
start_positions = [250, 150, 50, -50, -150]

class racer:
    def __init__(self, color, position):
        self.color = color
        self.position = position

def place_bet():
    return (screen.textinput(title = "Make Your Bet", prompt = "Which turtle will win the race? Enter a color"))

def is_winner(user_bet):
    for racer in colors:
        position = racer.xcor()
        if position >= 250 and racer.color == user_bet:
            print(f"The {racer.color()[0]} racer has won. You were right.")
            return True
        elif position >= 250 and racer.color != user_bet:
            print(f"The {racer.color()[0]} racer has won. You were wrong.")
            return True
        else:
            return False

for i in range(5):
    racer_info.append(racer(colors[i], (-250, start_positions[i])))
    colors[i] = turtle.Turtle()
    colors[i].shape("turtle")
    colors[i].color(racer_info[i].color)
    colors[i].penup()
    colors[i].goto(racer_info[i].position)
user_bet = place_bet()

while is_winner(user_bet) == False:
    random.shuffle(colors)
    for racer in colors:
        distance = random.randint(5, 20)
        racer.forward(distance)
        if racer.xcor() >= 250:
            continue


screen.exitonclick()



