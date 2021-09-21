import os
import random
import data
profit=0
def check_ingredients(oresources):
    for item in oresources:
        if item in oresources:
            if oresources[item]>=data.resources[item]:
                print(f"Sorry there isn't  enough {item}")
                return False
    return True
def process_coins():
    print("Please! insert coins:")
    total  = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def transacction(payment,drink_cost):
    if payment>=drink_cost:
        change=round(payment-drink_cost,2)
        print(f"Here is ${change} in change ")
        global profit
        profit+=drink_cost
        return True
    else:
        print(f"Sorry thats's not enough money. Money refunded.")
        return True

def make_coffe(drink_name,order):
    for item in order:
        data.resources[item]-=order[item]
    print(f"Here is your {drink_name}")
while True:
    drink =input("What would you like to drink? espresso/cappuccino?latte:").lower()
    if(drink == "off"):
        break
    elif drink =="report":
        for item in data.resources:
            print(f"{item}:{data.resources[item]}")
        print(f"Money:${profit}")
    else:
        coffee =data.MENU[drink]
        if check_ingredients(coffee["ingredients"]):
             payment=process_coins()
             if transacction(payment,coffee["cost"]):
                   make_coffe(drink,coffee["ingredients"])




