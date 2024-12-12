from Tools.scripts.fixdiv import report

from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()



flag=True

while flag:
    flag1=True
    options=menu.get_items()
    choice=input(f"What would you like?({options}): ")
    if choice=="off":
        flag=False
        flag1=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
        flag1=False
    else:
        drink=menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)








