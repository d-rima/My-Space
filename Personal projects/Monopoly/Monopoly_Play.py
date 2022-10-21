from distutils.command.build import build
from pickletools import read_int4, read_uint1
import random
from tokenize import ContStr
import pyodbc

Game = 0

runthroughs = input("How many games: ")

property_data = []

# Connect to SQL server 
cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'Monopoly')
cursor = cnxn.cursor()

def play_game(Game):
    # Establish all of the spaces that can be landed on it numerical order
    squares = ['Go', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Chance', 'Vermont Avenue', 'Connecticut Avenue', 'Jail / Just Visiting', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue', 'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance', 'Indiana Avenue', 'Illinois Avenue', 'B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Community Chest', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']
    available_properties = ['Mediterranean Avenue', 'Baltic Avenue', 'Reading Railroad', 'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Tennessee Avenue', 'New York Avenue', 'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue', 'B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']
    is_property = ['Mediterranean Avenue', 'Baltic Avenue', 'Reading Railroad', 'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Tennessee Avenue', 'New York Avenue', 'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue', 'B. & O. Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk']

# Establishes a class to create all of the property information
    class property:
        def __init__(self, name, set, set_no, space, cost, house_cost, rent, rent1, rent2, rent3, rent4, rent5, mortgage, houses):
            self.name = name
            self.set = set
            self.set_no = set_no
            self.space = space
            self.cost = cost 
            self.house_cost = house_cost
            self.rent = rent
            self.rent1 = rent1
            self.rent2 = rent2
            self.rent3 = rent3
            self.rent4 = rent4
            self.rent5 = rent5
            self.mortgage = mortgage
            self.houses = houses

# 0-1 Brown property info
    property_data.append(property("Mediterranean Avenue", "brown", 2, 2, 60, 50, 2, 10, 30, 90, 160, 250, 30, 0))
    property_data.append(property("Baltic Avenue", "brown", 2, 4, 60, 50, 4, 20, 60, 180, 320, 450, 30, 0))

# 2-4 Light blue property info
    property_data.append(property("Oriental Avenue", "light blue", 3, 7, 100, 50, 6, 30, 90, 270, 400, 550, 50, 0))
    property_data.append(property("Vermont Avenue", "light blue", 3, 9, 100, 50, 6, 30, 90, 270, 400, 550, 50, 0))
    property_data.append(property("Connecticut Avenue", "light blue", 3, 10, 120, 50, 8, 40, 100, 300, 450, 600, 60, 0))

# 5-7 Pink property info
    property_data.append(property('St. Charles Place', "pink", 3, 12, 140, 100, 10, 50, 150, 450, 625, 750, 70, 0))
    property_data.append(property('States Avenue', "pink", 3, 14, 140, 100, 10, 50, 150, 450, 625, 750, 70, 0))
    property_data.append(property('Virginia Avenue', "pink", 3, 15, 160, 100, 12, 60, 180, 500, 700, 900, 80, 0))

# 8-10 Orange property info
    property_data.append(property('St. James Place', "orange", 3, 17, 180, 100, 14, 70, 200, 550, 750, 950, 90, 0))
    property_data.append(property('Tennessee Avenue', "orange", 3, 19, 180, 100, 14, 70, 200, 550, 750, 950, 90, 0))
    property_data.append(property('New York Avenue', "orange", 3, 20, 200, 100, 16, 80, 220, 600, 800, 1000, 100, 0))

# 11-13 Red property info
    property_data.append(property('Kentucky Avenue', "red", 3, 22, 220, 150, 18, 90, 250, 700, 875, 1050, 110, 0))
    property_data.append(property('Indiana Avenue', "red", 3, 24, 220, 150, 18, 90, 250, 700, 875, 1050, 110, 0))
    property_data.append(property('Illinois Avenue', "red", 3, 25, 240, 150, 20, 100, 300, 750, 925, 1100, 120, 0))

# 14-16 Yellow property info
    property_data.append(property('Atlantic Avenue', "yellow", 3, 27, 260, 150, 22, 110, 330, 800, 975, 1150, 130, 0))
    property_data.append(property('Ventnor Avenue', "yellow", 3, 28, 260, 150, 22, 110, 330, 800, 975, 1150, 130, 0))
    property_data.append(property('Marvin Gardens', "yellow", 3, 30, 280, 150, 24, 120, 360, 850, 1025, 1200, 140, 0))

# 17-19 Green property info
    property_data.append(property('Pacific Avenue', "green", 3, 32, 300, 200, 26, 130, 390, 900, 1100, 1275, 150, 0))
    property_data.append(property('North Carolina Avenue', "green", 3, 33, 300, 200, 26, 130, 390, 900, 1100, 1275, 150, 0))
    property_data.append(property('Pennsylvania Avenue', "green", 3, 35, 320, 200, 28, 150, 450, 1000, 1200, 1400, 160, 0))

# 20-21 Dark blue property info
    property_data.append(property('Park Place', "dark blue", 2, 38, 350, 200, 35, 175, 500, 1100, 1300, 1500, 175, 0))
    property_data.append(property('Boardwalk', "dark blue", 2, 40, 400, 200, 50, 200, 600, 1400, 1700, 2000, 200, 0))

# 22-24 Railroad info
    property_data.append(property('Reading Railroad', "railroad", 10, 6, 200, 0, 25, 50, 100, 200, 0, 0, 100, 0))
    property_data.append(property('Pennsylvania Railroad', "railroad", 10, 16, 200, 0, 25, 50, 100, 200, 0, 0, 100, 0))
    property_data.append(property('B. & O. Railroad', "railroad", 10, 26, 200, 0, 25, 50, 100, 200, 0, 0, 100, 0))
    property_data.append(property("Short Line", "railroad", 10, 36, 200, 0, 25, 50, 100, 200, 0, 0, 100, 0))

# 25-26 Utility info
    property_data.append(property('Electric Company', "utility", 10, 13, 150, 0, 0, 0, 0, 0, 0, 0, 75, 0))
    property_data.append(property('Water Works', "utility", 10, 29, 150, 0, 0, 0, 0, 0, 0, 0, 75, 0))



    dice_rolls = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12 ]

    player_position = 1
    player_position2 = 1
    player_position3 = 1

    get_out_free = 0
    get_out_free2 = 0
    get_out_free3 = 0

    p1_cash = 1500
    p2_cash = 1500
    p3_cash = 1500

    p1_sets = []
    p2_sets =[]
    p3_sets = []
    all_sets = p1_sets + p2_sets + p3_sets

    p1_buildings = [0, 0]
    p2_buildings = [0, 0]
    p3_buildings = [0, 0]

    p1_properties = []
    p2_properties = []
    p3_properties = []

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
    def special_square(place_position, player_position, Chance_count, Chest_count, money, free_jail, buildings):
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
            if Chance_card == 11:
                money += 50
                return player_position
            if Chance_card == 12:
                free_jail += 1
                return player_position
            if Chance_card == 13:
                House_cost = (25 * buildings[0])
                Hotel_cost = (100 * buildings[1])
                Total_cost = (House_cost + Hotel_cost)
                money -= Total_cost
                return player_position
            if Chance_card == 14:
                money -= 15
                return player_position
            if Chance_card == 15:
                return player_position
            if Chance_card == 16:
                money += 150
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
            if Chest_card == 3:
                money += 200
                return player_position
            if Chest_card == 4:
                money -= 50
                return player_position
            if Chest_card == 5:
                money += 50
                return player_position
            if Chest_card == 6:
                free_jail += 1
                return player_position
            if Chest_card == 7:
                money += 100
                return player_position
            if Chest_card == 8:
                money += 20
                return player_position
            if Chest_card == 9:

                return player_position
            if Chest_card == 10:
                money += 100
                return player_position
            if Chest_card == 11:
                money -= 100
                return player_position
            if Chest_card == 12:
                money -= 50
                return player_position
            if Chest_card == 13:
                money += 25
                return player_position
            if Chest_card == 14:
                House_cost = (40 * buildings[0])
                Hotel_cost = (115 * buildings[1])
                Total_cost = (House_cost - Hotel_cost)
                money -= Total_cost
                return player_position
            if Chest_card == 15:
                money += 10
                return player_position
            if Chest_card == 16:
                money += 100
                return player_position
        return player_position

# Function to determine and return the cost of a property, when it gets landed on
    def property_cost(place_position, property_data):
        for item in property_data:
            if item.name == place_position:
                return item.cost

# Function to determine whether a property is a part of a completed set
    def is_set(property_data, p1_properties, p2_properties, p3_properties, p1_sets, p2_sets, p3_sets):
        colors1 = []
        colors2 = []
        colors3 = []
        for item in property_data:
            if item.name in p1_properties:
                colors1.append(item.set)
            if item.name in p2_properties:
                colors2.append(item.set)
            if item.name in p3_properties:
                colors3.append(item.set)
            if colors1.count(item.set) == item.set_no:
                if item.set not in p1_sets:
                    p1_sets.append(item.set)
            if colors2.count(item.set) == item.set_no:
                if item.set not in p2_sets:
                    p2_sets.append(item.set)
            if colors3.count(item.set) == item.set_no:
                if item.set not in p3_sets:
                    p3_sets.append(item.set)

# Function to determine the rent payed for landing on any given property
    def rent_cost(place_position, property_data):
        for item in property_data:
            if item.name == place_position:
                if item.houses == 0 and item.set not in all_sets:
                    return item.rent
                if item.houses == 0 and item.set in all_sets:
                    return (item.rent * 2)
                if item.houses == 1:
                    return item.rent1
                if item.houses == 2:
                    return item.rent2
                if item.houses == 3:
                    return item.rent3
                if item.houses == 4:
                    return item.rent4
                if item.houses == 5:
                    return item.rent5

# Define what happens when players have to pay for spaces they land on
    def cash_transactions(player_cash, place_position, available_properties, player_properties, p1_cash, p2_cash, p3_cash):
        if place_position == "Income Tax":
            player_cash -= 200
            return player_cash, player_properties
        if place_position == "Luxury Tax":
            player_cash -= 100
            return player_cash, player_properties
        if place_position in available_properties:
            cost = property_cost(place_position, property_data)
            if (player_cash - cost) > 0:
                player_cash -= cost
                player_properties.append(place_position)
                available_properties.remove(place_position)
                return player_cash, player_properties
        if place_position not in available_properties and place_position in is_property and place_position not in player_properties:
            cost = rent_cost(place_position, property_data)
            player_cash -= cost
            if place_position in p1_properties:
                p1_cash += cost
            elif place_position in p2_properties:
                p2_cash += cost
            elif place_position in p3_properties:
                p3_cash += cost
            return player_cash, player_properties
        return player_cash, player_properties

# Function for players to buy houses
    def buy_houses(property_data, player_cash, player_sets):
        houses_bought = 0
        if 'orange' in player_sets:
            houses_bought = player_cash % 100
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[10].houses < 5 and property_data[10].houses == property_data[8].houses:
                    property_data[10].houses += 1
                if i % 3 == 1 and property_data[9].houses < property_data[10].houses:
                    property_data[9].houses += 1
                if i % 3 == 2 and property_data[8].houses < property_data[9].houses:
                    property_data[8].houses += 1
        if 'red' in player_sets:
            houses_bought = player_cash % 150
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[13].houses < 5 and property_data[13].houses == property_data[11].houses:
                    property_data[13].houses += 1
                if i % 3 == 1 and property_data[11].houses < property_data[13].houses:
                    property_data[11].houses += 1
                if i % 3 == 2 and property_data[12].houses < property_data[11].houses:
                    property_data[12].houses += 1 
        if 'light blue' in player_sets:
            houses_bought = player_cash % 50
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[5].houses < 5 and property_data[5].houses == property_data[3].houses:
                    property_data[5].houses += 1
                if i % 3 == 1 and property_data[4].houses < property_data[5].houses:
                    property_data[4].houses += 1
                if i % 3 == 2 and property_data[3].houses < property_data[5].houses:
                    property_data[3].houses += 1
        if 'yellow' in player_sets:
            houses_bought = player_cash % 150
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[14].houses < 5 and property_data[14].houses == property_data[15].houses:
                    property_data[14].houses += 1
                if i % 3 == 1 and property_data[15].houses < property_data[14].houses:
                    property_data[15].houses += 1
                if i % 3 == 2 and property_data[16].houses < property_data[15].houses:
                    property_data[16].houses += 1
        if 'pink' in player_sets:
            houses_bought = player_cash % 100
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[6].houses < 5 and property_data[6].houses == property_data[8].houses:
                    property_data[6].houses += 1
                if i % 3 == 1 and property_data[8].houses < property_data[6].houses:
                    property_data[8].houses += 1
                if i % 3 == 2 and property_data[7].houses < property_data[8].houses:
                    property_data[7].houses += 1
        if 'dark blue' in player_sets:
            houses_bought = player_cash % 200
            for i in range(houses_bought):
                if i % 2 == 0 and property_data[21].houses < 5 and property_data[21].houses == property_data[20].houses:
                    property_data[21].houses += 1
                if i % 2 == 1 and property_data[20].houses < property_data[21].houses:
                    property_data[20].houses += 1
        if 'green' in player_sets:
            houses_bought = player_cash % 200
            for i in range(houses_bought):
                if i % 3 == 0 and property_data[19].houses < 5 and property_data[19].houses == property_data[17].houses:
                    property_data[19].houses += 1
                if i % 3 == 1 and property_data[17].houses < property_data[19].houses:
                    property_data[17].houses += 1
                if i % 3 == 2 and property_data[18].houses < property_data[17].houses:
                    property_data[18].houses += 1
        if 'brown' in player_sets:
            houses_bought = player_cash % 50
            for i in range(houses_bought):
                if i % 2 == 0 and property_data[2].houses < 5 and property_data[1].houses == property_data[2].houses:
                    property_data[2].houses += 1
                if i % 2 == 1 and property_data[1].houses < property_data[2].houses:
                    property_data[1].houses += 1
        return

    for i in range(30):
        player_position = move(player_position)
        place_position = squares[(player_position - 1)]
        player_position = special_square(place_position, player_position, Chest_count, Chance_count, p1_cash, get_out_free, p1_buildings)
        place_position = squares[(player_position - 1)]
        transaction = cash_transactions(p1_cash, place_position, available_properties, p1_properties, p1_cash, p2_cash, p3_cash)
        p1_cash = transaction[0]
        p1_properties = transaction[1]
        is_set(property_data, p1_properties, p2_properties, p3_properties, p1_sets, p2_sets, p3_sets)
        player_position2 = move(player_position2)
        place_position = squares[(player_position2 - 1)]
        player_position2 = special_square(place_position, player_position2, Chest_count, Chance_count, p2_cash, get_out_free2, p2_buildings)
        place_position = squares[(player_position2 - 1)]
        transaction = cash_transactions(p2_cash, place_position, available_properties, p2_properties, p1_cash, p2_cash, p3_cash)
        p2_cash = transaction[0]
        p2_properties = transaction[1]
        is_set(property_data, p1_properties, p2_properties, p3_properties, p1_sets, p2_sets, p3_sets)
        player_position3 = move(player_position3)
        place_position = squares[(player_position3 - 1)]
        player_position3 = special_square(place_position, player_position3, Chest_count, Chance_count, p3_cash, get_out_free3, p3_buildings)
        place_position = squares[(player_position3 - 1)]
        transaction = cash_transactions(p3_cash, place_position, available_properties, p3_properties, p1_cash, p2_cash, p3_cash)
        p3_cash = transaction[0]
        p3_properties = transaction[1]
        is_set(property_data, p1_properties, p2_properties, p3_properties, p1_sets, p2_sets, p3_sets)

# Performs as many games as the user indicates
for i in range(int(runthroughs)):
    play_game(Game)
    Game += 1

# Commits the actions indicated by the cursor
cnxn.commit()