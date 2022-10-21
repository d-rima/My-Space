MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def take_order(MENU, resources, profit):
    while True:
        payment = 0
        order = input("What would you like to drink? (espresso, latte, cappuccino): ")

        if order == 'resources':
            print(resources)

        if order == 'profit':
            print(profit)

        if order == 'espresso' or order == 'latte' or order == 'cappuccino':
            if resources["water"] < MENU[order]["ingredients"]["water"]:
                print("Insuffiecient resources, not enough water.")
                continue
            if 'milk' in MENU[order]["ingredients"]:
                if resources["milk"] < MENU[order]["ingredients"]["milk"]:
                    print("Insuffiecient resources, not enough milk.")
                    continue
            if resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
                print("Insuffiecient resources, not enough coffee.")
                continue
            
            resources["water"] -= MENU[order]["ingredients"]["water"]
            if 'milk' in MENU[order]["ingredients"]:
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]

            quarters = int(input("How many quarters would you like to pay: "))
            dimes = int(input("How many dimes would you like to pay: "))
            nickels = int(input("How many nickels would you like to pay: "))
            pennies = int(input("How many pennies would you like to pay: "))

            payment += quarters * .25 
            payment += dimes * .1 
            payment += nickels * .05 
            payment += pennies * .01

            if payment >= MENU[order]["cost"]:
                profit += MENU[order]["cost"]
                print(f"Your change is ${(payment - MENU[order]['cost'])}")
            else:
                print("Insufficient funds. Try again")
                continue


take_order(MENU, resources, profit)
