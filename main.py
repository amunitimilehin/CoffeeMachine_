
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Drink = Menu()
is_on = True
coffee = CoffeeMaker()
money = MoneyMachine()
while is_on == True:
    options = Drink.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = Drink.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)












