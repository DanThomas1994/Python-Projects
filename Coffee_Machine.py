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


# TODO 1: Print a report of all the coffee machine resources.

# Set the machine to be "ON" by default:
machine_on = True

# Set the initial amount of money in the machine to be $0:
resources["money"] = 0

# Set the milk required for the espresso to be 0:
MENU["espresso"]["ingredients"]["milk"] = 0

def check_resources(drink_selection):
    """Function to check if the current machine resources are sufficient to make the selected drink."""
    if resources["water"] < MENU[drink_selection]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return "Insufficient"
    elif resources["coffee"] < MENU[drink_selection]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return "Insufficient"
    elif resources["milk"] < MENU[drink_selection]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return "Insufficient"
    else:
        return "Sufficient"

def calculate_money():
    """Function to calculate the money inputted into the machine."""
    print("Please insert coins. This machine accepts quarters ($0.25), dimes ($0.10), nickels ($0.05) "
          "and pennies ($0.01).")
    q = int(input("Number of quarters: "))  # Explicitly tell the programme that the inputs are integers.
    d = int(input("Number of dimes: "))
    n = int(input("Number of nickels: "))
    p = int(input("Number of pennies: "))
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    print(f"Total: ${round(total,2)}") # Round the total to 2 d.p.
    return total # Simply return the total money inputted into the machine.

# Ask the user for input:
while machine_on:
    user_input = str(input("Which coffee would you like?\n").lower()) # Tell the programme that the user input is
    # a string.

    if user_input == "off":
        print("Machine turned off.")
        machine_on = False # Turn the machine off and exit the loop if the user turns the machine off.

    elif user_input == "report":
        print("The remaining resources are:")
        print(f"Water: {resources["water"]} ml")
        print(f"Milk: {resources["milk"]} ml")
        print(f"Coffee: {resources["coffee"]} g")
        print(f"Money: ${round(resources["money"],2)}") # Ensure the remaining money is displayed to 2 d.p.

    elif user_input == "espresso" or user_input == "cappuccino" or user_input == "latte": # Need to explicitly
        # put user_input for each OR statement to ensure that it works correctly. Otherwise, Python will evaluate
        # the second string to True, regardless of the input.
        print(f"You have selected {user_input}.")
        check_stock = check_resources(user_input)
        if check_stock == "Sufficient":
            total_money = calculate_money()
            if total_money >= MENU[user_input]["cost"]:
                resources["water"] -= MENU[user_input]["ingredients"]["water"]
                resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
                resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
                resources["money"] += total_money
                print(f"Here is your {user_input}. Enjoy!")
                change = round(total_money - MENU[user_input]["cost"],2) # Round the change to 2 decimal places.
                resources["money"] -= change
                print(f"Here is ${change} in change.")
            else:
                print("Sorry, that's not enough money. Money refunded.")

    else:
        print("Please enter a valid input.")




# TODO 2: Check that resources are sufficient to make the drink order.
