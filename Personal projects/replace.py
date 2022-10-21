property_data = []

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

property_data[10].houses += 1
print(property_data[10].houses)