"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Testing Multiple Conditions

Description:
This example demonstrates how an if-elif-else chain checks
multiple conditions and stops after the first condition is True.
"""

# Store the requested pizza toppings.
requested_toppings = ['mushrooms', 'extra cheese']

# Check whether mushrooms were requested.
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

# Check whether pepperoni was requested if the first condition is False.
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

# Check whether extra cheese was requested if the previous conditions are False.
elif 'extra cheese' in requested_toppings:
    print("Adding extra.")

# Display a message when the pizza is finished.
print("\nFinished making your pizza!")