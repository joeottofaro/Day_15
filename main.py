import data

# Power is used to control the while loop
# Money is storing our profits
power = "on"
money = 0


def resource_check(order):
    """Will return False if we are unable to fulfill order. Otherwise, it will return True"""
    if order == "espresso" and data.resources["water"] <= 50:
        print("Sorry that's not enough water!")
        return False
    elif order == "espresso" and data.resources["coffee"] <= 18:
        print("Sorry that's not enough coffee!")
        return False
    elif order == "latte" and data.resources["milk"] <= 150:
        print("Sorry that's not enough milk!")
        return False
    elif order == "latte" and data.resources["coffee"] <= 24:
        print("Sorry that's not enough coffee!")
        return False
    elif order == "latte" and data.resources["water"] <= 200:
        print("Sorry that's not enough water!")
        return False
    elif order == "cappuccino" and data.resources["coffee"] <= 24:
        print("Sorry that's not enough coffee!")
    elif order == "cappuccino" and data.resources["water"] <= 250:
        print("Sorry that's not enough water!")
        return False
    elif order == "cappuccino" and data.resources["milk"] <= 100:
        print("Sorry that's not enough milk!")
        return False
    return True


def process_coins(order, profit):
    """Returns profit if user has enough money to order a drink. Otherwise, returns False"""
    print("Please insert coins")
    total = quarters = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    if data.MENU[order]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total - data.MENU[order]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        profit += data.MENU[order]["cost"]
        return profit


def make_coffee(order):
    """Used to subtract resources and serve the drink"""
    if order == "espresso":
        data.resources["water"] -= 50
        data.resources["coffee"] -= 18
        print(f"Here is your {order} ☕️. Enjoy!")
    elif order == "latte":
        data.resources["water"] -= 200
        data.resources["coffee"] -= 24
        data.resources["milk"] -= 150
        print(f"Here is your {order} ☕️. Enjoy!")
    elif order == "cappuccino":
        data.resources["water"] -= 250
        data.resources["coffee"] -= 24
        data.resources["milk"] -= 100
        print(f"Here is your {order} ☕️. Enjoy!")


# Main while loop
while power == "on":
    user_request = input("What would you like? (espresso/latte/cappuccino):").lower()
    # If block to handle all options for user_request
    if user_request == "report":
        print(f"Water: {data.resources["water"]}ml\nMilk: {data.resources["milk"]}ml\n"
              f"Coffee: {data.resources["coffee"]}g\nMoney: ${money}")

    elif user_request == "off":
        power = "off"
        print("Powering off...\nGoodbye!")
        exit()

    elif user_request == "espresso" or user_request == "latte" or user_request == "cappuccino":
        checking_order = resource_check(user_request)
        if checking_order:
            cashier = process_coins(user_request, money)
            if cashier:
                money += round(cashier, 2)
                make_coffee(user_request)
    else:
        print("That is not a valid option. Please try again.")
