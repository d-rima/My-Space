from game_art import logo, vs
from game_data import data
import random

lives = 3

print(logo)
account = ''
previous_winner = []

def random_account():
    account = random.choice(data)
    data.remove(account)
    return account

def write_game(account):
    return(f"{account['name']}, a {account['description']}, from {account['country']}")

def print_comparison(account, previous_winner):
    account = previous_winner
    account_script = []
    followers = []
    accounts = []
    print(len(account))
    if len(account) < 1:
        account = random_account()
    else: 
        account = previous_winner
    accounts.append(account)
    account_script.append(write_game(account))
    followers.append(account["follower_count"])
    print("Compare A: " + account_script[0])
    print(vs)
    account = random_account()
    accounts.append(account)
    account_script.append(write_game(account))
    followers.append(account["follower_count"])
    print("Against B: " + account_script[1])
    return account_script, followers, accounts

def user_choice(accounts):
    choice = 0
    while choice != 'A' and choice != 'B:':
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice == 'A':
            user_selection = accounts[0]["follower_count"]
            letter = 'A'
            return user_selection, letter
        elif choice == 'B':
            user_selection = accounts[1]["follower_count"]
            letter = 'B'
            return user_selection, letter

def play_game(lives, previous_winner):
    previous_winner
    highest_count = 0
    results = print_comparison(account, previous_winner)
    round_data = results[0]
    followers = results[1]
    accounts = results[2]
    user_selection = user_choice(accounts)
    for person in followers:
        if person > highest_count:
            highest_count = person
    if user_selection[0] == highest_count:
        print("That is correct")
        if user_selection[1] == 'A':
            previous_winner = accounts[0]
            return previous_winner, lives
        else:
            previous_winner = accounts[1]
            return previous_winner, lives
    else:
        print("That is incorrect")
        lives -= 1
        print(f"You have {lives} lives left")
        if user_selection[1] == 'A':
            previous_winnesr = accounts[1]
            return previous_winner, lives
        else:
            previous_winner = accounts[0]
            return previous_winner, lives
while lives > 0:
    game = (play_game(lives, previous_winner))
    previous_winner = game[0]
    lives = game[1]