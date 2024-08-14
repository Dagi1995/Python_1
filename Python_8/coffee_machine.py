menu = {
    "espresso": {
        "ingredients": {
            "water": 18,
            "coffee": 50,
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
        "cost": 3.5,
    },

}


profit = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredient):
    for items in order_ingredient:
        if order_ingredient[items] >= resource[items]:
            print(f"sorry there is no enough {items}")
            return False
    return True
def process_coin():
    print("please insert the coin :")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total
def is_successful_transaction(received_cost, drink_cost):
    if received_cost >= drink_cost:
        change = round(received_cost - drink_cost , 2)
        print(f"Her is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry is not enough money , Money refunded. ")
        return False
def coffee_make(drink_name , ordered_ingredients):
    for item in ordered_ingredients:
        resource[item] -= ordered_ingredients[item]
    print(f"Her is you'r {drink_name}🍵 .Enjoy ")


is_no = True
while is_no:
    choice = input ("what would you like ? (espresso/latte/cappuccino) : ")
    if choice == 'off':
        is_no = False
    elif choice == 'report':
        print (f"Water {resource ['water']}ml")
        print(f"Milk {resource['milk']}ml")
        print(f"Coffee {resource['coffee']}g")
        print(f"Money {profit}")
    else:
        drink = menu [choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_successful_transaction(payment, drink['cost']):
                coffee_make(choice,drink['ingredients'])

