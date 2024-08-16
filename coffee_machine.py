MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    }
}

QUARTER_RATE = 0.25
DIME_RATE = 0.10
NICKLE_RATE = 0.05
PENNY_RATE = 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

money = 0.0

turn_off = False

result = 1


def report():
    for i in resources:
        if i == "coffee":
            print(f"{i.title()} : {resources[i]}g")
        else:
            print(f"{i.title()} : {resources[i]}ml")
    print(f"Money : ${money}")


def check_resources(res):
    if resources[res] < MENU[choice]["ingredients"][res]:
        print(f"Sorry there is no enough {res}.")
        return 0
    else:
        return 1


def collect_coins(type_of_coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total_money = currency_convertion(quarters, dimes, nickels, pennies)
    if total_money < MENU[type_of_coffee]["cost"]:
        return -1
    else:
        return total_money


def currency_convertion(q, d, n, p):
    return q * QUARTER_RATE + d * DIME_RATE + n * NICKLE_RATE + p * PENNY_RATE


def give_change(amount, type_of_coffee):
    if amount > MENU[type_of_coffee]["cost"]:
        return round(amount - MENU[type_of_coffee]["cost"], 2)


def update_resources(res):
    resources[res] -= MENU[choice]["ingredients"][res]


def update_money(type_of_coffee):
    return MENU[type_of_coffee]["cost"]


while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        turn_off = True
    elif choice == "report":
        report()
    else:
        for item in MENU[choice]["ingredients"]:
            result = check_resources(item)
            if result == 0:
                break

        if result == 1:
            amount_received = collect_coins(choice)
            if amount_received != -1:
                change_amount = give_change(amount_received, choice)
                print(f"Here is ${change_amount} in change")
                print(f"Here is your {choice} enjoy!!")
                money += update_money(choice)
                for item in MENU[choice]["ingredients"]:
                    update_resources(item)
            else:
                print("Sorry that's not enough money. Money refunded.")
