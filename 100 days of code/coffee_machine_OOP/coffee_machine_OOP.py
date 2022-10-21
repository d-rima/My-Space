from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on == True:
    drinks = menu.get_items()
    user_choice = input(f"What would you like to drink? ({drinks}): ")
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'quit':
        is_on = False
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        selection = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(selection) == True:
            coffee_maker.make_coffee(selection)
            money_machine.make_payment(selection.cost)