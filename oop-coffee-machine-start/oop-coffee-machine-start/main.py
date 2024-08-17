from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_machine = MoneyMachine()

is_off = False

while not is_off:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "report":
        coffee.report()
        money_machine.report()
    elif choice == "off":
        is_off = True
    else:
        drink = menu.find_drink(choice)
        if (drink is not None and coffee.is_resource_sufficient(drink) and
                money_machine.make_payment(drink.cost)):
            coffee.make_coffee(drink)
