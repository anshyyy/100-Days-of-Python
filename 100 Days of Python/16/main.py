from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
while True:
    choice = menu.get_items()
    drink = input(f"What would you like?({choice}):")
    if drink == "off":
        break
    elif drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        mychoice = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(mychoice):
            if money_machine.make_payment(mychoice.cost):
                coffee_maker.make_coffee(mychoice)





