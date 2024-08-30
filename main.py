
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()

my_coffemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()




is_on = True

while is_on is True:

   option = my_menu.get_items()

   order = input(f"What would like to order {option}")

   if order == "off":
       is_on = False
   elif order == "report":
       my_coffemaker.report()
       my_moneymachine.report()
   else:
     drink = my_menu.find_drink(order)
     print()
     if my_coffemaker.is_resource_sufficient(drink) is True:
        if my_moneymachine.make_payment(drink.cost) is True:
             my_coffemaker.make_coffee(drink)

