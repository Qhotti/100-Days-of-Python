MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def resource_report():
    water = print('Water:',resources['water'])
    milk = print('Milk:',resources['milk'])
    coffee = print('Coffee:',resources['coffee'])
    money = print('Money:',resources['money'])
    return ''



def user_choice():
    coffee_being_decided = True
    while coffee_being_decided:
        choice = input('What would you like? espresso/latte/cappuccino: ')
        coffee_being_decided = False
    return choice

choice = user_choice()

if choice == 'off':
    print('Machine Powering Down')
    exit()
elif choice == 'report':
    print(resource_report())
    

def sufficient_resources():
    sufficient_resources = False
    if choice in MENU:
        if resources['water'] >= MENU[choice]['ingredients'].get('water'):
            sufficient_resources = True
        else:
            sufficient_resources = False
            return print(f'Cant dispense {choice}, out of water.')
    if choice in MENU:
        if resources['milk'] >= MENU[choice]['ingredients'].get('milk'):
            sufficient_resources = True
        else:
            sufficient_resources = False
            return print(f'Cant dispense {choice}, out of milk.')
    if choice in MENU:
        if resources['coffee'] >= MENU[choice]['ingredients'].get('coffee'):
            sufficient_resources = True
        else:
            sufficient_resources = False
            return print(f'Cant dispense {choice}, out of coffee.')
    if sufficient_resources == False:
        exit()
        #insert loop
    return sufficient_resources
        
sufficient = sufficient_resources()

def input_coins():
    
    if sufficient == True:
        quarter = int(input('How many quarters?'))
        dime = int(input('How many dimes?'))
        nickle = int(input('How many nickles?'))
        penny = int(input('How many pennies?'))
        money = float((quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01))
        if money >= MENU[choice].get('cost'):
            resources.update({"money": money})
            
            change = money - MENU[choice].get('cost')
            if change > 0:
                print(f'Here is your change: ${change}')
            return True
        else:
            print('Not enough money. Heres your refund.')
            return False
        #insert loop
    #else:
    #insert loop
correct_coins = input_coins()


water_subtract = resources["water"] - MENU[choice]['ingredients'].get('water')
milk_subtract = resources["milk"] - MENU[choice]['ingredients'].get('milk')
coffee_subtract = resources["coffee"] - MENU[choice]['ingredients'].get('coffee')






def make_coffee():
    if correct_coins:
       resources.update(water_subtract)
       resources.update(milk_subtract)
       resources.update(coffee_subtract)
       print(f'Here is your {choice}. Enjoy!')
make_coffee()

print(resources.items())
        



    
