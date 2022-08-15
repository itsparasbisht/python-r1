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

# print("Espresso:", espresso)
# print("Latte:", latte)
# print("Cappuccino:", cappuccino)


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
        return "\nSorry there is not enough money."

    if flag == 0:
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee
        resources["money"] = resources["money"] - money

        return "AVAILABLE"


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
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(response)

    elif user_choice == "latte":
        response = check_for_resources(latte.water, latte.milk, latte.coffee, latte.money)
        if response == "AVAILABLE":
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(response)

    elif user_choice == "cappuccino":
        response = check_for_resources(cappuccino.water, cappuccino.milk, cappuccino.coffee, cappuccino.money)
        if response == "AVAILABLE":
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print(response)
