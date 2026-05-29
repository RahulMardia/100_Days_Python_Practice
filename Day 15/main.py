money = 0
totalMoneyInserted = 0
machine_turned_on = True

coins_values = {
    "quarters_value" : 0.25,
    "dimes_value" : 0.10,
    "nickels_value" : 0.05,
    "pennies_value" : 0.01,
}


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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while machine_turned_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice in MENU:
        enough_resources = True
        for ingredient in MENU[user_choice]["ingredients"]:

            if (resources[ingredient] < MENU[user_choice]["ingredients"][ingredient])  :
                print(f"Sorry there is not enough {ingredient}")
                enough_resources = False



        if enough_resources :
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            totalMoneyInserted = (quarters * coins_values["quarters_value"] + dimes * coins_values["dimes_value"] + nickels * coins_values["nickels_value"] + pennies * coins_values["pennies_value"])

            if totalMoneyInserted >= MENU[user_choice]["cost"]:
                if totalMoneyInserted > MENU[user_choice]["cost"]:
                    change = totalMoneyInserted - MENU[user_choice]["cost"]
                    print(f"Here's your change: ${round(change,2)}")
                for ingredient in MENU[user_choice]["ingredients"]:
                    resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]
                money += MENU[user_choice]["cost"]
                print(f"Here's your {user_choice}. Enjoy your coffee!!.")
            elif totalMoneyInserted < MENU[user_choice]["cost"]:
                print("Inserted coins less than needed coins. Returning your money back!.")




    elif user_choice == "report":
        resources["money"] = money
        for resource in resources:
            if resource == "money":
                print(f"Money: ${resources[resource]}")
            elif resource in ["water", "milk"]:
                print(f"{resource.capitalize()}: {resources[resource]}ml")
            else:
                print(f"{resource.capitalize()}: {resources[resource]}g")

    elif user_choice == "off":
        machine_turned_on = False

    else:
        print("Invalid choice. Please select from the given choice.")




