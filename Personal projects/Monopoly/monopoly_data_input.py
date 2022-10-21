import random
import pyodbc

Game = 0

runthroughs = input("How many games: ")

# Connect to SQL server 
cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'Monopoly')
cursor = cnxn.cursor()

def play_game(Game):
    # Establish all of the spaces that can be landed on it numerical order
    squares = ['Go', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Chance', 'Vermont Avenue', 'Connecticut Avenue', 'Jail / Just Visiting', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue', 'Illinois Avenue', 'B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']

    dice_rolls = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12 ]

    player_position = 1
    player_position2 = 1
    player_position3 = 1

    Chance_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    Chest_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


    def move(player_position):
        roll = random.choice(dice_rolls)
        player_position = (player_position + roll)
        print(roll)
        if player_position > 40:
            player_position -= 40
        return player_position

    # What the computer does with squares that have a chance to change the player's position
    def special_square(place_position, player_position, Chance_count, Chest_count):
        if place_position == 'Go To Jail':
            player_position = 11
            print('moved')
            return player_position

        if place_position == 'Chance':
            Chance_card = random.choice(Chance_count)
            Chance_count.remove(Chance_card)
            if len(Chance_count) == 0:
                Chance_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            if Chance_card == 1:
                player_position = 40
                print('moved')
                return player_position
            if Chance_card == 2:
                player_position = 1
                print('moved')
                return player_position
            if Chance_card == 3:
                player_position = 25
                print('moved')
                return player_position
            if Chance_card == 4:
                player_position = 12
                print('moved')
                return player_position
            if Chance_card == 5 or Chance_card == 6:
                if player_position < 6 or player_position > 36:
                    player_position = 6
                    print('moved')
                    return player_position
                elif player_position > 6 and player_position < 16:
                    player_position = 16
                    print('moved')
                    return player_position
                elif player_position > 16 and player_position < 26:
                    player_position = 26
                    print('moved')
                    return player_position
                else:
                    player_position = 36
                    print('moved')
                    return player_position
            if Chance_card == 7:
                if player_position < 13 or player_position > 29:
                    player_position = 13
                    print('moved')
                    return player_position
                else:
                    player_position = 29
                    print('moved')
                    return player_position
            if Chance_card == 8:
                player_position = 11
                print('moved')
                return player_position
            if Chance_card == 9:
                player_position = (player_position - 3)
                print('moved')
                return player_position
            if Chance_card == 10:
                player_position = 6
                print('moved')
                return player_position

        if place_position == 'Community Chest':
            Chest_card = random.choice(Chest_count)
            Chest_count.remove(Chest_card)
            if len(Chest_count) == 0:
                Chest_count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            if Chest_card == 1:
                player_position = 1
                return player_position
            if Chest_card == 2:
                player_position = 11
                return player_position
        return player_position

    for i in range(30):
        player_position = move(player_position)
        place_position = squares[(player_position - 1)]
        player_position = special_square(place_position, player_position, Chest_count, Chance_count)
        place_position = squares[(player_position - 1)]
        cursor.execute(f"INSERT INTO Game(GameID, Move, SpaceID, Landing) VALUES({Game + 1}, {i + 1}, {(player_position)}, '{place_position}')")
        player_position2 = move(player_position2)
        place_position = squares[(player_position2 - 1)]
        player_position2 = special_square(place_position, player_position2, Chest_count, Chance_count)
        place_position = squares[(player_position2 - 1)]
        cursor.execute(f"INSERT INTO Game(GameID, Move, SpaceID, Landing) VALUES({Game + 1}, {i + 1}, {(player_position2)}, '{place_position}')")
        player_position3 = move(player_position3)
        place_position = squares[(player_position3 - 1)]
        player_position3 = special_square(place_position, player_position3, Chest_count, Chance_count)
        place_position = squares[(player_position3 - 1)]
        cursor.execute(f"INSERT INTO Game(GameID, Move, SpaceID, Landing) VALUES({Game + 1}, {i + 1}, {(player_position3)}, '{place_position}')")

# Performs as many games as the user indicates
for i in range(int(runthroughs)):
    play_game(Game)
    cursor.execute(f"INSERT INTO GameID(Game_Number) VALUES({i + 1})")
    Game += 1

# Commits the actions indicated by the cursor
cnxn.commit()

