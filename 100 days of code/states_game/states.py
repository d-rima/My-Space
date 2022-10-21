import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "100 days of code/states_game/download.gif"
screen.addshape(image)

data = pandas.read_csv("100 days of code/states_game/fifty_states.csv")

states = data["state"].tolist()

guessed_states = []

def show_name(state):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    state_data = data[data.state == state]
    text.goto(int(state_data["x"]), int(state_data["y"]))
    text.write(f"{state}", align = "left", font = ("Calibri", 11, "normal"))

turtle.shape(image)

def guess_state():
    answer = screen.textinput(title = "Guess the State", prompt="What's another state's name?")
    if answer == "exit":
        terminate()
    answer = answer.upper()
    for state in states:
        if answer == state.upper():
            show_name(state)
            guessed_states.append(state)

def terminate():
    unanswered = []
    for state in states:
        if state not in guessed_states:
            unanswered.append(state)
    new_data = pandas.DataFrame(unanswered)
    new_data.to_csv("100 days of code/states_game/missing_states.csv")
    quit()

while True:
    guess_state()


screen.exitonclick()

