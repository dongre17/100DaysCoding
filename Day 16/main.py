# import modules
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

is_maintenance = False
menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def manage_order_request(order):
    """ Handle Order Request By Customer."""
    global is_maintenance
    if order == 'off':
        is_maintenance = True
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


# TODO 1: prompts user by asking "What would you like? (latte/espresso/cappuccino/): "

while not is_maintenance:

    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()
    manage_order_request(order_name)
