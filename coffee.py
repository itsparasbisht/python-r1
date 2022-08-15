resources = {"water": 2000, "milk": 650, "coffee": 450, "money": 15.5}


class Beverage:
    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def __repr__(self):
        return (
            f"\n \twater: {self.water}ml \n\tmilk: {self.milk}ml \n\tcoffee: {self.coffee}g \n\tmoney: ${self.money}\n"
        )


espresso = Beverage(100, 20, 55, 1.5)
latte = Beverage(200, 70, 35, 2.5)
cappuccino = Beverage(250, 100, 70, 3.0)


def check_for_resources(water, milk, coffee, money):
    flag = 0

    if water <= resources.get("water"):
        pass
    else:
        flag = 1
        return "\nSorry there is not enough water."

    if milk <= resources.get("milk"):
        pass
    else:
        flag = 1
        return "\nSorry there is not enough milk."

    if coffee <= resources.get("coffee"):
        pass
    else:
        flag = 1
        return "\nSorry there is not enough coffee."

    if money <= resources.get("money"):
        pass
    else:
        flag = 1
        return "\nSorry there is not enough change."

    if flag == 0:
        return "AVAILABLE"


def total_amount(quarters, dimes, nickles, pennies):
    return (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def calculate_change(amount, price):
    change = amount - price
    return round(change, 2)


def deduct_resources(water, milk, coffee):
    resources["water"] = resources["water"] - water
    resources["milk"] = resources["milk"] - milk
    resources["coffee"] = resources["coffee"] - coffee


def insert_coins(price):
    print("\n💲💲💲 Insert coins 💲💲💲\n")
    quarters = int(input("Insert QUARTERS: "))
    dimes = int(input("Insert DIMES: "))
    nickles = int(input("Insert NICKLES: "))
    pennies = int(input("Insert PENNIES: "))

    amount = total_amount(quarters, dimes, nickles, pennies)
    amount_rounded = round(amount, 2)
    change = calculate_change(amount_rounded, price)

    return [change, amount_rounded]


def process_transaction(change, amount_rounded, beverage):
    if change == 0:
        print(f"Here is your {user_choice}. Enjoy! ☕☕☕")
        resources["money"] += amount_rounded
    elif change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        deduct_resources(beverage.water, beverage.milk, beverage.coffee)
        resources["money"] = resources["money"] + amount_rounded
        resources["money"] = resources["money"] - change
        print(f"\nHere is ${change} dollars in change.")
        print(f"Enjoy your {user_choice}. ☕☕☕")


while True:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino):\n")

    if user_choice == "report":
        print(resources)

    if user_choice == "off":
        print("Machine turned off")
        break

    if user_choice == "espresso":
        response = check_for_resources(espresso.water, espresso.milk, espresso.coffee, espresso.money)
        if response == "AVAILABLE":
            change, amount_rounded = insert_coins(espresso.money)

            process_transaction(change, amount_rounded, espresso)

        else:
            print(response)

    elif user_choice == "latte":
        response = check_for_resources(latte.water, latte.milk, latte.coffee, latte.money)
        if response == "AVAILABLE":
            change, amount_rounded = insert_coins(latte.money)

            process_transaction(change, amount_rounded, latte)

        else:
            print(response)

    elif user_choice == "cappuccino":
        response = check_for_resources(cappuccino.water, cappuccino.milk, cappuccino.coffee, cappuccino.money)
        if response == "AVAILABLE":
            change, amount_rounded = insert_coins(cappuccino.money)

            process_transaction(change, amount_rounded, cappuccino)

        else:
            print(response)
