# import modules
from coffee_machine_data import coffee, coins, coffee_machine_stock

def print_report():

    print(f"Water: {coffee_machine_stock['Water']}")
    print(f"Milk: {coffee_machine_stock['Milk']}")
    print(f"Coffee: {coffee_machine_stock['Coffee']}")



def collect_coins():

    total_amount_paying = 0

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_amount_paying += quarters * coins["Quarter"]
    total_amount_paying += dimes * coins["Dime"]
    total_amount_paying += nickels * coins["Nickel"]
    total_amount_paying += pennies * coins["Penny"]

    return total_amount_paying


def check_stock(ordered_coffee):
    if coffee_machine_stock["Water"] < ordered_coffee["Water"]:
        return 'Water'
    elif coffee_machine_stock["Coffee"] < ordered_coffee["Coffee"]:
        return 'Coffee'
    elif coffee_machine_stock["Milk"] < ordered_coffee["Milk"]:
        return 'Milk'

    return ''


def check_coffee_machine_stock(order):
    print(f"Stock available for {order}")

    is_stock_available = True
    stock = check_stock(coffee[order])

    if stock != '':
        is_stock_available = False
        print(f"Sorry there is not enough {stock}")

    return is_stock_available


def make_coffee(coffee_name):
    coffee_machine_stock["Water"] -= coffee[coffee_name]["Water"]
    coffee_machine_stock["Milk"] -= coffee[coffee_name]["Milk"]
    coffee_machine_stock["Coffee"] -= coffee[coffee_name]["Coffee"]


def provide_order_item(ordered_coffee, amount_paying):

    price = coffee[ordered_coffee]['Price']

    if amount_paying < price:
        print("Sorry, You have not paid enough amount")
    else:
        make_coffee(ordered_coffee)
        return_amount = amount_paying - price
        print(f"Please collect amount {return_amount}.")
        print(f"You have your {ordered_coffee} coffee")


menu = ["Espresso", "Latte", "Cappuccino"]

is_maintenance = False

while len(menu) > 0 and not is_maintenance:
    coffee_order = input(f"What would you like? ({'/'.join(menu).lower()}): ").title()

    if coffee_order == 'Off':
        is_maintenance = True
    elif coffee_order == 'Report':
        print_report()
    else:
        if not check_coffee_machine_stock(coffee_order):
            menu.remove(coffee_order)
        else:
            total_amount_paid = collect_coins()
            provide_order_item(coffee_order, total_amount_paid)
            print(f"Total Amount Paid {total_amount_paid}.")
