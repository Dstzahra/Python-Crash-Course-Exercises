"""
Source: Python Crash Course, 3rd Edition
Chapter: 5
Topic: Checking for Special Items
Description: Use an if-else statement inside a for loop to handle a special topping.
"""

# Store the requested pizza toppings in a list.
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# Check each requested topping and handle green peppers differently.
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

# Indicate that the pizza is finished.
print("\nFinished making your pizza!")