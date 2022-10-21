import random

board = [
    ['-', '-', '-',],
    ['-', '-', '-',],
    ['-', '-', '-',]
    ]

number_board = [
    ['1', '2', '3',],
    ['4', '5', '6',],
    ['7', '8', '9',]
    ]

winnable_position = False

winning_coords = []

user_choice = 0

length = 0

turn = 0

players = 0

user_first = False

necessary_placement = []

free_corners = []

while players != '1' and players != '2':
    players = input("How many players: ")
    if players != '1' and players != '2':
        print("Invalid number of players")
        continue

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def print_number_board(number_board):
    for row in number_board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

def quit(user_input):
    if user_input.lower() == 'q':
        return True
    else:
        return False

def check_input(user_input):
    if is_numeric(user_input) == False:
        print("Invalid input, try again: ")
        return False
    else:
        return True

def in_bounds(user_input):
        if int(user_input) > 9 or int(user_input) < 1:
            print("Invalid input, try again: ")
            return False
        else:
            return True

def is_numeric(user_input):
    if user_input.isnumeric() == False:
        print("Invalid input, try again: ")
        return False
    else:
        return True

def is_used(coords, board):
    row = coords[0]

    column = coords[1]  
    if board[row][column] != '-':
        print("Location taken, try again: ")
        return True
    else: 
        return False

def coordinates(user_input):
    row = int(user_input / 3)
    column = int(user_input % 3)
    return (row,column)

def add_to_board(coords, board, turn):
    row = coords[0]
    column = coords[1]
    if turn % 2 == 0:
        board[row][column] = 'O'
    else:
        board[row][column] = 'X'

def is_winner(board):
    winner = False
    for i in range(3):
        if board[i][0] != "-" and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            print_board(board)
            print(f"{board[i][0]} player has won")
            winner = True
        elif board[0][i] != "-" and board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            print_board(board)
            print(f"{board[0][i]} player has won")
            winner = True
        elif board[0][0] != "-" and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            print_board(board)
            print(f"{board[0][0]} player has won")
            winner = True
        elif board[2][0] != "-" and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            print_board(board)
            print(f"{board[2][0]} player has won")
            winner = True
        else:
            continue
        return winner

def is_tie():
    tie = False
    if turn > 8:
        print('You tied')
        tie = True
    else:
        tie = False
    return tie

def single_player_turn_order():
    player_turn = random.randint(1,2)
    if player_turn == 1:
        return True
    else:
        return False

def is_corner_taken(board): 
    if board[0][0] == '-':
        free_corners.append(1)
    if board[2][0] == '-':
        free_corners.append(7)
    if board[0][2] == '-':
        free_corners.append(3)
    if board[2][2] == '-':
        free_corners.append(9)
    return free_corners

def can_player_win(board, necessary_placement, Order):
    if Order == True:
        for i in range(3):
            if board[i][0] == 'X' and board[i][0] == board[i][1] or board[i][0] == 'X' and board[i][0] == board[i][2] or board[i][1] == 'X' and board[i][1] == board[i][2]:
                for k in range(3):
                    if board[i][k] == '-':
                        necessary_placement = [i, k]
                        return necessary_placement
        for j in range(3):
            if board[0][j] == 'X' and board[0][j] == board[1][j] or board[0][j] == 'X' and board[0][j] == board[2][j] or board[1][j] == 'X' and board[1][j] == board[2][j]:
                for k in range(3):
                    if board[k][j] == '-':
                        necessary_placement = [k, j]
                        return necessary_placement
        if board[0][0] == 'X' and board[0][0] == board [1][1] or board[0][0] == 'X' and board[0][0] == board[2][2] or board[1][1] == 'X' and board[1][1] == board[2][2]:
            for i in range(3):
                if board[i][i] == '-':
                    necessary_placement = [i, i]
                    return necessary_placement
        if board[2][0] == 'X' and board[2][0] == board [1][1] or board[2][0] == 'X' and board[2][0] == board[0][2] or board[1][1] == 'X' and board[1][1] == board[0][2]:
            if board[2][0] == '-':
                necessary_placement = [2, 0]
                return necessary_placement
            if board[1][1] == '-':
                necessary_placement = [1, 1]
                return necessary_placement
            if board[0][2] == '-':
                necessary_placement = [0, 2]
                return necessary_placement
    if Order == False:
        for i in range(3):
            if board[i][0] == 'O' and board[i][0] == board[i][1] or board[i][0] == 'O' and board[i][0] == board[i][2] or board[i][1] == 'O' and board[i][1] == board[i][2]:
                for k in range(3):
                    if board[i][k] == '-':
                        necessary_placement = [i, k]
                        return necessary_placement
        for j in range(3):
            if board[0][j] == 'O' and board[0][j] == board[1][j] or board[0][j] == 'O' and board[0][j] == board[2][j] or board[1][j] == 'O' and board[1][j] == board[2][j]:
                for k in range(3):
                    if board[k][j] == '-':
                        necessary_placement = [k, j]
                        return necessary_placement
        if board[0][0] == 'O' and board[0][0] == board [1][1] or board[0][0] == 'O' and board[0][0] == board[2][2] or board[1][1] == 'O' and board[1][1] == board[2][2]:
            for i in range(3):
                if board[i][i] == '-':
                    necessary_placement = [i, i]
                    return necessary_placement
        if board[2][0] == 'O' and board[2][0] == board [1][1] or board[2][0] == 'O' and board[2][0] == board[0][2] or board[1][1] == 'O' and board[1][1] == board[0][2]:
            if board[2][0] == '-':
                    necessary_placement = [2, 0]
                    return necessary_placement
            if board[1][1] == '-':
                necessary_placement = [1, 1]
                return necessary_placement
            if board[0][2] == '-':
                necessary_placement = [0, 2]
                return necessary_placement
    if Order == True:
        for i in range(3):
            if board[i][0] == 'O' and board[i][0] == board[i][1] or board[i][0] == 'O' and board[i][0] == board[i][2] or board[i][1] == 'O' and board[i][1] == board[i][2]:
                for k in range(3):
                    if board[i][k] == '-':
                        necessary_placement = [i, k]
                        return necessary_placement
        for j in range(3):
            if board[0][j] == 'O' and board[0][j] == board[1][j] or board[0][j] == 'O' and board[0][j] == board[2][j] or board[1][j] == 'O' and board[1][j] == board[2][j]:
                for k in range(3):
                    if board[k][j] == '-':
                        necessary_placement = [k, j]
                        return necessary_placement
        if board[0][0] == 'O' and board[0][0] == board [1][1] or board[0][0] == 'O' and board[0][0] == board[2][2] or board[1][1] == 'O' and board[1][1] == board[2][2]:
            for i in range(3):
                if board[i][i] == '-':
                    necessary_placement = [i, i]
                    return necessary_placement
        if board[2][0] == 'O' and board[2][0] == board [1][1] or board[2][0] == 'O' and board[2][0] == board[0][2] or board[1][1] == 'O' and board[1][1] == board[0][2]:
            if board[2][0] == '-':
                    necessary_placement = [2, 0]
                    return necessary_placement
            if board[1][1] == '-':
                necessary_placement = [1, 1]
                return necessary_placement
            if board[0][2] == '-':
                necessary_placement = [0, 2]
                return necessary_placement
    if Order == False:
        for i in range(3):
            if board[i][0] == 'X' and board[i][0] == board[i][1] or board[i][0] == 'X' and board[i][0] == board[i][2] or board[i][1] == 'X' and board[i][1] == board[i][2]:
                for k in range(3):
                    if board[i][k] == '-':
                        necessary_placement = [i, k]
                        return necessary_placement
        for j in range(3):
            if board[0][j] == 'X' and board[0][j] == board[1][j] or board[0][j] == 'X' and board[0][j] == board[2][j] or board[1][j] == 'X' and board[1][j] == board[2][j]:
                for k in range(3):
                    if board[k][j] == '-':
                        necessary_placement = [k, j]
                        return necessary_placement
        if board[0][0] == 'X' and board[0][0] == board [1][1] or board[0][0] == 'X' and board[0][0] == board[2][2] or board[1][1] == 'X' and board[1][1] == board[2][2]:
            for i in range(3):
                if board[i][i] == '-':
                    necessary_placement = [i, i]
                    return necessary_placement
        if board[2][0] == 'X' and board[2][0] == board [1][1] or board[2][0] == 'X' and board[2][0] == board[0][2] or board[1][1] == 'X' and board[1][1] == board[0][2]:
            if board[2][0] == '-':
                    necessary_placement = [2, 0]
                    return necessary_placement
            if board[1][1] == '-':
                necessary_placement = [1, 1]
                return necessary_placement
            if board[0][2] == '-':
                necessary_placement = [0, 2]
                return necessary_placement
    return  necessary_placement

def get_computer_input(board, Order):
    sides = [2, 4, 6, 8]
    is_corner_taken(board)
    location = can_player_win(board, necessary_placement, Order)
    if len(location) > 0:
            row = location[0]
            column = location[1]
            winning_coords = (row, column)
            return winning_coords
    if Order == True and board[1][1] == '-':
        user_choice = 5
        return user_choice
    elif Order == True and len(free_corners) == 2 and board[0][0] == 'O' and board[2][2] == 'O' or Order == True and len(free_corners) == 2 and board[0][2] == 'O' and board[2][0] == 'O':
        user_choice = random.choice(sides)
        return user_choice
    elif len(free_corners) > 0:
            user_choice = int(random.choice(free_corners))
            return user_choice
    elif board[1][1] == '-' and len(free_corners) == 0:
            user_choice = 5
            return user_choice
    else:
            user_choice = int(random.choice(sides))
            return int(user_choice)

if players == '2':
    while True:
        print_number_board(number_board)
        print()
        print_board(board)
        user_input = input("Enter a position betwen 1-9, or enter \"q\" to quit: ")
        if quit(user_input) == True:
            exit()
        if check_input(user_input) == False:
            continue
        if in_bounds(user_input) == False:
            continue
        user_input = (int(user_input) - 1)
        coords = coordinates(user_input)
        if is_used(coords, board) == True:
            continue
        else:
            turn = turn + 1
            add_to_board(coords, board, turn)
        if is_winner(board) == True:
            exit()
        if is_tie() == True:
            exit()

Order = single_player_turn_order()
while True:
    if players == '1': 
        if Order == True and turn % 2 == 0:
            print_board(board)
            print()
            print_number_board(number_board)
            user_input = input("Enter a position betwen 1-9, or enter \"q\" to quit: ")
            if quit(user_input) == True:
                break
            if check_input(user_input) == False:
                continue
            if in_bounds(user_input) == False:
                continue
            user_input = (int(user_input) - 1)
            coords = coordinates(user_input)
            if is_used(coords, board) == True:
                continue
            else:
                add_to_board(coords, board, turn)
        if Order == False and turn % 2 == 1:
            print_board(board)
            print()
            print_number_board(number_board)
            user_input = input("Enter a position betwen 1-9, or enter \"q\" to quit: ")
            if quit(user_input) == True:
                break
            if check_input(user_input) == False:
                continue
            if in_bounds(user_input) == False:
                continue
            user_input = (int(user_input) - 1)
            coords = coordinates(user_input)
            if is_used(coords, board) == True:
                continue
            else:
                add_to_board(coords, board, turn)
        if Order == False and turn % 2 == 0:
            length = can_player_win(board, necessary_placement, Order)
            computer_choice = get_computer_input(board, Order)
            if isinstance(computer_choice, int) == True:
                user_input = int(computer_choice - 1)
            if len(length) > 0:
                coords = can_player_win(board, necessary_placement, Order)
            else:
                coords = coordinates(user_input)
            add_to_board(coords, board, turn)
            free_corners.clear()
            necessary_placement.clear()
        if Order == True and turn % 2 == 1:
            length = can_player_win(board, necessary_placement, Order)
            computer_choice = get_computer_input(board, Order)
            if  isinstance(computer_choice, int) == True:
                user_input = int(computer_choice - 1)
            if len(length) > 0:
                coords = can_player_win(board, necessary_placement, Order)
            else:
                coords = coordinates(user_input)
            add_to_board(coords, board, turn)
            free_corners.clear()
            necessary_placement.clear()
    turn = turn +1
    if is_winner(board) == True:
        exit()
    if is_tie() == True:
        exit()