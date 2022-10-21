from flask import Flask
import random


random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def play_game():
    return "<h1>Guess a number between 0 and 9<h1>" \
            "<img src='https://media.giphy.com/media/YGz18JiFxv8Zy/giphy.gif'/>"


@app.route("/<int:guess>")
def check_guess(guess):
    if guess > random_number:
        return "<h3>Too high! Guess again!<h3>" \
                "<img src='https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif'>"
    if guess < random_number:
        return "<h3>Too low! Guess again!<h3>" \
                "<img src='https://media.giphy.com/media/rS2uLYRGkGWySNX69v/giphy.gif'>"
    if guess == random_number:
        return f"<h3>You guessed it! The number was {guess}!<h3>" \
                "<img src='https://media.giphy.com/media/TW27HaGFc5mu1i1ByX/giphy.gif'>"


if __name__ == "__main__":
    app.run()