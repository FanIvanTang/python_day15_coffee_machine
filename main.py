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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def get_instrcution_from_user():
    """
    get instruction from user and the valid input should be "espresso, latte, cappucccino, report, and off"
    and return the instruction
    """
    instructions = ["espresso", "latte", "cappuccino", "report", "off"]

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    while user_input not in instructions:
        user_input = input(
            "Opoos, wrong instruction, what would you like? (espresso/latte/cappuccino)"
        )

    return user_input


def off_machine():
    """
    turn off machine
    """
    exit()


def print_report():
    """
    print the report of machine status

    """

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resource(coffee_type):
    """
    check resource status base on on coffe_type, return true or fale with messeage
    """

    is_enough = True

    for ingredient in MENU[coffee_type]["ingredients"]:
        # print(resources[ingredient])
        # print(MENU[coffee_type]["ingredients"][ingredient])
        if resources[ingredient] < MENU[coffee_type]["ingredients"][ingredient]:

            is_enough = False
            print(f"Sorry there is not enough {ingredient}")
            return False

    return is_enough


def get_coins_from_user(coin_type):

    """
    get input from user, and it has to be integer, and return number of coins user put in
    """
    user_inputs = input(f"how many {coin_type}?: ")

    while True:

        try:
            coins = int(user_inputs)
            return coins
        except ValueError:
            user_inputs = input(f"how many {coin_type}?: ")


def process_coins():
    """
    a.prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    """

    quarters = get_coins_from_user("quarters")
    dimes = get_coins_from_user("dimes")
    nickles = get_coins_from_user("nickles")
    pennie = get_coins_from_user("pennie")

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennie * 0.01


def check_enough_pay(amount_money, coffee_type):
    """
    a. Check that the user has inserted enough money to purchase the drink they selected.
        E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        program should say “Sorry that's not enough money. Money refunded.”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
        machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        Water: 100ml
        Milk: 50ml
        Coffee: 76g
        Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
        E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        places.
    """

    if MENU[coffee_type]["cost"] > amount_money:
        print("Sorry that's not enough money. Money refunded")

        return False
    else:

        resources["money"] += MENU[coffee_type]["cost"]

        if amount_money - MENU[coffee_type]["cost"] > 0:

            print(
                f"Here is ${round(amount_money-MENU[coffee_type]['cost'],2)} dollars in change"
            )

        return True


def make_coffee(coffee_type):
    """
    a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink.
    """

    for ingredient in MENU[coffee_type]["ingredients"]:

        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]

    print(f"Here is your {coffee_type},Enjoy")


if __name__ == "__main__":

    while True:

        instruction = get_instrcution_from_user()

        if instruction == "off":
            off_machine()

        elif instruction == "report":
            print_report()

        else:

            is_sufficient = check_resource(coffee_type=instruction)

            if is_sufficient:
                pay = process_coins()

                if check_enough_pay(amount_money=pay, coffee_type=instruction):
                    make_coffee(coffee_type=instruction)
