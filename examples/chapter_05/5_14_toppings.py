"""
Source: Python Crash Course, 3rd Edition
Chapter: 5
Topic: Checking That a List Is Not Empty
Description: Check whether a list contains items before running a for loop.
"""

# Store the requested pizza toppings in a list.
requested_toppings = []

# Check whether the list contains any toppings.
if requested_toppings:
    # Add each requested topping to the pizza.
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")

    # Indicate that the pizza is finished.
    print("\nFinished making your pizza!")

# Handle the case where no toppings were requested.
else:
    print("Are you sure you want a plain pizza?")