"""
Source: Python Crash Course, 3rd Edition
Chapter: 5
Topic: Checking for Available Toppings
Description: Check whether requested toppings are available before adding them to a pizza.
"""

# Store the toppings that are available at the pizzeria.
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

# Store the toppings requested by the customer.
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

# Check each requested topping against the available toppings.
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

# Indicate that the pizza is finished.
print("\nFinished making your pizza!")