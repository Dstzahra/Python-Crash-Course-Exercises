"""
Source: Python Crash Course, 3rd Edition
Chapter: 5
Topic: Looping Through a List
Description: Use a for loop to print each requested pizza topping.
"""

# Store the requested pizza toppings in a list.
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# Add each requested topping to the pizza.
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

# Indicate that the pizza is finished.
print("\nFinished making your pizza!")