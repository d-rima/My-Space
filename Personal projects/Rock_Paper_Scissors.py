import random

def play():
    selection = str(input("Choose rock, paper, or scissors: "))
    computer_selection = random.choice(['rock', 'paper', 'scissors'])
    if selection == computer_selection:
        print("It's a Tie")
        play()
    elif (selection == 'rock' and computer_selection == 'scissors') or (selection == 'paper' and computer_selection == 'rock') or (selection == 'scissors' and computer_selection == 'paper'):
        print("You win")
    else:
        print("You lose")
play()